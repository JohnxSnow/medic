"""
DarmanNas (دەرمانناس) - Flask Web Application & Official Medicine API
Zero Hallucination - Direct OpenFDA Integration & Kurdish Pharmaceutical Index.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 console output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS

from fda_service import fetch_openfda_data
from kurdish_medical_dict import (
    KURDISH_DRUG_INDEX,
    search_kurdish_index,
    get_by_generic_name
)
from interaction_engine import check_drug_interactions
from emergency_directory import EMERGENCY_DATA
from symptom_triage import triage_patient_symptom
from allergy_engine import check_drug_allergy
from meal_timing_engine import get_meal_timing_guide

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

app = Flask(__name__, static_folder=str(STATIC_DIR), template_folder=str(TEMPLATES_DIR))
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({
        "status": "online",
        "app_name": "دەرمانناس - DarmanNas",
        "fda_connection": "active",
        "total_indexed_drugs": len(KURDISH_DRUG_INDEX)
    })

@app.route("/api/search")
def search_drugs():
    """
    Search endpoint supporting Kurdish, Arabic, and English terms.
    Returns matched medicines with their generic names and categories.
    """
    query = request.args.get("q", "").strip()
    if not query:
        # Return popular items
        return jsonify({
            "results": KURDISH_DRUG_INDEX[:8]
        })

    # Search local clinical index
    local_results = search_kurdish_index(query)

    # If local results found, return them
    if local_results:
        return jsonify({"results": local_results})

    # Fallback to direct OpenFDA search for international medicines not in local index
    fda_data = fetch_openfda_data(query)
    if fda_data:
        dynamic_item = {
            "id": query.lower().replace(" ", "_"),
            "generic_name": fda_data["generic_name"],
            "kurdish_name": fda_data["generic_name"],
            "brand_names": [fda_data["brand_name"]] if fda_data["brand_name"] != fda_data["generic_name"] else [],
            "category": fda_data.get("route", "دەرمانی گشتی پۆلێنکراوی FDA"),
            "category_en": "FDA Certified Drug",
            "kurdish_summary": {
                "purpose": fda_data.get("indications_and_usage")[:250] + "..." if fda_data.get("indications_and_usage") else "بۆ زانیاری تەواو سەیری بڕگەی فەرمی FDA بکە.",
                "usage": "بەپێی ڕێنمایی پزیشک و دەقی فەرمی FDA.",
                "who_cannot_take": fda_data.get("contraindications")[:200] if fda_data.get("contraindications") else "سەیری بەشی هۆشداری بکە.",
                "pregnancy_safety": "پێویستە بە ڕاوێژی پزیشک بێت.",
                "crucial_warning": fda_data.get("warnings")[:250] if fda_data.get("warnings") else "دەبێت تەنها بەپێی ڕەچەتەی پزیشک بەکاربێت."
            },
            "is_direct_fda": True
        }
        return jsonify({"results": [dynamic_item]})

    return jsonify({"results": []})

@app.route("/api/drug/<drug_id>")
def get_drug_details(drug_id):
    """
    Fetches comprehensive verified drug details:
    Merges local Kurdish clinical summary with live, authentic OpenFDA label data.
    """
    clean_id = drug_id.lower().strip()

    # Find in local index
    drug_obj = None
    for item in KURDISH_DRUG_INDEX:
        if item["id"].lower() == clean_id or item["generic_name"].lower() == clean_id:
            drug_obj = item
            break

    if not drug_obj:
        # Search by query
        results = search_kurdish_index(drug_id)
        if results:
            drug_obj = results[0]

    generic_name = drug_obj["generic_name"] if drug_obj else drug_id
    primary_brand = drug_obj["brand_names"][0] if drug_obj and drug_obj.get("brand_names") else None

    # Fetch live verified FDA label data
    fda_data = fetch_openfda_data(generic_name, primary_brand)

    # Fetch meal timing & food administration guide
    meal_guide = get_meal_timing_guide(
        drug_obj["id"] if drug_obj else clean_id,
        generic_name,
        drug_obj.get("category_en", "") if drug_obj else ""
    )

    return jsonify({
        "success": True,
        "kurdish_info": drug_obj,
        "fda_official": fda_data,
        "meal_timing": meal_guide,
        "verified_fda": bool(fda_data and fda_data.get("verified_fda")),
        "disclaimer": "ئەم زانیارییانە بۆ مەبەستی ڕۆشنبیری و وریایی دەرمانە لە سەرچاوەی فەرمی FDA و جێگەی پشکنینی پزیشکی پسپۆڕ ناگرێتەوە."
    })

@app.route("/api/allergy-check", methods=["POST"])
def check_allergy():
    """Checks whether a drug is safe for a given allergy (e.g. Penicillin, NSAID, Sulfa)."""
    data = request.get_json(silent=True) or {}
    allergy = data.get("allergy", "").strip()
    drug = data.get("drug", "").strip()

    if not allergy or not drug:
        return jsonify({
            "success": False,
            "error_kurdish": "تکایە جۆری حەساسیەتەکەت و ناوی دەرمانەکە دیاری بکە."
        }), 400

    result = check_drug_allergy(allergy, drug)
    return jsonify(result)

@app.route("/api/interaction", methods=["POST"])
def check_interaction():
    """Checks interaction between two drugs."""
    data = request.get_json(silent=True) or {}
    drug1 = data.get("drug1", "").strip()
    drug2 = data.get("drug2", "").strip()

    if not drug1 or not drug2:
        return jsonify({
            "success": False,
            "error": "تکایە ناوی هەردوو دەرمانەکە دیاری بکە."
        }), 400

    result = check_drug_interactions(drug1, drug2)
    return jsonify({
        "success": True,
        "data": result
    })

@app.route("/api/triage", methods=["POST"])
def triage_symptom():
    """
    Evaluates patient complaint using non-hallucinatory clinical triage rules.
    Identifies possible causes, non-drug relief, red flags, and exact specialist.
    """
    data = request.get_json(silent=True) or {}
    complaint = data.get("complaint", "").strip()

    if not complaint:
        return jsonify({
            "success": False,
            "error_kurdish": "تکایە بە کورتی شوێنی ئازارەکە یان کێشەکەت بنووسە..."
        }), 400

    result = triage_patient_symptom(complaint)
    return jsonify(result)

@app.route("/api/emergency")
def get_emergency_info():
    """Returns emergency contacts and hospital directories."""
    return jsonify({
        "success": True,
        "data": EMERGENCY_DATA
    })

@app.route("/api/categories")
def get_categories():
    """Returns curated list of categories with drug counts."""
    categories = {}
    for drug in KURDISH_DRUG_INDEX:
        cat = drug["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append({
            "id": drug["id"],
            "kurdish_name": drug["kurdish_name"],
            "generic_name": drug["generic_name"],
            "brand_names": drug["brand_names"]
        })
    return jsonify({
        "success": True,
        "categories": categories
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    print("=" * 60)
    print("دەرمانناس - سیستەمی فەرمی زانیاری دەرمان و بەستنەوە بە FDA")
    print("DarmanNas Kurdish Medicine & OpenFDA System")
    print(f"Server running at: http://{host}:{port}")
    print("=" * 60)
    app.run(host=host, port=port, debug=False)
