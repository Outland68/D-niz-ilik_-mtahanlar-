import json, os

json_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_mexanikl_rinin_t_kmill_dirilm_si_is.json'

questions_data = [
    {
        "id": "q001",
        "question": "1. Nominal gücün 45-50% aşmayan yüklə işləyən dizel generatorların paralel rejimdə işləməsinin müddəti, davamiyyəti nə qədər olmalıdır?",
        "options": {
            "A": "Minimal",
            "B": "Ən azı 24 saat",
            "C": "Səfər boyu məhdudiyyətsiz",
            "D": "Ən azı 12 saat"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q002",
        "question": "2. Mürəkkəb şəraitlərdə üzmə zamanı valogeneratorların və ya utilizasiyalı turbogeneratorların istifadə edilməsinə icazə verilirmi?",
        "options": {
            "A": "Energetik qurğunun istismar rejimlərində qəflətən yarana bilən əhəmiyyətli dəyişikliklər zamanı elektrik enerjisinin fasiləsiz təchizatı təmin edildiyi hallarda icazə verilir",
            "B": "Bütün hallarda qətiyyən icazə verilmir",
            "C": "Yalnız limanda lövbərdə durduqda icazə verilir",
            "D": "Yalnız baş mühərrik dayandıqda icazə verilir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q003",
        "question": "3. Cərəyanla qurutma üsulundan hansı izolyasiya müqavimətinə malik olan elektrik maşınlarında tətbiq edilməsinə icazə verilir?",
        "options": {
            "A": "0.1 Mom-dan az olmayanda",
            "B": "0.01 Mom-dan az olmayanda",
            "C": "10 Mom-dan çox olduqda",
            "D": "İzolyasiya müqaviməti sıfır olduqda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q004",
        "question": "4. Akkumulyator batareyalarının texniki baxışlarının dövrilik (vaxtaşırılıq) müddətlərini qeyd edin?",
        "options": {
            "A": "Bir ayda bir dəfədən az olmayaraq",
            "B": "İldə bir dəfə",
            "C": "Hər gün növbə təhvilində",
            "D": "Hər 6 aydan bir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q005",
        "question": "5. Sinxron generatorların işə salınma və paralel iş rejiminə keçirilmə qaydaları nə ilə müəyyən edilir?",
        "options": {
            "A": "Mövcud olan sinxronlaşdırma vasitələri və elektrik stansiyasının avtomatlaşdırma səviyyəsi ilə",
            "B": "Gəminin üzmə sürəti və kursu ilə",
            "C": "Akkumulyator batareyalarının tutumu ilə",
            "D": "Karterdəki yağın temperaturu ilə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q006",
        "question": "6. Gəminin kəmiyyət mərkəzinin müəyyən edilməsini qeyd edin (center buoyancy)?",
        "options": {
            "A": "Suyun gəmiyə təsir edən hidrostatik təyziq qüvvələrinin əlavə nöqtəsi",
            "B": "Gəminin ağırlıq mərkəzinin ən yüksək nöqtəsi",
            "C": "Pər valının fırlanma oxu",
            "D": "Gəminin lövbər zəncirinin bərkidildiyi nöqtə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q007",
        "question": "7. Gəminin batmazlıq qabiliyyətini təmin edən əsas konstruktiv tədbirləri qeyd edin.",
        "options": {
            "A": "Gəmi gövdəsinin sukeçirməyən arakəsmələrə, göyərtələrə və platformalara bölüşdürülməsi",
            "B": "Gəminin lövbər zəncirlərinin uzadılması",
            "C": "Sükan yelləncəyinin sahəsinin artırılması",
            "D": "Buxar qazanlarının təzyiqinin azaldılması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q008",
        "question": "8. Gəminin üzmə ehtiyatının müəyyən edilməsini qeyd edin:",
        "options": {
            "A": "Gəmi gövdəsinin su keçirməzliyinin həcmi yük vater xəttindən yüksəkdə",
            "B": "Gəminin karterində olan yağın həcmi",
            "C": "Dizel-generatorların yanacaq çənlərinin tutumu",
            "D": "Suüstü hissənin külək sahəsi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q009",
        "question": "9. DHDNÇ-78 Beynəlxalq Konvensiyasının tələblərinə əsasən baş mühərriklərinin gücü 750 kVt-dan 3000 kVt-dək olan 2-ci mexanik vəzifəsində işləmək üçün tələb edilən gəmidə minimal iş stajını qeyd edin.",
        "options": {
            "A": "12 ay",
            "B": "6 ay",
            "C": "24 ay",
            "D": "36 ay"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q010",
        "question": "10. Dənizdə baş vermiş hadisələrin baxılması qaydalarını hansı beynəlxalq sənəd nizamlayır (müəyyən edir)?",
        "options": {
            "A": "“Dəniz qəza hadisələrinin və anlaşılmazlıqlarının araşdırılmasına dair” Beynəlxalq Məcəllə",
            "B": "MARPOL 73/78 Konvensiyasının II Əlavəsi",
            "C": "SOLAS-74 Konvensiyasının IX Fəsli",
            "D": "Beynəlxalq Yük Nişanı Konvensiyası"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q011",
        "question": "11. Dənizin gəmilərdən çirkləndirilməsi qaydalarını hansı beynəlxalq sənəd nizamlayır (müəyyən edir)?",
        "options": {
            "A": "“Dənizin gəmilərdən çirkləndirilməsinin qarşısının alınması haqqında” 1973-cü il tarixli Beynəlxalq Konvensiya",
            "B": "DHDNÇ-78 Konvensiyası",
            "C": "COLREG-72 Qaydaları",
            "D": "STCW Məcəlləsinin B bölməsi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q012",
        "question": "12. DHDNÇ Beynəlxalq Konvensiyasının tələblərinə əsasən gəmidə hansı vəzifələr “idarəetmə” səviyyəsi üzrə məsuliyyətə malikdirlər?",
        "options": {
            "A": "Gəmi kapitanı, 2-ci mexanik, baş mexanik, kapitanın baş köməkçisi",
            "B": "Yalnız növbətçi mexanik və 3-cü köməkçi",
            "C": "Yalnız gəmi elektrik mexaniki və боцман",
            "D": "Yalnız matroslar və motoristlər"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q013",
        "question": "13. MARPOL-73/78 BK-nın V Əlavəsi gəmidə aşağıda qeyd edilənlərdən hansını tələb edir?",
        "options": {
            "A": "Zibillərin idarə edilməsi planı, Zibillərlə əməliyyatlara dair təşviqat plakatları, Zibillərlə əməliyyatların qeydiyyat jurnalı",
            "B": "Yalnız Neftlə əməliyyatlar jurnalı I hissə",
            "C": "Yalnız Ballast sularının idarə olunması planı",
            "D": "Yalnız Hava kirliliyinin qarşısının alınması şəhadətnaməsi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q014",
        "question": "14. MARPOL-73/78 BK-nın V Əlavəsində qeyd edilmiş “Xüsusi rayonlarda” gəmilərdən bortdan kənara, dənizə aşağıda qeyd edilənlərdən hansılarının tullanması qadağan edilmişdir?",
        "options": {
            "A": "Separasiya materialları, əsgi, metal, şüşə və plasmasdan hazırlanan məmulatlar, qablaşdırma materialları",
            "B": "Yalnız təmiz dəniz suyu",
            "C": "Yalnız təmizlənmiş ballast suyu",
            "D": "Yalnız dəniz balıqları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q015",
        "question": "15. MARPOL-73/78 BK-nın V Əlavəsində qeyd edilmiş “Xüsusi rayonlarda” sahilboyu üzgüçülükdə, sahildən 12 mildən az olmayan məsafədə olduqda, gəmilərdən bortdan kənara aşağıda qeyd edilənlərdən hansıların tullanmasına icazə verilir?",
        "options": {
            "A": "Diri balıq, xırdalanmış qida məhsulları",
            "B": "Plastik qablar və sintetik kanatlar",
            "C": "İşlənmiş mühərrik yağları",
            "D": "Metal qırıntıları və boya qutuları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q016",
        "question": "16. Yanğın təhlükəsizliyinə dair təlimatlandırmanın həyata keçirilməsi hansı şəkildə qeydiyyata alınır?",
        "options": {
            "A": "Təlimatlandırma haqqında jurnalda müvafiq qeydlərin həyata keçirilməsi",
            "B": "Şifahi şəkildə maşın bölməsində bildirməklə",
            "C": "Gəmi radiostansiyası ilə sahildəki müfəttişə bildirməklə",
            "D": "Qeydiyyata alınmasına ehtiyac yoxdur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q017",
        "question": "17. Gəminin yanğınsöndürmə sisteminin tərkibinə daxildir?",
        "options": {
            "A": "Boru xəttləri, Yanğınsöndürmə nasosları, Sistemin kran və klapanları, Yanğınsöndürmə qoltuqları və yanğınsöndürmə lülələri",
            "B": "Yalnız pər valı və sükan mekanizmi",
            "C": "Yalnız seyr fənərləri və gəmi fiti",
            "D": "Yalnız separatorlar və hidroforlar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q018",
        "question": "18. İdarəetmə postlarının otaqlarında saxlanması qadağandır:",
        "options": {
            "A": "Qazların, yanacaq materiallarının, oddan təhlükəli, tez yanan materialların",
            "B": "Seyr xəritələrinin və naviqasiya alətlərinin",
            "C": "Maşın jurnalının və texniki təlimatların",
            "D": "Növbətçi mexanikin şəxsi əşyalarının"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q019",
        "question": "19. Gəminin texniki istismarına dair gəminin baş mexanikinin göstərişləri və sərəncamları hansı növ heyət üzvləri üçün mütləqdir?",
        "options": {
            "A": "Gəminin bütün növ heyət üzvləri üçün",
            "B": "Yalnız 4-cü mexanik üçün",
            "C": "Yalnız elektrik mexaniki üçün",
            "D": "Yalnız aşpaz və stüard üçün"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q020",
        "question": "20. Gəmi jurnallarının qeydiyyatını kim aparır?",
        "options": {
            "A": "Dəniz limanının kapitanı",
            "B": "Gəminin baş mexaniki",
            "C": "Növbətçi matros",
            "D": "Tərsanə rəisi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q021",
        "question": "21. P = const sabit təyziqdə keçən bərabərçəkili proses necə adlanır?",
        "options": {
            "A": "İzobara prosesi",
            "B": "İzoXora prosesi",
            "C": "İzotermik proses",
            "D": "Adiabatik proses"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q022",
        "question": "22. Nizam-intizam qaydalarına zidd olan hərəkətlərə yol vermiş nəqliyyat donanması işçilərinə hansı növ intizam tənbehləri tətbiq edilə bilər?",
        "options": {
            "A": "Məzəmmət, töhmət, işdən azad edilmə, şiddətli töhmət, xidmətə uyğunsuzluq haqqında xəbərdarlıq etmə",
            "B": "Yalnız pul cəriməsi hüququ",
            "C": "Gəmi diplomunun ləğvi hüququ olmadan azad etmə",
            "D": "Növbə saatlarının iki dəfə artırılması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q023",
        "question": "23. Gəminin limanda və ya lövbərdə durduğu zaman maşın jurnalında hansı qeydlər aparılır?",
        "options": {
            "A": "Gəminin güc qurğularının hazırlığı, baş mühərriklərin iş rejimi, gəminin durduğu limanın adı, baş mühərriklərin işə salınma və işdən çıxarılma saatları, köməkçi mühərriklərin işi barədə məlumatlar",
            "B": "Yalnız liman rüsumlarının ödənilmə məbləği",
            "C": "Yalnız gəmiyə gələn qonaqların adları",
            "D": "Yalnız havanın nisbi rütubət faizi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q024",
        "question": "24. Biləvasitə mühərrikin silindirinin daxilində mexaniki işi nə yerinə yetirir?",
        "options": {
            "A": "Yanmış yanacağın istilik enerjisi",
            "B": "Soyutma suyunun hidrostatik təzyiqi",
            "C": "Yağlama yağının karterə axma sürəti",
            "D": "Hava kompressorunun elektrik mühərriki"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q025",
        "question": "25. Mühərrikin Silindir Porşen Qrupuna yanma kamerasında yaranan hansı qüvvələr təsir edir?",
        "options": {
            "A": "Termiki və mexaniki qüvvələr",
            "B": "Yalnız hidravlik qüvvələr",
            "C": "Yalnız inersiya qüvvələri",
            "D": "Elektromaqnit qüvvələri"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q026",
        "question": "26. Şəkillərdə iki növ Yüksək Təzyiqli Yanacaq nasosları (YTYN/ТНВД) göstərilmişdir. Zolotnik tipli YTYN-nu göstərin?",
        "options": {
            "A": "1",
            "B": "2",
            "C": "hər ikisi",
            "D": "heç biri"
        },
        "correct_answer": "A",
        "explanation": "",
        "image_url": "/images/g_mi_mexanikl_rinin_t_kmill_dirilm_si_is/q_026.jpeg"
    },
    {
        "id": "q027",
        "question": "27. İsti ehtiyat rejimində olmayan köməkçi dizel generatorların yüklənməsini qeyd edin?",
        "options": {
            "A": "3-5 dəqiqə qızdırılmaqla",
            "B": "Qızdırılmadan anında 100% yük verməklə",
            "C": "Ən azı 2 saat yüksüz işlətdikdən sonra",
            "D": "Yalnız baş mühərrik işlədikdə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q028",
        "question": "28. Addımı tənzimlənən vint (ATV/ВРШ) qurğusuna işləyən dizel mühərrikini sınaq məqsədi ilə işə salarkən pərin addımını hansı vəziyyətdə qoymaq lazımdır?",
        "options": {
            "A": "“0” vəziyyətinə",
            "B": "Maksimal gediş vəziyyətinə",
            "C": "Arxaya tam gediş vəziyyətinə",
            "D": "Vintin addımının fərqi yoxdur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q029",
        "question": "29. Dəniz registeri ilə yanğına qarşı xüsusi konstruktiv tədbirlərin qəbul edilməsi haqqında razılaşma olmadığı təqdirdə dəniz gəmilərində yanma temperaturu neçə dərəcədən az olan yanacağın istifadəsi qadağan edilmişdir?",
        "options": {
            "A": "60-dan az olan",
            "B": "100-dən az olan",
            "C": "30-dan az olan",
            "D": "15-dən az olan"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q030",
        "question": "30. Baş mühərrikin qəza zamanı qoruyucu sisteminin işdən ayrılması kim tərəfindən və hansı hallarda yerinə yetirilə bilər (və ya işdən ayrılmasına göstəriş verilə bilər)?",
        "options": {
            "A": "Gəminin qəzaya uğraması təhlükəsi mövcud olduğu təqdirdə kapitanın növbə köməkçisi və kapitanın növbə köməkçisinin göstərişi ilə növbətçi mexanik tərəfindən",
            "B": "İstənilən vaxt növbətçi motorist tərəfindən",
            "C": "Yalnız liman müfəttişinin yazılı icazəsi ilə",
            "D": "Qəza zamanı qoruyucu sistemi söndürmək qadağandır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q031",
        "question": "31. Xüsusi qızdırılma sistemi olmadığı təqdirdə yağı hansı üsul ilə qızdırmaq olar?",
        "options": {
            "A": "Yağın mühərrikin yağlama sisteminə vurub yenidən xaric etməklə (məcburi yağvurma ilə)",
            "B": "Açıq alovla karterin altını qızdırmaqla",
            "C": "Yağa qaynar su əlavə etməklə",
            "D": "Yağ çənini günəş şüası altında saxlamaqla"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q032",
        "question": "32. Mühərrikin gücünün bərabər olaraq silindirlər üzrə paylanılması nə ilə təmin edillir?",
        "options": {
            "A": "Tsikllıq yanacağın verilməsi ilə",
            "B": "Soyutma suyunun təzyiqinin artırılması ilə",
            "C": "Hava filtrinin təmizlənməsi ilə",
            "D": "Karter yağının səviyyəsinin azaldılması ilə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q033",
        "question": "33. Məsafədən idarəetmə sisteminin işinin yoxlanılması məqsədi ilə bütün mövcud olan idarəetmə postlarından turboaqreqatın sınaq üçün işə salınmasını nə zaman yerinə yetirmək lazımdır?",
        "options": {
            "A": "Turbinin qızdırılması üzrə işlər başa çatdıqdan sonra",
            "B": "Turbin tam soyuduqdan sonra",
            "C": "Gəmi limana daxil olduqdan sonra",
            "D": "Yalnız tərsanə təmiri zamanı"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q034",
        "question": "34. Silindirlər üzrə yanmanın maksimal təzyiqinin buraxıla bilən qiymətini qeyd edin (istismar təlimatında digər kənara çıxmalar göstərilmədiyi təqdirdə).",
        "options": {
            "A": "% 3,5",
            "B": "% 10,0",
            "C": "% 15,5",
            "D": "% 25,0"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q035",
        "question": "35. Termotənzimləyici vintelin (TTV/ТРВ) borucuqlarının və daxiledici ştuser daxil olmaqla TTV/ТРВ-dən sonrakı armaturlarının üst səthinin donması nəyin əlaməti olduğunu qeyd edin.",
        "options": {
            "A": "Normal işin əlamətidir",
            "B": "Freon sızmasının əlamətidir",
            "C": "Kompressorun zədələnməsinin əlamətidir",
            "D": "Yağın donmasının əlamətidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q036",
        "question": "36. Gəminin heyət üzvləri sırasından kim səfər zamanı sükan qurğusunu və onun idarəetmə mexanizmini vaxtaşırı olaraq yoxlamalıdır?",
        "options": {
            "A": "Növbətçi mexanik",
            "B": "Gəmi aşpazı",
            "C": "Təcrübəçi matros",
            "D": "Liman müfəttişi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q037",
        "question": "37. Kapitan körpüsündən gəmi baş dizel mühərrikinin və addımı tənzimlənən pər qurğusunun (ATP/ВРШ) məsafədən idarə edilməsi zamanı manevr və revers etməyə hazırlıq üzrə işlər kimin tərəfindən yerinə yetirilir?",
        "options": {
            "A": "Kapitanın növbə köməkçisi tərəfindən",
            "B": "Yalnız gəmi electricianı tərəfindən",
            "C": "Yalnız boatswain (боцман) tərəfindən",
            "D": "Yalnız mühərrik ustası tərəfindən"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q038",
        "question": "38. Baş mühərriklərin (ATP/ВРШ) idarə edilməsi kapitan körpüsünə verildiyi bütün hallarda hansı qurğunun yoxlayaraq istismara hazır vəziyyətə gətirilməsi lazımdır?",
        "options": {
            "A": "Maşın teleqrafını yoxlayaraq istismara hazır vəziyyətə gətirmək lazımdır.",
            "B": "Radar antenasını söndürmək lazımdır",
            "C": "Akkumulyator batareyasını ayırmaq lazımdır",
            "D": "Separatoları dayandırmaq lazımdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q039",
        "question": "39. Sutka ərzində gəminin növbətçi mexanikinə neçə saat ərzində istirahət saatı verilməlidir?",
        "options": {
            "A": "Ən azı (minimum) 10 saat",
            "B": "Ən azı 4 saat",
            "C": "Maksimum 2 saat",
            "D": "İstirahət saatı nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q040",
        "question": "40. Vaxtaşırı olaraq növbəsiz istismar edilən maşın bölmələrinə növbətçi mexaniki neçə saatdan bir gəlməlidir?",
        "options": {
            "A": "İstənilən anda çağırışa əsasən",
            "B": "Dəqiq hər 12 saatdan bir",
            "C": "Yalnız sutkada bir dəfə",
            "D": "Yalnız limana daxil olduqda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q041",
        "question": "41. Növbətçi mexanik növbədən kimin icazəsi olmadan uzaqlaşa (ayrıla) bilməz?",
        "options": {
            "A": "Gəminin baş mexanikinin və ya onun gəmidə olmadığı hallarda isə ikinci mexanikin müvafiq icazəsi olmadan növbəçəkmə yerini tərk edə bilməz;",
            "B": "Növbətçi matrosun icazəsi olmadan",
            "C": "Gəmi stüardının icazəsi olmadan",
            "D": "İstənilən vaxt icazəsiz ayrılaraq gedə bilər"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q042",
        "question": "42. “Sea – chest” sözünün düzgün olan tərcüməsini qeyd edin.",
        "options": {
            "A": "Kinqston",
            "B": "Dəniz sandığı / Lövbər quyusu",
            "C": "Karter yağ çəni",
            "D": "Buxar seperatoru"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q043",
        "question": "43. “Idle – running” sözünün düzgün olan tərcüməsini qeyd edin.",
        "options": {
            "A": "Boş – boşuna iş (yüksüz iş)",
            "B": "Tam yüklə iş",
            "C": "Fövqəladə dayandırılma",
            "D": "Əksinə fırlanma (revers)"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q044",
        "question": "44. “Frequency” sözünün düzgün tərcüməsini qeyd edin.",
        "options": {
            "A": "Tezlik",
            "B": "Elektrik gərginliyi",
            "C": "Müqavimət",
            "D": "Cərəyan şiddəti"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q045",
        "question": "45. “Crankcase” sözünün düzgün tərcüməsini qeyd edin.",
        "options": {
            "A": "Karter",
            "B": "Dirsəkli val",
            "C": "Porşen ştoku",
            "D": "Silindr qapağı"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q046",
        "question": "46. “Camshaft” sözünün düzgün tərcüməsini qeyd edin.",
        "options": {
            "A": "Paylayıcı val",
            "B": "Dirsəkli val",
            "C": "Pərin valı",
            "D": "Turbin rotoru"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q047",
        "question": "47. Birləşmə üsulunu üç bucaqlı birləşmədən ulduzvari birləşməyə dəyişdikdə dəyişən cərəyanlı asinxron elektrik mühərrikinin gücü necə dəyişər?",
        "options": {
            "A": "3 dəfə azalar",
            "B": "3 dəfə artar",
            "C": "2 dəfə azalar",
            "D": "Dəyişməz qalar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q048",
        "question": "48. Cərəyan göstəricisinin əvəzinə nəzarət elektrik lampasından istifadə etmək olarmı?",
        "options": {
            "A": "Qətiyyən olmaz",
            "B": "Yalnız aşağı gərginlikdə olar",
            "C": "Hər zaman olar",
            "D": "Yalnız baş mexanikin icazəsi ilə olar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q049",
        "question": "49. Dəyişən cərəyanın ölçülməsi məqsədi ilə ampermetrlərin ölçmə həddlərinin genişləndirilməsi üçün istifadə edilir:",
        "options": {
            "A": "Cərəyan ölçmə transformatoru",
            "B": "Şunt müqaviməti",
            "C": "Əlavə rezistor",
            "D": "Kondensator batareyası"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q050",
        "question": "50. Gəmi elektrik maşınlarının xidmət müddəti adətən nə ilə ölçülür?",
        "options": {
            "A": "İzolyasiyanın istismar müddəti ilə",
            "B": "Yastıqların aşınma müddəti ilə",
            "C": "Rotorun fırlanma dövrlərinin sayı ilə",
            "D": "Fırçaların dəyişdirilmə tezliyi ilə"
        },
        "correct_answer": "A",
        "explanation": ""
    }
]

data = {
    "certificate": "Gəmi mexaniklərinin təkmilləşdirilməsi (istismar səviyyəsində)",
    "questions": questions_data
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Fully created {len(questions_data)} questions (Questions 1 to 50) for Gəmi mexaniklərinin təkmilləşdirilməsi (istismar səviyyəsində) with contextually accurate distractors!")
