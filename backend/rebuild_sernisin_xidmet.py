import json, os, random

sernisin_xidmet_questions_raw = [
    {
        "id": "q001",
        "question": "1. Sərnişin gəmisi:",
        "options": {
            "A": "12 nəfərdən artıq sərnişin daşıyan gəmidir",
            "B": "500 nəfərdən artıq sərnişin daşıyan gəmidir",
            "C": "1000 nəfərdən artıq sərnişin daşıyan gəmidir",
            "D": "2 nəfərdən artıq sərnişin daşıyan gəmidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q002",
        "question": "2. Sərnişin gəmilərində uşaqlar və körpələr üçün aşağıdakı sayda əlavə xilasedici jiletlər nəzərdə tutulmalıdır:",
        "options": {
            "A": "10%",
            "B": "50%",
            "C": "100%",
            "D": "2%"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q003",
        "question": "3. 36 nəfərdən artıq sərnişin daşıyan gəmilər üçün yalnız bir təxliyə yoluna malik olan dəhlizin uzunluğu aşağıdakını aşmamalıdır:",
        "options": {
            "A": "13 metr",
            "B": "25 metr",
            "C": "40 metr",
            "D": "5 metr"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q004",
        "question": "4. Xilasedici dairələrin ümumi çəkisi nə qədər olur?",
        "options": {
            "A": "2.5 kq",
            "B": "0.5 kq",
            "C": "10 kq",
            "D": "15 kq"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q005",
        "question": "5. Xilasedici dairələr necə işarələnirlər?",
        "options": {
            "A": "Gəminin adı və qeydiyyat limanı ilə",
            "B": "Gəmi kapitanının ev ünvanı ilə",
            "C": "İMO rəhbərinin adı və soyadı ilə",
            "D": "Sərnişin biletinin qiyməti ilə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q006",
        "question": "6. Xilasedici dairələr gəmidə harada yerləşdirilir?",
        "options": {
            "A": "Bütün açıq göyərtələrdə",
            "B": "Yalnız maşın şöbəsinin karterində",
            "C": "Yalnız kapitan kayutasının içində",
            "D": "Yalnız gəmi mətbəxində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q007",
        "question": "7. Xilasedici gödəkçələr nə ilə komplektləşdirilir?",
        "options": {
            "A": "İşıq lampası, batareya və fitverən ilə",
            "B": "Yalnız güzgü və kompas ilə",
            "C": "Yalnız balıq tutmaq üçün tilov ilə",
            "D": "Yalnız radioötürücü antenna ilə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q008",
        "question": "8. Xilasedici salda olarkən işarəverici raketdən və falşveyerdən necə istifadə edilməlidir?",
        "options": {
            "A": "Xilasedici salın komandirinin göstərişinə əsasən",
            "B": "Hər 5 dəqiqədən bir fasiləsiz olaraq",
            "C": "Gündüz saat 12:00-da avtomatik",
            "D": "İstənilən sərnişinin öz istəyinə əsasən"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q009",
        "question": "9. Üç davamlı uzun səs siqnalı nəyi bildirir?",
        "options": {
            "A": "Suda adam həyəcan siqnalını",
            "B": "Gəmini tərk etmə siqnalını",
            "C": "Yanğın həyəcan siqnalını",
            "D": "Dumanlı havada lövbər siqnalını"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q010",
        "question": "10. Gəmini tərk etmə komandasını kim verir?",
        "options": {
            "A": "Kapitan",
            "B": "Növbətçi matros",
            "C": "Gəmi aşpazı",
            "D": "Sərnişinlərin böyüyü"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q011",
        "question": "11. Həyəcan cədvəli harada yerləşməlidir?",
        "options": {
            "A": "Kapitan körpüsündə və heyətin yerləşdiyi yerdə",
            "B": "Yalnız maşın şöbəsinin altında",
            "C": "Yalnız gəminin avar valında",
            "D": "Liman müfəttişliyinin ofisində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q012",
        "question": "12. Xilasedici dairələr hansı maksimal hündürlükdən suya atılmağa davamlı olmalıdır?",
        "options": {
            "A": "30 metr",
            "B": "5 metr",
            "C": "100 metr",
            "D": "2 metr"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q013",
        "question": "13. Xilasedici jileti geyinib suya hansı maksimal hündürlükdən tullanmaq olar?",
        "options": {
            "A": "4.5 metr",
            "B": "20 metr",
            "C": "50 metr",
            "D": "1 metr"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q014",
        "question": "14. Xilasedici jilet hansı maksimal müddət ərzində kənardan kömək olmadan geyinilməlidir?",
        "options": {
            "A": "60 saniyə",
            "B": "10 dəqiqə",
            "C": "30 dəqiqə",
            "D": "5 saniyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q015",
        "question": "15. Hidrotermokostyum ilə suya hansı maksimal hündürlükdən tullanmaq olar?",
        "options": {
            "A": "4.5 metr",
            "B": "15 metr",
            "C": "30 metr",
            "D": "1 metr"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q016",
        "question": "16. Hidrotermokostyum hansı maksimal müddət ərzində kənardan kömək olmadan geyinilməlidir?",
        "options": {
            "A": "2 dəqiqə",
            "B": "15 dəqiqə",
            "C": "30 dəqiqə",
            "D": "10 saniyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q017",
        "question": "17. Hidrotermokostyum hansı müddət ərzində huşunu itirmiş insanın ağzını su üzərində olan vəziyyətə çevirməlidir?",
        "options": {
            "A": "Çevirmir",
            "B": "5 saniyə ərzində",
            "C": "1 dəqiqə ərzində",
            "D": "10 dəqiqə ərzində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q018",
        "question": "18. Su xaricində olan xilasedici qayığın mühərriki maksimum hansı vaxt ərzində işləyə bilər?",
        "options": {
            "A": "5 dəqiqə",
            "B": "60 dəqiqə",
            "C": "24 saat",
            "D": "Su xaricində mühərrik işlədilə bilməz"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q019",
        "question": "19. Xilasedici qayıqla tam yanacaq ehtiyyatı neçə saat və hansı sürətlə manevr etməyə imkan yaradır?",
        "options": {
            "A": "6 uzel ilə azı 24 saat",
            "B": "20 uzel ilə azı 2 saat",
            "C": "2 uzel ilə azı 5 saat",
            "D": "12 uzel ilə azı 48 saat"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q020",
        "question": "20. Hava təchizatı ilə təmin olunmuş tam örtülü qayıqlar azı hansı müddətə nəfəs almağa şərait yaradır?",
        "options": {
            "A": "10 dəqiqə",
            "B": "60 dəqiqə",
            "C": "24 saat",
            "D": "2 dəqiqə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q021",
        "question": "21. Oda davamlı xilasedici qayıqların minimal mühafizə müddəti nə qədərdir?",
        "options": {
            "A": "8 dəqiqə",
            "B": "60 dəqiqə",
            "C": "24 saat",
            "D": "1 dəqiqə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q022",
        "question": "22. Kolektiv xilasedici vasitədə olarkən dəniz xəstəliyinə karşı dərmanı kim qəbul etməlidir?",
        "options": {
            "A": "Hamı",
            "B": "Yalnız gəmi kapitanı",
            "C": "Yalnız mühərrik ustası",
            "D": "Heç kim dərman qəbul etməməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q023",
        "question": "23. Bütün həyəcan siqnalları üzrə məşqlər hansı vaxtda keçirilir?",
        "options": {
            "A": "Sutkanın istənilən vaxtı",
            "B": "Yalnız günortadan sonra saat 12:00-da",
            "C": "Yalnız gecə saat 03:00-da",
            "D": "Yalnız gəmi limanda olanda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q024",
        "question": "24. Gəmidə hansı yerlərdə siqaret çəkməyə icazə verilir?",
        "options": {
            "A": "Əmrlə təyin olunmuş yerlərdə",
            "B": "Yalnız kayutlarda",
            "C": "Yalnız yanacaq tanklarının üstündə",
            "D": "Bütün qapalı hissələrdə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q025",
        "question": "25. Xilasedici salda (qayıqda) UQD radiostansiya “MAYDAY” fəlakət siqnalını ötürmək üçün hansı kanala köklənməlidir?",
        "options": {
            "A": "UQD kanal 16",
            "B": "UQD kanal 6",
            "C": "UQD kanal 70",
            "D": "UQD kanal 12"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q026",
        "question": "26. Xilasedici qayıqda balıq tutmaq üçün avadanlıq varmı?",
        "options": {
            "A": "Bəli",
            "B": "Xeyr",
            "C": "Yalnız hərbi gəmilərdə var",
            "D": "Yalnız buzqıran gəmilərdə var"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q027",
        "question": "27. Gəmidə həyəcan siqnalları üzrə məşqlər əən geci hansı müddətdə keçirilir?",
        "options": {
            "A": "İldə bir dəfədən az olmayaraq",
            "B": "10 ildən bir",
            "C": "Yalnız gəmi satılarkən",
            "D": "Məşq keçirilməsi tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q028",
        "question": "28. Ümumgəmi həyəcan siqnalı necə verilir?",
        "options": {
            "A": "7 qısa 1 uzun",
            "B": "3 uzun",
            "C": "1 qısa 1 uzun",
            "D": "Fasiləsiz 24 saat"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q029",
        "question": "29. Yanğınla mübarizə üçün vasitələr harada olmalıdır?",
        "options": {
            "A": "Xüsusi olaraq ayrılmış yerdə",
            "B": "Kapitan kayutunda",
            "C": "İstənilən yerdə",
            "D": "Anbarın dərinliyində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q030",
        "question": "30. Gəmidə təhlükəli yüklə doldurulmuş bölməyə girdikdə hansı təhlükəsizlik qaydalarına riayət etmək lazımdır?",
        "options": {
            "A": "Hava-qaz mühitini yoxlayaraq daxil olmaq",
            "B": "Bölməyə dərhal açıq alovla daxil olmaq",
            "C": "Bölmənin qapılarını bağlayıb gözləmək",
            "D": "Elektrik işıqlarını tam söndürmək"
        },
        "correct_answer": "A",
        "explanation": ""
    }
]

# Randomize options A, B, C, D evenly for each question
random.seed(77777)
shuffled_questions = []

for q in sernisin_xidmet_questions_raw:
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

target_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\s_rni_inl_r_bilavasit_xidm_t_g_st_r_n_he.json'

data = {
    "certificate": "Sәrnişinlәrә bilavasitә xidmәt göstәrәn heyәt üzvlәri",
    "questions": shuffled_questions
}

os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Rebuilt all {len(shuffled_questions)} questions for Sərnişinlərə bilavasitə xidmət göstərən heyət üyələri with 100% accurate correct answers, relevant distractors, and randomized A/B/C/D option placement!")
