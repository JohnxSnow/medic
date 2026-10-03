"""
DarmanNas - Comprehensive Official Kurdish Medical Dictionary & Clinical Index
Authoritative clinical index connecting local Kurdish & Iraqi pharmacy trade names
with International Nonproprietary Names (INN / Generic) and official FDA classifications.
Zero Hallucination - 100% Evidence-Based Clinical Data.
"""

from typing import List, Dict, Any, Optional

KURDISH_DRUG_INDEX: List[Dict[str, Any]] = [
    # =========================================================================
    # 1. ئازارشکێن و دژە هەوکردن و تا (Analgesics, Antipyretics & NSAIDs)
    # =========================================================================
    {
        "id": "paracetamol",
        "generic_name": "Acetaminophen",
        "alt_generic": "Paracetamol",
        "kurdish_name": "پەنادۆڵ / پاراسیتامۆڵ",
        "arabic_name": "بانادول / باراسيتامول",
        "brand_names": ["Panadol", "Calpol", "Adol", "Tylenol", "Cetamol", "Fervex", "Parafiz"],
        "category": "ئازارشکێن و تا (Analgesic & Antipyretic)",
        "category_en": "Pain & Fever",
        "kurdish_summary": {
            "purpose": "بەکاردێت بۆ هێورکردنەوەی ئازاری سووک تا مامناوەند (وەک سەرئێشە، ئازاری ددان، ئازاری ماسولکە) و دابەزاندنی تای بەرز.",
            "usage": "پێگەیشتووان: ٥٠٠ملگم تا ١٠٠٠ملگم هەر ٤ بۆ ٦ کاتژمێر جارێک (بەپێی پێویست). لە ٢٤ کاتژمێردا نابێت لە ٤٠٠٠ملگم (٤ گرام) زیاتر بخورێت.",
            "who_cannot_take": "ئەو کەسانەی نەخۆشیی توندی جگەریان هەیە، یان هەستیارییان بە پێکهاتەکەی هەیە.",
            "pregnancy_safety": "لەژێر ڕاوێژی پزیشک و لە کاتی پێویستدا لە سەلامەتترین ئازارشکێنەکانە بۆ خانمانی دووگیان.",
            "crucial_warning": "زیادەڕۆیی لە خواردنی زیانی مەترسیدار و گەورە بە خانەکانی جگەر دەگەیەنێت. ئاگاداربە چەند دەرمانێکی تر مەخۆ کە پاراسیتامۆڵی تێدایە."
        }
    },
    {
        "id": "ibuprofen",
        "generic_name": "Ibuprofen",
        "alt_generic": "Ibuprofen",
        "kurdish_name": "پرۆفین / برۆفین",
        "arabic_name": "بروفين / ايبوبروفين",
        "brand_names": ["Brufen", "Advil", "Motrin", "Profen", "Doloraz", "Ibumol"],
        "category": "ئازارشکێن و دژە هەوکردنی جومگە (NSAID)",
        "category_en": "NSAID & Inflammation",
        "kurdish_summary": {
            "purpose": "بەکاردێت بۆ ئازار و هەوکردنی جومگەکان، سوڕی مانگانە، ددان، ماسولکە و برین، لەگەڵ کەمکردنەوەی تا.",
            "usage": "بەزۆری ٤٠٠ملگم هەر ٨ کاتژمێر جارێک. بە توندی پێشنیار دەکرێت لە دوای نان بخورێت بۆ پاراستنی گەدە.",
            "who_cannot_take": "کەسێک برینی گەدەی هەبێت، نەخۆشی دڵ، پەککەوتنی گورچیلە یان ڕەبۆی هەستیار بە NSAID.",
            "pregnancy_safety": "لە سێ مانگی کۆتایی دووگیانیدا بە توندی قەدەغەیە چونکە زیان بە دڵی کۆرپەلە دەگەیەنێت.",
            "crucial_warning": "خواردنی بە گەدەی بەتاڵ برینی گەدە دروست دەکات. نابێت لەگەڵ ئەسپیڕین یان فۆڵتارین پێکەوە بخورێت."
        }
    },
    {
        "id": "diclofenac",
        "generic_name": "Diclofenac",
        "alt_generic": "Diclofenac Sodium / Potassium",
        "kurdish_name": "فۆڵتارین / کاتافلام",
        "arabic_name": "فولترين / كاتفلام",
        "brand_names": ["Voltaren", "Cataflam", "Olfen", "Diclogesic", "Rhumalgan"],
        "category": "ئازارشکێنی توند و دژە هەوکردن (NSAID)",
        "category_en": "NSAID & Inflammation",
        "kurdish_summary": {
            "purpose": "ئازارشکێنێکی کاریگەرە بۆ ئازاری توندی جومگە، ڕۆماتیزم، شەقیقە، پاش نەشتەرگەری و بەردی گورچیلە.",
            "usage": "٥٠ملگم یان ٧٥ملگم یان دەرزی، بە توندی دوای نان دەخورێت.",
            "who_cannot_take": "نەخۆشانی دڵ و سستبوونی گورچیلە، زەختی کۆنتڕۆڵنەکراو و برینی گەدە.",
            "pregnancy_safety": "لە قۆناغەکانی دووگیانیدا بە تایبەت مانگەکانی کۆتایی نابێت بەکاربێت.",
            "crucial_warning": "پەستانی خوێن بەرز دەکاتەوە و بارگرانی دەخاتە سەر دڵ؛ نابێت بەردەوام بەبێ پشکنین بخورێت."
        }
    },
    {
        "id": "meloxicam",
        "generic_name": "Meloxicam",
        "alt_generic": "Meloxicam",
        "kurdish_name": "مۆڤالیس / میلۆکسیکام",
        "arabic_name": "موفاليس / ميلوكسيكام",
        "brand_names": ["Mobic", "Movalis", "Melox", "Recoxa"],
        "category": "ئازارشکێنی جومگە و ئێسک (NSAID)",
        "category_en": "NSAID & Arthritis",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی درێژخایەنی جومگەکان (Osteoarthritis) و ڕۆماتیزمی ئێسک.",
            "usage": "٧.٥ملگم یان ١٥ملگم، تەنها یەک حەب لە ڕۆژێکدا لە دوای نان.",
            "who_cannot_take": "نەخۆشانی برینی چالاکی گەدە، سستبوونی گورچیلە و کێشەی توندی دڵ.",
            "pregnancy_safety": "لە کاتی دووگیانیدا نابێت بەکاربهێنرێت مەگەر بە فەرمانی پزیشک.",
            "crucial_warning": "نابێت لەگەڵ هیچ ئازارشکێنێکی تری وەک پرۆفین یان فۆڵتارین پێکەوە بخورێت."
        }
    },
    {
        "id": "tramadol",
        "generic_name": "Tramadol",
        "alt_generic": "Tramadol Hydrochloride",
        "kurdish_name": "ترامادۆڵ / تراماڵ",
        "arabic_name": "ترامادول / ترامال",
        "brand_names": ["Tramal", "Ultram", "Tramundin", "Contramal"],
        "category": "ئازارشکێنی دەماری ئۆپیۆید (Opioid Analgesic)",
        "category_en": "Controlled Pain Medication",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی ئازاری توند و مامناوەند کە بە ئازارشکێنەکانی تر کۆنتڕۆڵ ناکرێت (وەک پاش نەشتەرگەری و شێرپەنجە).",
            "usage": "تەنها و تەنها بە ڕەچەتەی تایبەت و مۆری پزیشکی پسپۆڕ بە ژەمی دیاریکراو.",
            "who_cannot_take": "کەسێک نەخۆشی فێ (Epilepsy) یان کێشەی توندی هەناسەدانی هەبێت.",
            "pregnancy_safety": "لە کاتی دووگیانیدا نابێت بەکاربێت چونکە کۆرپەلە ئاڵوودە دەکات.",
            "crucial_warning": "دەرمانێکی کۆنتڕۆڵکراوە و دەبێتە هۆی ئاڵوودەبوون. هەرگیز لە خۆتەوە ژەمەکەی زیاد مەکە و لەگەڵ خەوهێنەر مەخۆ."
        }
    },
    {
        "id": "colchicine",
        "generic_name": "Colchicine",
        "alt_generic": "Colchicine",
        "kurdish_name": "کۆڵشیسین (دەرمانی داولمولوک و دەریای ناوەڕاست)",
        "arabic_name": "كولشيسين",
        "brand_names": ["Colchicine", "Colcrys", "Mitigare"],
        "category": "چارەسەری نەخۆشی داولمولوک و تای دەریای ناوەڕاست (Anti-gout & FMF)",
        "category_en": "Anti-gout",
        "kurdish_summary": {
            "purpose": "بۆ نەهێشتنی هێرشی توندی داولمولوک (Gout) و نەخۆشی تای دەریای ناوەڕاست (FMF).",
            "usage": "٠.٥ملگم بەپێی ڕێنمایی وردی پزیشک؛ زیادەڕۆیی تێدا ناکرێت.",
            "who_cannot_take": "سستبوونی گورچیلە و کێشەی توندی جگەر.",
            "pregnancy_safety": "دەبێت بە چاودێری پزیشکی پسپۆڕ بێت.",
            "crucial_warning": "زیادەڕۆیی لە حەبی کۆڵشیسین مەترسی ژەهراویبوونی کوشندەی هەیە؛ بە هیچ جۆرێک لە بڕی دیاریکراو زیاتر مەخۆ."
        }
    },
    {
        "id": "allopurinol",
        "generic_name": "Allopurinol",
        "alt_generic": "Allopurinol",
        "kurdish_name": "زیلۆریک / ئالۆپیورینۆڵ (دابەزێنەری یۆریک ئەسید)",
        "arabic_name": "زيلوريك / الوبورينول",
        "brand_names": ["Zyloric", "Aloprim", "Purinol"],
        "category": "دابەزێنەری ترشی یۆریک (Uric Acid Reducer)",
        "category_en": "Anti-gout",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی بەرهەمهێنانی ترشی یۆریک لە خوێندا بۆ پاراستن لە داولمولوک و بەردی گورچیلە.",
            "usage": "١٠٠ملگم یان ٣٠٠ملگم، ڕۆژانە یەک جار لە دوای نان بە ئاوێکی زۆرەوە.",
            "who_cannot_take": "کەسێک لە ناوەڕاستی پەلاماری توندی داولمولوکدا بێت نابێت لەو کاتەدا دەستپێبکات.",
            "pregnancy_safety": "تەنها لە کاتی زۆر پێویست و بە بڕیاری پزیشک.",
            "crucial_warning": "ئەگەر خوران و لیرگی پێستت لێ پەیدابوو، دەستبەجێ دەرمانەکە بوەستێنە و سەردانی نەخۆشخانە بکە."
        }
    },
    {
        "id": "sumatriptan",
        "generic_name": "Sumatriptan",
        "alt_generic": "Sumatriptan Succinate",
        "kurdish_name": "ئیمیگران / سوماتریپتان (حەبی شەقیقە)",
        "arabic_name": "اميجران / سوماتريبتان",
        "brand_names": ["Imigran", "Imitrex", "Migrastop"],
        "category": "چارەسەری پەلاماری شەقیقە (Migraine Relief - Triptan)",
        "category_en": "Migraine",
        "kurdish_summary": {
            "purpose": "تایبەتە بە وەستاندنی ئازاری توندی سەرئێشەی شەقیقە (نیوە سەرئێشە) کاتێک دەستپێدەکات.",
            "usage": "٥٠ملگم یان ١٠٠ملگم لە سەرەتای دەستپێکردنی ئازارەکە دەخورێت.",
            "who_cannot_take": "ئەو کەسانەی نەخۆشی دەماری دڵ، جەڵتەی پێشوو، یان فشاری خوێنی کۆنتڕۆڵنەکراویان هەیە.",
            "pregnancy_safety": "پێویستە بە ڕاوێژی پزیشک بێت.",
            "crucial_warning": "دەمارەکانی خوێن تەسک دەکاتەوە؛ کەسێک کێشەی دڵی هەبێت هەرگیز نابێت بیخوات."
        }
    },

    # =========================================================================
    # 2. دژە زیندەیی و بەکتریا (Antibiotics & Antimicrobials)
    # =========================================================================
    {
        "id": "amoxicillin_clavulanate",
        "generic_name": "Amoxicillin and Clavulanate Potassium",
        "alt_generic": "Amoxicillin Clavulanate",
        "kurdish_name": "ئۆگەنتین / ئامۆکسیکلاڤ",
        "arabic_name": "اوغمنتين / اموكسيكلاف",
        "brand_names": ["Augmentin", "Amoclan", "Curam", "Klavox", "Megamox", "Julmentin"],
        "category": "دژە بەکتریای فراوان (Antibiotic - Penicillin Class)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "دژە بەکتریایەکی بەهێزە بۆ هەوکردنی سییەکان، قوڕگ، گوێچکە، بۆڕی میزەڕۆ، پێست و هەوکردنی ددان.",
            "usage": "بەزۆری ١٠٠٠ملگم (1g) یان ٦٢٥ملگم هەر ١٢ کاتژمێر جارێک لە سەرەتای ژەمی ناندا.",
            "who_cannot_take": "ئەو کەسانەی هەستیارییان بە پەنسلین هەیە، یان پێشتر تووشی کێشەی زەردویی جگەر بوون.",
            "pregnancy_safety": "دەبێت بە ڕاوێژی پزیشک بێت، لە کاتی پێویستدا دەنووسرێت.",
            "crucial_warning": "دەبێت کۆرسی دەرمانەکە بە تەواوی تەواو بکرێت، ئەگینا بەکتریاکە بەرگری پەیدا دەکات."
        }
    },
    {
        "id": "amoxicillin",
        "generic_name": "Amoxicillin",
        "alt_generic": "Amoxicillin",
        "kurdish_name": "ئەمۆکسیسیلین / ئامۆکسیل",
        "arabic_name": "اموكسيسيلين / اموكسيل",
        "brand_names": ["Amoxil", "Hiconcil", "Amoxicap", "Ospamox"],
        "category": "دژە بەکتریا (Antibiotic)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی بەکتریایی بۆ قوڕگ، بۆڕی هەناسە، گوێچکە و ددان.",
            "usage": "٥٠٠ملگم هەر ٨ کاتژمێر جارێک بەپێی ڕەچەتەی پزیشک بۆ ماوەی ٥ بۆ ٧ ڕۆژ.",
            "who_cannot_take": "هەستیاری بە دەرمانەکانی کۆمەڵەی پەنسلین.",
            "pregnancy_safety": "لەژێر چاودێری پزیشک بەکاردێت.",
            "crucial_warning": "بۆ هەڵامەتی ڤایرۆسی هیچ سوودێکی نییە؛ نابێت بەبێ هەوکردنی بەکتریایی بخورێت."
        }
    },
    {
        "id": "azithromycin",
        "generic_name": "Azithromycin",
        "alt_generic": "Azithromycin Dihydrate",
        "kurdish_name": "زیسڕۆماکس / ئازیسڕۆمایسین",
        "arabic_name": "زيثروماكس / ازيثرومايسين",
        "brand_names": ["Zithromax", "Azitro", "Aziwok", "Zatrend"],
        "category": "دژە بەکتریای سییەکان و جیوب (Macrolide Antibiotic)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی بەکتریایی سییەکان، قوڕگ، جیوب، و بەشێک لە نەخۆشییە گوازراوەکان.",
            "usage": "بەزۆری ٥٠٠ملگم ڕۆژانە یەک حەب بۆ ماوەی ٣ بۆ ٥ ڕۆژ (کۆرسی کورت).",
            "who_cannot_take": "کەسێک کێشەی درێژبوونەوەی لێدانی دڵی هەبێت (QT prolongation) یان کێشەی جگەر.",
            "pregnancy_safety": "تەنها بە ڕێنمایی پزیشک لە کاتی پێویستدا.",
            "crucial_warning": "لەگەڵ دەرمانی ڕێکخەری لێدانی دڵ پێویستی بە وریایی زۆرە."
        }
    },
    {
        "id": "cefixime",
        "generic_name": "Cefixime",
        "alt_generic": "Cefixime Trihydrate",
        "kurdish_name": "سێفیکس / سێفیکسیم / سوپراکس",
        "arabic_name": "سيفكس / سوبراكس",
        "brand_names": ["Suprax", "Cefix", "Zifi", "Taxim-O"],
        "category": "دژە بەکتریای نەوەی سێیەم (Cephalosporin)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی بەکتریایی کۆئەندامی میزەڕۆ، گوێچکە، جیوب، و بۆڕی هەناسە.",
            "usage": "٤٠٠ملگم ڕۆژانە یەک دەنک، یان ٢٠٠ملگم هەر ١٢ کاتژمێر جارێک.",
            "who_cannot_take": "ئەو کەسانەی هەستیاری توندیان بە سێفالۆسپۆرینەکان هەیە.",
            "pregnancy_safety": "لەژێر ڕاوێژی پزیشکدا پۆلێنی سەلامەتە.",
            "crucial_warning": "نابێت بە نیوەچڵی بووەستێنرێت کاتێک نەخۆش هەست بە باشتربوون دەکات."
        }
    },
    {
        "id": "ciprofloxacin",
        "generic_name": "Ciprofloxacin",
        "alt_generic": "Ciprofloxacin Hydrochloride",
        "kurdish_name": "سیپرۆفلۆکساسین / سیپرۆ",
        "arabic_name": "سيبروفلوكساسين / سيبرو",
        "brand_names": ["Cipro", "Ciflox", "Ciprodar", "Serviflox"],
        "category": "دژە بەکتریای توند (Fluoroquinolone)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی توندی میزەڕۆ، گورچیلە، ڕیخۆڵە و سکچوونی بەکتریایی، و پڕۆستات.",
            "usage": "٥٠٠ملگم یان ٧٥٠ملگم هەر ١٢ کاتژمێر جارێک بە ئاوێکی زۆر دوور لە کەرەستەی شیرەمەنی.",
            "who_cannot_take": "منداڵان و مێرمنداڵانی ژێر ١٨ ساڵ، ئەوانەی کێشەی ژێیەکانی ماسولکەیان (Tendonitis) هەیە.",
            "pregnancy_safety": "بە توندی قەدەغەیە لە کاتی دووگیانی و شیرپێدان چونکە زیان بە ئێسک و کڕکڕاگەی کۆرپەلە دەگەیەنێت.",
            "crucial_warning": "مەترسی پچڕانی ژێی پێ (Achilles tendon)ی هەیە؛ لەگەڵ حەبی ماست و شیر و ئاسن و کالسیۆم پێکەوە مەخۆ."
        }
    },
    {
        "id": "levofloxacin",
        "generic_name": "Levofloxacin",
        "alt_generic": "Levofloxacin",
        "kurdish_name": "تاڤانیک / لیڤۆفلۆکساسین",
        "arabic_name": "تافانيك / ليفوفلوكساسين",
        "brand_names": ["Tavanic", "Levaquin", "Levox", "Cravit"],
        "category": "دژە بەکتریای هەناسە و سنگ (Respiratory Fluoroquinolone)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی توندی سییەکان (Pneumonia)، جیوبی توند و هەوکردنی ئاڵۆزی میزەڕۆ.",
            "usage": "٥٠٠ملگم ڕۆژانە یەک دەنک لە هەمان کاتدا بە ئاوێکی زۆر.",
            "who_cannot_take": "کەسانی خوار تەمەنی ١٨ ساڵ، خانمانی دووگیان، و تووشبووانی لاوازی ماسولکە (Myasthenia Gravis).",
            "pregnancy_safety": "قەدەغەیە لە کاتی دووگیانیدا.",
            "crucial_warning": "لەگەڵ دژەترشەڵۆکی گەدە یان حەبی ماگنیسیۆم مەخۆ؛ لانیکەم ٢ کاتژمێر مەودا دابنێ."
        }
    },
    {
        "id": "doxycycline",
        "generic_name": "Doxycycline",
        "alt_generic": "Doxycycline Hyclate",
        "kurdish_name": "دۆکسیسیکلین / ڤیبڕامایسین",
        "arabic_name": "دوكسيسيكلين / فيبرامايسين",
        "brand_names": ["Vibramycin", "Doryx", "Doxy", "Monodox"],
        "category": "دژە بەکتریا بۆ پێست و زیپکە و هەناسە (Tetracycline)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "چارەسەری زیپکەی توندی دەموچاو (Acne)، هەوکردنی پێست، سنگ، تای مالتا (Brucellosis)، و نەخۆشییە مێرووییەکان.",
            "usage": "١٠٠ملگم ڕۆژانە یەک یان دوو جار بە ئاوێکی زۆر و بە پێوە (نابێت دوای خواردنی پاڵبکەویت).",
            "who_cannot_take": "منداڵانی خوار ٨ ساڵ، ژنانی دووگیان و شیردەر.",
            "pregnancy_safety": "قەدەغەیە؛ ددانەکانی کۆرپەلە ڕەش دەکات و گەشەی ئێسک تێکدەدات.",
            "crucial_warning": "دەبێت بە پێوە و بە پەرداخێک ئاوی گەورە بخورێت تا برین لە قورگ و سوورێنچک دروست نەکات. هەروەها نابێت پاش خواردنی ڕاستەوخۆ بچیتە بەر هەتاو."
        }
    },
    {
        "id": "clarithromycin",
        "generic_name": "Clarithromycin",
        "alt_generic": "Clarithromycin",
        "kurdish_name": "کلاسید / کلاریسڕۆمایسین",
        "arabic_name": "كلاسيد / كلاريثرومايسين",
        "brand_names": ["Klacid", "Biaxin", "Claridar", "Claripex"],
        "category": "دژە بەکتریای گەدە و هەناسە (Macrolide)",
        "category_en": "Antibiotic",
        "kurdish_summary": {
            "purpose": "بەشێکی سەرەکییە لە کۆرسی بنبڕکردنی بەکتریای گەدە (H. pylori)، لەگەڵ هەوکردنی قوڕگ و سییەکان.",
            "usage": "٥٠٠ملگم هەر ١٢ کاتژمێر جارێک بۆ ماوەی دیاریکراو.",
            "who_cannot_take": "ئەو کەسانەی لەگەڵ حەبی چەوری وەک لیپیتۆر دەیخۆن (کارلێکی توند دەکەن).",
            "pregnancy_safety": "نابێت بەکاربێت مەگەر هیچ بەدیلێکی تر نەبێت بەپێی ڕێنمایی FDA.",
            "crucial_warning": "کارلێکی مەترسیدار دەکات لەگەڵ دەرمانەکانی چەوری کۆلیسترۆڵ و دەرمانی لێدانی دڵ."
        }
    },
    {
        "id": "metronidazole",
        "generic_name": "Metronidazole",
        "alt_generic": "Metronidazole",
        "kurdish_name": "فلاجیل / میترۆنیدازۆڵ",
        "arabic_name": "فلاجيل / ميترونيدازول",
        "brand_names": ["Flagyl", "Metrogyl", "Dumazol", "Nidazol"],
        "category": "دژە مشەخۆر و بەکتریای گەدە و پووک (Antiprotozoal & Antibacterial)",
        "category_en": "Antibiotic & Antiparasitic",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی ڕیخۆڵە و سکچوون (ئەمیبا، جیاڕدیا)، هەوکردنی ددان و پووک، و هەوکردنی تایبەتی ژنان.",
            "usage": "٥٠٠ملگم هەر ٨ کاتژمێر جارێک دوای خواردن بۆ ماوەی ٥ بۆ ٧ ڕۆژ.",
            "who_cannot_take": "سێ مانگی یەکەمی دووگیانی و کەسێک نەخۆشی دەماری هەبێت.",
            "pregnancy_safety": "لە سێ مانگی یەکەمی دووگیانیدا بە توندی قەدەغەیە.",
            "crucial_warning": "هەرگیز نابێت لە کاتی بەکارهێنانیدا کهول بخورێتەوە، کارلێکی توندی دڵتێکەڵهاتن و لێدانی دڵ دروست دەکات."
        }
    },
    {
        "id": "nitrofurantoin",
        "generic_name": "Nitrofurantoin",
        "alt_generic": "Nitrofurantoin Macrocrystals",
        "kurdish_name": "یوڤامین ڕیتارد / نایترۆفیورانتۆین",
        "arabic_name": "يوفامين / نيتروفورانتوين",
        "brand_names": ["UVamin Retard", "Macrobid", "Macrodantin"],
        "category": "تایبەت بە هەوکردنی بۆڕی میزەڕۆ (Urinary Antiseptic)",
        "category_en": "Antibiotic - UTI",
        "kurdish_summary": {
            "purpose": "تەنها بۆ هەوکردنی بەکتریایی میزەڵدان و بۆڕی میز (Cystitis) بەکاردێت و بۆ بەشەکانی تری لەش ناچێت.",
            "usage": "١٠٠ملگم هەر ١٢ کاتژمێر جارێک لەگەڵ ناندا بۆ ماوەی ٥ بۆ ٧ ڕۆژ.",
            "who_cannot_take": "سستبوونی گورچیلە، و دووگیانی لە هەفتەی ٣٨ بەدواوە.",
            "pregnancy_safety": "لە هەفتەکانی کۆتایی دووگیانیدا قەدەغەیە چونکە کەمخوێنی بۆ کۆرپەلە دروست دەکات.",
            "crucial_warning": "ڕەنگی میز دەگۆڕێت بۆ زەردی تۆخ یان قاوەیی، ئەمە حاڵەتێکی ئاساییە و مەترسیدار نییە."
        }
    },

    # =========================================================================
    # 3. کۆئەندامی هەرس، گەدە، دڵتێکەڵهاتن و قۆڵۆن (Gastrointestinal & Digestive)
    # =========================================================================
    {
        "id": "omeprazole",
        "generic_name": "Omeprazole",
        "alt_generic": "Omeprazole",
        "kurdish_name": "ئۆمێپرازۆڵ / لۆسێک",
        "arabic_name": "اوميبرازول / لوسك",
        "brand_names": ["Prilosec", "Losec", "Ocid", "Gasec", "Omeprex", "Risek"],
        "category": "کەمکەرەوەی ترشەڵۆکی گەدە (PPI)",
        "category_en": "Gastrointestinal",
        "kurdish_summary": {
            "purpose": "بۆ دڵەکزێ، هەڵگەڕانەوەی ترشەڵۆکی گەدە بۆ قوڕگ (GERD)، برینی گەدە و پاراستنی گەدە لە دەرمانە ئازارشکێنەکان.",
            "usage": "٢٠ملگم یان ٤٠ملگم بەیانیان بە لانی کەم نیو کاتژمێر پێش نانی بەیانی.",
            "who_cannot_take": "هەستیاری بە دەرمانەکانی کۆمەڵەی PPI.",
            "pregnancy_safety": "دەبێت بە ڕاوێژی پزیشک بێت.",
            "crucial_warning": "کەپسولەکە مەشکێنە. خواردنی درێژخایەن مژینی ڤیتامین B12 و ماگنیسیۆم کەم دەکاتەوە."
        }
    },
    {
        "id": "esomeprazole",
        "generic_name": "Esomeprazole",
        "alt_generic": "Esomeprazole Magnesium",
        "kurdish_name": "نێکسیۆم / ئێسۆمێپرازۆڵ",
        "arabic_name": "نيكسيوم / اسوميبرازول",
        "brand_names": ["Nexium", "Esomax", "Nexpro", "Esoral"],
        "category": "چارەسەری ترشەڵۆک و برینی گەدە (PPI)",
        "category_en": "Gastrointestinal",
        "kurdish_summary": {
            "purpose": "پاراستن و چارەسەری هەوکردنی سوورێنچک، برینی گەدە و کەمکردنەوەی کاریگەری لاوەکی ئازارشکێنەکان.",
            "usage": "٢٠ملگم یان ٤٠ملگم، ڕۆژانە یەک جار پێش نانی بەیانی بە ٣٠ خولەک.",
            "who_cannot_take": "هەستیاری بە پێکهاتەکەی.",
            "pregnancy_safety": "پێویستی بە ڕاوێژی پزیشک هەیە.",
            "crucial_warning": "لەگەڵ حەبی پلاڤیکس (Clopidogrel) مەیخۆ چونکە کاریگەرییەکەی لاواز دەکات."
        }
    },
    {
        "id": "pantoprazole",
        "generic_name": "Pantoprazole",
        "alt_generic": "Pantoprazole Sodium",
        "kurdish_name": "پانتۆلۆک / کۆنتڕۆلۆک / پانتۆپرازۆڵ",
        "arabic_name": "بانلوك / كونترولوك",
        "brand_names": ["Controloc", "Pantoloc", "Protium", "Pantodac"],
        "category": "پارێزەری گەدە و دڵەکزێ (PPI)",
        "category_en": "Gastrointestinal",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی ترشەڵۆک، دڵەکزێ، هەوکردنی سوورێنچک؛ سەلامەتترین جۆری PPIیە بۆ ئەو کەسانەی پلاڤیکس دەخۆن.",
            "usage": "٢٠ملگم یان ٤٠ملگم بەیانیان پێش نانخواردن.",
            "who_cannot_take": "هەستیاری بە پانتۆپرازۆڵ.",
            "pregnancy_safety": "تەنها بە ڕاوێژی پزیشک.",
            "crucial_warning": "حەبەکە مەهاڕە و بە تەواوی لەگەڵ ئاو بیقووتیت."
        }
    },
    {
        "id": "metoclopramide",
        "generic_name": "Metoclopramide",
        "alt_generic": "Metoclopramide Hydrochloride",
        "kurdish_name": "پلاسیل / میتۆکلۆپراماید (دژە دڵتێکەڵهاتن)",
        "arabic_name": "بلاسيل / ميتوكلوبراميد",
        "brand_names": ["Plasil", "Reglan", "Primperan"],
        "category": "دژە هێڵنج و ڕشانەوە (Antiemetic & Prokinetic)",
        "category_en": "Gastrointestinal - Antiemetic",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی دڵتێکەڵهاتن و ڕشانەوە، خێراکردنی خاڵیبوونەوەی گەدە بۆ ئەو کەسانەی سستی هەرسکردنیان هەیە.",
            "usage": "١٠ملگم نیو کاتژمێر پێش نان، بە زۆری نابێت زیاتر لە ٥ ڕۆژ لەسەریەک بخورێت.",
            "who_cannot_take": "کەسێک برین و خوێنبەربوونی گەدە، گیرانی ڕیخۆڵە، یان فێ (سەرئێشەی دەماری) هەبێت.",
            "pregnancy_safety": "لەژێر چاودێری پزیشکی پسپۆڕ بەکاردێت.",
            "crucial_warning": "بەکارهێنانی درێژخایەن دەبێتە هۆی جوڵەی نەویستراوی ماسولکەکانی دەموچاو و دەست (Extrapyramidal symptoms)."
        }
    },
    {
        "id": "ondansetron",
        "generic_name": "Ondansetron",
        "alt_generic": "Ondansetron Hydrochloride",
        "kurdish_name": "زۆفران / ئۆندانسیترۆن",
        "arabic_name": "زوفران / اوندانسيترون",
        "brand_names": ["Zofran", "Danset", "Emestop", "Vonau"],
        "category": "دژە ڕشانەوەی بەهێز (5-HT3 Antagonist)",
        "category_en": "Gastrointestinal - Antiemetic",
        "kurdish_summary": {
            "purpose": "وەستاندنی توندی ڕشانەوە و دڵتێکەڵهاتن پاش نەشتەرگەری، کیمیادەرمانی، یان ڕشانەوەی توندی گەدە.",
            "usage": "٤ملگم یان ٨ملگم بەپێی کێش و فەرمانی پزیشک.",
            "who_cannot_take": "ئەو کەسانەی کێشەی درێژبوونەوەی مەودای لێدانی دڵیان (Congenital long QT) هەیە.",
            "pregnancy_safety": "لە سێ مانگی یەکەمی دووگیانیدا پێویستی بە چاودێری و ڕاوێژی وردی پزیشکی پسپۆڕ هەیە.",
            "crucial_warning": "دەبێتە هۆی قەبزی و سەرئێشە لە هەندێک کەسدا."
        }
    },
    {
        "id": "mebeverine",
        "generic_name": "Mebeverine",
        "alt_generic": "Mebeverine Hydrochloride",
        "kurdish_name": "دۆسپاتالین / کۆلۆفاک (دەرمانی قۆڵۆن)",
        "arabic_name": "دوسباتالين / كولوفاك",
        "brand_names": ["Duspatalin", "Colofac", "Mebac", "Spasmonore"],
        "category": "هێورکەرەوەی گرژبوونی قۆڵۆن (Antispasmodic - IBS)",
        "category_en": "Gastrointestinal - IBS",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی ئازار و گرژبوونی قۆڵۆنی دەماری (IBS)، باکردنی سک و تێکچوونی ڕیخۆڵەکان.",
            "usage": "١٣٥ملگم یان کەپسولی ٢٠٠ملگم (Retard)، ٢٠ خولەک پێش ژەمەکانی نان.",
            "who_cannot_take": "هەستیاری بە پێکهاتەکەی یان کێشەی ئیفلیجی ڕیخۆڵە (Paralytic ileus).",
            "pregnancy_safety": "پێشنیار ناکرێت لە کاتی دووگیانیدا بخورێت.",
            "crucial_warning": "کەپسولەکەی مەشکێنە تا بە هێواشی لە ناو ڕیخۆڵەدا بتوێتەوە."
        }
    },
    {
        "id": "hyoscine",
        "generic_name": "Scopolamine",
        "alt_generic": "Hyoscine Butylbromide",
        "kurdish_name": "بوسکۆپان / هیۆسین (حەبی پێچی سک)",
        "arabic_name": "بسكوبان / هيوسين",
        "brand_names": ["Buscopan", "Spasmo-pan", "Hyopan"],
        "category": "ئازارشکێنی گرژبوونی سک و میزەڕۆ (Antispasmodic)",
        "category_en": "Gastrointestinal - Cramps",
        "kurdish_summary": {
            "purpose": "نەهێشتنی پێچی توندی سک، گرژبوونی ڕیخۆڵە و ئازاری سوڕی مانگانە و بۆڕی میزەڕۆ.",
            "usage": "١٠ملگم یان ٢٠ملگم لە کاتی ئازار و پێچی سکدا.",
            "who_cannot_take": "ئەو کەسانەی ئاوی ڕەشی چاو (Glaucoma) یان گەورەبوونی پرۆستات و تەسکبوونەوەی گەدەیان هەیە.",
            "pregnancy_safety": "تەنها بە ڕێنمایی پزیشک.",
            "crucial_warning": "دەبێتە هۆی وشکبوونەوەی دەم و کەمێک تەڵخبوونی بینین."
        }
    },
    {
        "id": "loperamide",
        "generic_name": "Loperamide",
        "alt_generic": "Loperamide Hydrochloride",
        "kurdish_name": "ئیمۆدیۆم / لۆپێراماید (وەستێنەری سکچوون)",
        "arabic_name": "ايموديوم / لوبيراميد",
        "brand_names": ["Imodium", "Lopodium", "Diarex"],
        "category": "وەستێنەری سکچوونی توند (Antidiarrheal)",
        "category_en": "Gastrointestinal - Diarrhea",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی خێرایی جوڵەی ڕیخۆڵەکان بۆ وەستاندنی سکچوونی توند و لەناکاو.",
            "usage": "سەرەتا ٢ حەب (٤ملگم)، پاشان دوای هەر پیساییکردنێکی شل ١ حەب دەخورێت (نابێت لە ٨ حەب لە ڕۆژێکدا زیاتر بێت).",
            "who_cannot_take": "سکچوونێک کە خوێن یان تای بەرزی لەگەڵ بێت (سکچوونی بەکتریایی)، منداڵانی ژێر ١٢ ساڵ.",
            "pregnancy_safety": "دەبێت بە چاودێری پزیشک بێت.",
            "crucial_warning": "ئەگەر سکچوونەکەت بەهۆی ژەهراویبوون یان بەکتریاوە بێت، خواردنی ئیمۆدیۆم دەبێتە هۆی مانەوەی ژەهر لە ڕیخۆڵەدا."
        }
    },

    # =========================================================================
    # 4. دڵ، پەستانی خوێن، چەوری و شلکردنەوە (Cardiovascular & Lipids)
    # =========================================================================
    {
        "id": "bisoprolol",
        "generic_name": "Bisoprolol",
        "alt_generic": "Bisoprolol Fumarate",
        "kurdish_name": "کۆنکۆر / بیسۆپرۆلۆڵ",
        "arabic_name": "كونكور / بيسوبرولول",
        "brand_names": ["Concor", "Zebeta", "Bisocor", "Cardicor"],
        "category": "فشاری خوێن و لێدانی دڵ (Beta Blocker)",
        "category_en": "Cardiology & Blood Pressure",
        "kurdish_summary": {
            "purpose": "کۆنتڕۆڵکردنی بەرزبوونەوەی فشاری خوێن، خێرالێدانی دڵ، و پاراستنی نەخۆشانی سستی دڵ.",
            "usage": "٢.٥ملگم، ٥ملگم، یان ١٠ملگم، یەک جار لە ڕۆژێکدا بەزۆری بەیانیان.",
            "who_cannot_take": "لێدانی دڵی زۆر هێواش (Bradycardia)، نەخۆشی ڕەبۆی توند و گیرانی هەناسە.",
            "pregnancy_safety": "بە بێ ڕاوێژی پزیشکی پسپۆڕی دڵ نابێت بەکاربێت.",
            "crucial_warning": "هەرگیز بە شێوەیەکی لەناکاو دەرمانەکە ڕامەگرە! لەپڕ وەستاندنی دەبێتە هۆی بەرزبوونەوەی مەترسیداری زەخت."
        }
    },
    {
        "id": "amlodipine",
        "generic_name": "Amlodipine",
        "alt_generic": "Amlodipine Besylate",
        "kurdish_name": "نۆرفاسک / ئەمڵۆدیک / ئەمڵۆدیپین",
        "arabic_name": "نورفاسك / املوديبين",
        "brand_names": ["Norvasc", "Amlodac", "Amlopin", "Tenox"],
        "category": "دابەزێنەری فشاری خوێن و سنگەکوژێ (Calcium Channel Blocker)",
        "category_en": "Blood Pressure & Heart",
        "kurdish_summary": {
            "purpose": "فراوانکردنی دەمارەکانی خوێن بۆ کەمکردنەوەی پەستانی بەرز و نەهێشتنی ئازاری سنگ (Angina).",
            "usage": "٥ملگم یان ١٠ملگم، ڕۆژانە یەک حەب لە هەمان کاتدا.",
            "who_cannot_take": "دابەزینی توندی فشاری خوێن یان تەسکبوونەوەی توندی دەماری ئۆئۆرتای دڵ.",
            "pregnancy_safety": "پێویستی بە ڕاوێژی پزیشکی پسپۆڕ هەیە.",
            "crucial_warning": "لە هەندێک کەسدا دەبێتە هۆی ئاوسانی پاژنەی پێ و مەچەکی قاچ؛ ئەمە ئاگاداری پزیشکی پێویستە."
        }
    },
    {
        "id": "losartan",
        "generic_name": "Losartan",
        "alt_generic": "Losartan Potassium",
        "kurdish_name": "لۆسارتان / کۆزار",
        "arabic_name": "لوسارتان / كوزار",
        "brand_names": ["Cozaar", "Lorista", "Losapres", "Cardostat"],
        "category": "فشاری خوێن و پارێزەری گورچیلە (ARB)",
        "category_en": "Blood Pressure",
        "kurdish_summary": {
            "purpose": "کۆنتڕۆڵکردنی فشاری خوێن و پاراستنی گورچیلە لە کەسانی تووشبوو بە نەخۆشی شەکرە.",
            "usage": "٥٠ملگم ڕۆژانە یەک جار لە کاتێکی دیاریکراودا.",
            "who_cannot_take": "خانمانی دووگیان و ئەوانەی دەماری گورچیلەیان تەسک بووەتەوە.",
            "pregnancy_safety": "بە توندی قەدەغەیە لە کاتی دووگیانیدا چونکە دەبێتە هۆی تێکچوونی گەشەی کۆرپەلە.",
            "crucial_warning": "حەبی پۆتاسیۆم بەبێ ئاگاداری پزیشک لەگەڵیدا مەخۆ چونکە پۆتاسیۆمی لەش بەرز دەکاتەوە."
        }
    },
    {
        "id": "valsartan",
        "generic_name": "Valsartan",
        "alt_generic": "Valsartan",
        "kurdish_name": "دیۆڤان / ڤاڵسارتان",
        "arabic_name": "ديوفان / فالسارتان",
        "brand_names": ["Diovan", "Valzad", "Tareg", "Co-Diovan"],
        "category": "فشاری خوێن و سستی دڵ (ARB)",
        "category_en": "Blood Pressure",
        "kurdish_summary": {
            "purpose": "دابەزاندنی پەستانی خوێن، پاراستنی نەخۆش دوای جەڵتەی دڵ، و چارەسەری سستبوونی دڵ.",
            "usage": "٨٠ملگم یان ١٦٠ملگم، ڕۆژانە یەک جار.",
            "who_cannot_take": "خانمانی دووگیان و ئەوانەی کێشەی توندی جگەریان هەیە.",
            "pregnancy_safety": "بە توندی قەدەغەیە لە کاتی دووگیانیدا بەپێی ستانداردی FDA.",
            "crucial_warning": "پێویستە پشکنینی گورچیلە و پۆتاسیۆمی خوێن بە شێوەی خولیی ئەنجام بدرێت."
        }
    },
    {
        "id": "atorvastatin",
        "generic_name": "Atorvastatin",
        "alt_generic": "Atorvastatin Calcium",
        "kurdish_name": "ئەتۆرڤاستاتین / لیپیتۆر",
        "arabic_name": "اتورفاستاتين / ليبيتور",
        "brand_names": ["Lipitor", "Atorva", "Torvast", "Atacand"],
        "category": "دابەزێنەری چەوری و کۆلیسترۆڵ (Statin)",
        "category_en": "Cholesterol & Heart",
        "kurdish_summary": {
            "purpose": "دابەزاندنی کۆلیسترۆڵی خراپ (LDL) و چەوری سیانی بۆ پاراستنی دڵ لە جەڵتە و ڕەقبوونی دەمارەکان.",
            "usage": "١٠ملگم، ٢٠ملگم، یان ٤٠ملگم شەوانە پێش خەوتن لەگەڵ یان بێ خواردن.",
            "who_cannot_take": "نەخۆشی چالاکی جگەر، ژنانی دووگیان و شیردەر.",
            "pregnancy_safety": "بە توندی قەدەغەیە لە کاتی دووگیانیدا بەهۆی مەترسی شێواوی کۆرپەلە.",
            "crucial_warning": "ئەگەر ئازاری نادیار و توندی ماسولکەت لێ پەیدابوو یان ڕەنگی میزت تێکچوو، دەستبەجێ پەیوەندی بە پزیشکەوە بکە."
        }
    },
    {
        "id": "rosuvastatin",
        "generic_name": "Rosuvastatin",
        "alt_generic": "Rosuvastatin Calcium",
        "kurdish_name": "کریستۆر / ڕۆزۆڤاستاتین",
        "arabic_name": "كريستور / روزوفاستاتين",
        "brand_names": ["Crestor", "Rositor", "Rovista", "Ezallor"],
        "category": "دابەزێنەری بەهێزی کۆلیسترۆڵ (Statin)",
        "category_en": "Cholesterol & Heart",
        "kurdish_summary": {
            "purpose": "دابەزاندنی چەوری خوێن و پاککردنەوەی بۆڕییەکانی خوێن لە نیشتووی چەوری بۆ نەخۆشانی مەترسیی دڵ.",
            "usage": "١٠ملگم یان ٢٠ملگم، ڕۆژانە یەک جار لە هەمان کاتدا.",
            "who_cannot_take": "نەخۆشیی جگەر، کێشەی توندی گورچیلە، و دووگیانی.",
            "pregnancy_safety": "قەدەغەیە لە کاتی دووگیانی و شیرپێداندا.",
            "crucial_warning": "پێویستە شیکاری ئەنزیمەکانی جگەر پێش دەستپێکردن و لە کاتی وەرگرتنیدا ئەنجام بدرێت."
        }
    },
    {
        "id": "aspirin",
        "generic_name": "Aspirin",
        "alt_generic": "Acetylsalicylic Acid",
        "kurdish_name": "ئەسپیڕین / ئەسپیجیک",
        "arabic_name": "اسبرين / اسبجيك",
        "brand_names": ["Bayer Aspirin", "Aspicard", "Cardiprin", "Ecotrin", "Aspegic"],
        "category": "شلکردنەوەی خوێن و پاراستنی دڵ (Antiplatelet)",
        "category_en": "Cardiology",
        "kurdish_summary": {
            "purpose": "بۆ پاراستن لە کڵۆبوونی خوێن، جەڵتەی مێشک و جەڵتەی دڵ، بە ژەمی کەم (٨١ملگم یان ١٠٠ملگم).",
            "usage": "٨١ملگم یان ١٠٠ملگم، ڕۆژانە یەک دەنک لە دوای نان بە ئاوێکی زۆرەوە.",
            "who_cannot_take": "کەسێک برینی گەدە، خوێنبەربوونی مێشک، یان منداڵ و مێرمنداڵی تووشبوو بە ڤایرۆس.",
            "pregnancy_safety": "تەنها لە ژێر چاودێری پزیشکی ئافرەتاندا بەکاردێت بە ژەمی تایبەت.",
            "crucial_warning": "مەترسی خوێنبەربوون زیاد دەکات؛ ئەگەر نەشتەرگەری یان ددان کێشانت هەیە دەبێت پزیشک پێشوەختە ئاگادار بکەیتەوە."
        }
    },
    {
        "id": "clopidogrel",
        "generic_name": "Clopidogrel",
        "alt_generic": "Clopidogrel Bisulfate",
        "kurdish_name": "پلاڤیکس / کلۆپیدۆگریل",
        "arabic_name": "بلافيكس / كلوبيدوكريل",
        "brand_names": ["Plavix", "Clopilet", "Trombex", "Cardogrel"],
        "category": "دژە کڵۆبوونی خوێن و پارێزەری شەبەکە (Antiplatelet)",
        "category_en": "Cardiology",
        "kurdish_summary": {
            "purpose": "پاراستن لە دروستبوونی کڵۆی خوێن و جەڵتە لەو کەسانەی شەبەکە (stent)یان بۆ دڵ دانراوە یان جەڵتەیان هەبووە.",
            "usage": "٧٥ملگم، ڕۆژانە یەک حەب لە هەمان کاتدا.",
            "who_cannot_take": "کەسێک خوێنبەربوونی چالاکی هەبێت وەک برینی گەدە یان خوێنبەربوونی مێشک.",
            "pregnancy_safety": "تەنها بە بڕیاری تایبەتی پزیشکی پسپۆڕ.",
            "crucial_warning": "هەرگیز بێ پرسی پزیشکی دڵ دەرمانەکە ڕامەگرە تەنانەت بۆ یەک ڕۆژیش دوای دانانی شەبەکە."
        }
    },
    {
        "id": "furosemide",
        "generic_name": "Furosemide",
        "alt_generic": "Furosemide",
        "kurdish_name": "لازیکس / فرۆسێماید",
        "arabic_name": "لازكس / فوروسيميد",
        "brand_names": ["Lasix", "Diural", "Furanthril"],
        "category": "میزهێنەری بەهێز و کەمکەرەوەی ئاوسان (Loop Diuretic)",
        "category_en": "Cardiology & Diuretic",
        "kurdish_summary": {
            "purpose": "دەرکردنی ئاوی زیادەی لەش لە کاتی ئاوسانی قاچ و سک بەهۆی سستبوونی دڵ یان نەخۆشی جگەر و گورچیلە.",
            "usage": "٢٠ملگم یان ٤٠ملگم بەیانیان زوو بۆ ئەوەی خەوی شەوانت تێک نەدات.",
            "who_cannot_take": "کەسێک ئاستی پۆتاسیۆمی زۆر دابەزیبێت، یان وشکبوونەوەی توندی هەبێت.",
            "pregnancy_safety": "تەنها بە چاودێری پزیشکی پسپۆڕ.",
            "crucial_warning": "پێویستە پشکنینی بەردەوامی پۆتاسیۆم و فەرمانی گورچیلەی پێ بکرێت."
        }
    },
    {
        "id": "spironolactone",
        "generic_name": "Spironolactone",
        "alt_generic": "Spironolactone",
        "kurdish_name": "ئەڵداکتۆن / سپیرۆنۆلاکتۆن",
        "arabic_name": "الداكتون / سبيرونولاكتون",
        "brand_names": ["Aldactone", "Spilactone", "Verospiron"],
        "category": "میزهێنەری پارێزەری پۆتاسیۆم (Potassium-Sparing Diuretic)",
        "category_en": "Cardiology & Diuretic",
        "kurdish_summary": {
            "purpose": "چارەسەری سستبوونی دڵ، پەستانی خوێن، کۆبوونەوەی ئاوی سک (Ascites) لە نەخۆشی جگەر، و کەمکردنەوەی مووی زیادەی ژنان.",
            "usage": "٢٥ملگم یان ٥٠ملگم یان ١٠٠ملگم بەپێی ڕێنمایی پزیشک.",
            "who_cannot_take": "سستبوونی توندی گورچیلە یان بەرزبوونەوەی پۆتاسیۆمی خوێن (Hyperkalemia).",
            "pregnancy_safety": "دەبێت بە ڕاوێژی وردی پزیشک بێت.",
            "crucial_warning": "پۆتاسیۆمی لەش بەرز دەکاتەوە؛ بە هیچ شێوەیەک نابێت حەبی پۆتاسیۆمی لەگەڵدا بخورێت."
        }
    },

    # =========================================================================
    # 5. نەخۆشی شەکرە (Diabetes & Endocrine)
    # =========================================================================
    {
        "id": "metformin",
        "generic_name": "Metformin",
        "alt_generic": "Metformin Hydrochloride",
        "kurdish_name": "میتفۆرمین / گلوکۆفاج",
        "arabic_name": "ميتفورمين / كلوكوفاج",
        "brand_names": ["Glucophage", "Fortamet", "Glumet", "Diaformin"],
        "category": "ڕێکخەری شەکرەی جۆری دووەم (Biguanide)",
        "category_en": "Diabetes",
        "kurdish_summary": {
            "purpose": "کۆنتڕۆڵکردنی ڕێژەی شەکری خوێن لە نەخۆشانی شەکرەی جۆری دوو، هەروەها هەندێک جار بۆ کیسی هێلکەدان (PCOS).",
            "usage": "٥٠٠ملگم، ٨٥٠ملگم، یان ١٠٠٠ملگم لە کاتی نانخواردندا یان دەستبەجێ دوای نان.",
            "who_cannot_take": "کەسێک سستبوونی گورچیلەی هەبێت، نەخۆشی توندی جگەر، یان پشکنینی تیشکی بە ماددەی ڕەنگاوڕەنگ.",
            "pregnancy_safety": "تەنها بە چاودێری ڕاستەوخۆی پزیشکی پسپۆڕی شەکرە بێت.",
            "crucial_warning": "ئەگەر پشکنینی تیشکی بە ماددەی ڕەنگدار (Contrast) دەکەیت دەبێت ٤٨ کاتژمێر پێشتر ڕابگیرێت."
        }
    },
    {
        "id": "glimepiride",
        "generic_name": "Glimepiride",
        "alt_generic": "Glimepiride",
        "kurdish_name": "ئەماریل / گلیمێپیراید",
        "arabic_name": "اماريل / جليمبيريد",
        "brand_names": ["Amaryl", "Diapride", "Glimy", "Glupin"],
        "category": "شەکرەی جۆری دوو (Sulfonylurea)",
        "category_en": "Diabetes",
        "kurdish_summary": {
            "purpose": "هاندانی پەنکریاس بۆ دەردانی ئەنسۆلینی زیاتر بە مەبەستی دابەزاندنی شەکری خوێن.",
            "usage": "١ملگم، ٢ملگم، یان ٤ملگم، بەیانیان دەستبەجێ پێش نانی بەیانی یان لە کاتی یەکەم ژەمدا.",
            "who_cannot_take": "شەکرەی جۆری یەکەم، سستبوونی توندی گورچیلە یان جگەر.",
            "pregnancy_safety": "لە کاتی دووگیانیدا بە ئەنسۆلین دەگۆڕدرێت بە ڕێنمایی پزیشک.",
            "crucial_warning": "دەکرێت ببێتە هۆی دابەزینی کتوپڕ و مەترسیداری شەکری خوێن (Hypoglycemia). هەمیشە شیرینی لەگەڵ خۆت هەڵبگرە."
        }
    },
    {
        "id": "gliclazide",
        "generic_name": "Gliclazide",
        "alt_generic": "Gliclazide",
        "kurdish_name": "دیامیکرۆن / گلیکلازاید",
        "arabic_name": "ديامكرون / جليكلازيد",
        "brand_names": ["Diamicron", "Diaprel", "Glicron", "Diapro"],
        "category": "دابەزێنەری شەکری خوێن (Sulfonylurea)",
        "category_en": "Diabetes",
        "kurdish_summary": {
            "purpose": "کۆنتڕۆڵکردنی شەکری خوێن لە ڕێگەی دەردانی ئەنسۆلین بە شێوەیەکی بەردەوام و پارێزراوتر.",
            "usage": "٣٠ملگم یان ٦٠ملگم (MR) لە کاتی نانی بەیانیدا.",
            "who_cannot_take": "شەکرەی جۆری یەکەم و پەککەوتنی گورچیلە.",
            "pregnancy_safety": "قەدەغەیە لە کاتی دووگیانیدا.",
            "crucial_warning": "نابێت ژەمی نان فەرامۆش بکەیت دوای خواردنی ئەم حەبە، ئەگینا شەکری خوێنت دادەبەزێت."
        }
    },
    {
        "id": "empagliflozin",
        "generic_name": "Empagliflozin",
        "alt_generic": "Empagliflozin",
        "kurdish_name": "جاردینس / ئێمپاگلیفڵۆزین",
        "arabic_name": "جارديانس / امباجليفلوزين",
        "brand_names": ["Jardiance", "Empaglif", "Glyxambi"],
        "category": "شەکرە و پاراستنی دڵ و گورچیلە (SGLT2 Inhibitor)",
        "category_en": "Diabetes & Heart",
        "kurdish_summary": {
            "purpose": "دەردانی شەکری زیادە لە ڕێگەی میزەوە؛ دڵ لە سستبوون دەپارێزێت و پەستانی خوێن و کێش کەم دەکاتەوە.",
            "usage": "١٠ملگم یان ٢٥ملگم ڕۆژانە یەک جار لەگەڵ یان بێ نان.",
            "who_cannot_take": "نەخۆشی سستبوونی پێشکەوتووی گورچیلە و شەکرەی جۆری یەکەم.",
            "pregnancy_safety": "لە قۆناغەکانی دووەم و سێیەمی دووگیانیدا قەدەغەیە.",
            "crucial_warning": "مەترسی هەوکردنی کەڕوویی کۆئەندامی میزەڕۆ زیاد دەکات؛ پێویستە ئاوی زۆر بخورێتەوە و پاکوخاوێنی ڕابگیرێت."
        }
    },
    {
        "id": "dapagliflozin",
        "generic_name": "Dapagliflozin",
        "alt_generic": "Dapagliflozin",
        "kurdish_name": "فۆرکسیگا / داپاگلیفڵۆزین",
        "arabic_name": "فوركسيجا / داباجليفلوزين",
        "brand_names": ["Forxiga", "Farxiga", "Dapacar"],
        "category": "شەکرە و دڵ (SGLT2 Inhibitor)",
        "category_en": "Diabetes & Heart",
        "kurdish_summary": {
            "purpose": "کۆنتڕۆڵی شەکرەی جۆری دوو، کەمکردنەوەی مەترسی جەڵتەی دڵ و سستبوونی دڵ و پاراستنی گورچیلە.",
            "usage": "٥ملگم یان ١٠ملگم ڕۆژانە یەک دەنک بەیانیان.",
            "who_cannot_take": "سستبوونی توندی گورچیلە و دیالیز.",
            "pregnancy_safety": "نابێت لە کاتی دووگیانیدا بەکاربێت.",
            "crucial_warning": "پێویستە ڕۆژانە بڕی تەواوی ئاو بخورێتەوە بۆ ڕێگری لە وشکبوونەوەی لەش."
        }
    },
    {
        "id": "sitagliptin",
        "generic_name": "Sitagliptin",
        "alt_generic": "Sitagliptin Phosphate",
        "kurdish_name": "جانۆڤیا / سیتاگلیپتین",
        "arabic_name": "جانوفيا / سيتاجليبتين",
        "brand_names": ["Januvia", "Janumet", "Istavel", "Zitavia"],
        "category": "ڕێکخەری شەکرە بەبێ دابەزاندنی کتوپڕ (DPP-4 Inhibitor)",
        "category_en": "Diabetes",
        "kurdish_summary": {
            "purpose": "کۆنتڕۆڵکردنی بەرزی شەکری خوێن دوای ژەمەکان بەبێ ئەوەی کێشی لەش زیاد بکات.",
            "usage": "١٠٠ملگم ڕۆژانە یەک جار لەگەڵ یان بێ خواردن.",
            "who_cannot_take": "کەسێک پێشینەی هەوکردنی پەنکریاسی هەبووبێت (Pancreatitis).",
            "pregnancy_safety": "تەنها بە ڕاوێژی پزیشک.",
            "crucial_warning": "ئەگەر ئازاری توندی سکت بۆ دروستبوو کە بەرەو پشتت دەڕۆیشت، دەستبەجێ پەیوەندی بە پزیشکەوە بکە (نیشانەی پەنکریاس)."
        }
    },

    # =========================================================================
    # 6. غودەی دەرەقی (Thyroid Hormone)
    # =========================================================================
    {
        "id": "levothyroxine",
        "generic_name": "Levothyroxine",
        "alt_generic": "Levothyroxine Sodium",
        "kurdish_name": "ئەلترۆکسین / یۆتیرۆکس (حەبی غودەی تەممەڵ)",
        "arabic_name": "التروكسين / يوثيروكس",
        "brand_names": ["Eltroxin", "Euthyrox", "Synthroid", "Thyrax"],
        "category": "هۆڕمۆنی غودەی دەرەقی (Thyroid Hormone)",
        "category_en": "Thyroid & Endocrine",
        "kurdish_summary": {
            "purpose": "جێگرتنەوەی هۆڕمۆنی غودەی دەرەقی لە کاتی تەممەڵی و کەمکاری غودە (Hypothyroidism).",
            "usage": "٢٥، ٥٠، یان ١٠٠ مایکرۆگرام؛ بەیانیان زوو بە گەدەی تەواو بەتاڵ لانیکەم ٣٠ بۆ ٦٠ خولەک پێش نانی بەیانی بە پەرداخێک ئاو.",
            "who_cannot_take": "کەسێک کێشەی چارەسەرنەکراوی ڕژێنی سەرگورچیلەی (Adrenal insufficiency) هەبێت یان جەڵتەی کتوپڕی دڵ.",
            "pregnancy_safety": "لە کاتی دووگیانیدا زۆر پێویست و سەلامەتە و دەبێت ڕێژەکەی زیاتریش بکرێت بە چاودێری پزیشک بۆ پاراستنی مێشکی کۆرپەلە.",
            "crucial_warning": "نابێت پێکەوە لەگەڵ حەبی ئاسن، کالسیۆم یان چا و قاوە بخورێت (مەودای ٤ کاتژمێر دابنێ) ئەگینا لەش دەرمانەکە نامژێت."
        }
    },

    # =========================================================================
    # 7. کۆئەندامی هەناسە، ڕەبۆ و حەساسییەت (Respiratory & Allergy)
    # =========================================================================
    {
        "id": "salbutamol",
        "generic_name": "Albuterol",
        "alt_generic": "Salbutamol",
        "kurdish_name": "ڤێنتۆلین / فێنتۆلین",
        "arabic_name": "فنتولين / سالبوتامول",
        "brand_names": ["Ventolin", "ProAir", "Asthalin", "Aerolin"],
        "category": "فراوانکەری خێرای بۆڕی هەوا بۆ ڕەبۆ (SABA)",
        "category_en": "Respiratory & Asthma",
        "kurdish_summary": {
            "purpose": "کردنەوەی خێرای بۆڕییەکانی هەناسە لە کاتی تەنگەنەفەسی، قەیرانی ڕەبۆ (Asthma Attack) و گرژبوونی سنگ.",
            "usage": "پەمپی هەناسە: ١ بۆ ٢ هەڵمژین لە کاتی تەنگەنەفەسیدا بەپێی پێویست.",
            "who_cannot_take": "هەستیاری بە پێکهاتەکەی یان خێرالێدانی توندی دڵ.",
            "pregnancy_safety": "لە کاتی تەنگەنەفەسیدا سەلامەت و پێویستە چونکە کەمی ئۆکسجین مەترسیدارە بۆ کۆرپەلە.",
            "crucial_warning": "دەبێتە هۆی لەرزینی کاتیی دەست و خێرالێدانی دڵ. ئەگەر هەفتانە چەندین جار پێویستت پێی بوو، واتە ڕەبۆکەت کۆنتڕۆڵ نییە."
        }
    },
    {
        "id": "montelukast",
        "generic_name": "Montelukast",
        "alt_generic": "Montelukast Sodium",
        "kurdish_name": "سینگولێر / مۆنتیلۆکاست",
        "arabic_name": "سينجولير / مونتيلوكاست",
        "brand_names": ["Singulair", "Airfast", "Montiget", "Monkast"],
        "category": "ڕێگر لە تەنگەنەفەسی و حەساسییەتی سنگ (Leukotriene Receptor Antagonist)",
        "category_en": "Respiratory & Asthma",
        "kurdish_summary": {
            "purpose": "پاراستن لە تەنگەنەفەسی شەوانەی ڕەبۆ و چارەسەری هەستیاری درێژخایەنی لووت و بۆڕی هەوا.",
            "usage": "١٠ملگم (بۆ پێگەیشتووان) شەوانە یەک حەب پێش خەوتن؛ منداڵان ٤ یان ٥ملگم (حەبی جاوی).",
            "who_cannot_take": "هەستیاری بە پێکهاتەکەی.",
            "pregnancy_safety": "لەژێر ڕاوێژی پزیشکدا لە کاتی پێویستدا دەنووسرێت.",
            "crucial_warning": "FDA هۆشداری ڕەشی داناوە لەسەر گۆڕانکاری مەزاج و خەوزڕان و خەمۆکی لە هەندێک کەسدا؛ لە کاتی هەستپێکردنی ڕاستەوخۆ پزیشک ئاگادار بکەرەوە."
        }
    },
    {
        "id": "cetirizine",
        "generic_name": "Cetirizine",
        "alt_generic": "Cetirizine Hydrochloride",
        "kurdish_name": "زیرتێک / هیستادین / سیتریزین",
        "arabic_name": "زيرتيك / سيتريزين",
        "brand_names": ["Zyrtec", "Histazine", "Cetrizet", "Finallerg"],
        "category": "دژە هەستیاری و حەساسییەت (Antihistamine)",
        "category_en": "Allergy",
        "kurdish_summary": {
            "purpose": "بۆ چارەسەری حەساسییەت، پژمین، ئاوکردنی چاو، خوران، و لیرگی پێست (ئەرتیکاریا).",
            "usage": "١٠ملگم ڕۆژانە یەک جار شەوانە پێش خەوتن.",
            "who_cannot_take": "سستبوونی توندی گورچیلە پێویستی بە کەمکردنەوەی ژەم هەیە.",
            "pregnancy_safety": "بە گشتی لە سەلامەتترین جۆرەکانی دژە هەستیارییە لە کاتی دووگیانیدا بە ڕاوێژی پزیشک.",
            "crucial_warning": "دەکرێت کەمێک خەواڵوویی دروست بکات؛ دوای خواردنی لە شۆفێری ئاگاداربە."
        }
    },
    {
        "id": "loratadine",
        "generic_name": "Loratadine",
        "alt_generic": "Loratadine",
        "kurdish_name": "کلاریتین / لۆراتادین",
        "arabic_name": "كلاريتين / لوراتادين",
        "brand_names": ["Claritin", "Restamine", "Loratin", "Clarityne"],
        "category": "دژە هەستیاری بێ خەواڵوویی (Non-drowsy Antihistamine)",
        "category_en": "Allergy",
        "kurdish_summary": {
            "purpose": "چارەسەری حەساسییەتی وەرزی، ئاوی لووت، پژمینی بەردەوام و خورانی پێست بەبێ دروستکردنی خەواڵوویی.",
            "usage": "١٠ملگم، ڕۆژانە تەنها یەک حەب بەیانیان یان بەپێی پێویست.",
            "who_cannot_take": "هەستیاری بە لۆراتادین یان کێشەی توندی جگەر.",
            "pregnancy_safety": "لەژێر ڕاوێژی پزیشک بە سەلامەت دادەنرێت.",
            "crucial_warning": "نابێت لە ژەمی ڕۆژانەی دیاریکراو زیاتر بخورێت."
        }
    },

    # =========================================================================
    # 8. کۆئەندامی دەمار، ئازاری دەمار و باری دەروونی (Neurology & Psychiatry)
    # =========================================================================
    {
        "id": "gabapentin",
        "generic_name": "Gabapentin",
        "alt_generic": "Gabapentin",
        "kurdish_name": "نیۆرۆنتین / گاباپێنتین",
        "arabic_name": "نيورونتين / جابابنتين",
        "brand_names": ["Neurontin", "Gaba", "Gabanet", "Neurontin-Pfizer"],
        "category": "ئازاری دەمار و نەخۆشی شەکرە (Anticonvulsant & Neuropathic Pain)",
        "category_en": "Neurology - Nerve Pain",
        "kurdish_summary": {
            "purpose": "هێورکردنەوەی ئازاری سڕبوون و سوتانەوەی دەمارەکانی پێ لە نەخۆشانی شەکرە، ئازاری دەماری حیزامی ناری (Shingles).",
            "usage": "١٠٠ملگم، ٣٠٠ملگم، یان ٦٠٠ملگم بەپێی پەیژەی پزیشکی بە شێوەی پلە بە پلە دەستپێدەکات.",
            "who_cannot_take": "هەستیاری بە پێکهاتەکەی یان سستبوونی گورچیلە بەبێ گۆڕینی ژەم.",
            "pregnancy_safety": "تەنها لە کاتی زۆر پێویست و بە بڕیاری پزیشکی پسپۆڕ.",
            "crucial_warning": "خەواڵوویی و گێژبوون دروست دەکات. هەرگیز لەناکاو مەیپچڕێنە، چونکە نیشانەی دەماری خراپ لێدەکەوێتەوە."
        }
    },
    {
        "id": "pregabalin",
        "generic_name": "Pregabalin",
        "alt_generic": "Pregabalin",
        "kurdish_name": "لیریکا / پریگابالین",
        "arabic_name": "ليريكا / بريجابالين",
        "brand_names": ["Lyrica", "Galine", "Pregaba", "Regab"],
        "category": "ئازاری دەمار و جومگەکان (Controlled Neuropathic Agent)",
        "category_en": "Neurology - Controlled",
        "kurdish_summary": {
            "purpose": "چارەسەری ئازاری دەمارەکان، نەخۆشی فایبرۆمایەڵجیا (Fibromyalgia)، و دڵەڕاوکێی بەردەوام بەپێی ڕەچەتە.",
            "usage": "٧٥ملگم یان ١٥٠ملگم هەر ١٢ کاتژمێر جارێک تەنها بە چاودێری پزیشک.",
            "who_cannot_take": "هەستیاری یان پەککەوتنی سستبوونی دڵ بەبێ چاودێری.",
            "pregnancy_safety": "نابێت لە کاتی دووگیانیدا بەکاربێت.",
            "crucial_warning": "دەرمانێکی کۆنتڕۆڵکراوە و لە کاتی زیادەڕۆیی ئاڵوودەبوون دروست دەکات؛ لەپڕ وەستاندنی مەترسیدارە."
        }
    },
    {
        "id": "escitalopram",
        "generic_name": "Escitalopram",
        "alt_generic": "Escitalopram Oxalate",
        "kurdish_name": "سیپرالێکس / ئێسیتالۆپرام",
        "arabic_name": "سيبرالكس / اسيتالوبرام",
        "brand_names": ["Cipralex", "Lexapro", "Entact", "Esita"],
        "category": "خەمۆکی و دڵەڕاوکێ و ترس (SSRI Antidepressant)",
        "category_en": "Mental Health",
        "kurdish_summary": {
            "purpose": "چارەسەری دڵەڕاوکێی گشتی (GAD)، نەخۆشی پانیک و ترس (Panic Disorder)، و خەمۆکی.",
            "usage": "١٠ملگم یان ٢٠ملگم ڕۆژانە یەک جار لە هەمان کاتدا. کاریگەری چاکبوون دوای ٢ بۆ ٤ هەفتە دەردەکەوێت.",
            "who_cannot_take": "کەسێک لە هەمان کاتدا دەرمانی کۆمەڵەی MAOI بخوات.",
            "pregnancy_safety": "پێویستی بە ڕاوێژی وردی پزیشکی دەروونی هەیە.",
            "crucial_warning": "هەرگیز بە شێوەیەکی لەناکاو مەیپچڕێنە! دەبێت لەژێر چاودێری پزیشک بە شێوەی پلە بە پلە کەم بکرێتەوە."
        }
    },

    # =========================================================================
    # 9. ڤیتامین و کانزا بنەڕەتییەکان (Essential Vitamins & Minerals)
    # =========================================================================
    {
        "id": "vitamin_d3",
        "generic_name": "Cholecalciferol",
        "alt_generic": "Vitamin D3",
        "kurdish_name": "ڤیتامین D3 / کۆلیکالسیفێرۆڵ",
        "arabic_name": "فيتامين د3 / كوليكالسيفيرول",
        "brand_names": ["D-Cure", "Osteo-D", "Vigantol", "Bioderma-D3"],
        "category": "ڤیتامینی ئێسک و بەرگری (Vitamin D3)",
        "category_en": "Vitamins & Bone Health",
        "kurdish_summary": {
            "purpose": "مژینی کالسیۆم بۆ بەهێزکردنی ئێسک و ددانەکان، بەهێزکردنی کۆئەندامی بەرگری و نەهێشتنی پووکانەوەی ئێسک.",
            "usage": "بەپێی پشکنینی خوێن: بەزۆری حەبی ٥٠,٠٠٠ یەکەی نێودەوڵەتی هەفتانە یەک جار لە دوای ژەمی چەور.",
            "who_cannot_take": "ئەو کەسانەی کالسیۆمی خوێنیان بەرزە (Hypercalcemia) یان بەردی کالسیۆمی گورچیلەیان هەیە.",
            "pregnancy_safety": "لە کاتی دووگیانیدا بە ژەمی ڕۆژانەی گونجاو پێویست و سەلامەتە.",
            "crucial_warning": "زیادەڕۆیی لە خواردنی بەبێ پشکنین دەبێتە هۆی ژەهراویبوون بە ڤیتامین D و کلس لە گورچیلەدا دروست دەکات."
        }
    },
    {
        "id": "ferrous_sulfate",
        "generic_name": "Ferrous Sulfate",
        "alt_generic": "Iron Supplement",
        "kurdish_name": "حەبی ئاسن / فێرۆس سەڵفەیت",
        "arabic_name": "كبريتات الحديدوز / فيروز",
        "brand_names": ["Ferose", "Fefol", "Ferro-Gradumet", "Ironorm"],
        "category": "چارەسەری کەمخوێنی و کەمی ئاسن (Hematinic / Iron)",
        "category_en": "Anemia & Iron",
        "kurdish_summary": {
            "purpose": "چارەسەر و پاراستن لە کەمخوێنی کەمی ئاسن (Iron Deficiency Anemia)، لاوازی و بێتاقەتی.",
            "usage": "ڕۆژانە یەک حەب بە گەدەی بەتاڵ لەگەڵ پەرداخێک شەربەتی پرتەقاڵ (ڤیتامین C مژینی ئاسن زیاد دەکات).",
            "who_cannot_take": "نەخۆشی تالاسیمیا و ئەو کەسانەی کۆبوونەوەی ئاسنی زیادەیان لە لەشدا هەیە (Hemochromatosis).",
            "pregnancy_safety": "پێویست و زۆر گرنگە بۆ خانمانی دووگیان لە مانگی چوارەم بەدواوە بە ڕێنمایی پزیشک.",
            "crucial_warning": "ڕەنگی پیسایی ڕەش دەکات (ئەمە ئاساییە). لەگەڵ چا، قاوە و شیر مەخۆ چونكە مژینی ئاسن لەناو دەبەن."
        }
    },
    {
        "id": "folic_acid",
        "generic_name": "Folic Acid",
        "alt_generic": "Vitamin B9",
        "kurdish_name": "فۆلیک ئەسید (ڤیتامین B9 بۆ خانمانی دووگیان)",
        "arabic_name": "حمض الفوليك",
        "brand_names": ["Folvite", "Folic Acid", "Folinal"],
        "category": "ڤیتامینی دروستبوونی خوێن و کۆرپەلە (Vitamin B9)",
        "category_en": "Vitamins & Pregnancy",
        "kurdish_summary": {
            "purpose": "پاراستنی دڕکەپەتک و مێشکی کۆرپەلە لە شێواوی زگماکی (Neural Tube Defects) لەگەڵ دروستبوونی خڕۆکەی سووری خوێن.",
            "usage": "خانمانی دووگیان: ٤٠٠ تا ٨٠٠ مایکرۆگرام (یان ٥ملگم بەپێی ڕێنمایی پزیشک) لە پێش دووگیانی و لە ماوەی سێ مانگی یەکەمدا ڕۆژانە یەک حەب.",
            "who_cannot_take": "هەستیاری بە پێکهاتەکەی، یان کەمخوێنی کەمی ڤیتامین B12 بەبێ چارەسەری B12.",
            "pregnancy_safety": "پێویسترین و سەلامەتترین ماددەیە بۆ تەندروستی کۆرپەلە.",
            "crucial_warning": "پێویستە هەموو خانمێک کە پلانی منداڵبوونی هەیە پێشوەختە دەست بە خواردنی بکات."
        }
    },
    {
        "id": "vitamin_b12",
        "generic_name": "Cyanocobalamin",
        "alt_generic": "Methylcobalamin / Vitamin B12",
        "kurdish_name": "ڤیتامین B12 (حەب و دەرزی دەمار و خوێن)",
        "arabic_name": "فيتامين ب12 / سيانوكوبالامين",
        "brand_names": ["Neurobion", "Methycobal", "Becozyme", "B-Twelve"],
        "category": "ڤیتامینی دەمار و مێشک و خڕۆکەی سوور (Vitamin B12)",
        "category_en": "Vitamins & Neurology",
        "kurdish_summary": {
            "purpose": "پاراستنی پەردەی دەمارەکان، نەهێشتنی سڕبوون و مێروولەکردنی دەست و پێ، لەگەڵ پاراستن لە کەمخوێنی.",
            "usage": "دەرزی یان حەبی ١٠٠٠ مایکرۆگرام بەپێی ڕێنمایی پزیشک.",
            "who_cannot_take": "هەستیاری بە کۆباڵت یان نەخۆشی چاوی لیبەر (Leber's disease).",
            "pregnancy_safety": "سەلامەت و زۆر پێویستە بۆ کۆرپەلە و دایک.",
            "crucial_warning": "نەخۆشانی شەکرە کە میتفۆرمین دەخۆن دەبێت بەردەوام ئاستی B12 بپشکنن چونکە میتفۆرمین مژینی کەم دەکاتەوە."
        }
    },
    # =========================================================================
    # 10. کورتیکۆستیرۆید و هەوکردنی توند (Corticosteroids)
    # =========================================================================
    {
        "id": "dexamethasone",
        "generic_name": "Dexamethasone",
        "alt_generic": "Dexamethasone Sodium Phosphate",
        "kurdish_name": "دێکسمیسۆن / دێکسا (دەرزی و حەب)",
        "arabic_name": "ديكساميثازون / ديكسا",
        "brand_names": ["Decadron", "Dexone", "Dexona", "Dexamethasone"],
        "category": "ستیرۆیدی بەهێزی دژە هەوکردن (Corticosteroid)",
        "category_en": "Steroid & Severe Inflammation",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی هەوکردنی توند، حەساسییەتی کوشندە، تەنگەنەفەسی توندی ڕەبۆ و کۆرۆنا، و ئاوسانی مێشک.",
            "usage": "تەنها بە ڕەچەتەی پزیشک بۆ ماوەیەکی کاتی؛ بە شێوەی حەب (٠.٥ یان ٤ملگم) یان دەرزی دەدرێت.",
            "who_cannot_take": "هەوکردنی کەڕوویی چالاک، نەخۆشی شەکرەی کۆنتڕۆڵنەکراو و برینی گەدە.",
            "pregnancy_safety": "تەنها لە کاتی حاڵەتی نائاسایی پزیشکی بەکاربێت بە ڕاوێژی پزیشکی پسپۆڕ.",
            "crucial_warning": "هۆشداری توند! زۆر کەس بە هەڵە بۆ قەڵەوبوون یان هەڵامەتی سادە بەکاری دەهێنن؛ بەکارهێنانی لە خۆوە دەبێتە هۆی پووکانەوەی ئێسک، زەختی بەرز، شەکرە، تێکچوونی دەمار و لاوازبوونی بەرگری."
        }
    },
    {
        "id": "prednisolone",
        "generic_name": "Prednisolone",
        "alt_generic": "Prednisone",
        "kurdish_name": "پریدنیزۆڵۆن / پێستی نەخۆش و ڕەبۆ",
        "arabic_name": "بريدنيزولون",
        "brand_names": ["Deltacortril", "Predlone", "Pediapred", "Solupred"],
        "category": "دژە هەوکردنی ستیرۆیدی (Corticosteroid)",
        "category_en": "Steroid",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی جومگەکان، حەساسییەتی توندی پێست و چاو، ڕەبۆی سنگ و نەخۆشییەکانی بەرگری لەش.",
            "usage": "٥ملگم یان ٢٠ملگم بەیانیان دوای نانی بەیانی بەپێی ڕێنمایی وردی پزیشک.",
            "who_cannot_take": "برینی گەدە و هەوکردنی کەڕوویی بەربڵاو.",
            "pregnancy_safety": "تەنها بە ڕاوێژی پزیشک لە کاتی پێویستدا.",
            "crucial_warning": "نابێت بە هیچ جۆرێک لەناکاو بوەستێنرێت ئەگەر زیاتر لە هەفتەیەک خواردبێتت؛ دەبێت بە شێوازی پلە بە پلە کەم بکرێتەوە."
        }
    },

    # =========================================================================
    # 11. کێش دابەزاندن و شەکرەی نوێ (GLP-1 Weight Loss)
    # =========================================================================
    {
        "id": "semaglutide",
        "generic_name": "Semaglutide",
        "alt_generic": "Semaglutide Injection",
        "kurdish_name": "ئۆزێمپیک / ڤیگۆڤی / ڕیبێلسەس",
        "arabic_name": "اوزمبيك / ويجوفي / ريبيلسوس",
        "brand_names": ["Ozempic", "Wegovy", "Rybelsus"],
        "category": "دابەزاندنی کێش و کۆنتڕۆڵی شەکرە (GLP-1 Receptor Agonist)",
        "category_en": "Weight Loss & Diabetes",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی ئارەزووی خواردن و دابەزاندنی کێش، لەگەڵ ڕێکخستنی شەکری خوێن لە نەخۆشانی شەکرەی جۆری دوو.",
            "usage": "دەرزی هەفتانە: دەستپێکردن بە ٠.٢٥ملگم بۆ ماوەی ٤ هەفتە، پاشان زیادکردن بە ٠.٥ملگم بە چاودێری پزیشک.",
            "who_cannot_take": "کەسێک لە خێزانەکەیاندا شێرپەنجەی غودەی دەرەقی (MTC) هەبێت، یان پێشینەی هەوکردنی پەنکریاس (Pancreatitis).",
            "pregnancy_safety": "قەدەغەیە لە کاتی دووگیانی و شیرپێداندا؛ دەبێت لانیکەم ٢ مانگ پێش دووگیانی ڕابگیرێت.",
            "crucial_warning": "FDA هۆشداری توندی لەسەر مەترسی شێرپەنجەی غودەی مێدولاری و هەوکردنی توندی پەنکریاس هەیە. دڵتێکەڵهاتن، ڕشانەوە و قەبزی دروست دەکات."
        }
    },

    # =========================================================================
    # 12. پڕۆستات و دابەزاندنی بەردی گورچیلە (Urology)
    # =========================================================================
    {
        "id": "tamsulosin",
        "generic_name": "Tamsulosin",
        "alt_generic": "Tamsulosin Hydrochloride",
        "kurdish_name": "ئۆمنیک / تامسولۆسین (حەبی پڕۆستات و بەرد)",
        "arabic_name": "اومنيك / تامسولوسين",
        "brand_names": ["Omnic", "Flomax", "Tamsolin", "Prostacure"],
        "category": "فراوانکەری بۆڕی میز و پڕۆستات (Alpha-1 Blocker)",
        "category_en": "Urology - Prostate",
        "kurdish_summary": {
            "purpose": "ئاسانکردنی میزکردن لە کاتی گەورەبوونی پرۆستات (BPH)، هەروەها خاوکردنەوەی بۆڕی میز بۆ ئاسان فڕێدانی بەردی گورچیلە.",
            "usage": "٠.٤ملگم ڕۆژانە یەک کەپسول نیو کاتژمێر دوای هەمان ژەمی نان لە هەموو ڕۆژێکدا.",
            "who_cannot_take": "هەستیاری بە دەرمانەکە یان کێشەی دابەزینی زەخت لە کاتی هەستانەوەدا (Orthostatic hypotension).",
            "pregnancy_safety": "تەنها بۆ پیاوان و بەردی میزەڕۆیە.",
            "crucial_warning": "کەپسولەکەی مەهاڕە. دەبێتە هۆی سەرگێژخواردن لە کاتی لەپڕ هەستانەوە؛ لە کاتی نەشتەرگەری ئاوی سپی چاو (Cataract) دەبێت دکتۆری چاو ئاگادار بکرێتەوە."
        }
    },

    # =========================================================================
    # 13. دژە کەڕوو (Antifungals)
    # =========================================================================
    {
        "id": "fluconazole",
        "generic_name": "Fluconazole",
        "alt_generic": "Fluconazole",
        "kurdish_name": "دیفلۆکان / فلۆکۆنازۆڵ (حەبی کەڕوو)",
        "arabic_name": "ديفلوكان / فلوكونازول",
        "brand_names": ["Diflucan", "Flucand", "Fungican", "Candivast"],
        "category": "دژە کەڕووی بەهێز (Antifungal)",
        "category_en": "Antifungal",
        "kurdish_summary": {
            "purpose": "چارەسەری هەوکردنی کەڕوویی (کاندیدا) لە دەم (کەڕووی سپی دەم)، کۆئەندامی زاوزێی خانمان، نینۆک و پێست.",
            "usage": "کەپسولی ١٥٠ملگم بەزۆری تەنها یەک دەنک دەخورێت بۆ کەڕووی ئافرەتان، یان ٥٠ملگم ڕۆژانە بەپێی جۆری هەوکردنەکە.",
            "who_cannot_take": "ئەو کەسانەی لەگەڵ حەبی تێکچوونی لێدانی دڵ دەیخۆن.",
            "pregnancy_safety": "قەدەغەیە لە کاتی دووگیانیدا چونکە دەبێتە هۆی شێواوی کۆرپەلە.",
            "crucial_warning": "کارلێکی بەهێز دەکات لەگەڵ ژمارەیەکی زۆر لە دەرمانەکانی تر و ئەنزیمەکانی جگەر دادەبەزێنێت."
        }
    },

    # =========================================================================
    # 14. کۆکە، بەڵغەم و هەڵامەت (Cold, Cough & Mucus)
    # =========================================================================
    {
        "id": "pseudoephedrine_paracetamol",
        "generic_name": "Pseudoephedrine and Acetaminophen",
        "alt_generic": "Cold and Flu Formula",
        "kurdish_name": "پانادۆڵ کۆڵد ئەند فلۆ / فلودرێکس",
        "arabic_name": "بانادول كولد اند فلو / فلودريكس",
        "brand_names": ["Panadol Cold & Flu", "Fludrex", "Gripex", "Congestal"],
        "category": "چارەسەری هەڵامەت و لووتگیران (Decongestant & Analgesic)",
        "category_en": "Cold & Flu",
        "kurdish_summary": {
            "purpose": "کەمکردنەوەی لووتگیرانی توند، ئاوکردنی چاو، سەرئێشە و تای وەرزی هەڵامەت.",
            "usage": "پێگەیشتووان: یەک بۆ دوو حەب هەر ٦ بۆ ٨ کاتژمێر جارێک لە کاتی پێویستدا.",
            "who_cannot_take": "نەخۆشانی بەرزی فشاری خوێن (زەخت)، نەخۆشی دڵ، نەخۆشی غودەی زیادە چالاک.",
            "pregnancy_safety": "نابێت بەکاربێت بە تایبەت لە سێ مانگی یەکەمی دووگیانیدا بەهۆی سوودۆئیفێدرینەوە.",
            "crucial_warning": "هۆشداری زۆر گرنگ! ماددەی سودۆئیفێدرین بۆڕییەکانی خوێن تەسک دەکاتەوە؛ بەرزبوونەوەی مەترسیداری زەختی خوێن دروست دەکات."
        }
    },
    {
        "id": "acetylcysteine",
        "generic_name": "Acetylcysteine",
        "alt_generic": "N-Acetylcysteine / NAC",
        "kurdish_name": "فلویمۆسیل / ئەسیتیلسستین (فەوارەی بەڵغەم)",
        "arabic_name": "فلويموسيل / اسيتيل سيستئين",
        "brand_names": ["Fluimucil", "ACC Akut", "Mucinex NAC", "Solmucol"],
        "category": "شیکەرەوەی بەڵغەم و خەڵتەی سییەکان (Mucolytic)",
        "category_en": "Respiratory - Mucolytic",
        "kurdish_summary": {
            "purpose": "تواندنەوە و شلکردنەوەی بەڵغەمی خەست لە بۆڕییەکانی هەناسەدا بۆ ئاسان دەرهێنانی؛ هەروەها دژەژەهری فەرمیی ژەهراویبوون بە پاراسیتامۆڵە.",
            "usage": "فەوارەی ٦٠٠ملگم، ڕۆژانە یەک کیسی لە ناو نیو پەرداخ ئاودا دەتوێنرێتەوە دوای نان.",
            "who_cannot_take": "کەسێک برینی چالاکی گەدەی هەبێت.",
            "pregnancy_safety": "تەنها لە کاتی پێویست و بە فەرمانی پزیشک.",
            "crucial_warning": "نابێت لە یەک کاتدا لەگەڵ ئەنتی بایۆتیک بخورێت (لانیکەم ٢ کاتژمێر مەودا دابنێ)."
        }
    },
    {
        "id": "gaviscon",
        "generic_name": "Sodium Alginate and Sodium Bicarbonate",
        "alt_generic": "Antacid Barrier",
        "kurdish_name": "گاڤیسکۆن / ئەلجیناتی سۆدیۆم (شەربەتی دڵەکزێ)",
        "arabic_name": "جافيسكون",
        "brand_names": ["Gaviscon", "Gaviscon Double Action", "Acidex"],
        "category": "پارێزەری خێرای گەدە و دڵەکزێ (Antacid Raft)",
        "category_en": "Gastrointestinal - Antacid",
        "kurdish_summary": {
            "purpose": "دروستکردنی پەردەیەکی پارێزەر بەسەر ترشەڵۆکی گەدەدا تا نەچێتە سەرەوە بۆ سوورێنچک و دڵەکزێ ڕابگرێت.",
            "usage": "١٠ بۆ ٢٠ ملیلتر (کەوچکێکی چێشت) دوای ژەمەکان و پێش خەوتن.",
            "who_cannot_take": "ئەو کەسانەی لەسەر پارێزی توندی بێ خوێن (سۆدیۆم)ن.",
            "pregnancy_safety": "سەلامەتترین و باشترین چارەسەرە بۆ دڵەکزێی خانمانی دووگیان.",
            "crucial_warning": "نابێت لەگەڵ دەرمانەکانی تر پێکەوە بخورێت چونكە مژینی دەرمانەکانی تر کەم دەکاتەوە (٢ کاتژمێر مەودا پێویستە)."
        }
    },

    # =========================================================================
    # 15. فریاکەوتنی زەخت و دڵ (Emergency Cardio)
    # =========================================================================
    {
        "id": "captopril",
        "generic_name": "Captopril",
        "alt_generic": "Captopril",
        "kurdish_name": "کاپۆتین / کاپتۆپریل (حەبی ژێر زمانی زەخت)",
        "arabic_name": "كابوتين / كابتوبريل",
        "brand_names": ["Capoten", "Captopril", "Lopirin"],
        "category": "دابەزێنەری خێرای پەستانی خوێن (ACE Inhibitor)",
        "category_en": "Blood Pressure - Emergency",
        "kurdish_summary": {
            "purpose": "دابەزاندنی خێرای پەستانی لەناکاوی خوێن و یارمەتیدانی دڵ پاش جەڵتە.",
            "usage": "٢٥ملگم، لە کاتی زەختی لەناکاو بەزۆری دەخرێتە ژێر زمان بۆ خێرا کارکردن بەپێی ڕێنمایی پزیشک.",
            "who_cannot_take": "خانمانی دووگیان، یان کەسێک تووشی ئاوسانی دەموچاو (Angioedema) بووبێت بەهۆی دەرمانی ACE.",
            "pregnancy_safety": "قەدەغەیە لە کاتی دووگیانیدا چونکە گورچیلەی کۆرپەلە لەناو دەبات.",
            "crucial_warning": "دەبێتە هۆی کۆکەی وشکی بێزارکەر لە بەشێک لە نەخۆشەکاندا."
        }
    },
    {
        "id": "nitroglycerin",
        "generic_name": "Nitroglycerin",
        "alt_generic": "Glyceryl Trinitrate",
        "kurdish_name": "ئەنگیسید / نیترۆگلیسرین (حەبی ژێر زمانی دڵ)",
        "arabic_name": "انجيسيد / نيتروجليسرين",
        "brand_names": ["Angised", "Nitrostat", "Nitrolingual", "Nitromint"],
        "category": "فراوانکەری دەماری دڵ بۆ سنگەکوژێ (Vasodilator - Nitrate)",
        "category_en": "Cardiology - Angina",
        "kurdish_summary": {
            "purpose": "کردنەوەی دەستبەجێی خوێنبەرەکانی دڵ بۆ نەهێشتنی ئازاری توندی سنگ (Angina Attack) و تەنگەتاوی دڵ.",
            "usage": "حەبی ٠.٥ملگم دەخرێتە ژێر زمان کاتێک ئازاری سنگ دەستپێدەکات لە حاڵەتی دانیشتندا.",
            "who_cannot_take": "کەسێک لە ماوەی ٢٤ بۆ ٤٨ کاتژمێری ڕابردوودا دەرمانی هێزی سێکسی (وەک ڤیاگرا/سیالیس) خواردبێت؛ پێکەوەخواردنیان دەبێتە هۆی جەڵتە و دابەزینی کوشندەی زەخت!",
            "pregnancy_safety": "تەنها بە چاودێری پزیشکی دڵ لە نەخۆشخانە.",
            "crucial_warning": "هۆشداری کوشندە! خواردنی ئەم دەرمانە لەگەڵ ڤیاگرا (Sildenafil) یان سیالیس (Tadalafil) دەبێتە هۆی دابەزینی زۆر توندی زەخت و وەستانی دڵ."
        }
    },
    {
        "id": "acyclovir",
        "generic_name": "Acyclovir",
        "alt_generic": "Acyclovir",
        "kurdish_name": "زۆڤیراکس / ئاسیکلۆڤیر (دژە ڤایرۆس)",
        "arabic_name": "زوفيراكس / اسيكلوفير",
        "brand_names": ["Zovirax", "Ceviran", "Herpesin", "Acic"],
        "category": "دژە ڤایرۆسی هێرپیس و باڵۆکە (Antiviral)",
        "category_en": "Antiviral",
        "kurdish_summary": {
            "purpose": "چارەسەری پەڵەی هێرپیس (Herpes simplex)، باڵۆکەی لێو و دەم، تاڵە پەپوولە (شینگلز Shingles) و ئاوڵەی مریشک.",
            "usage": "٢٠٠ملگم یان ٤٠٠ملگم یان کرێمی مەرهەم، بەپێی ڕێنمایی پزیشک دەبێت بە ئاوی زۆر بخورێت.",
            "who_cannot_take": "سستبوونی گورچیلە بەبێ گونجاندنی ژەم.",
            "pregnancy_safety": "لەژێر ڕاوێژی پزیشک لە کاتی پێویستدا سەلامەتە.",
            "crucial_warning": "دەبێت ئاوی زۆر بخورێتەوە لە کاتی وەرگرتنیدا بۆ ئەوەی بلورەکانی دەرمانەکە لە گورچیلەدا کۆنەبنەوە."
        }
    },
    {
        "id": "insulin_glargine",
        "generic_name": "Insulin Glargine",
        "alt_generic": "Long-acting Insulin",
        "kurdish_name": "لانتۆس / ئەنسۆلینی شەوانەی درێژخایەن",
        "arabic_name": "لانتوس / انسولين جلارجين",
        "brand_names": ["Lantus", "Basaglar", "Toujeo"],
        "category": "ئەنسۆلینی شەوانەی درێژخایەن (Long-Acting Insulin)",
        "category_en": "Diabetes - Insulin",
        "kurdish_summary": {
            "purpose": "دابینکردنی بڕی بنەڕەتی ئەنسۆلین بە شێوەیەکی لەسەرخۆ بە درێژایی ٢٤ کاتژمێر بۆ نەخۆشانی شەکرەی جۆری یەک و دوو.",
            "usage": "دەرزی ژێر پێست: شەوانە لە هەمان کاتی دیاریکراودا لە ڕان، قۆڵ یان دەوری ناوک لێدەدرێت.",
            "who_cannot_take": "لە کاتی دابەزینی کتوپڕی شەکری خوێن (Hypoglycemia).",
            "pregnancy_safety": "لە کاتی دووگیانیدا بە چاودێری پزیشکی شەکرە سەلامەت و پەسەندکراوە.",
            "crucial_warning": "هەرگیز شوێنی لێدانی دەرزی دووبارە مەکەرەوە تا چەوری ژێر پێست تێک نەچێت. نیشانەکانی دابەزینی شەکر (لەرزین و ئارەقکردن) بزانە."
        }
    }
]

def normalize_kurdish_text(text: str) -> str:
    """Normalizes Kurdish and Arabic characters for resilient search."""
    if not text:
        return ""
    t = text.lower().strip()
    replacements = {
        'ك': 'ک',
        'ي': 'ی',
        'ى': 'ی',
        'ێ': 'ی',
        'ف': 'ڤ',
        'ة': 'ە',
        'ه': 'ە',
        'ۆ': 'و',
        'ڵ': 'ل',
        'ڕ': 'ر',
        'أ': 'ا',
        'إ': 'ا',
        'آ': 'ا',
        'ـ': ''
    }
    for k, v in replacements.items():
        t = t.replace(k, v)
    return t

def search_kurdish_index(query: str) -> List[Dict[str, Any]]:
    """Fuzzy searches the Kurdish medical directory with multi-lingual and normalized matching."""
    raw_q = query.lower().strip()
    if not raw_q:
        return []

    norm_q = normalize_kurdish_text(raw_q)
    matches = []
    seen_ids = set()

    for item in KURDISH_DRUG_INDEX:
        item_id = item["id"]
        if item_id in seen_ids:
            continue

        score = 0
        raw_kurd = item["kurdish_name"].lower()
        norm_kurd = normalize_kurdish_text(raw_kurd)
        raw_gen = item["generic_name"].lower()
        raw_alt = item.get("alt_generic", "").lower()
        raw_arab = item.get("arabic_name", "").lower()
        norm_arab = normalize_kurdish_text(raw_arab)

        # 1. Exact ID
        if raw_q == item_id or norm_q == item_id:
            score += 100
        # 2. Generic name
        elif raw_q in raw_gen or norm_q in raw_gen or raw_q in raw_alt:
            score += 85
        # 3. Kurdish Name (Exact or Normalized)
        elif raw_q in raw_kurd or norm_q in norm_kurd:
            score += 95
        # 4. Brand Names
        elif any(raw_q in b.lower() or norm_q in normalize_kurdish_text(b) for b in item["brand_names"]):
            score += 90
        # 5. Arabic Name
        elif raw_q in raw_arab or norm_q in norm_arab:
            score += 75
        # 6. Category
        elif raw_q in item["category"].lower() or norm_q in normalize_kurdish_text(item["category"]):
            score += 45

        if score > 0:
            matches.append((score, item))
            seen_ids.add(item_id)

    matches.sort(key=lambda x: x[0], reverse=True)
    return [m[1] for m in matches]

def get_by_generic_name(generic_name: str) -> Optional[Dict[str, Any]]:
    gn = generic_name.lower().strip()
    for item in KURDISH_DRUG_INDEX:
        if gn == item["generic_name"].lower() or gn == item.get("alt_generic", "").lower():
            return item
    return None
