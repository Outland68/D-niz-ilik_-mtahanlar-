import json
import random

random.seed(33315)

data = [
    ("1. DHDNÇ-78/95 Beynalxalq Konvensiyasına son əsaslı düzəlişlər və əlavələr harada və nə zaman edilib?", "2010-cu il, 21-25 iyun, Manilada", "2006-cı il, 10-15 may, Cenevrədə", "2012-ci il, 12-16 avqust, Londonda", "1995-ci il, 1-7 iyul, Nyu-Yorkda"),
    ("2. DHDNÇ-78/95 Beynəlxalq Konvensiyası neçə fəsildən ibarətdir və hansılardır?", "3 fəsildən ibarətdir, maddələr, əlavələr və DHDNÇ-78/95 Beynəlxalq kodeksi", "4 fəsildən ibarətdir, qaydalar, təlimatlar və əlavələr", "2 fəsildən ibarətdir, əsas müddəalar və texniki sənədlər", "5 fəsildən ibarətdir, konvensiya, protokollar, qaydalar, əlavələr, qətnamələr"),
    ("3. Beynəlxalq kodeks nəyi təyin edir və hansı hissələrdən ibarətdir?", "Əlavələrdə göstərilənlərin daha dərin texniki detallarını təyin edir, A və B hissələrindən ibarətdir", "Gəmi avadanlıqlarının texniki xarakteristikasını təyin edir, 1 və 2-ci hissələrdən ibarətdir", "Liman nəzarət qaydalarını təyin edir, A, B və C hissələrindən ibarətdir", "Bütün konvensiyaların ümumi icmalını təyin edir, tək hissədən ibarətdir"),
    ("4. Beynəlxalq kodeksin B hissəsi nəyi təyin edir?", "Dənizçilərin hazırlanması, diplom verilməsi və növbə çəkmələri üçün tövsiyə olunan standartları", "Məcburi gəmiçilik qaydalarını və texniki normaları", "Liman dövlət nəzarəti tərəfindən yoxlamaların aparılması qaydalarını", "Gəmidə tibbi xidmətin təşkili üzrə standartları"),
    ("5. Beynəlxalq kodeksin A hissəsi nəyi təyin edir?", "Dənizçilərin hazırlanması, diplom verilməsi və növbə çəkmələri üçün mütləq standartları", "Gəmi texniki vasitələrinin yoxlanılması üzrə tövsiyələri", "Təhlükəsiz idarəetmə sisteminin sertifikatlaşdırılmasını", "Sərnişin gəmilərində xilasetmə vasitələrinin sayını"),
    ("6. Beynəlxalq Konvensiyaya 2010-cu ildə edilmiş əlavələr hansı tarixdən qüvvəyə minmişdir?", "1 yanvar 2012 ci ildən", "1 iyun 2011 ci ildən", "1 yanvar 2013 cü ildən", "1 iyul 2010 cu ildən"),
    ("7. Beynəlxalq Konvensiyaya 2010-cu ildə edilmiş əlavələr əsasən dənizçilərdə hansı xüsusiyyətlərin təkmilləşdirilməsinə istiqamətlənmişdir?", "Səriştə və bacarığa", "Maaş və iş saatlarına", "Qidalanma və istirahət rejiminə", "Fiziki hazırlıq və yaş həddinə"),
    ("8. Beynəlxalq Konvensiyanın əlavələr hissəsinin III fəsli nədən bəhs edir?", "Maşın bölmələrində növbə aparmağa diplom verilməsi üçün minimal mütləq tələblərdən", "Gəmi kapitanlarının sertifikatlaşdırılmasından", "Təhlükəli yüklərin daşınması qaydalarından", "Dəniz mühitinin qorunması tələblərindən"),
    ("9. Beynalxalq Konvensiyayanın tələbləri hansı dənizçilərə şamil olunur?", "Üzv ölkələrin bayrağı altında üzən gəmilərdə işləyən dənizçilərə", "Yalnız hərbi gəmilərdə xidmət edən dənizçilərə", "Yalnız sərnişin gəmilərinin heyətinə", "Daxili sularda üzən kiçik həcmli gəmi heyətinə"),
    ("10. Maşın şöbəsinin resurslarının idarə olunması dedikdə nə başa düşülür?", "Heyətin, avadanlığın və məlumatın düzgün, səmərəli idarə edilməsi.", "Maşın şöbəsində anbar ehtiyatlarının idarə edilməsi", "Yalnız yanacaq və yağın səmərəli istifadəsi", "Təmir işlərinin və ehtiyat hissələrin bölüşdürülməsi"),
    ("11. Maşın şöbəsində heyətin idarə edilməsi dedikdə nə başa düşülür?", "Heyətin ixtisasına, səriştəsinə, təcrübəsinə, sertifikatlarına görə yerləşdirilməsi", "Heyətin maaşlarının və məzuniyyətlərinin planlaşdırılması", "Heyət arasında qida təminatının bölünməsi", "Gəmi heyətinin vahid forma ilə təmin edilməsi"),
    ("12. Maşın şöbəsində avadanlığın idarə edilməsi dedikdə nə başa düşülür?", "Texniki vasitələrin fəaliyyətinin, istismarının, qulluğunun yüksək səviyyədə təşkil olunması", "Yalnız sıradan çıxmış avadanlığın dəyişdirilməsi", "Gəmi anbarındakı avadanlıqların siyahıya alınması", "Avadanlıqların mütəmadi olaraq istehsalçıya göndərilməsi"),
    ("13. Gəmi texniki vasitələrini işə salmazdan əvvəl yoxlanışı nədən başlamaq lazımdır?", "Diqqətli xarici yoxlanışdan", "Mexanizmin tam sürətdə sınaqdan keçirilməsindən", "Avtomatik idarəetmə pultunun sökülməsindən", "Bütün ventillərin tamamilə bağlanmasından"),
    ("14. Avtomatlaşdırılmış texniki vasitələr uzun müddət işləmədikdə, işə hazırlayarkən əsas nəyi yoxlamaq lazımdır?", "Avtomatika vasitələrini", "Gəminin naviqasiya cihazlarını", "Mexanizmin korpusunun rəngini", "Sərnişin salonunun havalandırmasını"),
    ("15. Mexanizmləri avtomatik və ya məsafədən işə salınan şöbənin girişində hansı xəbərdaredici lövhələr asılmalıdır?", "“Diqqət! Mexanizmilər avtomatik buraxılır”", "“Giriş qadağandır, yüksək gərginlik”", "“Ehtiyatlı olun, sürüşkən döşəmə”", "“Səs-küy zonası, qulaqcıq taxın”"),
    ("16. Texniki vasitəni işə salan zaman qeyri-normal səs eşidilərsə və titrəyişlər olarsa nə etmək lazımdır?", "Texniki vasitəni saxlamaq", "Sürəti maksimuma çatdırıb səsi yox etmək", "Səsi azaltmaq üçün yağlamaq", "Növbəti texniki baxışa qədər işi davam etdirmək"),
    ("17. Gəmi texniki vasitələrinin istismarında işlədilən nəzarət-ölçü cihazlarının vaxtında yoxlanılmasına kim məsuliyyət daşıyır?", "Baş mexanik", "Kapitan köməkçisi", "Gəmi həkimi", "Sıravi matros"),
    ("18. Gəmi texniki vasitələrinin zavod təmirindən sonra qəbulu hansı sənədin tələblərinə uyğun aparılır?", "Zavodlarda gəminin təmiri qaydalarına uyğun", "Beynəlxalq Dəniz Təşkilatının illik hesabatına uyğun", "Liman nəzarəti nizamnaməsinə uyğun", "Gəmi heyətinin daxili qaydalarına uyğun"),
    ("19. Gəminin manevr qeydiyyat lenti, gəmidə baş mexanikdə neçə müddət saxlanılmalıdır?", "1 il müddətində", "6 ay müddətində", "2 il müddətində", "Səfər bitənədək"),
    ("20. Maşın şöbəsində məlumatın idarə edilməsi dedikdə nə başa düşülür?", "Məlumatın qeydə alınması, cavab verilməsi, dərk edilməsi və səriştəli paylanmasıdır", "Gündəlik xəbərlərin heyətə oxunmasıdır", "Texniki sənədlərin arxivə verilməsidir", "Kapitana yalnız şifahi məruzələrin edilməsidir"),
    ("21. Maşın şöbəsində mexanizmlərin avtomatik idarəetmə sistemlərinin söndürülməsinə nə vaxt icazə verilir?", "Nasazlıq olanda və ya təmir zamanı", "Hər növbə dəyişimi zamanı", "Səfər bitdikdə lövbərə durarkən", "Yalnız liman dövlət nəzarəti yoxlamasında"),
    ("22. Avtomatik idarəetmə sisteminin söndürülməsi harada qeyd olunmalıdır?", "Maşın jurnalında", "Gəminin sanitar jurnalında", "Naviqasiya jurnalında", "Şəxsi heyətin qeydiyyat kitabçasında"),
    ("23. Əgər mühərrikin buraxılması təcili tələb olunarsa, mühərrikin hazırlanma əməliyyatı nəyin hesabına qısaldıla bilər?", "Mühərriki qızdırmaq ixtisara salınır", "Yağlama sisteminin yoxlanışı ixtisara salınır", "Soyutma sistemi söndürülmüş vəziyyətdə işə salınır", "Yanacaq filtrlərinin təmizlənməsi ləğv edilir"),
    ("24. Xilasedici qayıqların mühərrikləri və qəza yanğınsöndürmə nasosunun mühərrikləri ən geci neçə vaxtdan bir işə salınmalıdır?", "1 aydan gec olmayaraq", "6 aydan gec olmayaraq", "Hər gün", "Yalnız qəza vəziyyətində"),
    ("25. Maşın şöbəsində növbə çəkərkən nəyi bacarmaq lazımdır?", "Resursların idarə edilməsi prinsiplərini, effektiv ünsiyyəti, qətiyyətli, səriştəli lider olmağı", "Yalnız mexanizmləri işə salmağı və dayandırmağı", "Anbarda olan ehtiyat hissələrin dəqiq sayını bilməyi", "Körpücüklə heç bir əlaqə saxlamadan qərarlar qəbul etməyi"),
    ("26. Növbətçi mexanik kimə tabedir?", "Növbə köməkçisinə və texniki vasitələrin istismarı üzrə baş mexanikə", "Yalnız gəminin kapitanına", "Liman rəhbərliyinə və şirkət nümayəndəsinə", "Yalnız baş mexanikə"),
    ("27. Maşın şöbəsində əsas və köməkçi mexanizmləri istismar etmək üçün nəyi bilmək və bacarmaq lazımdır?", "Müxtəlif şəraitlərdə istismar qaydalarını, quruluşunu, avtomatik idarəetmə sistemlərini", "Yalnız mexanizmin vizual görünüşünü və rəngini", "Mexanizmin istehsalçısının tarixçəsini", "Köməkçi mexanizmləri istismar etmədən birbaşa əsas mühərrikə nəzarət etməyi"),
    ("28. Növbətçi mexanik yeni növbəyə azı neçə dəqiqə qalmış maşın şöbəsinə gəlməlidir?", "10 dəqiqə", "30 dəqiqə", "5 dəqiqə", "Dərhal növbə saatı başlayanda"),
    ("29. Maşın şöbəsinə məlumat hansı mənbələrdən daxil olur?", "Nəzarət-siqnal cihazlarından, heyətdən, avadanlığın qeyri- xarakterik işindən", "Yalnız liman nəzarətindən", "Yalnız gəmi kapitanının şifahi əmrlərindən", "Yalnız texniki sənədlərin oxunmasından"),
    ("30. Əgər başqa göstəriş yoxdursa, mühərriklərin yüksüz işləməsinə nə qədər vaxt icazə verilir?", "30 dəqiqə", "1 saat", "5 dəqiqə", "İstənilən qədər"),
    ("31. Əgər mühərrik demontaj olunmuş bir porşen və şatunla işə salınarsa neçə vaxtdan sonra yoxlamaq üçün saxlanılmalıdır?", "5-10 dəqiqə", "1 saat", "30 dəqiqə", "Yoxlamağa ehtiyac yoxdur"),
    ("32. Mühərrikdə indiqator diaqramı mühərrikin hansı iş rejimində çıxarılır?", "Stabil, dəyişməyən iş rejimində", "Yüksək sürətli manevrlər zamanı", "Mühərrik ilk dəfə işə salınarkən", "Yükün ani olaraq dəyişdiyi rejimdə"),
    ("33. Növbətçi mexanik növbəni hansı hallarda növbəyə yeni gələn növbətçi mexanikə təhvil verməli deyil?", "Əgər növbəyə yeni gələn növbətçi mexanikin vəzifəsini lazımi səviyyədəb icra edə bilməyəcəyinə əminlik varsa", "Yeni gələn növbətçi mexanik 10 dəqiqə əvvəl deyil, 5 dəqiqə əvvəl gəlibsə", "Yeni növbətçi geyim formasını tam geyinməyibsə", "Əgər yeni növbətçi maşın jurnalını hələ oxumayıbsa"),
    ("34. Maşın şöbəsinin növbə mexaniki nəyi təmin etməlidir?", "Baş və köməkçi qurğuların təhlükəsiz, effektiv işini", "Yalnız jurnalların doldurulmasını", "Gəmi xidməti personalının iş qrafikini", "Liman idarələri ilə əlaqəni"),
    ("35. Maşın şöbəsi növbsinə təyin edilən növbətçi mexanik və ya sıravi heyət üzvləri sutka ərzində neçə saat dincəlməlidir?", "10 saat", "8 saat", "6 saat", "12 saat"),
    ("36. Maşın şöbəsi növbəsinə təyin edilən növbətçi mexaniki və ya sıravi heyət üzvləri 7 sutka ərzində neçə saat dincəlməlidirlər?", "77 saat", "70 saat", "80 saat", "65 saat"),
    ("37. Növbətçi mexanik növbəni təhvil verməzdən əvvəl nə etməlidir?", "Baş və köməkçi qurğulara aid olan hadisələrin lazımi qaydada qeydiyatını aparmalıdır", "Bütün sistemləri söndürüb təhvil verməlidir", "Yalnız gəmi kapitanına şifahi məlumat verməlidir", "Növbəni tərk edib dincəlməyə getməlidir"),
    ("38. Bu sistemlərdən hansı baş mühərrikin işini təmin edən sistemlərdir?", "Yanacaq, yağ, soyutma, hava, məsafədən avtomatik idarəetmə", "Balaast, sükan, qurutma, sanitar, havalandırma", "Naviqasiya, rabitə, xilasetmə, lövbər", "İşıqlandırma, qaldırıcı kranlar, yük nasosları"),
    ("39. Dəniz ətraf mühitinin çirklənməsinin qarşısını almaq üçün nə etmək lazımdır?", "Beynalxalq sənədləri, mübarizə metodlarını, xəbərdarlıq tədbirlərini bilmək və əməl etmək", "Yalnız neft tullantılarını xüsusi çənlərə yığmaq", "Zibilləri gizlicə dənizə atmaq", "Dəniz kənarında gəminin təmizliyini həyata keçirməmək"),
    ("40. Maşın şöbəsində hansı rabitə vasitələri mövcuddur?", "Gəmidaxili rabitə, qəza rabitəsi, teleqraf", "Uzaqmənzilli VHF radiostansiya, peyk telefonu", "Yalnız mobil telefonlar", "Mors əlifbası siqnal lampaları"),
    ("41. “Kapitan körpüsü-maşın şöbəsi” arasında telefon əlaqəsi neçə vaxtdan bir yoxlanılmalıdır?", "Hər gün", "Hər həftə", "Hər növbə dəyişimində", "Yalnız səfərə çıxmazdan əvvəl"),
    ("42. Gəmi səfərə çıxmamışdan qabaq gəmi teleqrafını kimlər yoxlamalıdırlar?", "Baş köməkçisi və növbətçi mexanik", "Kapitan və baş mexanik", "Matros və motorçu", "Yalnız növbətçi mexanik"),
    ("43. Funksiyalara görə gəmidə hansı məsuliyyət səviyyələri təyin edilmişdir?", "İdarəetmə, istismar, köməkçi", "Rəhbərlik, nəzarət, icra", "Kapitan, mexaniklər, matroslar", "Baza, əsas, ehtiyat"),
    ("44. İdarəetmə səviyəsinə gəminin hansı heyəti aiddir?", "kapitan, baş köməkçi, baş mexanik və ikinci mexanik", "bütün mexaniklər və şturmanlar", "növbə köməkçisi, növbətçi mexanik, elektrik mexaniki", "yalnız kapitan və baş mexanik"),
    ("45. İstismar səviyyəsinə gəminin hansı heyəti aiddir?", "növbə köməkçisi, növbətçi mexanik, elektrik mexaniki", "sıravi heyət və motorçular", "kapitan, baş köməkçi, baş mexanik və ikinci mexanik", "aşpaz və xidmətçi personal"),
    ("46. Köməkçi səviyyəsinə gəminin hansı heyəti aiddir?", "sıravi heyət", "kapitan və köməkçiləri", "növbətçi mexaniklər", "baş mexanik və ikinci mexanik"),
    ("47. Səriştəlik (bilik, anlayış, bacarıq) standartları nədir?", "Dənizçilərin minimal bilik, anlayış və bacarıq nümayiş etdirmək qabliyyəti", "Gəminin texniki baxışdan keçmək bacarığı", "Gəmiqayırma zavodlarının keyfiyyət meyarları", "Liman işçilərinin peşəkarlıq səviyyəsi"),
    ("48. Gəmini tərk edərkən sağ qalmaq üçün səriştəliliyə dair minimal tələblər hansılardır?", "Bütün xilasetmə vasitələrinin növlərini bilmək və istifadə etməyi bacarmaq", "Gəminin texniki jurnalını özü ilə götürmək", "Əlavə yanacaq ehtiyatı toplamaq", "Rabitə vasitələrini məhv etmək"),
    ("49. Xəsarət alanlara ilk tibbi yardımın göstərilməsi üçün səriştəliliyə dair minimal tələblər hansılardır?", "Tibbi yardımın göstərilməsi tələb olunan bədbəxt hadisələr zamanı təxirəsalınmaz tədbirləri görmək", "Yalnız gəmi həkiminə xəbər vermək", "Zərərçəkmişin şəxsi əşyalarını qorumaq", "Təcili yardıma zəng vurub gözləmək"),
    ("50. Yanğın təhlükəsizliyi və yanğınla mübarizə üçün səriştəliliyə dair minimal tələblər hansılardır?", "Yanğın riskinin minumuma endirilməsi və texniki vasitələri daima işə salınmağa hazır saxlamaq", "Yalnız yanğın söndürən balonların yerini bilmək", "Yanğın anında gəmini dərhal tərk etmək", "Odla işləri tamamilə qadağan etmək"),
    ("51. Növbətçi mexanikin insanlara qayğı göstərilməsi səviyyəsində səriştəsinə dair minimal tələblər hansılardır?", "Personalın idarə edilməsi və hazırlanması sahəsində qanunları bilmək və əməl etmək", "Heyətin asudə vaxtını təşkil etmək", "Mətbəxin və qida təminatının yoxlanışını aparmaq", "Gəmi həkiminə kömək etmək"),
    ("52. Yanğınla mübarizə geniş proqramı üzrə qəza qruplarının təşkili və hazırlanması üçün səriştəliliyə dair tələblər hansılardır?", "Fövqəladə vəziyyətlərdə hərəkət planlarını, odla mübarizə strategiyasını və taktikasını bilmək", "Yalnız yanğın həyəcanı siqnalını çalmaq", "Yanğın zonasına girməkdən qəti şəkildə imtina etmək", "Bütün havalandırma sistemlərini daimi açıq saxlamaq"),
    ("53. Gəmi səfərə çıxmamışdan əvvəl baş mexanik kapitanla məsləhətləşərkən əvvəlcədən səfər üçün hansı tələbatları təyin etməlidir?", "Yanacaq, su, yağ, kimyəvi maddələr, sərfi materiallar, ehtiyat hissələri, alətlər", "Yalnız qida ehtiyatları və tibbi ləvazimatlar", "Xilasetmə halqalarının və jiletlərinin sayını", "Sərnişinlərin sayını və biletlərini"),
    ("54. Gəmi dənizdə olarkən baş mexanik maşın şöbəsində nəyi təmin etməlidir?", "Maşın şöbəsinin növbətçisinin lazımi səviyyədə təhlükəsiz, səriştəli təşkilini", "Yalnız yanacağın miqdarına nəzarəti", "Körpücükdə naviqasiya növbəsinin təşkilini", "Liman rüsumlarının ödənilməsi prosesini"),
    ("55. Gəmi müxtəlif ərazilərdə və hava şəraitlərində üzərkən növbətçi mexanik nə etməlidir?", "kapitan körpüsündən hər an verilən əmrin yerinə yetirilməsinə hazır olmalıdır", "Mexanizmləri dayandırıb havanın düzəlməsini gözləməlidir", "Bütün nəzarəti avtomatika sisteminə tapşırmalıdır", "Təcili olaraq baş mexaniki yuxudan oyatmalıdır"),
    ("56. Növbətçi mexanik gəmi çətin keçilə bilən və ya sahilyanı sularda üzərkən gəminin manevrini necə təmin etməlidir?", "Əl ilə idarə edilə bilən mexanizmlərin dərhal əl ilə idarə etməyə keçməsinə hazır olmalıdır", "Bütün avadanlıqları tam gücü ilə işlətməlidir", "Gəmi dayananacan heç bir tədbir görməməlidir", "Körpücüyə çıxıb vizual müşahidə aparmalıdır"),
    ("57. Maşın şöbəsinin idarə edilməsi üçün nəyi bilmək və anlamaq lazımdır?", "Resursların bölüşdürülməsini, prioritetlərin təyin edilməsini, effektiv ünsiyyəti, liderliyi, vəzifələri analiz etməyi, komanda tərkibində işləməyi", "Yalnız hesabatların tərtib edilməsi qaydasını", "Hava proqnozunu oxumağı və dəniz cərəyanlarını", "Limandakı yükləmə və boşaltma proseslərini"),
    ("58. Avadanlıqlara texniki xidmətin göstərilməsi və təmiri üçün nəyi bilmək və anlamaq lazımdır?", "Quruluşunu, istismar və təmir təlimatlarını, xarakterik nasazlıqlarını və təhlükəsizlik tədbirlərini", "Yalnız alətlərin adlarını və sayını", "Dəniz hüququ və ticarət müqavilələrini", "Gəmi sahibinin iqtisadi vəziyyətini")
]

questions_list = []
for idx, (q_text, correct, d1, d2, d3) in enumerate(data):
    opts = [correct, d1, d2, d3]
    random.shuffle(opts)
    
    mapping = {
        "A": opts[0],
        "B": opts[1],
        "C": opts[2],
        "D": opts[3]
    }
    
    correct_letter = "A"
    for letter, text in mapping.items():
        if text == correct:
            correct_letter = letter
            break
            
    questions_list.append({
        "id": f"q{idx+1:03d}",
        "question": q_text,
        "options": mapping,
        "correct_answer": correct_letter,
        "explanation": ""
    })

out_data = {
    "certificate": "Maşın şöbәsi resurslarının idarә olunması",
    "questions": questions_list
}

with open(r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\ma_n_b_si_resurslar_n_n_idar_olunmas.json', 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

print("Rebuild complete. 58 questions saved.")
