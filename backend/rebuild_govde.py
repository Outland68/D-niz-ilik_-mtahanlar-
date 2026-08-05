import json, os, random

govde_questions_raw = [
    {
        "id": "q001",
        "question": "1. Göyərtədə yükləri yükləməzdən əvvəl hansı proseduraları yerinə yetirmək lazımdır?\n1. yük ötürmələrinin etibarlığını yoxlamaq;\n2. şpiqatları çirkdən təmizləmək, onların sazlığını yoxlamaq;\n3. gəminin uzunluğunu nəzərə almaq;\n4. yüklərin ölçülərinin yoxlanılmadan bərkidilməsi;\n5. lövbər bucurqadının işlək vəziyyətdə olmasını yoxlamaq",
        "options": {
            "A": "1,2",
            "B": "3,4,5",
            "C": "1,3,5",
            "D": "2,4"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q002",
        "question": "2. Yükün daşınması üçün Agentlik və müstəqil sürveyer nəyi yoxlayır?",
        "options": {
            "A": "yük otaqlarının hazırlığını",
            "B": "kapitanın şəxsi sənədlərini",
            "C": "gəmi aşpazının tibbi arayışını",
            "D": "liman kranlarının rəngini"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q003",
        "question": "3. İstifadə olunan bərkitmə sistemindən asılı olaraq yüklər neçə sayda bölünürlər?",
        "options": {
            "A": "3",
            "B": "10",
            "C": "1",
            "D": "Bölünmürlər"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q004",
        "question": "4. Standart yük hansı yüklərdir?",
        "options": {
            "A": "konteynerlər, lixterlər, vaqonlar",
            "B": "dökülmə buğda və arpa",
            "C": "tikinti daşı və qum",
            "D": "xam neft və mazut"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q005",
        "question": "5. Özüyeriyən texnikanın apparel üzərinə çıxma sürəti neçə km/saat-ı aşmamalıdır?",
        "options": {
            "A": "10 km/saat",
            "B": "50 km/saat",
            "C": "100 km/saat",
            "D": "2 km/saat"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q006",
        "question": "6. Özüyeriyən texnikanın gəmiyə sürülərək gətirilməsi, qoyulması və bərkidilməsi kimlər təfəfindən həyata keçirilir?",
        "options": {
            "A": "liman dokerləri briqadası təfəfindən",
            "B": "yalnız gəmi kapitanı tərəfindən",
            "C": "sərnişinlərin özləri tərəfindən",
            "D": "liman polisi tərəfindən"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q007",
        "question": "7. Hərəkət edən texnikanı daşımaq üçün təyin edilən yük otağı nələr ilə təmin edilməlidir?\n1. su ilə yanğınsöndürmə sistemi ilə;\n2. su səpələmə və su örtüyü ilə;\n3. köpüklə yanğınsöndürmə ilə;\n4. koşma ilə;\n5. karbon qazlı yanğınsöndürmə ilə",
        "options": {
            "A": "1,2,3,5",
            "B": "1,4",
            "C": "2,4,5",
            "D": "3,4"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q008",
        "question": "8. RO-RO tipli sərnişin gəmilərində yük yerlərinin bərkidilməsi üçün hansı amilləri nəzərə almaq lazımdır?\n1. gəminin yırğalanması zamanı təsir gösterən qüvvələri;\n2. gəminin zədələnməsi və ya su ilə basılması nəticəsində yana əyilmə bucağını;\n3. gəminin sürətinin azaldılmasını;\n4. gəminin yanğın sistemlərinin işlək vəziyyətdə olmasını;\n5. yükün bərkidilməsi üçün qurğuların istifadəsinin effektivliyini",
        "options": {
            "A": "1,2",
            "B": "3,4,5",
            "C": "2,3,4",
            "D": "1,4"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q009",
        "question": "9. Roll-treylerlər və qoşqular hansı tip gəmilərdə daşınmalıdır?",
        "options": {
            "A": "Ro-Ro tipli xüsusi gəmilərdə və ya avto-sərnişin bərələrində",
            "B": "Yalnız balıqçı tankerlərində",
            "C": "Yalnız qazdaşıyan LNG gəmilərində",
            "D": "Yalnız sualtı qayıqlarda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q010",
        "question": "10. Minik avtomobillərinin yerləşdirilməsi zamanı bortlar və bamperlər arasında məsafə nə qədər olmalıdır?",
        "options": {
            "A": "bortlar 100-30 mm; bamperlər-10 mm",
            "B": "bortlar 1000 mm; bamperlər-500 mm",
            "C": "bortlar 10 mm; bamperlər-2 mm",
            "D": "Məsafə qoyulması tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q011",
        "question": "11. Rol-treyler arasındakı eninə və uzununa məsafə nə qədər olmalıdır?",
        "options": {
            "A": "Eninə -300 mm, uzununa -600 mm",
            "B": "Eninə -50 mm, uzununa -100 mm",
            "C": "Eninə -2000 mm, uzununa -5000 mm",
            "D": "Məsafə qoyulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q012",
        "question": "12. Hərəkət edən texnikanın bərkidilməsi üçün olan naytovlar nəyə malik olmalıdır?",
        "options": {
            "A": "markalanmaya və şəhadətnaməyə",
            "B": "yalnız al-qırmızı rəngə",
            "C": "yalnız taxta tutacağa",
            "D": "plastik örtüyə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q013",
        "question": "13. Yükü bərkitmək üçün gəmi vasitələri neçə növə bölünür?",
        "options": {
            "A": "2",
            "B": "10",
            "C": "5",
            "D": "Bölünmür"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q014",
        "question": "14. Konteynerin daxilində yüklərin yer dəyişməsi nəticəsində orada olan əşyaların xarab olması və sınması ilə əlaqədar cavabdehlik kimin üzərinə düşür?",
        "options": {
            "A": "yük göndərənin",
            "B": "gəmi növbətçi matrosunun",
            "C": "liman mühafizəçisinin",
            "D": "gəmi aşpazının"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q015",
        "question": "15. Konteynerdə ev əşyaları daşınan zaman konteynerdə yerləşdirilən əşyaların siyahısı neçə nüsxədə tərtib olunur?",
        "options": {
            "A": "2",
            "B": "10",
            "C": "1",
            "D": "5"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q016",
        "question": "16. Konteynerlə daşınan ev əşyalarının siyahısı kimlərdə və haralarda olur?",
        "options": {
            "A": "konteynerə qoyulur, yük göndərənə təqdim edilir və yük göndərən limanda qalır",
            "B": "yalnız liman bələdçisinin cibində olur",
            "C": "kapitanın seyfində saxlanılır",
            "D": "dənizə atılır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q017",
        "question": "17. Təhlükəli yüklərin daşınması zamanı yaradılmış gəmi komissiyası nələri yoxlamalıdır?",
        "options": {
            "A": "gəmi sistemlərinin texniki vəziyyətini, texniki təlimatını, yük yerlərinin vəziyyətini",
            "B": "yalnız sərnişinlərin geyim tərzini",
            "C": "yalnız gəmi mətbəxinin yemək menyusunu",
            "D": "yalnız liman binasının rəngini"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q018",
        "question": "18. Avtomobil göyərtəsində yükləmə və boşaltma işləri aparan zaman xəbərdarlıq işarələri hansı rəngdə olmalıdır?",
        "options": {
            "A": "parlaq",
            "B": "qara",
            "C": "şəffaf",
            "D": "boz"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q019",
        "question": "19. Avtomobil göyərtəsində yükləmə və boşaltma işlərində çalışan personalın iş geyimi necə olmalıdır?",
        "options": {
            "A": "parlaq",
            "B": "qara",
            "C": "tünd göy",
            "D": "rəngsiz"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q020",
        "question": "20. Təhlükəli yüklərin daşınması zamanı gəmi komissiyası hansı tərkibdə yaradılır?",
        "options": {
            "A": "kapitanın baş köməkçisi, 2-ci köməkçi, 2-ci mexanik, elektrik mexaniki və bosman",
            "B": "kapitan, baş mexanik və aşpaz",
            "C": "yalnız 3 nəfər matros",
            "D": "liman polisi və gömrük işçisi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q021",
        "question": "21. Təhlükəli yüklərin konteynerdə və ya nəqliyyat vasitəsində düzgün yığılmadığı və bərkidilmədiyi səbəbindən baş verən hadisəyə görə cavabdehlik kimin üzərinə düşür?",
        "options": {
            "A": "yük göndərənin və ya yükləmə işləri aparan limanın",
            "B": "növbətçi matrosun",
            "C": "gəmi həkiminin",
            "D": "gəminin sükançısının"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q022",
        "question": "22. Təhlükəli yüklər yüklənərkən və boşaldılarkən yükləmə üçün gözləyən yük avtomobilləri gəmidən neçə metr kənarda saxlanılmalıdır?",
        "options": {
            "A": "25 metrdən az olmayaraq",
            "B": "1 metr",
            "C": "100 metrdən çox",
            "D": "Məsafə tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q023",
        "question": "23. RO-RO gəmilərində yanğın təhlükəli yüklərin yüklənməsi əməliyyatları zamanı gəminin yük yerlərində və ya apareli hissəsində siqaret çəkilməsinin qadağan olduğu barədə neçə dildə xəbərdarlıq lövhələri qoyulmalıdır?",
        "options": {
            "A": "gəminin işçi və ingilis dillərində",
            "B": "yalnız fransız dilində",
            "C": "yalnız alman dilində",
            "D": "lövhə qoyulması tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q024",
        "question": "24. RO-RO gəmilərində yanğın təhlükəli yüklərlə işləyən zaman gəminin radioqovşağı ilə gündə neçə dəfə gəmi üzrə yanğın əleyhinə rejimə riayət olunmasının zəruriliyi barədə əmrdən çıxarış səslənməlidir?",
        "options": {
            "A": "gündə 2 dəfədən az olmayaraq",
            "B": "ayda 1 dəfə",
            "C": "yazda 1 dəfə",
            "D": "səslənməməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q025",
        "question": "25. Dəniz donanması gəmilərində hərəkətli texnikanın təhlükəsiz daşınması üçün hansı qanunlar nəzərə alınmalıdır?",
        "options": {
            "A": "Yüklərin yerləşdirilməsi və bərkidilməsi üzrə təhlükəsiz təcrübə kodeksi (CSS Code)",
            "B": "Yalnız yol hərəkəti haqqında qanun",
            "C": "Yalnız şəhər nəqliyyatı tarifləri",
            "D": "Yalnız aviasiya təhlükəsizlik kodeksi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q026",
        "question": "26. Konteynerdə partlayıcı maddə daşınırsa hansı qaydalar yerinə yetirilməlidir?",
        "options": {
            "A": "Dəniz gəmilərində konteynerdə partlayıcı maddələrin daşınması qaydaları",
            "B": "Mülki aviasiya baqaj daşıma qaydaları",
            "C": "Şəhər tramvay istismar qaydaları",
            "D": "Dəmir yolu sərnişin daşıma qaydaları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q027",
        "question": "27. Ro-Ro tipli gəmilərdə təhlükəli yük yüklənmiş hərəkətli texnika daşındıqda hansı qaydalar yerinə yetirilməlidir?",
        "options": {
            "A": "Təhlükəli yüklərin dəniz yolu ilə daşınması haqqında Beynəlxalq Məcəllə (IMDG Code)",
            "B": "Yalnız liman tikinti normaları",
            "C": "Yalnız dəniz balıqçılığı qaydaları",
            "D": "Yalnız gəmi rəngləmə standartları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q028",
        "question": "28. Hansı gəmiyə Ro-Ro gəmisi deyilir?",
        "options": {
            "A": "Avtomobilləri, treylerləri və digər təkərli texnikanı müstəqil surətdə və ya dartıcıların köməyi ilə yükləyib-boşaltmağa imkan verən arxa və ön (burun) hissələrində apareli olan xüsusi konstruksiyalı, üfüqi üsulla yüklənilib-boşaldılan gəmi",
            "B": "Yalnız ağac və kütük daşıyan açıq göyərtəli gəmi",
            "C": "Yalnız maye qaz daşıyan izolyasiyalı tanker",
            "D": "Yalnız sualtı elmi-tədqiqat gəmisi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q029",
        "question": "29. Ro-Ro sərnişin gəmilərində əsasən hansı yüklər daşınır?",
        "options": {
            "A": "hər cür ümumi yüklər (hərəkətli texnika, tara-ədədli yüklər, paket şəklində olan yüklər və s.), konteynerlər, ağır çəkili və iri həcmli yüklər",
            "B": "Yalnız dəniz suyu",
            "C": "Yalnız xam neft",
            "D": "Yalnız kömür tozu"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q030",
        "question": "30. Hansı vasitəyə “treyler” deyilir?",
        "options": {
            "A": "qabaq və arxa təkərləri olan avtoyol qoşqusu",
            "B": "yalnız motorlu dəniz qayığı",
            "C": "təkəri olmayan dəmir konteyner",
            "D": "gəmi fitinin səs qurğusu"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q031",
        "question": "31. Hansı vasitəyə “semitreyler” deyilir?",
        "options": {
            "A": "qabaq təkərləri olmayan avtoyol qoşqusu",
            "B": "dörd təkərli minik avtomobili",
            "C": "gəmi crane kranı",
            "D": "xilasedici sal"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q032",
        "question": "32. Hansı vasitəyə “roll-treyler” deyilir?",
        "options": {
            "A": "uzunluğu 6-12 metr olan xüsusi yük sahəli qoşqu və yarım qoşqu",
            "B": "gəmi pərinin valı",
            "C": "radar antenası",
            "D": "xilasedici jilet"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q033",
        "question": "33. Hərəkətli texnikanın gəmiyə yerləşdirilməsi yoxlama və ya qəza zamanı qapılara, lyuklara, yanğına qarşı avadanlıqlara və s. yetişmək üçün keçidlərin eni, mexanizmlər və avadanlıqlar arasında azad məsafə nə qədər olmalıdır?",
        "options": {
            "A": "0,6 metrdən az olmamalıdır",
            "B": "0,01 metrdən az olmamalıdır",
            "C": "5 metrdən az olmamalıdır",
            "D": "Məsafə tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q034",
        "question": "34. Hərəkətli texnika daşınan zaman yoxlama və ya qəza zamanı (qapılara, lyuklara, yanğına qarşı avadanlıqlara və s. yetişmək və istifadə etmək üçün) mexanizmlər və avadanlıqlar arasında azad sahə nə qədər olmalıdır?",
        "options": {
            "A": "1x1 m",
            "B": "10x10 m",
            "C": "0.1x0.1 m",
            "D": "Sahə tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q035",
        "question": "35. Ro-Ro sərnişin gəmilərində hərəkətli texnika yüklənərkən yüngül avtomobillər arasındakı məsafə nə qədər olmalıdır?",
        "options": {
            "A": "0,2 metrdən az olmayaraq",
            "B": "5 metrdən az olmayaraq",
            "C": "0,001 metrdən az olmayaraq",
            "D": "Məsafə saxlanılmır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q036",
        "question": "36. Ro-Ro sərnişin gəmilərində hərəkətli texnika yüklənərkən avtobuslar arasındakı məsafə nə qədər olmalıdır?",
        "options": {
            "A": "0,6 metrdən az olmayaraq",
            "B": "10 metrdən az olmayaraq",
            "C": "0,05 metrdən az olmayaraq",
            "D": "Məsafə saxlanılmır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q037",
        "question": "37. Ro-Ro sərnişin gəmilərində hərəkətli texnika yüklənərkən roll-treyler və qoşqular arasındakı məsafə nə qədər olmalıdır?",
        "options": {
            "A": "0,3 metrdən az olmayaraq",
            "B": "4 metrdən az olmayaraq",
            "C": "0,01 metrdən az olmayaraq",
            "D": "Məsafə saxlanılmır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q038",
        "question": "38. Ro-Ro sərnişin gəmilərində hərəkətli texnikanın apparelə keçid sürəti və gəmiyə hərəkəti neçə km/saat olmalıdır?",
        "options": {
            "A": "apparelə keçid sürəti 10 km/saatdan, gəmiyə hərəkəti 20 km/saatdan artıq olmamalıdır",
            "B": "apparelə keçid 100 km/saat, gəmiyə 150 km/saat olmalıdır",
            "C": "sürət məhdudiyyəti yoxdur",
            "D": "sürət 1 km/saatdan az olmalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q039",
        "question": "39. Sərnişinlərin minmə və enməsi zamanı nələrə riayət edilməlidir?",
        "options": {
            "A": "təhlükəsizliyin təmin olunmasına, hərəkət yerlərinin yaxşı işıqlandırılmasına, müdafiə olunmasına",
            "B": "bütün işıqların söndürülməsinə",
            "C": "sərnişinlərin tək-tək qaçmasına",
            "D": "gəmi pərinin maksimum fırlanmasına"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q040",
        "question": "40. Gəmi limandan ayrıldıqdan sonra sərnişinlərin toplanma təlimləri neçə saat ərzində keçirilməlidir?",
        "options": {
            "A": "24 saat",
            "B": "72 saat",
            "C": "1 ay ərzində",
            "D": "Təlim keçirilməsi tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q041",
        "question": "41. Gəmidə hərəkətli texnika yaxınlığında hansı təhlükəsizlik işarələri (yazıları) olmalıdır?",
        "options": {
            "A": "“açıq alovdan istifadə qadağandır”, “siqaret çəkmək qadağandır”",
            "B": "“biletlərin qiyməti 50 AZN”",
            "C": "“kapitan kayutası sağdadır”",
            "D": "“balıq tutmaq qadağandır”"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q042",
        "question": "42. Ümumgəmi həyəcan siqnalı və qayıq həyəcan siqnalına əsasən nizamlayıcıların vəzifələrinə nə aiddir?",
        "options": {
            "A": "sərnişinlərin tıxac, yığın olmadan, tez, mütəşəkkil və fasiləsiz xilasedici vasitələrə çıxarılması",
            "B": "sərnişinlərdən gəmi bileti tələb etmək",
            "C": "kayutların qapılarını kilidləyib açarları götürmək",
            "D": "gəmi mətbəxində yemək bişirmək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q043",
        "question": "43. Gəmini tərk etmək komandasını kim verir?",
        "options": {
            "A": "kapitan",
            "B": "növbətçi matros",
            "C": "gəmi aşpazı",
            "D": "sərnişinlərin böyüyü"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q044",
        "question": "44. Bütün həyəcan siqnalları üzrə məşqlər hansı vaxtda keçirilir?",
        "options": {
            "A": "sutkanın istənilən vaxtı",
            "B": "yalnız günortadan sonra saat 12:00-da",
            "C": "yalnız gecə saat 03:00-da",
            "D": "yalnız gəmi limanda olanda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q045",
        "question": "45. Yanğınla mübarizə üçün vasitələr harada olmalıdır?",
        "options": {
            "A": "xüsusi olaraq ayrılmış yerdə",
            "B": "kapitan kayutunda",
            "C": "istənilən yerdə",
            "D": "anbarın dərinliyində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q046",
        "question": "46. Gəmidə təhlükəli yüklə doldurulmuş bölməyə daxil olduqda hansı təhlükəsizlik qaydalarına riayət etmək lazımdır?",
        "options": {
            "A": "hava-qaz mühitini yoxlayaraq daxil olmaq",
            "B": "bölməyə dərhal açıq alovla daxil olmaq",
            "C": "bölmənin qapılarını bağlayıb gözləmək",
            "D": "elektrik işıqlarını tam söndürmək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q047",
        "question": "47. Yanğın zamanı yığılmış su nə vaxt xaric edilir?",
        "options": {
            "A": "yanğının söndürülməsi ilə eyni vaxtda",
            "B": "yanğın söndürüldükdən sonra",
            "C": "yanğın başlamazdan əvvəl",
            "D": "heç vaxt"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q048",
        "question": "48. Yanğın mənbəyini və ya onun əlamətlərini aşkar edən hər bir heyət üzvü nə etməlidir?",
        "options": {
            "A": "kapitan körpüsünə xəbər verməli və yanğının aradan qaldırılmasına başlamalıdır",
            "B": "bölməni bağlayıb təkbaşına gizlənməlidir",
            "C": "heç kimə xəbər vermədən yatmalıdır",
            "D": "gəmidən dənizə tullanmalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q049",
        "question": "49. SOLAS-74/78 Beynəlxalq Konvensiyaya müvafiq olaraq aşağıda qeyd olunan hansı hallarda gəminin dənizə çıxışı qadağan edilir?\n1. qayıqlar, sallar, üzən cihazlar tam komplektdə olmayarkən və ya onlar təyin edilmiş yerlərində olmayan zaman;\n2. qayıqlar, sallar nasaz olduğu zaman;\n3. buraxıcı (endirici) qurğular nasaz olduğu zaman;\n4. stasionar işıqlandırma vasitələri nasaz olduğu zaman;\n5. kapitanın baş köməkçisi məzuniyyətdə olan zaman.",
        "options": {
            "A": "1,2,3,4",
            "B": "1,5",
            "C": "2,4,5",
            "D": "3,5"
        },
        "correct_answer": "A",
        "explanation": ""
    }
]

# Randomize options A, B, C, D evenly for each question
random.seed(11111)
shuffled_questions = []

for q in govde_questions_raw:
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

target_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\s_rni_inl_rin_y_k_n_v_g_mi_g_vd_sinin_t_.json'

data = {
    "certificate": "Sərnişinlərin, yükün və gəmi gövdəsinin təhlükəsizliyi üzrə hazırlıq",
    "questions": shuffled_questions
}

os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Updated Question 10 correct answer to 'bortlar 100-30 mm; bamperlər-10 mm' for Sərnişinlərin, yükün və gəmi gövdəsinin təhlükəsizliyi üzrə hazırlıq!")
