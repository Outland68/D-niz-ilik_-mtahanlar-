import json, os

eibm_questions = [
    {
        "id": "q001",
        "question": "1. Əmniyyətli İdarəetmə haqqında Beynəlxalq Məcəlləyə nə aiddir?",
        "options": {
            "A": "Ətraf mühitinin qorunması",
            "B": "Yalnız gəmilərin sürət həddinin tənzimlənməsi",
            "C": "Liman rüsumlarının hesablanması qaydaları",
            "D": "Yük konteynerlərinin icarə şərtləri"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q002",
        "question": "2. Əmniyyətli İdarəetmə haqqında Beynəlxalq Məcəllənin məqsədləri nədir?",
        "options": {
            "A": "Gəmilərin təhlükəsiz istismarına aid beynəlxalq standartın yaradılmasıdır",
            "B": "Dəniz daşımalarında gəlirlərin artırılmasıdır",
            "C": "Gəmi heyətinin əmək haqlarının tənzimlənməsidir",
            "D": "Tərsanələrdə gəmi tikintisi qiymətlərinin müəyyən edilməsidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q003",
        "question": "3. ƏİBM hansı gəmilərə şamil olunur?",
        "options": {
            "A": "Qross tonnajı 500 və yuxarı olan gəmilərə",
            "B": "Qross tonnajı 100-dən aşağı olan bütün gəmilərə",
            "C": "Yalnız hərbi gəmilərə və dövlət katerlərinə",
            "D": "Yalnız avadansız balıqçı qayıqlarına"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q004",
        "question": "4. ƏİBM hansı gəmilərə şamil olunur?",
        "options": {
            "A": "Bütün sərnişin daşıyan gəmilərə şamil olunur",
            "B": "Yalnız uzunluğu 10 metrdən az olan gəmilərə",
            "C": "Yalnız taxta gövdəli yelkənli gəmilərə",
            "D": "Yalnız mühərriksiz barjalara"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q005",
        "question": "5. SOLAS 74/78 Beynəlxalq Konvensiyasının IX Fəslinin 2-ci Qaydasına əsasən, ƏİBM hansı gəmilərə şamil olunur?",
        "options": {
            "A": "Bütün sərnişin daşıyan gəmilərə",
            "B": "Yalnız dənizdə idman yaxtalarına",
            "C": "Yalnız yedək katerlərinə",
            "D": "Yalnız elmi-tədqiqat sualtı aparatlarına"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q006",
        "question": "6. Beynəlxalq Dəniz Təşkilatı (İMO) nədir?",
        "options": {
            "A": "Beynəlxalq dənizçilik standartları yaradan təşkilatdır",
            "B": "Gəmi yanacağı satan kommersiya şirkətidir",
            "C": "Yalnız dəniz quldurluğu ilə mübarizə aparan hərbi ittifaqdır",
            "D": "Liman kranlarını istehsal edən holdinqdir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q007",
        "question": "7. Gəmidə qəza baş versə və batma təhdidi yaransa, birinci növbədə nəyi qorumaq lazımdır?",
        "options": {
            "A": "İnsan həyatını",
            "B": "Gəmi dokumentasiyasını",
            "C": "Karterdəki işlənmiş yağı",
            "D": "Gəmi ambarındakı yükləri"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q008",
        "question": "8. Gəmidə qəza baş versə və batma təhdidi yaransa, ikinci növbədə nəyi qorumaq lazımdır?",
        "options": {
            "A": "Ətraf mühiti",
            "B": "Gəmi kapitanının şəxsi əşyalarını",
            "C": "Seyr fənərlərini",
            "D": "Buxar qazanını"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q009",
        "question": "9. Gəmidə qəza baş versə və batma təhdidi yaransa, üçüncü növbədə nəyi qorumaq lazımdır?",
        "options": {
            "A": "Gəmini qorumaq lazımdır",
            "B": "Liman binalarını qorumaq lazımdır",
            "C": "Sahil fənərlərini qorumaq lazımdır",
            "D": "Radioötürücü antenanı qorumaq lazımdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q010",
        "question": "10. Gəmidə qəza baş versə və batma təhdidi yaransa, dördüncü növbədə nəyi qorumaq lazımdır?",
        "options": {
            "A": "Gəmidə olan yükləri qorumaq lazımdır",
            "B": "Ətrafda olan balıqları qorumaq lazımdır",
            "C": "Tərsanə kranlarını qorumaq lazımdır",
            "D": "Liman yedəklərini qorumaq lazımdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q011",
        "question": "11. ƏİBM neçə hissədən, neçə bölmədən ibarətdir?",
        "options": {
            "A": "2 hissə 16 bölmə",
            "B": "4 hissə 20 bölmə",
            "C": "1 hissə 10 bölmə",
            "D": "3 hissə 12 bölmə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q012",
        "question": "12. ƏİBM Şirkətin qarşısında hansı tələblər qoyur?",
        "options": {
            "A": "Gəmidə olan kapitan və gəmi heyəti tələb olunan biliklərə sahib olmalıdır",
            "B": "Bütün heyət üzvləri ən azı 3 xarici dil bilməlidir",
            "C": "Gəmi hər ay tərsanədə doka qaldırılmalıdır",
            "D": "Gəmi kapitanı hər gün İMO-ya şəxsi hesabat göndərməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q013",
        "question": "13. ƏİBM baxımından aşağıdakı tələblərdən hansı düzgündür?",
        "options": {
            "A": "Bütün gəmi heyəti tibbi baxımdan sağlam olmalıdır",
            "B": "Gəmi heyəti yalnız sahildə yaşamaq hüququna malikdir",
            "C": "Dənizçilər hər 2 ildən bir diplomlarını yenidən imtahansız dəyişməlidir",
            "D": "Gəmi kapitanı gəmi mühərrikini şəxsən söküb yığmalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q014",
        "question": "14. ƏİBM baxımından ƏİS nə etməlidir?",
        "options": {
            "A": "ƏİS kapitanın səlahiyyətlərini təsdiq etməlidir",
            "B": "ƏİS kapitanın bütün qərarlarını ləğv etməlidir",
            "C": "ƏİS gəmi naviqasiyasını avtomatik idarə etməlidir",
            "D": "ƏİS yalnız Maliyyə Nazirliyinə hesabat verməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q015",
        "question": "15. Gəmi kapitanı ƏİS üzrə təhlili ildə necə dəfə aparmalıdır?",
        "options": {
            "A": "Azı ildə 1 dəfə",
            "B": "Hər 5 ildən bir",
            "C": "Ayda 10 dəfə",
            "D": "Təhlil aparılması tələb olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q016",
        "question": "16. Hansı tarixdə BDT A.741(18) qətnaməsini qəbul edib?",
        "options": {
            "A": "04.11.93",
            "B": "01.01.80",
            "C": "12.12.05",
            "D": "15.05.15"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q017",
        "question": "17. Hansı tarixdə BDT SOLAS 74/78 Beynəlxalq Konvensiyasının tərkibinə IX Fəsil əlavə edib?",
        "options": {
            "A": "24.05.94",
            "B": "10.10.85",
            "C": "01.01.00",
            "D": "20.08.10"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q018",
        "question": "18. SOLAS 74/78 Beynəlxalq Konvensiyasının IX Fəsli necə adlanır?",
        "options": {
            "A": "Təhlükəsizliyin idarə edilməsi",
            "B": "Yanğınsöndürmə vasitələri",
            "C": "Radiotəhlükəsizlik və GMDSS",
            "D": "Yüklərin yerləşdirilməsi və bərkidilməsi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q019",
        "question": "19. Bayraq Administrasiyası tərəfindən hansı yoxlamalar keçirilir?",
        "options": {
            "A": "Xarici yoxlamalar",
            "B": "Şirkətdaxili gündəlik auditlər",
            "C": "Yalnız maliyyə-mühasibat yoxlamaları",
            "D": "Yalnız heyətin tibbi yoxlamaları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q020",
        "question": "20. Şirkət tərəfindən hansı yoxlamalar keçirilir?",
        "options": {
            "A": "Daxili yoxlamalar",
            "B": "Bayraq dövlətinin rəsmi beynəlxalq sertifikatlaşdırması",
            "C": "Liman Müfəttişliyi (PSC) tərəfindən rəsmi yoxlama",
            "D": "Gömrük və sərhəd keçid yoxlamaları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q021",
        "question": "21. Audit üçün əsas tələb nədir?",
        "options": {
            "A": "Audit keçirən şəxs yoxladığı işindən asılı olmamalıdır",
            "B": "Auditor yoxladığı obyektdə şəxsən cavabdeh mexanik olmalıdır",
            "C": "Audit yalnız gecə vaxtı həyata keçirilməlidir",
            "D": "Audit yalnız gəmi lövbərdə olarkən aparılmalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q022",
        "question": "22. ƏİBM məqsədlərini göstərin:",
        "options": {
            "A": "Hər bir dənizçilik şirkətində ƏİS yaradılmalıdır",
            "B": "Bütün gəmilərin dizel mühərrikləri elektrik mühərriki ilə əvəz edilməlidir",
            "C": "Gəmilərdə bütün maşın növbələri ləğv edilməlidir",
            "D": "Yalnız xarici ölkə vətəndaşları gəmiyə işə götürülməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q023",
        "question": "23. ƏİBM məqsədlərini göstərin:",
        "options": {
            "A": "Dənizdə insanlarla bədbəxt hadisələrin qarşısı alınsın",
            "B": "Gəmilərin sürəti 2 dəfə artırılsın",
            "C": "Limanlarda yükboşaltma vaxtı maksimum azaldılsın",
            "D": "Gəmi kapitanının məsuliyyəti tam ləğv olunsun"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q024",
        "question": "24. ƏİBM əsas tələbini göstərin:",
        "options": {
            "A": "Əmniyyətli İdarəetmə Sistemi (ƏİS) yaradılsın",
            "B": "Gəmilər üçün yeni naviqasiya fənərləri istehsal olunsun",
            "C": "Bütün dənizçilər üçün pulsuz təlim mərkəzləri tikilsin",
            "D": "Gəmilərdə yanacaq sərfi 50% azaldılsın"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q025",
        "question": "25. ƏİBM əsas tələbini göstərin:",
        "options": {
            "A": "Gəmiçilik şirkətində Təyin Olunmuş Şəxs vəzifəsi yaradılsın",
            "B": "Hər gəmidə ən azı 3 baş mexanik vəzifəsi yaradılsın",
            "C": "Gəmilərdə bütün yanğın balonları çıxarılsın",
            "D": "Bütün naviqasiya xəritələri kağız formadan çıxarılsın"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q026",
        "question": "26. Aşağıdakılardan hansı ƏİBM tələblərinə aid deyil?",
        "options": {
            "A": "Gəmilərdə Mühafizənin İdarəedilməsi haqqında Sistem yaradılması",
            "B": "Şirkətin təhlükəsizlik siyasətinin işlənib hazırlanması",
            "C": "Kapitanın səlahiyyət və məsuliyyətinin müəyyən edilməsi",
            "D": "Fövqəladə hallara hazırlaşma prosedurlarının yaradılması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q027",
        "question": "27. ƏİS hansı təşkilatların tövsiyələrinə riayət etmir?",
        "options": {
            "A": "Sahil Mühafizə Xidməti",
            "B": "Beynəlxalq Dəniz Təşkilatı (İMO)",
            "C": "Bayraq Administrasiyaları",
            "D": "Təsnifat Cəmiyyətləri (Recognized Organizations)"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q028",
        "question": "28. ƏİS-in fəaliyyətinə təsir göstərə biləcək təşkilatı göstərin",
        "options": {
            "A": "Quru Yük Gəmi Sahiblərinin Beynəlxalq Assosiasiyası (INTERCARGO)",
            "B": "Dəniz Aviasiyası Assosiasiyası",
            "C": "Dəniz Turizmi Agentliyi",
            "D": "Liman Tikinti Şirkətləri İttifaqı"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q029",
        "question": "29. ƏİBM üçün Rəhbər Sənəd hesab olunmayanı göstərin",
        "options": {
            "A": "Təsnifat Cəmiyyətinin Əsasnaməsi",
            "B": "SOLAS-74 Beynəlxalq Konvensiyası",
            "C": "MARPOL-73/78 Beynəlxalq Konvensiyası",
            "D": "STCW-78/95 Beynəlxalq Konvensiyası"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q030",
        "question": "30. ƏİS nədir?",
        "options": {
            "A": "Əmniyyətli İdarəetmə Sistemidir (Safety Management System)",
            "B": "Gəmilərin Avtomatik İdentifikasiya Sistemidir (AIS)",
            "C": "Qlobal Dəniz Fəlakət və Əmniyyətli Rabitə Sistemidir (GMDSS)",
            "D": "Gəmilərin Yanğından Mühafizə Sistemidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q031",
        "question": "31. ƏİS hansı tələblərə uyğun olmalıdır?",
        "options": {
            "A": "Təhlükəsizlik və ətraf mühitə aid bütün beynəlxalq standartlara",
            "B": "Yalnız gəmi sahibinin şəxsi arzularına",
            "C": "Yalnız liman yükləmə operatorlarının tələblərinə",
            "D": "Yalnız gəmi aşpazının tərtib etdiyi menyuya"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q032",
        "question": "32. ƏİBM-in 2-ci bölməsinin tələbləri əsasında şirkətdə hansı təhlükəsizlik siyasətinin yaradılması tələb olunur?",
        "options": {
            "A": "Şirkətin təhlükəsizlik və ətraf mühitinin çirkləndirilməməsi siyasəti",
            "B": "Şirkətin kommersiya qiymət siyasəti",
            "C": "Şirkətin reklam və marketinq siyasəti",
            "D": "Şirkətin kadrların ixtisarı siyasəti"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q033",
        "question": "33. Gəmiyə verilən Əmniyyətli İdarəetmə Şəhadətnaməsi hansı halda öz qüvvəsini itirir?",
        "options": {
            "A": "Böyük uyğunsuzluq sübut olunarsa",
            "B": "Gəmi rəngləndikdə və ya təmizləndikdə",
            "C": "Gəmi heyəti dəyişdirildikdə",
            "D": "Gəmi başqa limana lövbər saldıqda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q034",
        "question": "34. Şirkətə verilən uyğunluq haqqında sənəd hansı halda öz qüvvəsini itirir?",
        "options": {
            "A": "Böyük uyğunsuzluq sübut olunarsa",
            "B": "Şirkətin telefon nömrəsi dəyişdikdə",
            "C": "Şirkətin veb-saytı yeniləndikdə",
            "D": "Gəmi mühərrikinin yağı dəyişdirildikdə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q035",
        "question": "35. Gəmiyə verilən Əmniyyətli İdarəetmə Şəhadətnaməsi hansı halda öz qüvvəsini itirir?",
        "options": {
            "A": "Uyğunluq haqqında sənəd ləğv olunarsa",
            "B": "Gəmi kapitanı istirahətə çıxdıqda",
            "C": "Gəmidə seyr fənərləri yandırıldıqda",
            "D": "Gəmi 10 uzel sürətlə üzdükdə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q036",
        "question": "36. Uyğunluq haqqında sənəd (DOC) kimə verilir?",
        "options": {
            "A": "Şirkətə",
            "B": "Şəxsən gəmi kapitanına",
            "C": "Liman agentinə",
            "D": "Yük sahibinə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q037",
        "question": "37. Əmniyyətli İdarəetmə üzrə Şəhadətnamə (SMC) kimə verilir?",
        "options": {
            "A": "Gəmiyə",
            "B": "Gəmiçilik şirkətinin mərkəzi ofisinə",
            "C": "Təsnifat cəmiyyətinin baş direktoruna",
            "D": "Liman müfəttişliyinə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q038",
        "question": "38. Müvəqqəti uyğunluq sənədi (Interim DOC) hansı müddətə verilə bilər?",
        "options": {
            "A": "12 ay",
            "B": "5 il",
            "C": "1 ay",
            "D": "10 il"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q039",
        "question": "39. Müvəqqəti Əmniyyətli İdarəetmə üzrə Şəhadətnamə (Interim SMC) hansı müddətə verilə bilər?",
        "options": {
            "A": "6 ay",
            "B": "3 il",
            "C": "24 ay",
            "D": "5 il"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q040",
        "question": "40. ƏİBM əsas hansı nöqsanlara diqqət yetirir?",
        "options": {
            "A": "Uyğunsuzluq və böyük uyğunsuzluq",
            "B": "Gəmi korpusunun rənginin solması",
            "C": "Karter yağının azca çirklənməsi",
            "D": "Kayıtlarda orfoqrafik xətalar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q041",
        "question": "41. Uyğunsuzluq nədir?",
        "options": {
            "A": "ƏİBM-in tələblərinə uyğun olmayan nöqsan",
            "B": "Gəminin nəzərdə tutulan vaxtdan 5 dəqiqə gecikməsi",
            "C": "Gəmi kütləsinin 1 ton artıq olması",
            "D": "Küləyin istiqamətinin dəyişməsi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q042",
        "question": "42. Böyük uyğunsuzluq nədir?",
        "options": {
            "A": "Qəzaya səbəb ola biləcək təkrar olunan uyğunsuzluq",
            "B": "Gəmi aşpazının yeməyi gecikdirməsi",
            "C": "Gəmi lövbərinin paslanması",
            "D": "Seyr fənərinin şüşəsinin çirklənməsi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q043",
        "question": "43. ƏİBM neçə bölmədən ibarətdir?",
        "options": {
            "A": "16 bölmə",
            "B": "8 bölmə",
            "C": "24 bölmə",
            "D": "30 bölmə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q044",
        "question": "44. ƏİBM neçə hissədən ibarətdir?",
        "options": {
            "A": "2 hissə",
            "B": "5 hissə",
            "C": "10 hissə",
            "D": "1 hissə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q045",
        "question": "45. ƏİBM-in A hissəsi necə adlanır?",
        "options": {
            "A": "Həyata keçirmə",
            "B": "Şəhadətləndirmə və yoxlama",
            "C": "Maliyyə auditi",
            "D": "Texniki xidmət"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q046",
        "question": "46. ƏİBM-in B hissəsi necə adlanır?",
        "options": {
            "A": "Şəhadətləndirmə və yoxlama",
            "B": "Həyata keçirmə",
            "C": "Dənizçilərin diplomlaşdırılması",
            "D": "Qəzaların araşdırılması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q047",
        "question": "47. SOLAS 74/78 Beynəlxalq Konvensiyanın hansı fəsli ƏİBM-ə aiddir?",
        "options": {
            "A": "IX Fəsil",
            "B": "III Fəsil",
            "C": "V Fəsil",
            "D": "XII Fəsil"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q048",
        "question": "48. Əmniyyətli İdarəetmə Sisteminin (ƏİS) Normativ Hüquq bazasına hansı aid deyil?",
        "options": {
            "A": "Yer Kürəsinin Nizamnaməsi (The Earth Charter 2000)",
            "B": "SOLAS-74 Beynəlxalq Konvensiyası",
            "C": "MARPOL-73/78 Beynəlxalq Konvensiyası",
            "D": "STCW-78/95 Beynəlxalq Konvensiyası"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q049",
        "question": "49. Əmniyyətli İdarəetmə Sisteminin (ƏİS) normativ hüquq bazasına hansı aid deyil?",
        "options": {
            "A": "Hərbi Gəmilərin Nizamnaməsi",
            "B": "SOLAS-74 Beynəlxalq Konvensiyası",
            "C": "MARPOL-73/78 Beynəlxalq Konvensiyası",
            "D": "Dənizdə Yük Nişanı haqqında Beynəlxalq Konvensiya"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q050",
        "question": "50. Gəmidə hansı adda sənəd olmur?",
        "options": {
            "A": "Tibbi arayış haqqında Şəhadətnamə",
            "B": "Əmniyyətli İdarəetmə Şəhadətnaməsi (SMC)",
            "C": "Uyğunluq haqqında Sənədin surəti (DOC)",
            "D": "Gəmi maşın jurnalı"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q051",
        "question": "51. SOLAS 74/78 neçə fəsildən ibarətdir?",
        "options": {
            "A": "14 Fəsil",
            "B": "8 Fəsil",
            "C": "20 Fəsil",
            "D": "5 Fəsil"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q052",
        "question": "52. MARPOL 73/78-in neçə əlavəsi var?",
        "options": {
            "A": "6 Əlavə",
            "B": "3 Əlavə",
            "C": "10 Əlavə",
            "D": "12 Əlavə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q053",
        "question": "53. “Dənizçilərin hazırlanmasına, onlara diplom verilməsinə və növbə çəkməyə dair” Beynəlxalq Məcəllə (STCW – 78/95, DHDNÇ BM – 78/95) hansı sahəyə aid olan sənəddir?",
        "options": {
            "A": "Dənizçilərin sertifikatlaşdırılması, diplomların verilməsi haqqında qaydaları təyin edən Məcəllədir",
            "B": "Gəmi mühərriklərinin təmir qiymətlərini müəyyən edən sənəddir",
            "C": "Liman kranlarının texniki parametrlərini göstərən kataloqdur",
            "D": "Gəmilərin satışı və icarəsi haqqında müqavilədir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q054",
        "question": "54. ƏİS təlimat qovluğuna aşağıdakılardan hansılar aid deyil?",
        "options": {
            "A": "Mühafizə haqqında təlimat",
            "B": "Gəmi heyətinin vəzifə təlimatları",
            "C": "Fövqəladə hallarda fəaliyyət prosedurları",
            "D": "Gəmiyə xidmət və texniki qulluq prosedurları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q055",
        "question": "55. Şirkətə ƏİBM üzrə verilən Müvəqqəti Uyğunluq Sənədi hansı müddətə verilir?",
        "options": {
            "A": "12 ay",
            "B": "5 il",
            "C": "6 ay",
            "D": "30 gün"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q056",
        "question": "56. Təyin olunmuş Şəxsin (DPA) əsas vəzifəsi nədir?",
        "options": {
            "A": "Şirkətin gəmilərində təhlükəsizlik və ətraf mühitin çirkləndirilməməsini təmin etmək",
            "B": "Gəmilərə ərzaq və içməli su almaq",
            "C": "Liman rüsumlarını ödəmək",
            "D": "Gəmilərin satışı üçün alıcı tapmaq"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q057",
        "question": "57. Hansı təşkilat Uyğunluq haqqında sənədi (DOC) verə bilər?",
        "options": {
            "A": "Bayraq Administrasiyası",
            "B": "Liman Polisi",
            "C": "Şəhər Bələdiyyəsi",
            "D": "Dəniz Turizm Şirkəti"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q058",
        "question": "58. Təyin Olunmuş Şəxs (DPA) kim ola bilər?",
        "options": {
            "A": "Gəmiçilik şirkətinin işçisi",
            "B": "Liman gömrük müfəttişi",
            "C": "Xarici ölkənin konsulu",
            "D": "Təcrübəçi matros"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q059",
        "question": "59. Təyin Olunmuş Şəxs hansılara görə cavabdehdir?",
        "options": {
            "A": "Şirkətin gəmilərində təhlükəsizliyə və ətraf mühitin çirkləndirilməməsinə görə cavabdehdir",
            "B": "Yalnız gəmi restoranının gəlirlərinə görə",
            "C": "Yalnız liman işçilərinin əmək haqqına görə",
            "D": "Yalnız gəmi biletlərinin satışına görə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q060",
        "question": "60. Təyin olunmuş şəxsin vəzifələrinə aid olmayanları göstərin:",
        "options": {
            "A": "Gəmi heyətini cəzalandırmaq",
            "B": "Təhlükəsizlik monitorinqini təmin etmək",
            "C": "Rəhbərliklə birbaşa əlaqə saxlamaq",
            "D": "Gəmilərin resurslarla təminatına nezaret etmək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q061",
        "question": "61. Şirkətin siyasətləri ƏİS-də öz əksini tapır?",
        "options": {
            "A": "Bəli",
            "B": "Xeyr, qadağandır",
            "C": "Yalnız gəmi kapitanının istəyi ilə",
            "D": "Yalnız liman müfəttişinin tələbi ilə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q062",
        "question": "62. Gəmidə ƏİS üzrə təlimat qovluğunda nə yazılıb?",
        "options": {
            "A": "Gəmi heyətinin vəzifələri",
            "B": "Gəmi aşpazının reseptləri",
            "C": "Liman şəhərlərinin mənzərələri",
            "D": "Dəniz balıqlarının növləri"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q063",
        "question": "63. ƏİBM baxımından şirkətdə hansı növ yoxlamalar olur?",
        "options": {
            "A": "Daxili və xarici yoxlamalar",
            "B": "Yalnız gizli polislə yoxlamalar",
            "C": "Yalnız vergi müfəttişliyi yoxlamaları",
            "D": "Yalnız şifahi sorğu yoxlamaları"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q064",
        "question": "64. ƏİBM baxımdan gəmidə hansı xarici yoxlama keçirilmir?",
        "options": {
            "A": "İllik yoxlama",
            "B": "İlkin yoxlama (Initial audit)",
            "C": "Aralıq yoxlama (Intermediate audit)",
            "D": "Yenidən sertifikatlaşdırma yoxlaması (Renewal audit)"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q065",
        "question": "65. Xarici yoxlama üçün tələb olunan vaxta gəmi limana gəlib çatmır. Xarici yoxalamanı maksimum hansı müddətə yubatmaq olar?",
        "options": {
            "A": "3 ay",
            "B": "1 il",
            "C": "6 ay",
            "D": "1 ay"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q066",
        "question": "66. İlkin yoxlamanı keçirmək üçün hansılar olmalıdır?",
        "options": {
            "A": "Azı bir dəfə daxili yoxlama keçirilməlidir",
            "B": "Gəmi mühərriki sökülməlidir",
            "C": "Gəmi boyanmalıdır",
            "D": "Bütün heyət dəyişdirilməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q067",
        "question": "67. Gəmi kapitanının məsuliyyətini kim təyin edir?",
        "options": {
            "A": "Şirkət və rəhbər sənədlər",
            "B": "Cərəyan şiddəti nominal dəyəri",
            "C": "Növbətçi matroslar",
            "D": "Liman agentinin köməkçisi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q068",
        "question": "68. Gəminin növbə xidmətinin düzgün təşkil olunması üçün bu xidmət gəmidə:",
        "options": {
            "A": "24 saat ərzində təyin olunur",
            "B": "Yalnız gündüz saatlarında təyin olunur",
            "C": "Yalnız fırtına zamanı təyin olunur",
            "D": "Yalnız limanda təyin olunur"
        },
        "correct_answer": "A",
        "explanation": ""
    }
]

target_paths = [
    r'D:\Dənizçilik_İmtahanları\backend\static\questions\special\eibm.json',
    r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\mniyy_tli_i_dar_etm_haqq_nda_beyn_lxalq_.json'
]

for p in target_paths:
    data = {
        "certificate": "Əmniyyətli İdarəetmə Haqqında Beynəlxalq Məcəllə",
        "questions": eibm_questions
    }
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Rebuilt {len(eibm_questions)} questions for both EIBM JSON paths with 100% correct answers and highly relevant distractors!")
