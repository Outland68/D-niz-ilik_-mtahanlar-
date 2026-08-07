import json
import random
import re

questions_data = [
    {
        'q': '1. Nominal gücün 45-50% aşmayan yüklə işləyən dizel generatorların paralel rejimdə işləməsinin müddəti, davamiyyəti nə qədər olmalıdır?',
        'a': 'Minimal',
        'd': ['Maksimal (şəbəkənin tələbatına uyğun)', '4 saatdan çox olmamaq şərtilə', 'Yanacaq sərfi sabitləşənə qədər']
    },
    {
        'q': '2. Mürəkkəb şəraitlərdə üzmə zamanı valogeneratorların və ya utilizasiyalı turbogeneratorların istifadə edilməsinə icazə verilirmi?',
        'a': 'Energetik qurğunun istismar rejimlərində qəflətən yarana bilən əhəmiyyətli dəyişikliklər zamanı elektrik enerjisinin fasiləsiz təchizatı təmin edildiyi hallarda icazə verilir',
        'd': ['Yalnız baş mühərrik nominal dövrlər sayında işlədikdə icazə verilir', 'Sükan maşınının elektrik təchizatı tamamilə valogeneratordan asılı olduqda icazə verilir', 'Heç bir halda icazə verilmir, yalnız dizel-generatorlar istifadə edilməlidir']
    },
    {
        'q': '3. Cərəyanla qurutma üsulundan hansı izolyasiya müqavimətinə malik olan elektrik maşınlarında tətbiq edilməsinə icazə verilir?',
        'a': '0.1 Mom-dan az olmayanda',
        'd': ['0.5 Mom-dan çox olduqda', '5 Mom və daha yuxarı olduqda', 'Yalnız qısaqapanma sınaqlarından sonra']
    },
    {
        'q': '4. Akkumulyator batareyalarının texniki baxışlarının dövrilik (vaxtaşırılıq) müddətlərini qeyd edin?',
        'a': 'Bir ayda bir dəfədən az olmayaraq',
        'd': ['Hər növbə təhvili zamanı', 'Altı ayda bir dəfə', 'İldə iki dəfə, mövsüm dəyişkənliyində']
    },
    {
        'q': '5. Sinxron generatorların işə salınma və paralel iş rejiminə keçirilmə qaydaları nə ilə müəyyən edilir?',
        'a': 'Mövcud olan sinxronlaşdırma vasitələri və elektrik stansiyasının avtomatlaşdırma səviyyəsi ilə',
        'd': ['Baş mühərrikin gücü və faza gərginliyi ilə', 'Gəminin baş mexanikinin şəxsi təlimatı ilə', 'Köməkçi qazanların buxar istehsalı gücü ilə']
    },
    {
        'q': '6. Gəminin kəmiyyət mərkəzinin müəyyən edilməsini qeyd edin (center buoyancy)?',
        'a': 'Suyun gəmiyə təsir edən hidrostatik təyziq qüvvələrinin əlavə nöqtəsi',
        'd': ['Gəminin ağırlıq mərkəzinin su səthi ilə kəsişdiyi nöqtə', 'Gəminin burun və qıç hissələrinin kəsişmə kütlə mərkəzi', 'Yük ambarlarının həndəsi mərkəzlərinin cəmi']
    },
    {
        'q': '7. Gəminin batmazlıq qabiliyyətini təmin edən əsas konstruktiv tədbirləri qeyd edin.',
        'a': 'Gəmi gövdəsinin sukeçirməyən arakəsmələrə, göyərtələrə və platformalara bölüşdürülməsi',
        'd': ['Balast tanklarının daimi olaraq təmiz su ilə doldurulması', 'Baş mühərrikin ağırlıq mərkəzinin aşağı salınması', 'Köməkçi mexanizmlərin ikiqat dibdə yerləşdirilməsi']
    },
    {
        'q': '8. Gəminin üzmə ehtiyatının müəyyən edilməsini qeyd edin:',
        'a': 'Gəmi gövdəsinin su keçirməzliyinin həcmi yük vater xəttindən yüksəkdə',
        'd': ['Gəminin tam yüklü halda suya oturduğu dərinlik', 'Balast sularının ümumi həcminin gəmi həcminə nisbəti', 'Kiloqramla ifadə olunan xalis yük tutumu']
    },
    {
        'q': '9. DHDNÇ-78 Beynəlxalq Konvensiyasının tələblərinə əsasən baş mühərriklərinin gücü 750 kVt-dan 3000 kVt-dək olan 2-ci mexanik vəzifəsində işləmək üçün tələb edilən gəmidə minimal iş stajını qeyd edin.',
        'a': '12 ay',
        'd': ['6 ay', '24 ay', '36 ay']
    },
    {
        'q': '10. Dənizdə baş vermiş hadisələrin baxılması qaydalarını hansı beynəlxalq sənəd nizamlayır (müəyyən edir)?',
        'a': '“Dəniz qəza hadisələrinin və anlaşılmazlıqlarının araşdırılmasına dair” Beynəlxalq Məcəllə',
        'd': ['“Beynəlxalq Dənizçilik Təşkilatının (IMO) Ümumi Qaydaları”', '“Dənizdə gəmilərin toqquşmasının qarşısının alınması haqqında” Beynəlxalq Qaydalar (COLREG)', '“Gəmilərin ölçülməsi haqqında” Beynəlxalq Konvensiya']
    },
    {
        'q': '11. Dənizin gəmilərdən çirkləndirilməsi qaydalarını hansı beynəlxalq sənəd nizamlayır (müəyyən edir)?',
        'a': '“Dənizin gəmilərdən çirkləndirilməsinin qarşısının alınması haqqında” 1973-cü il tarixli Beynəlxalq Konvensiya',
        'd': ['“Dənizdə İnsan Həyatının Mühafizəsinə dair” Beynəlxalq Konvensiya (SOLAS)', '“Dənizçilərin Hazırlanması, Diplomlandırılması və Növbə çəkməsi haqqında” Konvensiya', '“Gəmilərin Yük markası haqqında” Beynəlxalq Konvensiya']
    },
    {
        'q': '12. DHDNÇ Beynəlxalq Konvensiyasının tələblərinə əsasən gəmidə hansı vəzifələr “idarəetmə” səviyyəsi üzrə məsuliyyətə malikdirlər?',
        'a': 'Gəmi kapitanı, 2-ci mexanik, baş mexanik, kapitanın baş köməkçisi',
        'd': ['Bütün naviqasiya zabitləri və bosman', 'Yalnız gəmi kapitanı və baş mexanik', 'Növbətçi mexanik, elektrik mexaniki və motorçular']
    },
    {
        'q': '13. MARPOL-73/78 BK-nın V Əlavəsi gəmidə aşağıda qeyd edilənlərdən hansını tələb edir?',
        'a': 'Zibillərin idarə edilməsi planı, Zibillərlə əməliyyatlara dair təşviqat plakatları, Zibillərlə əməliyyatların qeydiyyat jurnalı',
        'd': ['Neft əməliyyatları jurnalı, Çirkab suların qeydiyyatı, Ballast sularının idarə edilməsi planı', 'Yanacaq sərfi jurnalı, Xüsusi təhlükəli yüklərin qeydiyyatı, Emissiya kontrol cədvəli', 'Yük əməliyyatları planı, Gəmi maşın jurnalı, Dəniz mühitinin qorunması təlimatı']
    },
    {
        'q': '14. MARPOL-73/78 BK-nın V Əlavəsində qeyd edilmiş “Xüsusi rayonlarda” gəmilərdən bortdan kənara, dənizə aşağıda qeyd edilənlərdən hansılarının tullanması qadağan edilmişdir?',
        'a': 'Separasiya materialları, əsgi, metal, şüşə və plasmasdan hazırlanan məmulatlar, qablaşdırma materialları;',
        'd': ['Yalnız qida tullantıları və heyvan cəmdəkləri', 'Heç bir tullantının atılmasına məhdudiyyət yoxdur', 'Yalnız təhlükəli kimyəvi qalıqlar və xam neft çöküntüləri']
    },
    {
        'q': '15. MARPOL-73/78 BK-nın V Əlavəsində qeyd edilmiş “Xüsusi rayonlarda” sahilboyu üzgüçülükdə, sahildən 12 mildən az olmayan məsafədə olduqda, gəmilərdən bortdan kənara aşağıda qeyd edilənlərdən hansıların tullanmasına icazə verilir?',
        'a': 'Diri balıq, xırdalanmış qida məhsulları',
        'd': ['Yalnız plastik butulkalar və kağız tullantıları', 'Təmizlənmiş neft suları və sürtkü yağları', 'Sənaye tullantıları və taxta qırıntıları']
    },
    {
        'q': '16. Yanğın təhlükəsizliyinə dair təlimatlandırmanın həyata keçirilməsi hansı şəkildə qeydiyyata alınır?',
        'a': 'Təlimatlandırma haqqında jurnalda müvafiq qeydlərin həyata keçirilməsi',
        'd': ['Baş mühərrikin formulyarında imzalanması ilə', 'Şəxsi gəmiçilik kitabçasında qeyd olunması ilə', 'Yalnız kapitanın şifahi təsdiqi ilə']
    },
    {
        'q': '17. Gəminin yanğınsöndürmə sisteminin tərkibinə daxildir?',
        'a': 'Boru xəttləri, Yanğınsöndürmə nasosları, Sistemin kran və klapanları, Yanğınsöndürmə qoltuqları və yanğınsöndürmə lülələri',
        'd': ['Balast nasosları, foseptik tankları, separasiya klapanları', 'Sükan maşını hidravlikası, baş mühərrik soyutma boruları', 'İqlimləndirmə sisteminin havalandırma şaxtaları və freon kompressorları']
    },
    {
        'q': '18. İdarəetmə postlarının otaqlarında saxlanması qadağandır:',
        'a': 'Qazların, yanacaq materiallarının, oddan təhlükəli, tez yanan materialların',
        'd': ['Qəza işıqlandırma fənərlərinin və xilasedici jiletlərin', 'Rabitə avadanlıqlarının və naviqasiya xəritələrinin', 'İstismar jurnallarının və qeydiyyat kitablarının']
    },
    {
        'q': '19. Gəminin texniki istismarına dair gəminin baş mexanikinin göstərişləri və sərəncamları hansı növ heyət üzvləri üçün mütləqdir?',
        'a': 'Gəminin bütün növ heyət üzvləri üçün',
        'd': ['Yalnız maşın şöbəsinin heyəti üçün', 'Yalnız mühərrik motoristləri və təmizləyicilər üçün', 'Yalnız elektrik mexanikləri üçün']
    },
    {
        'q': '20. Gəmi jurnallarının qeydiyyatını kim aparır?',
        'a': 'Dəniz limanının kapitanı',
        'd': ['Gəminin baş mexaniki', 'Gəmi kapitanı', 'Gəmi sahibi şirkətin nümayəndəsi']
    },
    {
        'q': '21. P = const sabit təyziqdə keçən bərabərçəkili proses necə adlanır?',
        'a': 'İzobara prosesi',
        'd': ['İzoxora prosesi', 'İzotermik proses', 'Adiabatik proses']
    },
    {
        'q': '22. Nizam-intizam qaydalarına zidd olan hərəkətlərə yol vermiş nəqliyyat donanması işçilərinə hansı növ intizam tənbehləri tətbiq edilə bilər?',
        'a': 'Məzəmmət, töhmət, işdən azad edilmə, şiddətli töhmət, xidmətə uyğunsuzluq haqqında xəbərdarlıq etmə',
        'd': ['Cərimə, maaş kəsilməsi, məzuniyyətin ləğvi', 'Yalnız şifahi xəbərdarlıq və növbədən uzaqlaşdırma', 'Rütbənin aşağı salınması və gəmidən deportasiya']
    },
    {
        'q': '23. Gəminin limanda və ya lövbərdə durduğu zaman maşın jurnalında hansı qeydlər aparılır?',
        'a': 'Gəminin güc qurğularının hazırlığı, baş mühərriklərin iş rejimi, gəminin durduğu limanın adı, baş mühərriklərin işə salınma və işdən çıxarılma saatları, köməkçi mühərriklərin işi barədə məlumatlar',
        'd': ['Yalnız yanacaq sərfi və balast əməliyyatları barədə məlumatlar', 'Naviqasiya xəbərdarlıqları və hava proqnozu məlumatları', 'Yük əməliyyatlarının gedişatı və liman işçilərinin adları']
    },
    {
        'q': '24. Biləvasitə mühərrikin silindirinin daxilində mexaniki işi nə yerinə yetirir?',
        'a': 'Yanmış yanacağın istilik enerjisi',
        'd': ['Dirsəkli valın fırlanma ətaləti', 'Porşen halqalarının sürtünmə qüvvəsi', 'Turboüfləyicinin yaratdığı hava təzyiqi']
    },
    {
        'q': '25. Mühərrikin Silindir Porşen Qrupuna yanma kamerasında yaranan hansı qüvvələr təsir edir?',
        'a': 'Termiki və mexaniki qüvvələr',
        'd': ['Yalnız elektromaqnit qüvvələr', 'Mərkəzdənqaçma və kariolez qüvvələri', 'Hidrodinamik və aerodinamik qüvvələr']
    },
    {
        'q': '26. Şəkillərdə iki növ Yüksək Təyziqli Yanacaq nasosları (YTYN/ТНВД) göstərilmişdir. Zolotnik tipli YTYN-nu göstərin?\n1.\n2.',
        'a': '1',
        'd': ['2', 'Heç biri', 'Hər ikisi']
    },
    {
        'q': '27. İsti ehtiyat rejimində olmayan köməkçi dizel generatorların yüklənməsini qeyd edin?',
        'a': '3-5 dəqiqə qızdırılmaqla',
        'd': ['İşə salınan kimi dərhal tam yüklənməklə', 'Ən azı 1 saat boş rejimdə işlədikdən sonra', 'Dövrələr sayı nominala çatan kimi 100% yüklə']
    },
    {
        'q': '28. Addımı tənzimlənən vint (ATV/ВРШ) qurğusuna işləyən dizel mühərrikini sınaq məqsədi ilə işə salarkən pərin addımını hansı vəziyyətdə qoymaq lazımdır?',
        'a': '“0” vəziyyətinə',
        'd': ['“Tam irəli” vəziyyətinə', '“Tam geri” vəziyyətinə', '“50% irəli” vəziyyətinə']
    },
    {
        'q': '29. Dəniz registeri ilə yanğına qarşı xüsusi konstruktiv tədbirlərin qəbul edilməsi haqqında razılaşma olmadığı təqdirdə dəniz gəmilərində yanma temperaturu neçə dərəcədən az olan yanacağın istifadəsi qadağan edilmişdir?',
        'a': '60-dan az olan',
        'd': ['45-dən az olan', '80-dən az olan', '100-dən az olan']
    },
    {
        'q': '30. Baş mühərrikin qəza zamanı qoruyucu sisteminin işdən ayrılması kim tərəfindən və hansı hallarda yerinə yetirilə bilər (və ya işdən ayrılmasına göstəriş verilə bilər)?',
        'a': 'Gəminin qəzaya uğraması təhlükəsi mövcud olduğu təqdirdə kapitanın növbə köməkçisi və kapitanın növbə köməkçisinin göstərişi ilə növbətçi mexanik tərəfindən',
        'd': ['İstənilən şvartov əməliyyatları zamanı yalnız baş mexanik tərəfindən', 'Yalnız liman nəzarətçisi tələb etdikdə kapitan tərəfindən', 'Mühərrikdə yağ təzyiqi düşdükdə avtomatik olaraq siqnalizasiya sistemi tərəfindən']
    },
    {
        'q': '31. Xüsusi qızdırılma sistemi olmadığı təqdirdə yağı hansı üsul ilə qızdırmaq olar?',
        'a': 'Yağın mühərrikin yağlama sisteminə vurub yenidən xaric etməklə (məcburi yağvurma ilə)',
        'd': ['Karterin xaricdən açıq alovla qızdırılması ilə', 'Yağa qaynar su qarışdırmaqla', 'Buxar borularını birbaşa karterə yönləndirməklə']
    },
    {
        'q': '32. Mühərrikin gücünün bərabər olaraq silindirlər üzrə paylanılması nə ilə təmin edillir?',
        'a': 'Tsikllıq yanacağın verilməsi ilə',
        'd': ['Soyutma suyunun temperaturunun tənzimlənməsi ilə', 'Sübutedici klapanların bağlanması ilə', 'Valın fırlanma tezliyinin dəyişdirilməsi ilə']
    },
    {
        'q': '33. Məsafədən idarəetmə sisteminin işinin yoxlanılması məqsədi ilə bütün mövcud olan idarəetmə postlarından turboaqreqatın sınaq üçün işə salınmasını nə zaman yerinə yetirmək lazımdır?',
        'a': 'Turbinin qızdırılması üzrə işlər başa çatdıqdan sonra',
        'd': ['Mühərrik soyuq vəziyyətdə olduqda', 'Gəmi limana çatdıqdan dərhal sonra', 'Yük əməliyyatları tam gücü ilə davam edərkən']
    },
    {
        'q': '34. Silindirlər üzrə yanmanın maksimal təzyiqinin buraxıla bilən qiymətini qeyd edin (istismar təlimatında digər kənara çıxmalar göstərilmədiyi təqdirdə).',
        'a': '3,5',
        'd': ['10,5', '7,0', '1,5']
    },
    {
        'q': '35. Termotənzimləyici vintelin (TTV/ТРВ) borucuqlarının və daxiledici ştuser daxil olmaqla TTV/ТРВ-dən sonrakı armaturlarının üst səthinin donması nəyin əlaməti olduğunu qeyd edin.',
        'a': 'Normal işin əlamətidir',
        'd': ['Freon sızmasının əlamətidir', 'Kompressorun həddən artıq isinməsinin əlamətidir', 'Sistemin yağla dolmasının əlamətidir']
    },
    {
        'q': '36. Gəminin heyət üzvləri sırasından kim səfər zamanı sükan qurğusunu və onun idarəetmə mexanizmini vaxtaşırı olaraq yoxlamalıdır?',
        'a': 'növbətçi mexanik',
        'd': ['elektrik mexaniki', 'motorçu', 'bosman']
    },
    {
        'q': '37. Kapitan körpüsündən gəmi baş dizel mühərrikinin və addımı tənzimlənən pər qurğusunun (ATP/ВРШ) məsafədən idarə edilməsi zamanı manevr və revers etməyə hazırlıq üzrə işlər kimin tərəfindən yerinə yetirilir?',
        'a': 'kapitanın növbə köməkçisi tərəfindən',
        'd': ['baş mexanik tərəfindən', 'növbətçi motorist tərəfindən', 'gəminin elektrik mexaniki tərəfindən']
    },
    {
        'q': '38. Baş mühərriklərin (ATP/ВРШ) idarə edilməsi kapitan körpüsünə verildiyi bütün hallarda hansı qurğunun yoxlayaraq istismara hazır vəziyyətə gətirilməsi lazımdır?',
        'a': 'Maşın teleqrafını yoxlayaraq istismara hazır vəziyyətə gətirmək lazımdır.',
        'd': ['Yanacaq separasiya sistemini söndürmək lazımdır.', 'Köməkçi qazanların avtomatikasını əllə idarəetməyə keçirmək lazımdır.', 'Sükan maşınlarının hər iki nasosunu eyni anda dayandırmaq lazımdır.']
    },
    {
        'q': '39. Sutka ərzində gəminin növbətçi mexanikinə neçə saat ərzində istirahət saatı verilməlidir?',
        'a': 'Ən azı (minimum) 10 saat',
        'd': ['Ən azı 6 saat', 'Ən azı 14 saat', 'Ən azı 8 saat']
    },
    {
        'q': '40. Vaxtaşırı olaraq növbəsiz istismar edilən maşın bölmələrinə növbətçi mexaniki neçə saatdan bir gəlməlidir?',
        'a': 'İstənilən anda çağırışa əsasən',
        'd': ['Hər 2 saatdan bir', 'Yalnız növbə təhvili zamanı', 'Gündə cəmi 1 dəfə']
    },
    {
        'q': '41. Növbətçi mexanik növbədən kimin icazəsi olmadan uzaqlaşa (ayrıla) bilməz?',
        'a': 'Gəminin baş mexanikinin və ya onun gəmidə olmadığı hallarda isə ikinci mexanikin müvafiq icazəsi olmadan növbəçəkmə yerini tərk edə bilməz;',
        'd': ['Yalnız gəmi kapitanının icazəsi olmadan', 'Növbətçi naviqatorun və sükançının icazəsi olmadan', 'Motoristin və elektrik mexanikinin razılığı olmadan']
    },
    {
        'q': '42. “Sea – chest” sözünün düzgün olan tərcüməsini qeyd edin.',
        'a': 'Kinqston',
        'd': ['Dəniz sandığı', 'Dalğaqıran', 'Trüm qapağı']
    },
    {
        'q': '43. “Idle – running” sözünün düzgün olan tərcüməsini qeyd edin.',
        'a': 'Boş – boşuna iş',
        'd': ['Tam güclə iş', 'Qəza dayanması', 'Sınaq gedişi']
    },
    {
        'q': '44. “Frequency” sözünün düzgün tərcüməsini qeyd edin.',
        'a': 'Tezlik',
        'd': ['Gərginlik', 'Cərəyan', 'Müqavimət']
    },
    {
        'q': '45. “Crankcase” sözünün düzgün tərcüməsini qeyd edin.',
        'a': 'Karter',
        'd': ['Silindr qapağı', 'Dirsəkli val', 'Porşen barmağı']
    },
    {
        'q': '46. “Camshaft” sözünün düzgün tərcüməsini qeyd edin.',
        'a': 'Paylayıcı val',
        'd': ['Dirsəkli val', 'İtələyici', 'Şatun']
    },
    {
        'q': '47. Birləşmə üsulunu üç bucaqlı birləşmədən ulduzvari birləşməyə dəyişdikdə dəyişən cərəyanlı asinxron elektrik mühərrikinin gücü necə dəyişər?',
        'a': '3 dəfə azalar',
        'd': ['3 dəfə artar', 'Dəyişməz qalar', '1.5 dəfə artar']
    },
    {
        'q': '48. Cərəyan göstəricisinin əvəzinə nəzarət elektrik lampasından istifadə etmək olarmı?',
        'a': 'Qətiyyən olmaz',
        'd': ['Yalnız aşağı gərginlik dövrələrində olar', 'Qəza vəziyyətində 2 saatlıq icazə verilir', 'Elektrik mexanikinin nəzarəti altında olar']
    },
    {
        'q': '49. Dəyişən cərəyanın ölçülməsi məqsədi ilə ampermetrlərin ölçmə həddlərinin genişləndirilməsi üçün istifadə edilir:',
        'a': 'Cərəyan ölçmə transformatoru',
        'd': ['Şuntlayıcı müqavimət', 'Potensiometr', 'Tezlik çeviricisi']
    },
    {
        'q': '50. Gəmi elektrik maşınlarının xidmət müddəti adətən nə ilə ölçülür?',
        'a': 'İzolyasiyanın istismar müddəti ilə',
        'd': ['Kollektorun aşınma dərəcəsi ilə', 'Rulmanların dəyişdirilmə intervalı ilə', 'Stator sarğılarının sayı ilə']
    }
]

out_json = {
    'certificate': 'Gəmi mexaniklərinin təkmilləşdirilməsi (istismar səviyyəsində)',
    'questions': []
}

random.seed(33326)

for idx, qdata in enumerate(questions_data):
    # Strip question number if exists
    q_text = re.sub(r'^\d+\.\s*', '', qdata['q'])
    
    options = [qdata['a']] + qdata['d']
    random.shuffle(options)
    
    opts_dict = {}
    correct_key = ''
    letters = ['A', 'B', 'C', 'D']
    for i, opt in enumerate(options):
        opts_dict[letters[i]] = opt
        if opt == qdata['a']:
            correct_key = letters[i]
            
    out_json['questions'].append({
        'id': f'q{(idx+1):03d}',
        'question': q_text,
        'options': opts_dict,
        'correct_answer': correct_key,
        'explanation': ''
    })

with open(r'static/questions/xususi/g_mi_mexanikl_rinin_t_kmill_dirilm_si_is.json', 'w', encoding='utf-8') as f:
    json.dump(out_json, f, ensure_ascii=False, indent=4)
print("Rebuild complete.")
