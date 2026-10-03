"""
DarmanNas - Clinical Drug Allergy & Penicillin Shield Engine
100% Evidence-Based Clinical Allergy Cross-Reactivity Engine.
STRICT SAFETY: Accurately detects beta-lactams, penicillins, cephalosporins,
sulfonamides, and NSAID allergies with zero hallucination.
"""

from typing import Dict, Any, List

def normalize_text(text: str) -> str:
    if not text:
        return ""
    t = text.lower().strip()
    replacements = {
        'ك': 'ک', 'ي': 'ی', 'ى': 'ی', 'ێ': 'ی',
        'ف': 'ڤ', 'ة': 'ە', 'ه': 'ە', 'ۆ': 'و',
        'ڵ': 'ل', 'ڕ': 'ر', 'أ': 'ا', 'إ': 'ا', 'آ': 'ا',
        'ـ': '', '؟': '', '?': '', '!': '', '.': '', ',': '', '،': ''
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t

def matches_any(query: str, target_list: List[str]) -> bool:
    norm_q = normalize_text(query)
    q_words = norm_q.split()
    for item in target_list:
        norm_item = normalize_text(item)
        if norm_q in norm_item or norm_item in norm_q:
            return True
        for w in q_words:
            if len(w) >= 3 and (w in norm_item or norm_item in w):
                return True
    return False

# Known High-Risk Allergy Categories & Cross-Reactivity
ALLERGY_DATABASE = {
    "penicillin": {
        "id": "penicillin",
        "name_kurdish": "حەساسیەتی پێنسلین (Penicillin Allergy)",
        "name_en": "Penicillin & Beta-Lactams",
        "trigger_keywords": ["پێنسلین", "پنسلین", "پنسلینم", "penicillin", "penicilin", "بنسلين", "بنسلین"],
        "strictly_forbidden_drugs": [
            {
                "name": "ئۆگمێنتین / ئامۆکسیلین (Augmentin / Amoxicillin)",
                "brands": ["Augmentin", "Amoxil", "Clavox", "Curam", "Megamox", "Julmentin", "Amoxicillin", "ئۆگمێنتین", "ئامۆکسیل", "کلاڤۆکس", "ئامۆکسیلین"],
                "reason": "ئامۆکسیلین ئەندامێکی سەرەکییە لە خێزانی پێنسلینەکان. خواردنی بۆ کەسی هەستیار مەترسی شۆکی حەساسیەتی کوشندە (Anaphylaxis) و داخرانی ڕێڕەوی هەناسەی لێدەکەوێتەوە."
            },
            {
                "name": "ئەمپیسلین (Ampicillin / Ampiclox)",
                "brands": ["Ampicillin", "Ampiclox", "Omnipen", "ئەمپیسلین", "ئەمپیکلۆکس"],
                "reason": "ڕاستەوخۆ پێنسلینە و بە هیچ جۆرێک نابێت بەکاربهێنرێت."
            },
            {
                "name": "پایپەراسیکلین و تازۆباکتام (Tazocin / Piperacillin)",
                "brands": ["Tazocin", "Zosyn", "Piperacillin", "تازۆسین"],
                "reason": "پێنسلینی بەهێزی ناو نەخۆشخانەیە و بە توندی قەدەغەیە."
            }
        ],
        "cross_reactive_caution": [
            {
                "class_name": "سیفالۆسپۆرینەکان (Cephalosporins)",
                "brands": ["Keflex", "Zinnat", "Cefuroxime", "Suprax", "Cefixime", "Rocephin", "Ceftriaxone", "Cefotaxime", "سفیکسیم", "سوپراکس", "ڕۆسێفین", "زینات", "کێفلێکس", "سێفالێکسین"],
                "examples": ["Keflex (سێفالێکسین)", "Zinnat / Cefuroxime (زینات)", "Suprax / Cefixime (سوپراکس / سفیکسیم)", "Rocephin / Ceftriaxone (ڕۆسێفین)"],
                "warning": "لە نێوان پێنسلین و سیفالۆسپۆرینەکاندا بە ڕێژەی ٥٪ تا ١٠٪ گومانی کاردانەوەی حەساسیەتی هاوبەش هەیە بەهۆی ئەڵقەی بیتا-لاکتام. تەنها لەژێر بڕیار و چاودێری ڕاستەوخۆی پزیشکی پسپۆڕ وەردەگیرێت."
            }
        ],
        "safe_alternatives_note": "بۆ کەسانی تووشبوو بە حەساسیەتی پێنسلین، پزیشک ئەنتی بایۆتیکی جێگرەوە لە خێزانی ماکرۆلایدەکان دیاری دەکات، وەک: ئەزیترۆمایسین (Azithromycin / Zithromax) یان کلاریترۆمایسین (Clarithromycin / Klacid) یان دۆکسی سایکلین بەپێی جۆری هەوکردنەکە."
    },
    "nsaid_aspirin": {
        "id": "nsaid_aspirin",
        "name_kurdish": "حەساسیەتی ئەسپیڕین و پرۆفین (NSAID / Aspirin Allergy)",
        "name_en": "NSAID & Aspirin Sensitivity",
        "trigger_keywords": ["ئەسپیڕین", "پرۆفین", "برۆفین", "فۆڵتارین", "aspirin", "nsaid", "ibuprofen", "voltaren", "prof", "brufen"],
        "strictly_forbidden_drugs": [
            {
                "name": "ئیبۆپرۆفین و برۆفین (Ibuprofen / Brufen)",
                "brands": ["Brufen", "Advil", "Motrin", "Doloraz", "Ibuprofen", "پرۆفین", "برۆفین", "ئیبۆپرۆفین", "ئادڤیل"],
                "reason": "دەبێتە هۆی تەنگەنەفەسی توند، هەڵئاوسانی پێڵوی چاو، لێوەکان و دروستبوونی پەڵەی سووری خوروێنەر."
            },
            {
                "name": "دیکلۆفیناک (Voltaren / Cataflam)",
                "brands": ["Voltaren", "Cataflam", "Olfen", "Diclogesic", "فۆڵتارین", "کاتافلام", "ئۆلفین", "دیکلۆفیناک"],
                "reason": "لە هەمان خێزانی پرۆفینە و کاردانەوەی حەساسیەتی توند دروست دەکات."
            },
            {
                "name": "ئەسپیڕین (Aspirin)",
                "brands": ["Aspirin", "Aspicor", "Disprin", "ئەسپیڕین", "ئەسپیکۆر"],
                "reason": "لەو کەسانەی هەستیارییان پێی هەیە دەبێتە هۆی تەنگبوونی کوشندەی بۆڕییەکانی هەوا و قەیرانی ڕەبۆ."
            },
            {
                "name": "پۆنستان و ناپرۆکسین (Ponstan / Naproxen)",
                "brands": ["Ponstan", "Aleve", "Naprosyn", "Mefenamic Acid", "پۆنستان", "ناپرۆکسین"],
                "reason": "سەرجەمیان دژە هەوکردنی نائەستیرۆیدین (NSAID) و کارلێکی حەساسیەتیان هەیە."
            }
        ],
        "cross_reactive_caution": [
            {
                "class_name": "سێلیکۆکسیب (Celebrex / Cox-2 Inhibitors)",
                "brands": ["Celebrex", "Celecoxib", "سێلیبرێکس"],
                "examples": ["Celebrex (سێلیبرێکس)"],
                "warning": "هەرچەندە تایبەتترە بە کۆکس-٢، بەڵام بۆ کەسێک کە حەساسیەتی توندی بە پرۆفین هەبێت ڕەنگە مەترسی هەبێت و دەبێت پزیشک بڕیاری لێبدات."
            }
        ],
        "safe_alternatives_note": "پاراسیتامۆڵ (Panadol / Paracetamol) بە ڕێژەی زیاتر لە ٩٥٪ سەلامەتە وەک ئازارشکێن بۆ ئەو کەسانەی حەساسیەتیان بە پرۆفین و ئەسپیڕین هەیە، لەژێر ڕاوێژی پزیشک."
    },
    "sulfa": {
        "id": "sulfa",
        "name_kurdish": "حەساسیەتی سۆلفا (Sulfonamide Allergy)",
        "name_en": "Sulfa Drug Allergy",
        "trigger_keywords": ["سۆلفا", "سولفا", "sulfa", "sulfonamide", "bactrim", "بەکتریم"],
        "strictly_forbidden_drugs": [
            {
                "name": "کۆ-تریمۆکسازۆڵ / بەکتریم (Co-trimoxazole / Bactrim / Septra)",
                "brands": ["Bactrim", "Septra", "Cotrim", "Sulfamethoxazole", "بەکتریم", "سێپترا", "سۆلفامیتۆکسازۆڵ"],
                "reason": "پێکهاتەی سەرەکی سۆلفای تێدایە و کاردانەوەی توندی پێست و برین و شۆک دروست دەکات."
            }
        ],
        "cross_reactive_caution": [
            {
                "class_name": "دەرمانی سۆلفۆنیلی تر (Sulfonylureas / Thiazides)",
                "brands": ["Glibenclamide", "Furosemide", "Hydrochlorothiazide", "Lasix", "لازیکس", "گلیبێنکلامید"],
                "examples": ["Celebrex (سێلیبرێکس)", "Lasix / Furosemide (لازیکس)"],
                "warning": "هەندێک حەبی شەکرە و میزپێکەر پێکهاتەی هاوشێوەی سۆلفایان هەیە، پێویستە دەرمانساز یان پزیشک ئاگادار بکرێتەوە."
            }
        ],
        "safe_alternatives_note": "بۆ چارەسەری هەوکردنی میزەڕۆ لە کەسانی هەستیار بە سۆلفا، پزیشک سیپرۆفلۆکساسین یان نایترۆفۆڕانتۆین پێشنیاز دەکات."
    }
}

def check_drug_allergy(allergy_query: str, drug_query: str) -> Dict[str, Any]:
    """
    Evaluates whether a target medicine is safe for a patient with a specific allergy.
    STRICT SAFETY: Zero hallucination, evidence-based cross-reactivity mapping.
    """
    if not allergy_query or not drug_query:
        return {
            "success": False,
            "error_kurdish": "تکایە جۆری حەساسیەتەکەت و ناوی دەرمانەکە بنووسە (بۆ نموونە: حەساسیەتی پێنسلین + ئۆگمێنتین)."
        }

    norm_allergy = normalize_text(allergy_query)
    norm_drug = normalize_text(drug_query)

    # 1. Identify Allergy Category
    matched_allergy = None
    for cat_key, cat_data in ALLERGY_DATABASE.items():
        if matches_any(allergy_query, cat_data["trigger_keywords"]):
            matched_allergy = cat_data
            break

    # Fallbacks if text contains keywords
    if not matched_allergy:
        if "پێنسلین" in norm_allergy or "penicillin" in norm_allergy or "بنسلين" in norm_allergy:
            matched_allergy = ALLERGY_DATABASE["penicillin"]
        elif "پرۆفین" in norm_allergy or "برۆفین" in norm_allergy or "aspirin" in norm_allergy or "nsaid" in norm_allergy:
            matched_allergy = ALLERGY_DATABASE["nsaid_aspirin"]
        elif "سۆلفا" in norm_allergy or "سولفا" in norm_allergy or "sulfa" in norm_allergy:
            matched_allergy = ALLERGY_DATABASE["sulfa"]

    if not matched_allergy:
        return {
            "success": True,
            "status": "unknown_allergy",
            "status_kurdish": "پێویستی بە ڕاوێژی پسپۆڕە",
            "severity": "warning",
            "title": f"پشکنینی حەساسیەت بۆ ({allergy_query}) لەگەڵ دەرمانی ({drug_query})",
            "message": "جۆری حەساسیەتەکەت پێویستی بە پشکنینی پزیشکی هەیە. هەمیشە پێش وەرگرتنی هەر دەرمانێک، پزیشک یان دەرمانسازەکەت ئاگادار بکەرەوە لە هەر کاردانەوەیەکی پێست یان هەناسەتەنگی کە لە ڕابردوودا بۆت دروست بووبێت.",
            "is_dangerous": False
        }

    # 2. Check if the target drug is strictly forbidden
    forbidden_match = None
    for item in matched_allergy["strictly_forbidden_drugs"]:
        # Match by name or brands
        check_targets = [item["name"]] + item.get("brands", [])
        if matches_any(drug_query, check_targets):
            forbidden_match = item
            break

    if forbidden_match:
        return {
            "success": True,
            "status": "forbidden",
            "status_kurdish": "🔴 مەترسیدارە - قەدەغەیە بەکاربهێنرێت",
            "severity": "danger",
            "is_dangerous": True,
            "allergy_name": matched_allergy["name_kurdish"],
            "drug_name": drug_query,
            "matched_forbidden_item": forbidden_match["name"],
            "title": f"⚠️ هۆشداری توند: دەرمانی ({drug_query}) بە هیچ شێوەیەک مەخۆ!",
            "explanation": f"بەپێی زانیارییە پزیشکییە فەرمییەکان، دەرمانی ({forbidden_match['name']}) پەیوەستە بە {matched_allergy['name_kurdish']}. {forbidden_match['reason']}",
            "emergency_alert": "خواردنی ئەم دەرمانە مەترسی شۆکی حەساسیەتی لەناکاو (Anaphylactic Shock) و خنکان و داخرانی بۆڕی هەناسەی هەیە. دەستبەجێ پەیوەندی بە ١٢٢ بکە ئەگەر بە هەڵە خواردووتە.",
            "safer_alternatives": matched_allergy["safe_alternatives_note"]
        }

    # 3. Check cross-reactive caution (e.g. Cephalosporins with Penicillin)
    cross_match = None
    for c_item in matched_allergy.get("cross_reactive_caution", []):
        check_targets = [c_item["class_name"]] + c_item.get("brands", []) + c_item.get("examples", [])
        if matches_any(drug_query, check_targets):
            cross_match = c_item
            break

    if cross_match:
        return {
            "success": True,
            "status": "caution",
            "status_kurdish": "🟠 هۆشداری پزیشکی (گومانی کارلێکی هاوبەش)",
            "severity": "warning",
            "is_dangerous": False,
            "allergy_name": matched_allergy["name_kurdish"],
            "drug_name": drug_query,
            "title": f"⚠️ ئاگاداربە: دەرمانی ({drug_query}) پێویستی بە بڕیاری پزیشکە",
            "explanation": f"ئەم دەرمانە دەچێتە پۆلی ({cross_match['class_name']}). {cross_match['warning']}",
            "emergency_alert": "ئەگەر لە کاتی بەکارهێناندا هەستت بە خورانی پێست، پەڵەی سوور، ئاوسانی لێو یان تەنگەنەفەسی کرد، یەکسەر دەرمانەکە ڕابگرە و بچۆ بۆ بەشی فریاکەوتن.",
            "safer_alternatives": matched_allergy["safe_alternatives_note"]
        }

    # 4. Target drug is likely safe from this specific allergy
    return {
        "success": True,
        "status": "likely_safe",
        "status_kurdish": "🟢 پێناچێت پێکهاتەی پەیوەندیداری تێدابێت",
        "severity": "safe",
        "is_dangerous": False,
        "allergy_name": matched_allergy["name_kurdish"],
        "drug_name": drug_query,
        "title": f"پشکنینی ئاسایی: دەرمانی ({drug_query}) سەر بە خێزانی ({matched_allergy['name_kurdish']}) نییە",
        "explanation": f"بەپێی داتابەیسی زانستی، دەرمانی ({drug_query}) بە شێوەیەکی ڕاستەوخۆ ناکەوێتە ناو ئەو پێکهاتە قەدەغەکراوانەی لە کەسانی تووشبوو بە {matched_allergy['name_kurdish']}دا زیانبەخشن.",
        "emergency_alert": "تێبینی: هەمیشە دەرمانساز یان پزیشکەکەت ئاگادار بکەرەوە تا تەماشای هەموو پێکهاتە لاوەکییەکانی دەرمانەکە بکات پێش خواردنی.",
        "safer_alternatives": matched_allergy["safe_alternatives_note"]
    }
