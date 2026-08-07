import json
import random

random.seed(33325)

data = {
    "certificate": "Gəmi mexaniklərinin təkmilləşdirilməsi (idarəetmə səviyyəsində)",
    "questions": []
}

raw_questions = [
    {
        "q": "Gəmi elektrik avadanlıqlarının sxemlərində və konstruksiyalarında aparılan dəyişikliklər hansı sənədlərdə əks edilməlidir?",
        "c": "Gəminin texniki istismar sənədlərində",
        "w": ["Gəminin maşın jurnalında", "Avtomatlaşdırma və nəzarət sistemlərinin qeydiyyat jurnalında", "Gəmi layihəsinin ilkin çertyojlarında"]
    },
    {
        "q": "Akkumulyator batareyalarının üzərində keçirilən texniki baxışların mütəmadilik müddətini qeyd edin.",
        "c": "Ayda bir dəfədən tez olmayaraq",
        "w": ["Həftədə bir dəfədən tez olmayaraq", "Altı ayda bir dəfədən az olmayaraq", "Hər reysdən əvvəl və sonra"]
    },
    {
        "q": "Hansı hallarda generatorun qurudulmasına ehtiyac olduğunu qeyd edin:",
        "c": "Generator nəm olduğu təqdirdə, generatorun izolyasiyasının müqaviməti aşağı düşdüyü təqdirdə",
        "w": ["Generator uzun müddət tam yükdə işlədikdə, soyutma sistemi qızdıqda", "Kömür fırçalarının aşınması artdıqda, kollektor qığılcımlandıqda", "Tezlik tənzimləyicisi sıradan çıxdıqda və gərginlik sabit olmadıqda"]
    },
    {
        "q": "Gəmidə asılmış yük gəminin dəyanətliliyinə necə təsir edir?",
        "c": "Gəminin dəyanətliliyini azaldır",
        "w": ["Metasentrik hündürlüyü artıraraq dəyanətliliyi yaxşılaşdırır", "Yükün ağırlıq mərkəzi asma nöqtəsindən asılı olmadığı üçün dəyanətliliyə təsir etmir", "Uzununa dəyanətliliyi artırır, lakin eninə dəyanətliliyə təsir etmir"]
    },
    {
        "q": "Hansı hallarda gəmidən dənizə tərkibində neft olan maye qarışığının və ya neftin tullanmasına dair MARPOL-73/78 BK-nın qaydaları tətbiq edilmir?",
        "c": "Gəminin zədələnməsi, onun təhlükəsizliyinin təmin edilməsi, habelə insan həyatının qorunması məqsədi ilə baş verdikdə",
        "w": ["Maşın şöbəsində tutumu aşan yağlı suların axıdılması zərurəti yarandıqda", "Xüsusi rayonlardan kənarda neft tərkibi 15 ppm-dən yuxarı olduqda", "Neft süzgəc avadanlığı (OWS) nasaz olduqda və ballast qəbulu vacib olduqda"]
    },
    {
        "q": "Gəminin neft əməliyyatları jurnalı hansı hallarda doldurulur?",
        "c": "Neft məhsullarının gəmidən xaric edildiyi zaman, maşın bölməsinin döşəmə altı sularının gəmidən xaric edildiyi zaman, yanacaq çənlərinə ballast qəbul edildiyi zaman və ya onların təmizlənməsi zamanı",
        "w": ["Yalnız liman dövləti nəzarəti (PSC) yoxlamasından dərhal əvvəl", "Gündəlik növbə təhvil-təslimində maşın jurnalına əlavə kimi", "Yalnız yağ separatörü təmizləndikdə və çöküntülər yığıldıqda"]
    },
    {
        "q": "DHDNÇ-78 BK-ya edilmiş əlavələr onun tərkib hissəsi sayılırmı?",
        "c": "Bəli sayılır",
        "w": ["Xeyr, onlar sadəcə tövsiyə xarakterlidir", "Yalnız Bayraq Administrasiyası tərəfindən ratifikasiya olunduqdan sonra sayılır", "Xeyr, əlavələr ayrı-ayrı müstəqil konvensiya kimi qəbul edilir"]
    },
    {
        "q": "Konvensiyaya istinad etmək Konvensiyanın əlavələrinə istinad etmək hesab edilirmi?",
        "c": "Bəli edilir",
        "w": ["Xeyr, əlavələrə ayrıca istinad olunmalıdır", "Yalnız Beynəlxalq Dəniz Təşkilatı (IMO) xüsusi qərar qəbul etdikdə edilir", "Xeyr, istinad yalnız əsas mətnin maddələrinə şamil olunur"]
    },
    {
        "q": "DHDNÇ-78 əlavələr edilmiş Beynəlxalq Konvensiya hansı dənizçilərə tətbiq edilir?",
        "c": "Dəniz gəmilərində çalışan dənizçilərə",
        "w": ["Yalnız sərnişin gəmilərində çalışan rəhbər heyətə", "Yalnız xüsusi təhlükəli yüklər daşıyan gəmilərin heyətinə", "Limanda fəaliyyət göstərən köməkçi gəmilərin mexaniklərinə"]
    },
    {
        "q": "Gəminin kapitanına və ya rəhbər heyət üzvlərinə Bayraq Administrasiyası tərəfindən verilən diploma hər hansı bir təsdiqləyici sənəd verilirmi, verilirsə o sənəd Beynəlxalq Konvensiyanın hansı qaydalarına əsasən verilir?",
        "c": "Bəli, belə bir sənəd DHDNÇ-78 BK-nın 1/2 qaydalarında qeyd olunmuş formaya uyğun olmalıdır",
        "w": ["Xeyr, yalnız əsas diplom kifayət edir və əlavə təsdiqləmə tələb olunmur", "Bəli, ISM Məcəlləsinin sənədləşdirmə tələblərinə uyğun olaraq verilir", "Bəli, MARPOL Konvensiyasının əlavələrinə uyğun qeydiyyata alınır"]
    },
    {
        "q": "Liman Dövlətinin nəzarətçi müfəttişi hansı hallarda gəmidə DHDNÇ-78 BK-nın tələblərinə riayət edildiyini yoxlamaq hüququna malikdir?",
        "c": "Gəmi təhlükəli manevr etdiyi zaman",
        "w": ["Gəminin yanacaq sərfiyyatı norma həddini aşdıqda", "Gəminin maşın şöbəsində planlı profilaktik təmir işləri aparıldıqda", "Mühərrikin işlənmiş qazlarının istilik dərəcəsi artdıqda"]
    },
    {
        "q": "Liman Dövlətinin nəzarətçi müfəttişi gəminin limanda olduğu zaman heyət üzvlərinin diplomlarının, onlaların tutduqları vəzifələrə uyğun olub olmamasını yoxlaya bilərmi?",
        "c": "Bəli yoxlaya bilər",
        "w": ["Xeyr, bunu yalnız gəmi sahibi edə bilər", "Xeyr, bu səlahiyyət yalnız gəminin qeydiyyat limanına aiddir", "Yalnız gəmi qəzaya uğradıqdan sonra yoxlaya bilər"]
    },
    {
        "q": "DHDNÇ Konvensiyasının tələblərinə əsasən tələb edilən diplom onun sahibinin çalışdığı gəmidə saxlanılmalıdırmı?",
        "c": "Bəli, saxlanılmalıdır",
        "w": ["Xeyr, əsilləri gəmiçilik şirkətinin kadrlar şöbəsində saxlanılmalıdır", "Xeyr, liman idarəsində depozitə qoyulmalıdır", "Yalnız beynəlxalq reyslər həyata keçirən gəmilərdə tələb olunmur"]
    },
    {
        "q": "Diplomun təsdiqnaməsində onun sahibinin işləməyə icazəsi olduğu vəzifə göstərilməlidirmi?",
        "c": "Bəli, göstərilməlidir",
        "w": ["Xeyr, vəzifə yalnız dənizçinin kitabçasında yazılır", "Xeyr, təsdiqnamədə yalnız gəminin tipi və tonnajı qeyd olunur", "Yalnız 3000 kVt-dan yuxarı güc qurğusu olan gəmilər üçün göstərilməlidir"]
    },
    {
        "q": "İstilik izolyasiyalı materialdan hazırlanmış hidrokostyum geyinmiş insan neçə saat ərzində temperaturu 2 dərəcə selsi olan soyuq suda sağ qala bilər?",
        "c": "6 saat",
        "w": ["24 saat", "12 saat", "2 saat"]
    },
    {
        "q": "İstilik izolyasiyalı olmayan materialdan hazırlanmış hidrokostyum geyinmiş insan neçə saat ərzində temperaturu 5 dərəcə S olan suda sağ qala bilər?",
        "c": "Bir saat ərzində",
        "w": ["Üç saat ərzində", "Beş saat ərzində", "Yarım saat ərzində"]
    },
    {
        "q": "Xilasedici salı neçə metr hündürlükdən təhlükəsiz olaraq bədən xəsarəti almadan, jiletin özünü zədələmədən və yerdəyişməsinə yol vermədən suya tullamaq olar?",
        "c": "4.5 metr hündürlükdən",
        "w": ["10 metr hündürlükdən", "8 metr hündürlükdən", "15 metr hündürlükdən"]
    },
    {
        "q": "Növbətçi qayıq hansı sürətlə manevr etmə imkanlarına malik olmalıdır?",
        "c": "6 uzel sürətdən az olmayaraq",
        "w": ["10 uzel sürətdən az olmayaraq", "4 uzel sürətdən az olmayaraq", "12 uzel sürətdən az olmayaraq"]
    },
    {
        "q": "Xilasedici qayığın tam yüklənmiş və sakit suda olduğu halda sürəti neçə uzel olmalıdır?",
        "c": "6 uzeldən az olmamalıdır",
        "w": ["4 uzeldən az olmamalıdır", "8 uzeldən az olmamalıdır", "12 uzeldən az olmamalıdır"]
    },
    {
        "q": "Təhlükə yarandığı zaman, xilasedici salı zədələmədən hansı hündürlükdən tullamaq olar?",
        "c": "18 metr hündürlükdən",
        "w": ["25 metr hündürlükdən", "12 metr hündürlükdən", "30 metr hündürlükdən"]
    },
    {
        "q": "Həyacan siqnalları üzrə cədvəllər harada saxlanılmalıdır?",
        "c": "Kapitan körpüsündə və heyət üzvlərinin kayutlarında",
        "w": ["Yalnız Mərkəzi İdarəetmə Postunda (MİP) və yeməkxanada", "Maşın şöbəsinin çıxışlarında və ballast idarəetmə otağında", "Təcridxana və akkumulyator otağının qarşısında"]
    },
    {
        "q": "Gəmi stasionar yanğınsöndürmə sistemlərini hansı əlamətlərinə görə təsnifləndirmək olar?",
        "c": "Yanğınsöndürmə prinsipinə və otaqların kateqoriyasına görə",
        "w": ["Boruların diametrinə və su nasoslarının ümumi məhsuldarlığına görə", "Detektorların həssaslığına və avtomatika səviyyəsinə görə", "Köpük konsentratının markasına və saxlanma müddətinə görə"]
    },
    {
        "q": "Mühərrikin dövrlərnin sayı artdıqda, onun indikator Faydalı İş Əmsalında hansı dəyişikliklər baş verir?",
        "c": "İndikator Faydalı İş Əmsalı azalır",
        "w": ["İndikator Faydalı İş Əmsalı kəskin artır", "Dəyişməz qalır, çünki bu mühərrikin konstruksiyasından asılıdır", "Termodinamik itkilər azaldığı üçün əmsal yüksəlir"]
    },
    {
        "q": "İşçi maddənin temperaturu və tərkibi dəyişdikdən sonra, silindirdə işçi maddənin termodinamiki xassələri ilə yanaşı daha hansı xassələr dəyişir ?",
        "c": "Entalpiya, İstilik həcmi, Daxili energiya",
        "w": ["Süxurların sıxlığı və özlülük əmsalı", "Kavitasiya əmsalı və kinematik özlülük", "Mühərrikin sıxılma dərəcəsi və pistonun gedişi"]
    },
    {
        "q": "İş tsikli dirsəkli valın iki dövrü ərzində, yəni iş prosesi porşenin dörd yolu (dörd takt ərzində) baş verən dizel mühərriklərinə?",
        "c": "Dörd taktlı mühərriklər deyilir",
        "w": ["İki taktlı mühərriklər deyilir", "Qazturbin qurğuları deyilir", "Buxar porşenli maşınlar deyilir"]
    },
    {
        "q": "Mühərrikin dirsəkli valının bir qaydada, qeyri müntəzəm olaraq fırlanması mühərrikin işinə necə təsir edir?",
        "c": "Mənfi təsir edir",
        "w": ["Müsbət təsir edir, sürtünməni azaldır", "Dövrlərin orta sayı sabit qaldıqda təsir etmir", "Silindrlərin doldurulmasını yaxşılaşdırır"]
    },
    {
        "q": "Yanacağın püskürülməsinin hidrodinamikası asılıdır:",
        "c": "Gəmiyə qəbul edilmiş və istifadə edilən yanacağın sıxlığından və sıxlaşma qabiliyyətindən",
        "w": ["Egzoz qazlarının turbokompressora daxil olma sürətindən", "Soyutma suyunun nasosda yaratdığı dinamik təzyiqdən", "Porşenin soyudulma intensivliyindən və yağın özlülüyündən"]
    },
    {
        "q": "Buxar maşınının əsas iş prinsipini qeyd edin.",
        "c": "Buxarın potensial enerjisinin istifadə edilməsi",
        "w": ["Daxili yanmanın kinetik enerjiyə çevrilməsi", "Termoelektrik generator effekti əsasında istiliyin enerjiyə çevrilməsi", "Suyun kavitasiyası nəticəsində yaranan hidrodinamik gücün istifadəsi"]
    },
    {
        "q": "Daxili yanma mühərrikinin əsas iş prinsipini qeyd edin.",
        "c": "Yanmış yanacağın kimyəvi enerjisinin mexaniki işə çevrilməsi",
        "w": ["Elektrik enerjisinin maqnit sahəsi vasitəsilə mexaniki hərəkətə çevrilməsi", "Mühərrik daxilindəki mayenin hidravlik təzyiqinin fırlanma hərəkətinə çevrilməsi", "Sıxılmış havanın potensial enerjisinin birbaşa istifadəsi"]
    },
    {
        "q": "Turbin pilləsi hansı elementlərdən ibarətdir?",
        "c": "Diskdən, gövdə elementlərindən, işçi dairəvi reşotkadan, soplovoy dairəvi reşotkadan",
        "w": ["Krank-şatun mexanizmindən, silindr qapağından, forsunkadan", "Maqnit statorundan, rotor sarğılarından, kollektordan", "Reduktor dişlilərindən, ara valdan və pərvanədən"]
    },
    {
        "q": "Gəmi baş mühərriklərinin parametrlərinə nəzarət etmənin vaxtaşırılığı kim tərəfindən təyin edilir?",
        "c": "Baş mexanik tərəfindən",
        "w": ["Yalnız gəmi kapitanı tərəfindən", "Beynəlxalq Dəniz Təşkilatı (IMO) rəsmi inspektorları tərəfindən", "Liman Dövlətinin Nəzarəti (PSC) tərəfindən"]
    },
    {
        "q": "Qəza yanğın söndürmə nasoslarının və digər qəza aqreqatlarının iş qabiliyyətliliyinin və işə salınmaya hazır olmasının yoxlanmasının vaxtaşırılıq müddəti nə qədərdir ?",
        "c": "Hər həftədə",
        "w": ["Ayda bir dəfə", "Altı ayda bir dəfə", "Gündəlik növbə zamanı"]
    },
    {
        "q": "Dövri yağ sistemindəki yağın təzyiqi, yağ soyuducusundakı suyun təzyiqindən az yoxsa çox saxlanmalıdır?",
        "c": "Yüksək təzyiqdə saxlanılmalıdır",
        "w": ["Aşağı təzyiqdə saxlanılmalıdır ki, su asanlıqla dövr etsin", "Bərabər saxlanılmalıdır ki, hidravlik zərbə yaranmasın", "Bunun heç bir əhəmiyyəti yoxdur, çünki yağ və su qarışmır"]
    },
    {
        "q": "Mühərrikin yastıqlarında və ya digər sürtünən hissələrində temperaturun artması zamanı yerinə yetirilən tədbirləri qeyd edin?",
        "c": "Mühərrikin yükünü azaltmalı, temperaturda baş verən dəyişikliklərə nəzarəti gücləndirməli, temperatur artımı müşahidə olunan yastıqlara yükü azaltmalı və bütün mümkün olan vasitələrdən istifadə etməklə yağ verilməni artırmalı",
        "w": ["Mühərriki dərhal tam gücünə çatdırmalı ki, dövran artsın və qızma azalsın", "Mühərrikin yükünü dəyişmədən yalnız xaricdən hava ilə soyutmalı", "Yağ verilməsini dayandırmalı və suyu birbaşa yastıqlara yönləndirməli"]
    },
    {
        "q": "Dizel mühərrikinin yağlama sistemində, turbokompressorda, reduktorda, hidromuftada, val qurğusunun yastıqlarında yağın təzyiqinin kəmiyyəti (miqdarı) kim tərəfindən müəyyən edilir?",
        "c": "İstehsalçı müəssisə və gəmi sahibi tərəfindən",
        "w": ["Yalnız klas cəmiyyətinin mühəndisləri tərəfindən", "Gəminin kapitanı və ikinci mexanik tərəfindən", "Beynəlxalq standartlar təşkilatı (ISO) tərəfindən standart olaraq"]
    },
    {
        "q": "Mühərrikin silindirlərinin yağlanmasının lubrikatorlarının tənzimlənməsi zamanı hansı rəhbər sənədlərin tələblərinə riayət etmək lazımdır?",
        "c": "Mühərriki istehsal edən müəssisənin və gəmi sahibinin təlimatlarına",
        "w": ["Gəminin yanğınla mübarizə planına", "Ballast sularının idarəolunması planına", "Liman maşınqayırma zavodunun standartlarına"]
    },
    {
        "q": "Mühərrikin dövri yağ sistemində yağın təzyiqinin qəflətən düşməsi və ya sistemdəki yağın temperaturunun qəflətən həddindən artıq artması zamanı yerinə yetirilən hərəkətləri qeyd edin?",
        "c": "Mühərrikin dərhal fəaliyyətini dayandırmalı",
        "w": ["Yağ pompalarının sürətini maksimuma qaldırıb işə davam etməli", "Mühərrikin gücünü 50%-ə qədər endirib limana qədər hərəkət etməli", "Bypass klapanlarını açaraq soyuducunu dövrədən kənarlaşdırmalı"]
    },
    {
        "q": "Turbokompressorların yağ sistemlərinin yağ axıdan, navalça sistemlərində hansı faktor daimi nəzarətdə saxlanılmalıdır?",
        "c": "Suyun olmaması faktoru",
        "w": ["Yağın tamamilə buxarlanması faktoru", "Yağ təzyiqinin 10 bar-ı keçməsi faktoru", "Çirklənmiş qazların navlçaya daxil olması faktoru"]
    },
    {
        "q": "Mühərrikdə istifadə edilən yağın növü nəyə müvafiq olmalıdır?",
        "c": "İstifadə edilən yanacağın növünə",
        "w": ["Gəminin hərəkət etdiyi dənizin suyunun duzluluğuna", "Mühərrikin istifadə edildiyi iqlim zonasının temperaturuna", "Səs-küyün azaldılması standartlarına"]
    },
    {
        "q": "Mühərrikin anker birləşmələrinin boşalmasını müəyyən etdikdən sonra hansı tədbirləri yerinə yetirmək lazımdır?",
        "c": "Nəzarət müddətini azaltmalı",
        "w": ["Bütün mühərrik detallarını söküb yenidən yığmalı", "Bağlantıların ətrafına xüsusi yapışqan tətbiq etməli", "Mühərrikin fırlanma sürətini həddən artıq artırmalı"]
    },
    {
        "q": "Neçə müddətdən bir baş mexaniklər tərəfindən plan qrafiklərinin aparılması və onların yerinə yetirilməsi yoxlanılmalıdır?",
        "c": "Hər ayda bir dəfə",
        "w": ["Hər reysdən əvvəl və reys bitdikdən dərhal sonra", "İldə iki dəfə, yalnız quru dok təmiri ərəfəsində", "Hər altı ayda bir dəfə klas yoxlamasından əvvəl"]
    },
    {
        "q": "Manevr etmənin göstəricisini hansı hallarda söndürmək icazəsi verilir?",
        "c": "Nasazlıqların aradan qaldırılması zamanı",
        "w": ["Gəmi lövbərdə dayanarkən enerjiyə qənaət etmək üçün", "Gündüz vaxtı aydın hava şəraitində", "Maşın şöbəsində yalnız gündəlik yoxlamalar aparıldıqda"]
    },
    {
        "q": "Gəminin davamlılığı uğrunda mübarizəyə dair sənədlər toplusunun qovluğu harada saxlanılmalıdır?",
        "c": "Kapitan körpüsündə",
        "w": ["Maşın şöbəsinin nəzarət postunda", "Baş mexanikin kayutunda", "Mərkəzi karantin otağında"]
    },
    {
        "q": "Dizel mühərriyinin əhəmiyyət kəsb edən detallarının defektoloji nəzarətinin yerinə yetirilməsi zamanı istifadə edilən əsas rəhbəredici sənədləri qeyd edin?",
        "c": "Mühərrikin təmirinə dair texniki şərtlər və istehsalçı müəssisənin təlimatı",
        "w": ["Dəniz mühitinin qorunması qaydaları (MARPOL)", "Gəminin yükləmə-boşaltma təlimatları", "Həyat xilasedici vasitələrin (LSA) beynəlxalq məcəlləsi"]
    },
    {
        "q": "Dörd taktlı mühərriklərin “şatun” boltlarına dair vaxt aşırı yerinə yetirilməsi vacib olan işləri qeyd edin?",
        "c": "Qalıq uzunluğunun ölçülməsi və defektoskopik nəzarət",
        "w": ["Tork açarı istifadə edilmədən çəkiclə vuraraq möhkəmləndirilməsi", "Səthlərinin xüsusi antifriksion boya ilə rənglənməsi", "Yalnız gözlə baxış və yağ sızıntılarının təmizlənməsi"]
    },
    {
        "q": "Elastik, asanlıqla əyilə bilən, əyilgənli rotora malik olan turboaqreqatların fırlanma tezliyinin kritik nöqtəsini keçmə üsulunu qeyd edin.",
        "c": "Tez bir zamanda",
        "w": ["Yavaş-yavaş, pilləli şəkildə", "Rotoru isitdikdən sonra yalnız minimum gücdə", "Mühərriki bir neçə dəfə dayandırıb-işə salmaqla"]
    },
    {
        "q": "Aqreqatı fövqəladə hallarda işə salarkən hansı parametrlərin qoruyucularının işdən çıxarılmasına icazə verilir?",
        "c": "Rotorun oxu üzrə tərpənməsinə və kondensatda vakuma görə qoruyucuları",
        "w": ["Baş sürtkü yağının minimum təzyiq qoruyucularını", "Soyutma suyunun maksimal temperatur qoruyucularını", "Silindr daxilindəki maksimal partlayış təzyiqi qoruyucularını"]
    },
    {
        "q": "Ən yaxın məsafələrdən hansı məsafədə üzmə qabiliyyətinə malik olan materialların dənizə tullanmasına icazə verilir?",
        "c": "25 mil",
        "w": ["3 mil", "12 mil", "50 mil"]
    },
    {
        "q": "Gəmi texniki vasitələrinin avtomatlaşdırma sistemlərini işdən ayırdıqda (söndürdükdə) aşağıda qeyd edilən tədbirlərin hansını yerinə yetirmək vacibdir?",
        "c": "Baş mexanikdən icazə almalı, növbətçi mexaniki xəbərdar etməli, söndürülmə əməliyyatının yerinə yetirilməsi haqqında maşın jurnalında müvafiq qeydlər aparmalı",
        "w": ["Yalnız kapitanı xəbərdar etməli və jurnalda heç bir qeyd aparmamalı", "Gəminin gediş sürətini dərhal sıfıra endirməli və lövbər atmalı", "Sistemə yalnız yeni proqram təminatı yükləndikdən sonra yenidən işə salmalı"]
    }
]

out_data = data.copy()

for i, qd in enumerate(raw_questions):
    opts = [qd["c"]] + qd["w"]
    random.shuffle(opts)
    opt_dict = {}
    correct_letter = "A"
    for letter, opt in zip(["A", "B", "C", "D"], opts):
        opt_dict[letter] = opt
        if opt == qd["c"]:
            correct_letter = letter
    out_data["questions"].append({
        "id": f"q{i+1:03d}",
        "question": qd["q"],
        "options": opt_dict,
        "correct_answer": correct_letter,
        "explanation": ""
    })

out_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_mexanikl_rinin_t_kmill_dirilm_si_id.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(out_data, f, ensure_ascii=False, indent=4)

print("Build successful.")
