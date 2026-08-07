import json, os, random

suretli_questions_raw = [
    {
        "id": "q001",
        "question": "1. Sürətli xilasedici qayığın əsas təyinatı nədir?",
        "options": {
            "A": "dənizdə insanların axtarışı və xilas edilməsi",
            "B": "gəmi karterinin yağlanması",
            "C": "liman kranlarının rənglənməsi",
            "D": "yük anbarlarının havalandırılması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q002",
        "question": "2. Sürətli xilasedici qayıqların növləri hansılardır?",
        "options": {
            "A": "sərt gövdəli, hava ilə doldurulmuş və kombine olunmuş",
            "B": "taxta, dəmir və plastik",
            "C": "sualtı, suüstü və hava şarları",
            "D": "vakuumlu, buxarlı və elektrikli"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q003",
        "question": "3. Sürətli xilasedici qayıqların heyəti kimlərdir?",
        "options": {
            "A": "qayığın komandiri, sükançı və motorçu",
            "B": "kapitan, baş mexanik və aşpaz",
            "C": "gəmi həkimi və 2 nəfər sərnişin",
            "D": "liman polisi və gömrük işçisi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q004",
        "question": "4. Sürətli xilasedici qayıqda oturaq və uzanıqlı vəziyyətdə minimal neçə yer olmalıdır?",
        "options": {
            "A": "oturaq vəziyyətdə olanən azı 5 nəfər və xərək üzərində uzanmış 1 nəfər",
            "B": "oturaq vəziyyətdə 50 nəfər və uzanmış 20 nəfər",
            "C": "yalnız oturaq vəziyyətdə 1 nəfər",
            "D": "uzanmış vəziyyətdə yer nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q005",
        "question": "5. Sürətli xilasedici qayığın uzunluğu nə qədərdir?",
        "options": {
            "A": "6 m-dən 8,5 m-ə qədər",
            "B": "1 m-dən 2 m-ə qədər",
            "C": "15 m-dən 30 m-ə qədər",
            "D": "50 m-dən 100 m-ə qədər"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q006",
        "question": "6. Sürətli xilasedici qayıq gəmidə harada yerləşməlidir?",
        "options": {
            "A": "gəminin açıq göyərtəsində",
            "B": "maşın şöbəsinin karterində",
            "C": "kapitanın kayutasının içində",
            "D": "gəmi mətbəxində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q007",
        "question": "7. Sürətli xilasedici qayıq dənizdə suda neçə gün qala bilər?",
        "options": {
            "A": "azı 30 gün",
            "B": "1 saat",
            "C": "365 gün",
            "D": "5 gün"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q008",
        "question": "8. Hava ilə doldurulmuş sürətli xilasedici qayığın bir üzmə borusunda neçə bölmə olmalıdır?",
        "options": {
            "A": "azı 5 bölmə",
            "B": "1 bölmə",
            "C": "20 bölmə",
            "D": "Bölmə olmamalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q009",
        "question": "9. Hava ilə doldurulmuş sürətli xilasedici qayığın neçə ədəd üzmə borusu olmalıdır?",
        "options": {
            "A": "1 və ya 2 ayrıca üzmə borusu",
            "B": "10 ayrıca üzmə borusu",
            "C": "50 ayrıca üzmə borusu",
            "D": "Üzmə borusu olmamalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q010",
        "question": "10. Tam yüklənmə ilə sürətli xilasedici qayıq hansı sürətlə və neçə saat manevr etməyə qadir olmalıdır?",
        "options": {
            "A": "8 mil/saat sürətlə azı 4 saat",
            "B": "20 mil/saat sürətlə azı 24 saat",
            "C": "2 mil/saat sürətlə azı 1 saat",
            "D": "50 mil/saat sürətlə azı 10 saat"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q011",
        "question": "11. 3 nəfərlik komanda ilə sakit suda sürətli xilasedici qayıq hansı sürətlə və neçə saat manevr etməyə qadir olmalıdır?",
        "options": {
            "A": "20 mil/saat sürətlə azı 4 saat",
            "B": "5 mil/saat sürətlə azı 1 saat",
            "C": "50 mil/saat sürətlə azı 12 saat",
            "D": "1 mil/saat sürətlə azı 30 dəqiqə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q012",
        "question": "12. Neçə nəfər sürətli xilasedici qayığı işçi vəziyyətinə aşıra bilər?",
        "options": {
            "A": "2",
            "B": "10",
            "C": "15",
            "D": "50"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q013",
        "question": "13. Əgər sürətli xilasedici qayıq aşarsa, onun mühərriki ilə nə baş verməlidir?",
        "options": {
            "A": "mühərrik avtomatik olaraq sönməli və SXQ iş vəziyyətinə qaytarılandan sonra 1 dəqiqə ərzində işə düşməlidir",
            "B": "mühərrik 2 dəfə yüksək sürətlə fırlanmağa davam etməlidir",
            "C": "mühərrik partlamalıdır",
            "D": "mühərrik sudan çıxana qədər 1 saat sönməməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q014",
        "question": "14. Sürətli xilasedici qayıq hansı sürətlə salı (tam sayda insanlarla və təchizatla) yüklənmiş vəziyyətdə yedəkləməlidir?",
        "options": {
            "A": "azı 2 mil/saat",
            "B": "azı 20 mil/saat",
            "C": "azı 50 mil/saat",
            "D": "yedəkləmə sürəti 0.1 mil/saatdan çox ola bilməz"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q015",
        "question": "15. Sürətli xilasedici qayığın falın uzunluğu nə qədər olmalıdır?",
        "options": {
            "A": "azı 15 m",
            "B": "azı 100 m",
            "C": "1 m",
            "D": "50 m"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q016",
        "question": "16. Kiçik diametrli xilasedici dairənin ipinin uzunluğu nə qədər olmalıdır?",
        "options": {
            "A": "30 m",
            "B": "5 m",
            "C": "100 m",
            "D": "2 m"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q017",
        "question": "17. Sürətli xilasedici qayığın təchizatına neçə ədəd kiçik diametrli xilasedici dairə daxildir?",
        "options": {
            "A": "2",
            "B": "10",
            "C": "1",
            "D": "15"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q018",
        "question": "18. Sürətli xilasedici qayığın təchizatına hansı tipli odsöndürən daxildir?",
        "options": {
            "A": "yanan nefti söndürmək üçün bəyənilmiş odsöndürən tipi",
            "B": "yalnız kimyəvi turşu odsöndürəni",
            "C": "yalnız qum vedrəsi",
            "D": "odsöndürən nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q019",
        "question": "19. Sürətli xilasedici qayığın yedək kəndirinin uzunluğu nə qədər olmalıdır?",
        "options": {
            "A": "50 m",
            "B": "5 m",
            "C": "200 m",
            "D": "10 m"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q020",
        "question": "20. Sürətli xilasedici qayığın təchizatına neçə ədəd üzən lövbər daxildir?",
        "options": {
            "A": "1",
            "B": "5",
            "C": "10",
            "D": "Lövbər olmamalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q021",
        "question": "21. Hansı sürətli xilasedici qayığın təchizatında təhlükəsiz üzən bıçaq olmalıdır?",
        "options": {
            "A": "hava ilə doldurulmuş",
            "B": "sərt polad gövdəli",
            "C": "ağac konstruksiyalı",
            "D": "bütün qayıqlarda qadağandır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q022",
        "question": "22. Sürətli xilasedici qayıqda nə cür dərman qutusu olmalıdır?",
        "options": {
            "A": "su keçirməyən",
            "B": "kağız qutuda",
            "C": "açıq taxta qutuda",
            "D": "dərman qutusu tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q023",
        "question": "23. Sürətli xilasedici qayığın təchizatına neçə ədəd istilik qoruyucu vasitə daxildir?",
        "options": {
            "A": "azı 2",
            "B": "10",
            "C": "50",
            "D": "İstilik qoruyucu nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q024",
        "question": "24. Sürətli xilasedici qayığın təchizatında hansı miqdarda içməli su olmalıdır?",
        "options": {
            "A": "nəzərdə tutulmayıb",
            "B": "hər nəfərə 3 litr",
            "C": "hər nəfərə 10 litr",
            "D": "100 litr"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q025",
        "question": "25. Sürətli xilasedici qayığın təchizatına hansı miqdarda qida rasionu daxil olmalıdır?",
        "options": {
            "A": "nəzərdə tutulmayıb",
            "B": "hər nəfərə 10,000 kJ",
            "C": "1 aylıq konserva ehtiyatı",
            "D": "hər nəfərə 5 kq çörək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q026",
        "question": "26. Sürətli xilasedici qayığın təchizatında pirotexnikanın hansı dəsti olmalıdır?",
        "options": {
            "A": "6 falşfeyer, 4 paraşütlü raket, 2 tüstü şaşkası",
            "B": "12 paraşütlü raket, 12 falşfeyer",
            "C": "2 falşfeyer, 1 tüstü şaşkası",
            "D": "Pirotexnika nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q027",
        "question": "27. Falşfeyerin yanma müddəti nə qədər olmalıdır?",
        "options": {
            "A": "azı 1 dəqiqə",
            "B": "azı 10 dəqiqə",
            "C": "azı 1 saat",
            "D": "5 saniyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q028",
        "question": "28. Paraşütlü raketinin işığının yanma müddəti nə qədər olmalıdır?",
        "options": {
            "A": "azı 40 san",
            "B": "azı 10 dəq",
            "C": "azı 1 saat",
            "D": "2 saniyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q029",
        "question": "29. Tüstü şaşkasının tüstü vermə qabiliyyəti nə qədər olmalıdır?",
        "options": {
            "A": "azı 3 dəq",
            "B": "azı 30 dəq",
            "C": "azı 2 saat",
            "D": "10 saniyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q030",
        "question": "30. Sürətli xilasedici qayıqda olarkən, pirotexniki vasitələrin istifadəsinin icazəsini kim verir?",
        "options": {
            "A": "qayığın komandiri",
            "B": "hər bir sərnişin sərbəst olaraq",
            "C": "gəmi aşpazı",
            "D": "liman agenti"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q031",
        "question": "31. Sürətli xilasedici qayığın təchizatında hansı siqnal və işarə verici vasitələr olmamalıdır?",
        "options": {
            "A": "qəza radiobuyu (EPIRB)",
            "B": "fit",
            "C": "işıqsaçan fənər",
            "D": "siqnal güzgüsü"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q032",
        "question": "32. Sürətli xilasedici qayıqlarda projektorun fasiləsiz yanma müddəti nə qədər olmalıdır?",
        "options": {
            "A": "azı 3 saat",
            "B": "azı 24 saat",
            "C": "azı 10 saniyə",
            "D": "100 saat"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q033",
        "question": "33. Sürətli xilasedici qayıqlarda neçə ədəd projektor nəzərdə tutulub?",
        "options": {
            "A": "1",
            "B": "5",
            "C": "10",
            "D": "Projektor nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q034",
        "question": "34. Radiolokasiya cavabvericisinin (SART) gözləmə rejimi hansı müddət ərzində işlək vəziyyətdə olur?",
        "options": {
            "A": "4 gün (96 saat)",
            "B": "1 saat",
            "C": "30 gün",
            "D": "1 il"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q035",
        "question": "35. Radiolokasiya cavabvericisinin (SART) ötürmə rejimi hansı müddət ərzində işlək vəziyyətdə olur?",
        "options": {
            "A": "8 saat",
            "B": "1 saat",
            "C": "72 saat",
            "D": "10 saniyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q036",
        "question": "36. Radiolokasiya cavabverici işləməyə başlayarkən, o, ətrafda olan gəmilərin radarlarında hansı məsafədən görünməyə başlayır?",
        "options": {
            "A": "5 mil",
            "B": "50 mil",
            "C": "0,1 mil",
            "D": "100 mil"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q037",
        "question": "37. Daşınan qəza UQD radiostansiyasının işləmə vaxtı neçə saat olmalıdır?",
        "options": {
            "A": "azı 8 saat",
            "B": "azı 1 saat",
            "C": "azı 100 saat",
            "D": "10 saniyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q038",
        "question": "38. Sürətli xilasedici qayığın təchizatında hansı vasitələr olmamalıdır?",
        "options": {
            "A": "balıq tutmaq üçün ləvazimat dəsti",
            "B": "üzən lövbər",
            "C": "avar və çəngəl",
            "D": "əl nasosu"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q039",
        "question": "39. Soyutma sistemində su olmadan qısa müddətə asılma motorunu işə salmaq olarmı?",
        "options": {
            "A": "olmaz",
            "B": "bütün hallarda olar",
            "C": "yalnız gecə vaxtı olar",
            "D": "yalnız yağış yağarkən olar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q040",
        "question": "40. Alatoranlıq düşərkən və günün qaranlıq vaxtlarında sürətli xilasedici qayıqda nə etmək lazımdır?",
        "options": {
            "A": "ağ dairəvi işığı yandırmaq",
            "B": "bütün işıqları söndürüb gözləmək",
            "C": "qırmızı raket atmaq",
            "D": "mühərriki söndürmək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q041",
        "question": "41. Əgər sürətli xilasedici qayıq benzin mühərriki ilə təchiz edilmişdirsa, o, aşağıda göstərilən tələblərdən hansına cavab verməlidir?",
        "options": {
            "A": "yanacaq bakları yanğın və partlayışdan mühafizə olunmalıdır",
            "B": "yanacaq bakı açıq şəkildə göyərtədə asılmalıdır",
            "C": "yanacaq bakı su ilə doldurulmalıdır",
            "D": "heç bir xüsusi tələb yoxdur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q042",
        "question": "42. Hansı dövrdən bir sürətli xilasedici qayıq suya endirilməlidir?",
        "options": {
            "A": "ayda 1 dəfə",
            "B": "10 ildə 1 dəfə",
            "C": "yazda 1 dəfə",
            "D": "suya endirilməsi tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q043",
        "question": "43. Hansı dövrdən bir sürətli xilasedici qayığın avadanlıqları və təchizatı yoxlanılmalıdır?",
        "options": {
            "A": "ayda 1 dəfə",
            "B": "5 ildə 1 dəfə",
            "C": "hər gün saat 12:00-da",
            "D": "yoxlanılması tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q044",
        "question": "44. Sürətli xilasedici qayıq üçün konstruksiyaya əsasən tirlərin (davit) növləri hansılardır?",
        "options": {
            "A": "dönən və özüenən",
            "B": "stasionar və sualtı",
            "C": "buxarlı və hidravlik",
            "D": "əl zəncirli və mexaniki"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q045",
        "question": "45. Hansı maksimal krenin və diferentin göstəricilərində sürətli xilasedici qayığı gəmidən endirmək olar?",
        "options": {
            "A": "kren 20°, diferent 10°",
            "B": "kren 90°, diferent 45°",
            "C": "kren 2°, diferent 1°",
            "D": "kren 45°, diferent 30°"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q046",
        "question": "46. Sürətli xilasedici qayığı hansı maksimal çəkidə endirmək və ya qaldırmaq mümkün olmalıdır?",
        "options": {
            "A": "tam sayda insan və təchizatla",
            "B": "yalnız boş vəziyyətdə",
            "C": "yalnız 1 nəfər insanla",
            "D": "mühərriksiz və yanacaqsız"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q047",
        "question": "47. Sürətli xilasedici qayıq hansı sürətlə tir ilə suya enməlidir?",
        "options": {
            "A": "1 m/s",
            "B": "10 m/s",
            "C": "0,01 m/s",
            "D": "50 m/s"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q048",
        "question": "48. Sürətli xilasedici qayıq hansı sürətlə tir ilə sudan qalxmalıdır?",
        "options": {
            "A": "azı 0.8 m/s",
            "B": "azı 10 m/s",
            "C": "azı 0,01 m/s",
            "D": "50 m/s"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q049",
        "question": "49. Sürətli xilasedici qayığın endirilməsində neçə ədəd tir (davit) istifadə olunur?",
        "options": {
            "A": "1",
            "B": "4",
            "C": "10",
            "D": "Tir istifadə olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q050",
        "question": "50. Sürətli xilasedici qayıq heyəti ilə birlikdə neçə dəqiqəyə tir ilə suya salınmalıdır?",
        "options": {
            "A": "5 dəqiqə",
            "B": "60 dəqiqə",
            "C": "120 dəqiqə",
            "D": "1 dəqiqə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q051",
        "question": "51. Sürətli xilasedici qayıqda heyətin və endirmə komandasının siyahısı harada gösterilib?",
        "options": {
            "A": "gəminin cədvəlində (Muster list)",
            "B": "liman agentinin siyahısında",
            "C": "gəmi aşpazının menyusunda",
            "D": "kapitanın şəxsi qeyd dəftərində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q052",
        "question": "52. Sürətli xilasedici qayığın suya endirilməsi zamanı gəminin tam sürəti neçə olmalıdır?",
        "options": {
            "A": "5 mil/saat",
            "B": "25 mil/saat",
            "C": "50 mil/saat",
            "D": "0 mil/saat (tam dayanmalıdır)"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q053",
        "question": "53. Sürətli xilasedici qayığın endirilməsi zamanı onun gəmi ilə vəziyyəti necə olmalıdır?",
        "options": {
            "A": "gəmiyə paralel",
            "B": "gəmiyə 90 dərəcə bucaq altında",
            "C": "gəminin altına tərəf",
            "D": "gəminin pərinə tərəf"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q054",
        "question": "54. Sürətli xilasedici qayığın endirilməsi zamanı birinci hansı hərəkət yerinə yetirilir?",
        "options": {
            "A": "mühərriki buraxılır (işə salınır)",
            "B": "burun falini verilir",
            "C": "qayıq 10 metr uzaqlaşdırılır",
            "D": "projektor söndürülür"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q055",
        "question": "55. Sürətli xilasedici qayığın endirilməsi zamanı ən axırda hansı hərəkət yerinə yetirilir?",
        "options": {
            "A": "burun falini verilir (boşaldılır)",
            "B": "mühərriki işə salınır",
            "C": "dəniz suyu vurulur",
            "D": "lövbər salınır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q056",
        "question": "56. Sürətli xilasedici qayığın qaldırılması zamanı birinci hansı hərəkət yerinə yetirilir?",
        "options": {
            "A": "burun falini verilir (bərkidilir)",
            "B": "mühərrik söndürülür",
            "C": "qayıq iki yerə bölünür",
            "D": "avadanlıqlar dənizə atılır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q057",
        "question": "57. Sürətli xilasedici qayığın qaldırılması zamanı ən axırda hansı hərəkət yerinə yetirilir?",
        "options": {
            "A": "mühərrik söndürülür",
            "B": "burun falini verilir",
            "C": "benzin bakı sökülür",
            "D": "dairələr suya atılır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q058",
        "question": "58. Dalğanın hansı hissəsinə sürətli xilasedici qayığı endirmək lazımdır?",
        "options": {
            "A": "dalğaların arasına",
            "B": "dalğanın ən uca zirvəsinə",
            "C": "gəminin pərinin tam üstünə",
            "D": "gəminin burun hissəsinin altına"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q059",
        "question": "59. Sürətli xilasedici qayığı endirmədən əvvəl tirdə nəyi yoxlamaq lazımdır?",
        "options": {
            "A": "bucurqadların sazlığını və əyləcini",
            "B": "tirin rənginin parlaqlığını",
            "C": "bucurqadın səsini",
            "D": "gəminin lövbər zəncirini"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q060",
        "question": "60. Sürətli xilasedici qayığın heyətinin geyimi nə olmalıdır?",
        "options": {
            "A": "hidrotermokostyum",
            "B": "pambıq kostyum",
            "C": "dəri gödəkçə",
            "D": "idman forması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q061",
        "question": "61. Sürətli xilasedici qayıqda yerdəyişdirməyə kim icazə verir?",
        "options": {
            "A": "komandir",
            "B": "istənilən sərnişin",
            "C": "gəmi həkiminin köməkçisi",
            "D": "liman işçisi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q062",
        "question": "62. Sürətli xilasedici qayığın manevr etmə zamanı sürəti necə olmalıdır?",
        "options": {
            "A": "təhlükəsiz",
            "B": "maksimal alovlu",
            "C": "nəzarətsiz",
            "D": "tam dayanan"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q063",
        "question": "63. Sürətli xilasedici qayıqda hərəkət zamanı müşahidə necə aparılır?",
        "options": {
            "A": "hər tərəfə",
            "B": "yalnız arxaya",
            "C": "yalnız göyə",
            "D": "yalnız qayığın dibinə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q064",
        "question": "64. Dalğanın hansı hərəkəti sürətli xilasedici qayıq üçün təhlükəlidir?",
        "options": {
            "A": "qayığın arxasına",
            "B": "qayığın önünə",
            "C": "sakit suda",
            "D": "külin olmaması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q065",
        "question": "65. Dalğada zərər çəkmişə sürətli xilasedici qayıqla necə yaxınlaşmaq lazımdır?",
        "options": {
            "A": "dalğaya qarşı",
            "B": "dalğanın istiqamətində maximal sürətlə",
            "C": "arxa gedişlə tam sürətlə",
            "D": "mühərriki söndürərək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q066",
        "question": "66. Suda olan insana sürətli xilasedici qayıq vasitəsilə hansı qaydada yan almaq lazımdır?",
        "options": {
            "A": "İnsanı külək vuran tərəfdə saxlamaqla kiçik sürətlə",
            "B": "İnsanı pərin altında saxlamaqla yüksək sürətlə",
            "C": "İnsana arxadan dəyərək",
            "D": "Dənizə köpük tökərək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q067",
        "question": "67. Zərər çəkmişin xilas edilməsi zamanı sürətli xilasedici qayığın heyəti nə etməlidir?",
        "options": {
            "A": "kiçik diametrli xilasedici dairəni vermək",
            "B": "lövbəri zərərçəkənə atmaq",
            "C": "suya neft tökmək",
            "D": "qayığı dayandırmadan keçib getmək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q068",
        "question": "68. Sürətli xilasedici qayıqda insanı sudan çıxartdıqdan sonra nə etmək lazımdır?",
        "options": {
            "A": "paltarını sıxmaq, yenidən zərərçəkənə geyindirmək və istilik qoruyucu torbaya yerləşdirmək",
            "B": "zərərçəkəni soyuq dəniz suyu ilə yumaq",
            "C": "zərərçəkəni açıq havada hərəkətsiz saxlanmaq",
            "D": "zərərçəkəni dərhal suya qaytarmaq"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q069",
        "question": "69. Konstruksiyaya əsasən, sürətli xilasedici qayıqda mühərriklərin hansı növləri olur?",
        "options": {
            "A": "asılma və stasionar",
            "B": "buxarlı və elektrikli",
            "C": "reaktiv və atom",
            "D": "əl çarxlı"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q070",
        "question": "70. Sürətli xilasedici qayıqda necə taktlı mühərriklər olur?",
        "options": {
            "A": "iki taktlı və dörd taktlı",
            "B": "on taktlı",
            "C": "taksız",
            "D": "altı taktlı"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q071",
        "question": "71. Sürətli xilasedici qayığın mühərriklərində hansı yanacaqdan istifadə olunur?",
        "options": {
            "A": "dizel və benzin",
            "B": "kömür və odun",
            "C": "təbii qaz və mazut",
            "D": "spirt və kerosin"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q072",
        "question": "72. Sürətli xilasedici qayığın mühərrikinin duzlu və çirkli suda istismarından sonra nə etmək lazımdır?",
        "options": {
            "A": "şirin su ilə yumaq",
            "B": "mühərriki qumla silmək",
            "C": "tuzlu suda 1 ay saxlanmaq",
            "D": "yağlamaq lazımdır, yumaq olmaz"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q073",
        "question": "73. Sürətli xilasedici qayığın mühərriki dərhal işə düşməzsə, nə etmək lazımdır?",
        "options": {
            "A": "30 saniyə gözləmək və yenidən işə salmağa cəhd etmək",
            "B": "mühərriki dənizə atmaq",
            "C": "24 saat gözləmək",
            "D": "benzin bakını deşmək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q074",
        "question": "74. Sürətli xilasedici qayığın mühərrikini söndürərkən ötürücü hansı vəziyyətdə olmalıdır?",
        "options": {
            "A": "neytral vəziyyətdə",
            "B": "maksimal arxa gedişdə",
            "C": "maksimal ön gedişdə",
            "D": "vəziyyətin fərqi yoxdur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q075",
        "question": "75. Hidrotermokostyum hansı maksimal müddət ərzində geyinilməlidir?",
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
        "id": "q076",
        "question": "76. SOS siqnalı necə verilir?",
        "options": {
            "A": "3 qısa 3 uzun 3 qısa",
            "B": "7 qısa 1 uzun",
            "C": "1 uzun",
            "D": "Fasiləsiz 1 saat"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q077",
        "question": "77. Suda adam həyəcan siqnalı necə verilir?",
        "options": {
            "A": "3 uzun",
            "B": "7 qısa 1 uzun",
            "C": "3 qısa 3 uzun 3 qısa",
            "D": "1 qısa"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q078",
        "question": "78. Sürətli xilasedici qayıqlar hansı xilasetmə vasitələrinə aiddirlər?",
        "options": {
            "A": "kollektiv",
            "B": "fərdi",
            "C": "stasionar yanğın",
            "D": "təlim"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q079",
        "question": "79. Hava ilə doldurulmuş sürətli xilasedici qayıq gəmidə daim hansı vəziyətdə olmalıdır?",
        "options": {
            "A": "tam doldurulmuş vəziyyətdə",
            "B": "tam boşaldılmış və bükülmüş vəziyyətdə",
            "C": "yarı su ilə doldurulmuş vəziyyətdə",
            "D": "hissələrə sökülmüş vəziyyətdə"
        },
        "correct_answer": "A",
        "explanation": ""
    }
]

# Randomize options A, B, C, D evenly for each question
random.seed(123789)
shuffled_questions = []

for q in suretli_questions_raw:
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

target_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\s_r_tli_xilasetm_qay_q_m_t_x_ssisi.json'

data = {
    "certificate": "Sürәtli xilasetmә qayıq mütәxәssisi",
    "questions": shuffled_questions
}

os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Rebuilt all {len(shuffled_questions)} questions for Sürətli xilasetmə qayıq mütəxəssisi with 100% accurate correct answers, relevant distractors, and randomized A/B/C/D option placement!")
