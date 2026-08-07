import json
import random
import os

def build():
    seed_val = 33319
    random.seed(seed_val)

    questions_data = [
        {
            "id": "q001",
            "q": "1. ARPA-da yaxınlaşma elementlərinə nə aiddir?",
            "ans": "CPA və TCPA",
            "distractors": ["BCR və BCT", "SOG və COG", "XTE və WOP"]
        },
        {
            "id": "q002",
            "q": "2. RADAR-da «True Motion» (TM) rejimində işləyərkən, müşahidə edən gəminin sürəti və kursu daxil etmə yanlışları nəticəsində hansı xətalar yarana bilər?",
            "ans": "Vəziyyətin qiymətləndirilməsində və manevrin seçilməsində",
            "distractors": [
                "Ekranda yalnız sabit hədəflərin itməsi müşahidə ediləcək",
                "Dalğalanma müdaxiləsi artacaq və ekran qaralacaq",
                "İmpulsun davamlılığı avtomatik olaraq aşağı düşəcək"
            ]
        },
        {
            "id": "q003",
            "q": "3. ARPA-da manevrin imitasiyası hansı hərəkət rejimində keçirilə bilər?",
            "ans": "RM (Relative Motion) və TM (True Motion)-da",
            "distractors": ["Yalnız Head Up (HU) rejimində", "Yalnız Course Up (CU) rejimində", "Yalnız North Up (NU) rejimində"]
        },
        {
            "id": "q004",
            "q": "4. RADAR-ın ekranında müşahidəçi vəziyyəti qiymətləndirərkən, ilkin məlumatın təhlilində nəyə diqqət etməlidir?",
            "ans": "Hədəfin və ya hədəflərin əks-səda siqnallarına",
            "distractors": [
                "Antennanın fırlanma sürətinə",
                "İmpulsun təkrarlanma tezliyinə",
                "Qəbuledicinin gücləndirilməsi səviyyəsinə"
            ]
        },
        {
            "id": "q005",
            "q": "5. Hədəfi tutduqdan sonra, ARPA-da sürət vektorunun ekranda görünməsinə qədər keçən vaxt nə qədər olmalıdır?",
            "ans": "1 dəqiqədən çox olmamalıdır",
            "distractors": ["30 saniyədən az olmalıdır", "3 dəqiqədən çox olmamalıdır", "5 dəqiqədən çox olmamalıdır"]
        },
        {
            "id": "q006",
            "q": "6. Hədəfi tutduqdan sonra, ARPA-da hərəkət elementlərinin hesablanmasına qədər keçən vaxt nə qədər olmalıdır?",
            "ans": "3 dəqiqədən çox olmamalıdır",
            "distractors": ["1 dəqiqədən çox olmamalıdır", "5 dəqiqədən çox olmamalıdır", "10 dəqiqədən çox olmamalıdır"]
        },
        {
            "id": "q007",
            "q": "7. ARPA-da seçilmiş manevrin statik imitasiyasında nə təsvir olunur?",
            "ans": "Manevrin sonuna uyğun vəziyyət",
            "distractors": [
                "Hədəflərin ancaq nisbi hərəkət sürəti",
                "Gəminin həqiqi hərəkət trayektoriyası",
                "Radar antennasının quraşdırılma xətası"
            ]
        },
        {
            "id": "q008",
            "q": "8. «Off Center» düyməsindən istifadə edərək, gəmimizin işarəsi, ekranın radiusuna görə, neçə faiz yerini dəyişə bilər?",
            "ans": "22%, 44%, 66%",
            "distractors": ["10%, 20%, 30%", "25%, 50%, 75%", "33%, 66%, 99%"]
        },
        {
            "id": "q009",
            "q": "9. Aşağıda göstərilən şəkil nə bildirir? RADAR «Relative Motion» (RM) rejimində işləyir.",
            "ans": "Hədəf hərəkətsizdir",
            "distractors": [
                "Hədəf bizimlə eyni kursda hərəkət edir",
                "Hədəf bizə qarşı hərəkət edir",
                "Hədəfin sürəti bizimkindən çoxdur"
            ]
        },
        {
            "id": "q010",
            "q": "10. Aşağıda göstərilən şəkil nə bildirir? RADAR «True Motion» (TM) rejimində işləyir.",
            "ans": "Hədəfin kursu 220º - dir",
            "distractors": ["Hədəfin sürəti 22 uzeldur", "Hədəfə qədər məsafə 2.2 mildir", "Hədəfin pelenqi 220º - dir"]
        },
        {
            "id": "q011",
            "q": "11. Aşağıda göstərilən şəkil nə bildirir? RADAR «Relative Motion» (RM) rejimində işləyir.",
            "ans": "Hədəfin kursu və sürəti bizim gəmimizinki ilə eynidir",
            "distractors": [
                "Hədəf hərəkətsizdir",
                "Hədəf dreyf edir",
                "Hədəfin kursu bizimkinə əksdir"
            ]
        },
        {
            "id": "q012",
            "q": "12. Aşağıda göstərilən şəkil nə bildirir? RADAR «True Motion» (TM) rejimində işləyir.",
            "ans": "Hədəf hərəkətsizdir",
            "distractors": [
                "Hədəf lövbərə durmaq üzrədir",
                "Hədəf sürətlə bizə yaxınlaşır",
                "Hədəf bizim sürətlə eyni sürətdə hərəkət edir"
            ]
        },
        {
            "id": "q013",
            "q": "13. Aşağıdakı şəkildə RADAR-ın təsviri hansı rejimində göstərilib?",
            "ans": "Nup",
            "distractors": ["Hup", "Cup", "RM"]
        },
        {
            "id": "q014",
            "q": "14. Aşağıdakı şəkildə RADAR-ın təsviri hansı rejimində göstərilib?",
            "ans": "Cup",
            "distractors": ["Nup", "Hup", "TM"]
        },
        {
            "id": "q015",
            "q": "15. Aşağıdakı şəkildə RADAR-ın təsviri hansı rejimində göstərilib?",
            "ans": "Hup",
            "distractors": ["Nup", "Cup", "True Vectors"]
        },
        {
            "id": "q016",
            "q": "16. İmpulsun davamlığı «MP» nə zaman istifadə etmək daha faydalıdır?",
            "ans": "Adi üzmə şəraitində",
            "distractors": [
                "Qatı duman şəraitində lövbərə durarkən",
                "Yalnız açıq okeanda uzaq hədəflər axtararkən",
                "Kanalda iki gəminin arasından keçərkən"
            ]
        },
        {
            "id": "q017",
            "q": "17. İmpulsun davamlığı «SP» nə zaman istifadə etmək daha faydalıdır?",
            "ans": "Hövzələrdə, körfəzlərdə hədəflərin çox olduğu yerlərdə. Yağışlı və fırtınalı havalarda",
            "distractors": [
                "Okeanda uzaq gəmiləri vaxtında aşkarlamaq üçün",
                "Günəşli havada dəniz sakit olarkən",
                "Sahildən çox uzaq məsafədə hərəkət edərkən"
            ]
        },
        {
            "id": "q018",
            "q": "18. İmpulsun davamlığı «LP» nə zaman istifadə etmək daha faydalıdır?",
            "ans": "Yaxşı hava şəraitində kiçik ölçülü hədəflərin aşkar edilməsində",
            "distractors": [
                "Liman akvatoriyasında manevr edərkən",
                "Dar kanallarda və ya çaylarda",
                "Buzlaq ərazilərində yaxınlıqdakı buzları görərkən"
            ]
        },
        {
            "id": "q019",
            "q": "19. RADAR hansı diapazonda işləyərkən, ölçülərin yüksək dəqiqliyi üçün imkan yaradır?",
            "ans": "X Band",
            "distractors": ["S Band", "L Band", "C Band"]
        },
        {
            "id": "q020",
            "q": "20. RADAR hansı diapazonda işləyərkən, maneələrə qarşı yüksək dayanıqlıq üçün imkan yaradır?",
            "ans": "S Band",
            "distractors": ["X Band", "L Band", "K Band"]
        },
        {
            "id": "q021",
            "q": "21. «Subrefraksiya» nə deməkdir?",
            "ans": "Hündürlükdə hava rütübətinin çoxalması nəticəsində və ya hava istiliyinin kəskin aşağı düşməsi nəticəsində əmələ gələn maneə",
            "distractors": [
                "Dalğaların təsiri altındakı radar şüalarının qırılması",
                "Radar siqnallarının buz dağlarından qayıtması",
                "Hava istiliyinin qəfil artması ilə yaranan vizual aldanma"
            ]
        },
        {
            "id": "q022",
            "q": "22. «No-Return Point» nə deməkdir?",
            "ans": "Dar keçiddə bu nöqtəni keçdikdən sonra, əgər vəziyyət ağırlaşarsa, gəmi açıq dənizə çıxa bilməyəcək",
            "distractors": [
                "Radarın hədəfi izləmə qabiliyyətini itirdiyi uzaq nöqtə",
                "Körpüdə olan bütün cihazların qəfil sıradan çıxması halı",
                "Radar siqnalının geri qayıtmadığı coğrafi mövqe"
            ]
        },
        {
            "id": "q023",
            "q": "23. Dar keçidlərdə təhlükəsiz üzməni təmin etmək üçün hansı stvorlardan istifadə olunur?",
            "ans": "Aparıcı, kəsən, çəpərləyici",
            "distractors": [
                "Yalnız lazer stvorlarından",
                "Zonal, radial, xətti stvorlardan",
                "Fırlanan və yanıb-sönən stvorlardan"
            ]
        },
        {
            "id": "q024",
            "q": "24. “Paralel İndeksasiyasından” (PI) nə zaman istifadə olunur?",
            "ans": "«RM» hərəkətin və «Nup» təsvirin rejimlərində, gəminin yerinə fasiləsiz nəzarət üçün",
            "distractors": [
                "TM rejimində ARPA vektorlarını ölçmək üçün",
                "Açıq okeanda avtopilotu tənzimləmək üçün",
                "Gəminin sürətini su üzərinə görə hesablamaq üçün"
            ]
        },
        {
            "id": "q025",
            "q": "25. Sürətin iki dəfə azaldılması manevrini yerinə yetirərkən, hədəfin Nisbi Hərəkət Xətti (NHX) və nisbi sürət vektoru (VN) necə dəyişir?",
            "ans": "NHX gəmimizin burun tərəfinə dəyişir, nisbi sürət azalır",
            "distractors": [
                "NHX arxa tərəfə dəyişir, nisbi sürət dəyişmir",
                "NHX dəyişmir, nisbi sürət çoxalır",
                "NHX gəmimizin bortu istiqamətində olur, nisbi sürət sıfıra bərabər olur"
            ]
        },
        {
            "id": "q026",
            "q": "26. Sürətin artırılması manevrini yerinə yetirərkən, hədəfin Nisbi Hərəkət Xətti (NHX) və nisbi sürət vektoru (VN) necə dəyişir?",
            "ans": "NHX gəmimizin arxa tərəfinə dəyişir, nisbi sürət artır",
            "distractors": [
                "NHX gəmimizin burun tərəfinə dəyişir, nisbi sürət artır",
                "NHX dəyişmir, lakin nisbi sürət azalır",
                "NHX sağ tərəfə meyl edir, nisbi sürət sabit qalır"
            ]
        },
        {
            "id": "q027",
            "q": "27. Sağa dönüb, sürəti artırmaq təhlükəli manevrində hansı hərəkət parametrlərinə diqqət vermək lazımdır?",
            "ans": "Bizim gəmimizin yeni kursuna",
            "distractors": [
                "Yalnız küləyin istiqamətinə",
                "Digər gəmilərin SOG göstəricisinə",
                "Yalnız əks axının sürətinə"
            ]
        },
        {
            "id": "q028",
            "q": "28. Sola dönüb, sürəti azaltmaq təhlükəli manevrində hansı hərəkət parametrlərinə diqqət vermək lazımdır?",
            "ans": "Bizim gəmimizin yeni sürətinə",
            "distractors": [
                "Ətrafdakı yelkənli gəmilərin sayına",
                "Radar antennasının hündürlüyünə",
                "Hədəflərin ancaq COG göstəricisinə"
            ]
        },
        {
            "id": "q029",
            "q": "29. Aşağıda göstərilən manevrlərdən hansı təhlükəli ola bilər?",
            "ans": "Sağa dönməklə sürətin artırılması",
            "distractors": [
                "Sağa dönməklə sürətin azaldılması",
                "Sola dönməklə sürətin azaldılması",
                "Heç bir kurs dəyişikliyi etmədən dayandırılması"
            ]
        },
        {
            "id": "q030",
            "q": "30. Aşağıda göstərilən manevrlərdən hansı effektli sayılır?",
            "ans": "Sağa dönməklə sürətin azaldılması",
            "distractors": [
                "Sola dönməklə sürətin artırılması",
                "Yalnız sola dönüş etmək",
                "Sürəti maksimal dərəcədə artırmaq"
            ]
        },
        {
            "id": "q031",
            "q": "31. Toqquşma təhlükəsi hansı ölçülərə əsasən qiymətləndirilir?",
            "ans": "CPA, TCPA",
            "distractors": ["BCR, BCT", "XTE, BTW", "COG, SOG"]
        },
        {
            "id": "q032",
            "q": "32. RADAR “X Band”-də dalğanın uzunluğu və tezliklərin diapazonu nə qədər olmalıdır?",
            "ans": "Tezlik: 9000 MHz, dalğanın uzunluğu 3 sm",
            "distractors": [
                "Tezlik: 3000 MHz, dalğanın uzunluğu 10 sm",
                "Tezlik: 5000 MHz, dalğanın uzunluğu 5 sm",
                "Tezlik: 1500 MHz, dalğanın uzunluğu 20 sm"
            ]
        },
        {
            "id": "q033",
            "q": "33. RADAR “S Band”-də dalğanın uzunluğu və tezliklərin diapazonu nə qədər olmalıdır?",
            "ans": "Tezlik: 3000 MHz, dalğanın uzunluğu 10 sm",
            "distractors": [
                "Tezlik: 9000 MHz, dalğanın uzunluğu 3 sm",
                "Tezlik: 4000 MHz, dalğanın uzunluğu 7 sm",
                "Tezlik: 6000 MHz, dalğanın uzunluğu 8 sm"
            ]
        },
        {
            "id": "q034",
            "q": "34. Planşetdə gördüyünüz gəmi (qırmızı nöqtələr) hansı manevr edib?",
            "ans": "Hədəf 6-cı dəqiqədən sonra sola dönüb və təhlükəli olub",
            "distractors": [
                "Hədəf sürətini kəskin azaldıb və bizdən uzaqlaşıb",
                "Hədəf sağa dönərək toqquşma ehtimalını azaldıb",
                "Hədəf dreyf edir və hərəkətsizdir"
            ]
        },
        {
            "id": "q035",
            "q": "35. Əgər biz öz gəmimizin kursunu 45º sağ tərəfə dəyişsək, bizim üçün planşetdə göstərilən gəmilərdən hansı ən təhlükəli olabilər?",
            "ans": "B və C gəmilər",
            "distractors": ["A və D gəmilər", "Yalnız E gəmisi", "Heç bir gəmi"]
        },
        {
            "id": "q036",
            "q": "36. Planşetdə gördüyünüz gəmi (qırmızı nöqtələr) hansı manevr edib?",
            "ans": "9-cu dəqiqədən sonra kursunu sol tərəfə dəyişib, sürətini azaldıb",
            "distractors": [
                "Kursunu sağa dəyişib, sürətini artırıb",
                "Sürətini artıraraq bizimlə paralel kursa keçib",
                "Maşını geri işlədərək təcili dayanıb"
            ]
        },
        {
            "id": "q037",
            "q": "37. Planşetdə gördüyünüz gəmi (qırmızı nöqtələr) hansı manevr edib?",
            "ans": "Hərəkətsiz hədəf 6-cı dəqiqədən sonra hərəkətə başlayıb",
            "distractors": [
                "Hədəf sağa dönüş edərək arxamıza keçib",
                "Hədəf qəflətən yoxa çıxıb, radar siqnalı itib",
                "Hədəf lövbərə dayanıb"
            ]
        },
        {
            "id": "q038",
            "q": "38. Planşetdə gördüyünüz gəmi (qırmızı nöqtələr) hansı manevr edib?",
            "ans": "12-ci dəqiqədən sonra hədəf bizim gəmimizlə eyni kursla hərəkət edir, sürətini azaldıb",
            "distractors": [
                "12-ci dəqiqədən sonra hədəf əks kursla tam sürətlə hərəkətə başlayıb",
                "Hədəf 90 dərəcə sola dönüb",
                "Hədəf hərəkətsiz vəziyyətə keçib"
            ]
        },
        {
            "id": "q039",
            "q": "39. Planşetdə gördüyünüz gəmi (qırmızı nöqtələr) hansı manevr edib?",
            "ans": "12-ci dəqiqədən sonra hədəfin kursu bizim gəmimizin əksidir",
            "distractors": [
                "Hədəf bizimlə paralel kursda hərəkətini davam etdirir",
                "Hədəf xəbərdarlıq siqnalı vermədən dayanıb",
                "12-ci dəqiqədən sonra hədəfin sürəti bizimkindən 3 dəfə çoxdur"
            ]
        },
        {
            "id": "q040",
            "q": "40. Qaydalara əsasən yelkənli gəmi hərəkətdə olarkən yol verməlidir:",
            "ans": "Balıq ovu ilə məşğul olan gəmiyə",
            "distractors": [
                "Bütün mexaniki mühərrikli gəmilərə",
                "Heç bir gəmiyə yol verməməlidir",
                "Yalnız uzunluğu 50 metrdən çox olan gəmilərə"
            ]
        },
        {
            "id": "q041",
            "q": "41. Qaydalara əsasən mexaniki mühərrikli gəmi hərəkətdə olarkən yol verməlidir:",
            "ans": "Balıq ovu ilə məşğul olan, yelkənli gəmilərə",
            "distractors": [
                "Yalnız digər mexaniki mühərrikli gəmilərə",
                "Bütün sərnişin gəmilərinə",
                "Lokmansız gəmilərə"
            ]
        },
        {
            "id": "q042",
            "q": "42. Qaydalara əsasən, hansı gəminin və ya gəmilərin vəzifə borcu - suya oturumundan çəkinən gəmiyə yol verməkdir?",
            "ans": "Heç bir gəminin",
            "distractors": [
                "Balıq ovu ilə məşğul olan gəmilərin",
                "Yelkənli gəmilərin",
                "Bütün mexaniki mühərrikli gəmilərin"
            ]
        },
        {
            "id": "q043",
            "q": "43. Hansı manevr imkanı məhdudlaşmış gəmilərdə vertikal xətt boyunca yerləşmiş “qırmızı, ağ, qırmızı” işıqlar və “şar, romb, şar” işarələri göstərilmir?",
            "ans": "Mina təhlükəsini aradan qaldırma işləri ilə məşğul olan gəmilərdə",
            "distractors": [
                "Kabel və ya boru kəməri çəkən gəmilərdə",
                "Dənizdə digər gəmini yedəyə alan gəmilərdə",
                "Dib dərinləşdirmə işləri aparan gəmilərdə"
            ]
        },
        {
            "id": "q044",
            "q": "44. Suya oturumundan çəkinən gəmiyə aid olan doğru cavabı qeyd edin.",
            "ans": "Yaxşı görünən yerdə vertikal xətt boyunca üç dairəvi qırmızı işıq və ya silindir göstərə bilər",
            "distractors": [
                "Vertikal xətt boyunca üç yaşıl işıq və ya konus göstərməlidir",
                "Sadəcə bir ağ lövbər işığı yandırmalıdır",
                "Göy bayraq və iki dairəvi sarı işıq göstərməlidir"
            ]
        },
        {
            "id": "q045",
            "q": "45. COLREG-72-də Qayda-18 nə bildirir?",
            "ans": "Ekranoplan havaya qalxarkən, enərkən və səthə yaxın uçarkən bütün gəmilərdən kənarda durmalı və onların hərəkətini çətinləşdirməməlidir. Ekranoplan su üzərində olarkən “B” Hissəsinin Qaydalarını mexaniki mühərrikli gəmi kimi yerinə yetirməlidir",
            "distractors": [
                "Bütün hərbi gəmilər dar kanallarda xüsusi üstünlüyə malikdir",
                "Yelkənli gəmilər hər zaman mühərrikli gəmilərdən yol tələb edə bilər",
                "Yedək gəmiləri ancaq gündüz vaxtı digər gəmilərə yol verməlidir"
            ]
        },
        {
            "id": "q046",
            "q": "46. Balıq ovu ilə məşğul olan gəmi hərəkətdə olarkən:",
            "ans": "İdarəetmə imkanından məhrum olunmuş və manevretmə imkanı məhdudlaşmış gəmilərə mümkün qədər yol verməlidir, suya oturumundan çəkinən gəminin təhlükəsiz keçidini, əgər vəziyyət imkan verirsə çətinləşdirməməlidir",
            "distractors": [
                "Bütün digər gəmilər ona yol verməlidir",
                "Yalnız mühərrikli gəmilərə yol verməlidir",
                "Dar kanalda hər zaman üstünlük təşkil edir və yol vermir"
            ]
        },
        {
            "id": "q047",
            "q": "47. RADAR-ın ekranında müşahidəçi vəziyyəti qiymətləndirərkən, ikinci məlumatın təhlilində nəyə diqqət edilməlidir?",
            "ans": "Vektorlara və rəqəmsal məlumatlara",
            "distractors": [
                "Hava şəraitinin pisləşməsinə və buludlara",
                "Suyun dərinliyinə və qabarma göstəricisinə",
                "Qəbuledicinin tezlik diapazonuna"
            ]
        },
        {
            "id": "q048",
            "q": "48. Hərəkətin bölünmə sistemindən istifadə edən gəmi digər qabağda hərəkət edən gəmini sağ bortu tərəfindən ötmək üçün səs ilə hansı siqnalı verməlidir?",
            "ans": "Heç bir siqnal verməməlidir",
            "distractors": [
                "Bir uzun və bir qısa səs siqnalı",
                "İki qısa səs siqnalı",
                "Üç qısa və iki uzun səs siqnalı"
            ]
        },
        {
            "id": "q049",
            "q": "49. Dar keçiddə və ya farvaterdə hərəkət edən gəmi digər qabağda hərəkət edən gəmini sağ bortu tərəfindən ötmək üçün (gəmilər məhdud görünüş şəraitində hərəkət edirlər) səs ilə hansı siqnalı verməlidir?",
            "ans": "Heç bir siqnal verməməlidir",
            "distractors": [
                "Fasiləsiz zəng səsi",
                "İki uzun və bir qısa siqnal",
                "Bir qısa səs siqnalı"
            ]
        },
        {
            "id": "q050",
            "q": "50. Şəkildə gördüyünüz “B” yelkənli gəmi Qaydalara əsasən hansı tədbir görməlidir? (toqquşma təhlükəsi mövcuddur)",
            "ans": "“A” gəmi tam keçilməyənədək, tam arxada qalmayanadək, “A” gəminin yolundan kənar olmalıdır",
            "distractors": [
                "Dərhal sürətini artıraraq A gəmisinin önündən keçməlidir",
                "Beş qısa səs siqnalı verib öz kursunu qorumalıdır",
                "Yelkənlərini yığıb mühərriki işə salaraq əks tərəfə getməlidir"
            ]
        }
    ]

    out_json_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\radar_avtomatik_radar_m_ahid_vasit_l_ri_.json"

    formatted_questions = []
    
    for i, item in enumerate(questions_data, start=1):
        options = [item["ans"]] + item["distractors"]
        random.shuffle(options)
        
        opt_dict = {}
        correct_letter = "A"
        letters = ["A", "B", "C", "D"]
        for j, letter in enumerate(letters):
            opt_dict[letter] = options[j]
            if options[j] == item["ans"]:
                correct_letter = letter
        
        # formatting question id as q001 etc.
        qid = f"q{i:03d}"
        
        formatted_questions.append({
            "id": qid,
            "question": item["q"],
            "options": opt_dict,
            "correct_answer": correct_letter,
            "explanation": ""
        })
    
    final_data = {
        "certificate": "Radar, avtomatik radar müşahidə vasitələri, kapitan körpüsü komandası və axtarış xilasetmə (idarəetmə səviyyəsində)",
        "questions": formatted_questions
    }
    
    os.makedirs(os.path.dirname(out_json_path), exist_ok=True)
    
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
        
    print(f"Generated {len(formatted_questions)} questions to {out_json_path}")

if __name__ == '__main__':
    build()
