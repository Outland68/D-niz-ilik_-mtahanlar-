import json
import random

questions_data = [
    {
        "id": "q001",
        "question": "1. MARPOL-73/78 Beynəlxalq Konvensiyasının tələblərinə əsasən tankerdən dənizə atılan suların tərkibində neftin miqdarı nə qədər olmalıdır?",
        "correct": "15 ppm",
        "wrong": ["30 ppm", "50 ppm", "100 ppm"]
    },
    {
        "id": "q002",
        "question": "2. Xam neft boşaldan zamanı eyni vaxtda xam neftlə tankların yuyulmasına icazə verilirmi?",
        "correct": "icazə verilir",
        "wrong": ["qəti qadağandır", "yalnız liman rəhbərliyinin icazəsi ilə", "yalnız xüsusi rayonlarda icazə verilir"]
    },
    {
        "id": "q003",
        "question": "3. Yük şlanqlarının üzərində onların işlək vəziyyətdə olduqlarını təsdiqləyən yazılardan hansı vurulur?\n1. yük şlanqı hansı tip yükə aiddir;\n2. sınaq təzyiqi;\n3. istehsal olunduğu ay və il;\n4. elektrik keçirməsi barədə məlumat;\n5. yük şlanqlarının çəkisi.",
        "correct": "1,2,3,4",
        "wrong": ["1,3,5", "2,4,5", "yalnız 1 və 2"]
    },
    {
        "id": "q004",
        "question": "4. Hansı neft məhsulları alışma temperaturuna görə uçan yüklərə aiddir?",
        "correct": "alışma temperaturuna görə 600 C-dən aşağı olan neft məhsulları",
        "wrong": ["alışma temperaturuna görə 600 C-dən yuxarı olan neft məhsulları", "donma dərəcəsi 0 C-dən aşağı olan neft məhsulları", "buxarlanma qabiliyyəti olmayan ağır mazutlar"]
    },
    {
        "id": "q005",
        "question": "5. Gəmidən-gəmiyə neft məhsulları ötürmə zamanı yük şlanqlarının minimal əyilmə radiusu nə qədər olmalıdır?",
        "correct": "şlanqın diametrinin 6 mislindən az olmamalıdır",
        "wrong": ["şlanqın diametrinin 2 mislindən az olmamalıdır", "şlanqın uzunluğunun 10 faizi qədər", "diametrindən asılı olmayaraq 1 metr"]
    },
    {
        "id": "q006",
        "question": "6. Gəmi-Sahil yoxlama vərəqi yük göyərtəsi rayonunda daşınan elektrik avadanlıqları barəsində nəyi nəzərdə tutur?",
        "correct": "Daşınan elektrik avadanlığının kabelləri şəbəkədən ayrılmalıdır",
        "wrong": ["Daşınan avadanlıqlar daim şəbəkəyə qoşulu qalmalıdır", "Yalnız yüksək gərginlikli kabellər ayrılmalıdır", "İşıqlandırma kabelləri yoxlanılmadan istifadə edilə bilər"]
    },
    {
        "id": "q007",
        "question": "7. Boşaltma / xam neftlə yuma əməliyyatı zamanı inert qaz sistemi sıradan çıxarsa, nə etmək lazımdır?",
        "correct": "Boşaltmanı, xam neftlə yumanı saxlamaq",
        "wrong": ["Nasosların gücünü artırmaqla əməliyyata davam etmək", "Ventilyasiya sistemini qoşub yumanı bitirmək", "Dərhal dəniz suyundan istifadə etməyə başlamaq"]
    },
    {
        "id": "q008",
        "question": "8. Yük şlanqlarının sınağı zamanı yoxlama təzyiqi işçi təzyiqdən neçə dəfə çox olmalıdır?",
        "correct": "1.5 dəfə",
        "wrong": ["2.5 dəfə", "eyni səviyyədə", "3 dəfə"]
    },
    {
        "id": "q009",
        "question": "9. Bağlama (burazlanma) və gəminin bortunda yedək gəmisi durduqda yükün ölçülməsinə və nümunələrin götürülməsinə:",
        "correct": "Qadağan olunur",
        "wrong": ["İcazə verilir", "Yalnız kapitanın iştirakı ilə icazə verilir", "Gündüz vaxtı icazə verilir"]
    },
    {
        "id": "q010",
        "question": "10. 1-ci tip kimyəvi tankerlərdə yük zonasının konstruktiv müdafiəsinə görə yük tanklarından borta qədər olan məsafə neçə metr təşkil edir?",
        "correct": "11.5 metr",
        "wrong": ["5.5 metr", "2.5 metr", "15.5 metr"]
    },
    {
        "id": "q011",
        "question": "11. Tankerlərdə neçə əsas yükləmə xətti sistemindən istifadə olunur?",
        "correct": "3 sistem",
        "wrong": ["1 sistem", "2 sistem", "4 sistem"]
    },
    {
        "id": "q012",
        "question": "12. Yükləmə əməliyyatına başlamazdan əvvəl inert qaz sisteminin 3 yollu klapanı hansı vəziyyətdə olmalıdır?",
        "correct": "qapalı",
        "wrong": ["tam açıq", "yarıaçıq", "avtomatik tənzimlənən rejimdə"]
    },
    {
        "id": "q013",
        "question": "13. Neçə növ qazayırıcı sistem mövcuddur?",
        "correct": "2",
        "wrong": ["3", "4", "5"]
    },
    {
        "id": "q014",
        "question": "14. MARPOL-73/78-in I əlavəsinin tələblərinə uyğun olaraq xüsusi rayonlardan kənarda yük tanklarından tərkibində neft suları tullayarkən nəyə riayət etmək vacib deyil?",
        "correct": "Ətraf mühitin temperaturuna",
        "wrong": ["Gəminin sürətinə", "Sahildən olan məsafəyə", "Atılan qarışığın həcminə"]
    },
    {
        "id": "q015",
        "question": "15. İnertizə olunmuş tanklı tankerlərdə ildırımlı tufan xəbərdarlığı alınan zaman uçan neft məhsulları ilə əməliyyatların keçirilməsi:",
        "correct": "Qadağan olunur",
        "wrong": ["Xüsusi nəzarət altında davam etdirilir", "Sürəti azaltmaqla icazə verilir", "Yalnız ballast tanklarında icazə verilir"]
    },
    {
        "id": "q016",
        "question": "16. Yük tanklarının içində partlama təhlükəsinin qarşısını almaq üçün hansı sistemdən istifadə olunur?",
        "correct": "İnert qaz sistemindən",
        "wrong": ["Məcburi ventilyasiya sistemindən", "Qaz-analizator sistemindən", "Dəniz suyu ilə yuyulma sistemindən"]
    },
    {
        "id": "q017",
        "question": "17. Hansı neft məhsulları alışma temperaturuna görə uçmayan yüklərə aiddir?",
        "correct": "alışma temperaturuna görə 600 C-dən yuxarı olan neft məhsulları",
        "wrong": ["alışma temperaturuna görə 600 C-dən aşağı olan neft məhsulları", "bütün növ xam neft növləri", "tərkibində kükürd az olan neft məhsulları"]
    },
    {
        "id": "q018",
        "question": "18. SOLAS-74 Beynəlxalq Konvensiyası ilə tankerlerdə ən azı neçə yanğın əleyhinə komplekti nəzərdə tutulub?",
        "correct": "4",
        "wrong": ["2", "6", "8"]
    },
    {
        "id": "q019",
        "question": "19. Yük əməliyyatları zamanı ballast tanklarının qapaqları hansı vəziyyətdə olmalıdır?",
        "correct": "bağlı",
        "wrong": ["açıq", "yarıaçıq", "havalandırma rejimində"]
    },
    {
        "id": "q020",
        "question": "20. Kimyəvi yük daşıyan tankerlərdə yük şlanqlarının qırılma / cırılma sınağı zamanı yoxlama təzyiqi işçi təzyiqdən neçə dəfə çox olmalıdır?",
        "correct": "5 dəfə",
        "wrong": ["2 dəfə", "3 dəfə", "10 dəfə"]
    },
    {
        "id": "q021",
        "question": "21. İnert qazın yük tankının girişində temperaturu neçə dərəcədən artıq olmamalıdır?",
        "correct": "650 C",
        "wrong": ["850 C", "450 C", "250 C"]
    },
    {
        "id": "q022",
        "question": "22. Yük zonasının konstruktiv müdafiəsinə görə zərərli və təhlükəli yükdaşıyan tankerlərin neçə tipi vardır?",
        "correct": "3",
        "wrong": ["2", "4", "5"]
    },
    {
        "id": "q023",
        "question": "23. Yükün boşaldılmasının ilkin mərhələsində yükün axar sürəti neçə m/s olmalıdır?",
        "correct": "1 m/s",
        "wrong": ["3 m/s", "5 m/s", "7 m/s"]
    },
    {
        "id": "q024",
        "question": "24. Yük əməliyyatları zamanı fövqəladə hallar baş verərsə hansı tədbirlər görülməlidir?",
        "correct": "Yük əməliyyatlarını saxlamaq, terminal nümayəndələrinə xəbər vermək, plan üzrə hərəkət etmək",
        "wrong": ["Əməliyyatı davam etdirərək səbəbi axtarmaq", "Gəminin sürətini artıraraq limandan çıxmaq", "Yalnız gəmi heyətinə məlumat verib gözləmək"]
    },
    {
        "id": "q025",
        "question": "25. Yuyucu sistemin kəmərlərində təzyiq nə qədər olmalıdır?",
        "correct": "8 kq/sm2",
        "wrong": ["2 kq/sm2", "12 kq/sm2", "15 kq/sm2"]
    },
    {
        "id": "q026",
        "question": "26. Yükün səviyyəsinin ölçülməsinin neçə əsas üsulu mövcuddur?",
        "correct": "3",
        "wrong": ["2", "4", "5"]
    },
    {
        "id": "q027",
        "question": "27. Tankların qurudulması və təmizlənməsi zamanı neçə üsuldan istifadə olunur?",
        "correct": "3",
        "wrong": ["1", "2", "4"]
    },
    {
        "id": "q028",
        "question": "28. Yük boşaltmazdan əvvəl yük nasosunun klapanları hansı vəziyyətdə olmalıdır?",
        "correct": "Basma klapanı bağlı ,sovurucu klapanı açıq",
        "wrong": ["Basma klapanı açıq ,sovurucu klapanı bağlı", "Hər iki klapan tam açıq", "Hər iki klapan tam bağlı"]
    },
    {
        "id": "q029",
        "question": "29. Xüsusi rayonda olan zaman tankların yuyulmasında hansı üsullardan istifadə olunur?",
        "correct": "Qapalı dövrlü",
        "wrong": ["Açıq dövrlü", "Yarıaçıq sistemli", "Yalnız dəniz suyu ilə yuyulma"]
    },
    {
        "id": "q030",
        "question": "30. Tankların yuma sisteminə nə daxil deyil?",
        "correct": "Qaz-analizator",
        "wrong": ["Yuma maşınları", "Yük nasosları", "Qızdırıcılar (istilik dəyişdiriciləri)"]
    },
    {
        "id": "q031",
        "question": "31. Tankların yuyulması zamanı neçə üsuldan istifadə olunur?",
        "correct": "3",
        "wrong": ["2", "4", "5"]
    },
    {
        "id": "q032",
        "question": "32. Tankların yuyulması nə zaman zəruri deyil?",
        "correct": "Təmirdən çıxan zaman",
        "wrong": ["Gəmi quru doka gedərkən", "Yük növü dəyişdirildikdə", "Təmiz ballast qəbul ediləcək tanklarda"]
    }
]

def rebuild_json():
    random.seed(33323)
    final_questions = []
    
    for q in questions_data:
        options = [q["correct"]] + q["wrong"]
        random.shuffle(options)
        
        letters = ["A", "B", "C", "D"]
        options_dict = {}
        correct_letter = ""
        
        for i, opt in enumerate(options):
            letters[i]: opt
            options_dict[letters[i]] = opt
            if opt == q["correct"]:
                correct_letter = letters[i]
                
        final_questions.append({
            "id": q["id"],
            "question": q["question"],
            "options": options_dict,
            "correct_answer": correct_letter,
            "explanation": ""
        })
        
    out_data = {
        "certificate": "Xam Neftlə Yuyulma Sistemi",
        "questions": final_questions
    }
    
    with open(r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\xam_neftl_yuyulma_sistemi.json", "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
        
    print("Rebuild complete. 32 questions processed.")

if __name__ == "__main__":
    rebuild_json()
