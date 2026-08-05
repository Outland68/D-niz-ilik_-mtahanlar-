import json, os, random

tehlukeli_questions_raw = [
    {
        "id": "q001",
        "question": "1. Təhlükəli yüklərin dəniz nəqliyyatı vasitəsi ilə daşınması hansı Beynəlxalq Məcəllənin tələbləri əsasında tənzimlənir?",
        "options": {
            "A": "Təhlükəli yüklərin dənizdə daşınmasının Beynəlxalq Məcəlləsi (IMDG Code)",
            "B": "Əmniyyətli İdarəetmə Haqqında Beynəlxalq Məcəllə (ISM Code)",
            "C": "Gəmilərin və Liman Vasitələrinin Mühafizəsi Məcəlləsi (ISPS Code)",
            "D": "Qlobal Dəniz Fəlakət Məcəlləsi (GMDSS Code)"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q002",
        "question": "2. “Dəniz çirkləndirici”nin tərifi hansı Beynəlxalq sənəddə göstərir?",
        "options": {
            "A": "MARPOL-73/78 Konvensiyasının III əlavəsi",
            "B": "SOLAS-74 Konvensiyasının I fəsli",
            "C": "STCW-78/95 Konvensiyasının B bölməsi",
            "D": "COLREG-72 Beynəlxalq Qaydaları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q003",
        "question": "3. Təhlükəli yüklərin daşınmasına qoyulan tələblər SOLAS-74 Konvesniyasının hansı fəslinin tərkibinə daxildir?",
        "options": {
            "A": "VII Fəsil",
            "B": "III Fəsil",
            "C": "IX Fəsil",
            "D": "XII Fəsil"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q004",
        "question": "4. Zərərli maddələr dəniz çirkləndiriciləri MARPOL-73/78 Konvensiyasının hansı əlavəsində göstərilir?",
        "options": {
            "A": "III Əlavə",
            "B": "I Əlavə",
            "C": "VI Əlavə",
            "D": "V Əlavə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q005",
        "question": "5. “Zərərli maddələrə” nələr daxildir?",
        "options": {
            "A": "İnsanların sağlamlığına və ətraf mühitə zərər vura biləcək maddələr",
            "B": "Yalnız təmiz dəniz qumu və çınqıl",
            "C": "Yalnız içməli qablaşdırılmış su",
            "D": "Yalnız təzə meyvə və tərəvəz"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q006",
        "question": "6. Gəmilərin təhlükəli yüklərin daşınması üçün yararlı olması haqqında sənədləri hansı təşkilat verir?",
        "options": {
            "A": "Bayraq Dövlətinin Administrasiyası",
            "B": "Liman Polisi İdarəsi",
            "C": "Dəniz Turizm Agentliyi",
            "D": "Şəhər İcra Hakimiyyəti"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q007",
        "question": "7. Təhlükəli yüklərin daşınması zamanı gəmi heyətinin icra edəcəyi tədbirlər hansı sənəddə göstərilir?",
        "options": {
            "A": "Qəza tədbirləri üzrə göstərişlərdə",
            "B": "Gəmi aşpazının menyu cədvəlində",
            "C": "Gəmi teleqraf jurnalı qeydlərində",
            "D": "Gəminin lövbər dayanacağı cədvəlində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q008",
        "question": "8. TXDDBM (IMDG Code) neçə cilddən ibarətdir?",
        "options": {
            "A": "2",
            "B": "5",
            "C": "10",
            "D": "1"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q009",
        "question": "9. Təhlükəli yüklərin dəniz nəqliyyatı ilə daşınması hansı Beynəlxalq təşkilatın tələbləri əsasında tənzimlənir?",
        "options": {
            "A": "Beynəlxalq Dəniz Təşkilatı (IMO)",
            "B": "Beynəlxalq Valyuta Fondu (IMF)",
            "C": "Ümumdünya Səhiyyə Təşkilatı (WHO)",
            "D": "Beynəlxalq Mülki Aviasiya Təşkilatı (ICAO)"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q010",
        "question": "10. Qısaldılmış EMS yazılışı nəyi ifadə edir?",
        "options": {
            "A": "Qəza tədbirləri üzrə göstərişlər qəza kartoçkaları",
            "B": "Elektrik mühərriklərinin sınaq cədvəli",
            "C": "Ekologiya və meşə təsərrüfatı xidməti",
            "D": "Elektron naviqasiya xəritələri sistemi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q011",
        "question": "11. Qısaldılmiş MFAQ yazılışı nəyi ifadə edir?",
        "options": {
            "A": "İlkin tibbi yardım göstərilməsi üzrə rəhbərlik",
            "B": "Gəmi mühərriklərinin avtomatlaşdırma dərəcəsi",
            "C": "Dənizdə meteoroloji proqnozlaşdırma mərkəzi",
            "D": "Gəmi yanacaq filtrlərinin təmizlənmə qaydası"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q012",
        "question": "12. HAZMAT termini nəyi ifadə edir?",
        "options": {
            "A": "Təhlükəli materiallar",
            "B": "Gəmi havalandırma sistemləri",
            "C": "Hidrostatik azadölçən cihazlar",
            "D": "Avtomatik sükan aparatları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q013",
        "question": "13. Qısaldılmış CFR US yazılışı nəyi ifadə edir?",
        "options": {
            "A": "ABŞ-ın Federal Qaydalar Məcəlləsi",
            "B": "Böyük Britaniya Dənizçi Şəhadətnaməsi",
            "C": "Kanada Dəniz Mühafizəsi Qaydaları",
            "D": "Fransa Dəniz Təsnifat Cəmiyyəti"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q014",
        "question": "14. “MARİNE POLLUTANTE” yazısı nəyi ifadə edir?",
        "options": {
            "A": "Dəniz çirkləndiricisi",
            "B": "Yanğın söndürən maddə",
            "C": "İçməli dəniz suyu",
            "D": "Zərərsiz neytral yük"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q015",
        "question": "15. Hidrogen peroksid 3% nə üçün işlədilir?",
        "options": {
            "A": "Yaraları yumaq üçün dezinfeksiya edici maddə",
            "B": "Gəmi mühərrikinə yanacaq əlavəsi kimi",
            "C": "Gəmi korpusunu rəngləmək üçün",
            "D": "Buxar qazanının soyudulması üçün"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q016",
        "question": "16. Ammonyakla zəhərlənmə zamanı zərərçəkənə neçə %-li süd məhlulu verilməlidir?",
        "options": {
            "A": "3%-li",
            "B": "20%-li",
            "C": "50%-li",
            "D": "0.1%-li"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q017",
        "question": "17. Yanıq toxumaların zədələnməsi neçə qrupa bölünür?",
        "options": {
            "A": "3",
            "B": "10",
            "C": "1",
            "D": "15"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q018",
        "question": "18. Ağırlığına görə yanıqlar neçə dərəcəyə bölünür?",
        "options": {
            "A": "4-dək",
            "B": "10-dək",
            "C": "2-dək",
            "D": "7-dək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q019",
        "question": "19. Təhükəli yüklər neçə sinifə bölünülər?",
        "options": {
            "A": "9 sinifə",
            "B": "3 sinifə",
            "C": "15 sinifə",
            "D": "20 sinifə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q020",
        "question": "20. Oksidləşdirici və üzvi peroksidlər hansı sinifə aiddir?",
        "options": {
            "A": "5 sinif",
            "B": "1 sinif",
            "C": "8 sinif",
            "D": "2 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q021",
        "question": "21. Tez alışan mayelər hansı sinifə aiddir?",
        "options": {
            "A": "3 sinif",
            "B": "7 sinif",
            "C": "1 sinif",
            "D": "9 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q022",
        "question": "22. Tez alışan bərk maddələr hansı sinifə aiddir?",
        "options": {
            "A": "4 sinif",
            "B": "2 sinif",
            "C": "8 sinif",
            "D": "6 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q023",
        "question": "23. Qazlar hansı sinifə aiddir?",
        "options": {
            "A": "2 sinif",
            "B": "5 sinif",
            "C": "9 sinif",
            "D": "3 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q024",
        "question": "24. Partlayıcı maddələr hansı sinifə aiddir?",
        "options": {
            "A": "1 sinif",
            "B": "6 sinif",
            "C": "4 sinif",
            "D": "8 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q025",
        "question": "25. Radioaktiv maddələr hansı sinifə aiddir?",
        "options": {
            "A": "7 sinif",
            "B": "3 sinif",
            "C": "1 sinif",
            "D": "5 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q026",
        "question": "26. Aşılayıcı və korroziya doğuran maddələr hansı sinifə aiddir?",
        "options": {
            "A": "8 sinif",
            "B": "2 sinif",
            "C": "4 sinif",
            "D": "7 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q027",
        "question": "27. Digər təhlükəli yüklər hansı sinifə aiddir?",
        "options": {
            "A": "9 sinif",
            "B": "1 sinif",
            "C": "5 sinif",
            "D": "3 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q028",
        "question": "28. Zəhərli və yoluxucu maddələr hansı sinifə aiddir?",
        "options": {
            "A": "6 sinif",
            "B": "2 sinif",
            "C": "8 sinif",
            "D": "4 sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q029",
        "question": "29. 2-ci sinifin neçə yarım sinifi var?",
        "options": {
            "A": "4 yarım sinif",
            "B": "2 yarım sinif",
            "C": "6 yarım sinif",
            "D": "1 yarım sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q030",
        "question": "30. 1-ci sinifin neçə yarım sinifi var?",
        "options": {
            "A": "4 yarım sinif",
            "B": "2 yarım sinif",
            "C": "8 yarım sinif",
            "D": "1 yarım sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q031",
        "question": "31. 3-cü sinifin neçə yarım sinifi var?",
        "options": {
            "A": "3 yarım sinif",
            "B": "8 yarım sinif",
            "C": "1 yarım sinif",
            "D": "5 yarım sinif"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q032",
        "question": "32. Alışma temperaturu aşağı (-18˚S) olan yüklər hansı yarım sinifə aiddir?",
        "options": {
            "A": "3.1 yarım sinifinə",
            "B": "3.3 yarım sinifinə",
            "C": "4.2 yarım sinifinə",
            "D": "5.1 yarım sinifinə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q033",
        "question": "33. Alışma temperatur (-18˚C-dən + 23˚C) qədər olan yüklər hansı yarım sinifə aiddir?",
        "options": {
            "A": "3.2 yarım sinifinə",
            "B": "3.1 yarım sinifinə",
            "C": "4.1 yarım sinifinə",
            "D": "6.2 yarım sinifinə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q034",
        "question": "34. Alışma temperatur (+23˚C-dən + 61˚C) qədər olan yüklər hansı yarım sinifə aiddir?",
        "options": {
            "A": "3.3 yarım sinifinə",
            "B": "3.1 yarım sinifinə",
            "C": "2.1 yarım sinifinə",
            "D": "8.2 yarım sinifinə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q035",
        "question": "35. Qida yükü neçə yarım sinifə bölünür?",
        "options": {
            "A": "3 yarım sinifə",
            "B": "10 yarım sinifə",
            "C": "1 yarım sinifə",
            "D": "Bölünmür"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q036",
        "question": "36. Qida yükləri hansı sinifə aiddir?",
        "options": {
            "A": "3 sinifə",
            "B": "1 sinifə",
            "C": "7 sinifə",
            "D": "8 sinifə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q037",
        "question": "37. L.V.J. abreviaturası hansı sinifə aiddir?",
        "options": {
            "A": "3 sinifə",
            "B": "1 sinifə",
            "C": "5 sinifə",
            "D": "9 sinifə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q038",
        "question": "38. L.V.T. abreviaturası hansı sinfinə aiddir?",
        "options": {
            "A": "4 sinifinə",
            "B": "2 sinifinə",
            "C": "6 sinifinə",
            "D": "8 sinifinə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q039",
        "question": "39. “SQ” abreviaturası hansı sinifə aiddir?",
        "options": {
            "A": "2 sinifə",
            "B": "7 sinifə",
            "C": "4 sinifə",
            "D": "9 sinifə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q040",
        "question": "40. “V.M” abreviaturası hansı yarım sinifə aiddir?",
        "options": {
            "A": "1 sinifə",
            "B": "5 sinifə",
            "C": "3 sinifə",
            "D": "8 sinifə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q041",
        "question": "41. Qatı bitki yağlarının daşınması zamanı yükün temperaturuna nəzarət neçə saatdan bir keçirilir?",
        "options": {
            "A": "4 saatdan bir",
            "B": "24 saatdan bir",
            "C": "Hər 10 dəqiqədən bir",
            "D": "Yalnız limandan çıxarkən"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q042",
        "question": "42. Piy və bitki yağlarının boşaldılması zamanı temperatur göstəricisinin aşağı həddi neçə dərəcədir?",
        "options": {
            "A": "20˚C",
            "B": "80˚C",
            "C": "-10˚C",
            "D": "0˚C"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q043",
        "question": "43. Partlayıcı maddələrin xüsusi yığımın neçə növü mövcuddur?",
        "options": {
            "A": "3 növü",
            "B": "10 növü",
            "C": "1 növü",
            "D": "20 növü"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q044",
        "question": "44. V sinif təhlükəli yüklərin I yarım sinifi nece adlanır?",
        "options": {
            "A": "Turşu əmələ gətirən maddələr",
            "B": "Partlayıcı maddələr",
            "C": "Radioaktiv maddələr",
            "D": "Zəhərli qazlar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q045",
        "question": "45. V sinif təhlükəli yüklərin II yarım sinifi nece adlanır?",
        "options": {
            "A": "Üzvi maddələr",
            "B": "İnert qazlar",
            "C": "Aşılayıcı mayelər",
            "D": "Quru tikinti qumu"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q046",
        "question": "46. VI sinif təhlükəli yüklərin I yarım sinifi necə adlanır?",
        "options": {
            "A": "Zəhərli maddələr",
            "B": "Radioaktiv maddələr",
            "C": "Oksidləşdirici peroksidlər",
            "D": "Tez alışan bərk maddələr"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q047",
        "question": "47. VI sinif təhlükəli yüklərin II yarım sinifi nece adlanır?",
        "options": {
            "A": "Yoluxucu maddələr",
            "B": "Partlayıcı sursatlar",
            "C": "Sıxılmış hava balonu",
            "D": "Dəniz duzu"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q048",
        "question": "48. VII sinif təhlükəli yüklər nece adlanır?",
        "options": {
            "A": "Radioaktiv maddələr",
            "B": "Zəhərli qazlar",
            "C": "Korroziya doğuran maddələr",
            "D": "Tez alışan mayelər"
        },
        "correct_answer": "A",
        "explanation": ""
    }
]

# Randomize options A, B, C, D evenly for each question
random.seed(88888)
shuffled_questions = []

for q in tehlukeli_questions_raw:
    correct_val = q['options'][q['correct_answer']]
    val_list = list(q['options'].values())
    random.shuffle(val_list)
    
    keys = ['A', 'B', 'C', 'D']
    new_options = {keys[i]: val_list[i] for i in range(len(keys))}
    
    new_correct_key = None
    for k, v in new_options.items():
        if v == correct_val:
            new_correct_key = k
            break
            
    q['options'] = new_options
    q['correct_answer'] = new_correct_key
    shuffled_questions.append(q)

target_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\t_hl_k_li_v_z_r_rli_y_kl_rin_da_nmas.json'

data = {
    "certificate": "Təhlükəli və zərərli yüklərin daşınması",
    "questions": shuffled_questions
}

os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Corrected questions 29, 30, 44, 45 to exact PDF specifications for Təhlükəli və zərərli yüklərin daşınması!")
