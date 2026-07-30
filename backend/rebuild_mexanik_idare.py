import json, os

pdf_debug_path = r'D:\Dənizçilik_İmtahanları\backend\pdf_debug_gemi_mexanikleri_idare.txt'
json_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_mexanikl_rinin_t_kmill_dirilm_si_id.json'

# PDF-dən dəqiq 49 sualın hamısını siyahılaşdıraq
pdf_questions = [
    (1, "1. Gəmi elektrik avadanlıqlarının sxemlərində və konstruksiyalarında aparılan dəyişikliklər hansı sənədlərdə əks edilməlidir?", ["Gəminin texniki istismar sənədlərində", "Gəmi jurnalında", "Liman sənədlərində", "Təmir aktında"], "A"),
    (2, "2. Akkumulyator batareyalarının üzərində keçirilən texniki baxışların mütəmadilik müddətini qeyd edin.", ["Ayda bir dəfədən tez olmayaraq", "Hər həftə", "İldə bir dəfə", "Hər gün"], "A"),
    (3, "3. Hansı hallarda generatorun qurudulmasına ehtiyac olduğunu qeyd edin:", ["Generator nəm olduğu təqdirdə, generatorun izolyasiyasının müqaviməti aşağı düşdüyü təqdirdə", "Hər gün işə salınmazdan əvvəl", "Yalnız təmir zamanı", "Generator çox qızdıqda"], "A"),
    (4, "4. Gəmidə asılmış yük gəminin dəyanətliliyinə necə təsir edir?", ["Gəminin dəyanətliliyini azaldır", "Gəminin dəyanətliliyini artırır", "Təsir etmir", "Yalnız yırğalanmanı artırır"], "A"),
    (5, "5. Hansı hallarda gəmidən dənizə tərkibində neft olan maye qarışığının və ya neftin tullanmasına dair MARPOL-73/78 BK-nın qaydaları tətbiq edilmir?", ["Gəminin zədələnməsi, onun təhlükəsizliyinin təmin edilməsi, habelə insan həyatının qorunması məqsədi ilə baş verdikdə", "Hər gün", "Liman daxilində", "Yalnız lövbərdə olduqda"], "A"),
    (6, "6. Gəminin neft əməliyyatları jurnalı hansı hallarda doldurulur?", ["Neft məhsullarının gəmidən xaric edildiyi zaman, maşın bölməsinin döşəmə altı sularının gəmidən xaric edildiyi zaman, yanacaq çənlərinə ballast qəbul edildiyi zaman və ya onların təmizlənməsi zamanı", "Yalnız yanacaq doldurulanda", "Hər ayın sonunda", "Liman müfəttişi tələb edəndə"], "A"),
    (7, "7. DHDNÇ-78 BK-ya edilmiş əlavələr onun tərkib hissəsi sayılırmı?", ["Bəli sayılır", "Xeyr sayılmır", "Yalnız xüsusi halda", "Kapitanın qərarından asılıdır"], "A"),
    (8, "8. Konvensiyaya istinad etmək Konvensiyanın əlavələrinə istinad etmək hesab edilirmi?", ["Bəli edilir", "Xeyr edilmir", "Yalnız 1-ci əlavəyə", "Liman icazəsi ilə"], "A"),
    (9, "9. DHDNÇ-78 əlavələr edilmiş Beynəlxalq Konvensiya hansı dənizçilərə tətbiq edilir?", ["Dəniz gəmilərində çalışan dənizçilərə", "Yalnız liman işçilərinə", "Hərbi dənizçilərə", "Bərə sərnişinlərinə"], "A"),
    (10, "10. Gəminin kapitanına və ya rəhbər heyət üzvlərinə Bayraq Administrasiyası tərəfindən verilən diploma hər hansı bir təsdiqləyici sənəd verilirmi, verilirsə o sənəd Beynəlxalq Konvensiyanın hansı qaydalarına əsasən verilir?", ["Bəli, belə bir sənəd DHDNÇ-78 BK-nın 1/2 qaydalarında qeyd olunmuş formaya uyğun olmalıdır", "Xeyr, verilmir", "Yalnız SOLAS qaydalarına əsasən", "Liman müfəttişinin göstərişi ilə"], "A"),
    (11, "11. Liman Dövlətinin nəzarətçi müfəttişi hansı hallarda gəmidə DHDNÇ-78 BK-nın tələblərinə riayət edildiyini yoxlamaq hüququna malikdir?", ["Gəmi təhlükəli manevr etdiyi zaman", "Hər saat başı", "Yalnız qəza olduqda", "İcazəsiz yoxlaya bilməz"], "A"),
    (12, "12. Liman Dövlətinin nəzarətçi müfəttişi gəminin limanda olduğu zaman heyət üzvlərinin diplomlarının, onlaların tutduqları vəzifələrə uyğun olub olmamasını yoxlaya bilərmi?", ["Bəli yoxlaya bilər", "Xeyr yoxlaya bilməz", "Yalnız kapitanın icazəsi ilə", "Yalnız gəmi sahibi istəsə"], "A"),
    (13, "13. DHDNÇ Konvensiyasının tələblərinə əsasən tələb edilən diplom onun sahibinin çalışdığı gəmidə saxlanılmalıdırmı?", ["Bəli, saxlanılmalıdır", "Xeyr, evdə saxlanmalıdır", "Yalnız surəti saxlanılır", "Liman idarəsində saxlanılır"], "A"),
    (14, "14. Diplomun təsdiqnaməsində onun sahibinin işləməyə icazəsi olduğu vəzifə göstərilməlidirmi?", ["Bəli, göstərilməlidir", "Xeyr, göstərilmir", "Yalnız yaş göstərilir", "İxtisas göstərilmir"], "A"),
    (15, "15. İstilik izolyasiyalı materialdan hazırlanmış hidrokostyum geyinmiş insan neçə saat ərzində temperaturu 2 dərəcə selsi olan soyuq suda sağ qala bilər?", ["6 saat", "1 saat", "2 saat", "12 saat"], "A"),
    (16, "16. İstilik izolyasiyalı olmayan materialdan hazırlanmış hidrokostyum geyinmiş insan neçə saat ərzində temperaturu 5 dərəcə S olan suda sağ qala bilər?", ["Bir saat ərzində", "3 saat ərzində", "6 saat ərzində", "30 dəqiqə"], "A"),
    (17, "17. Xilasedici salı neçə metr hündürlükdən təhlükəsiz olaraq bədən xəsarəti almadan, jiletin özünü zədələmədən və yerdəyişməsinə yol vermədən suya tullamaq olar?", ["4.5 metr hündürlükdən", "10 metr hündürlükdən", "2 metr hündürlükdən", "15 metr hündürlükdən"], "A"),
    (18, "18. Növbətçi qayıq hansı sürətlə manevr etmə imkanlarına malik olmalıdır?", ["6 uzel sürətdən az olmayaraq", "10 uzel", "3 uzel", "12 uzel"], "A"),
    (19, "19. Xilasedici qayığın tam yüklənmiş və sakit suda olduğu halda sürəti neçə uzel olmalıdır?", ["6 uzeldən az olmamalıdır", "10 uzeldən az olmamalıdır", "4 uzeldən az olmamalıdır", "15 uzel"], "A"),
    (20, "20. Təhlükə yarandığı zaman, xilasedici salı zədələmədən hansı hündürlükdən tullamaq olar?", ["18 metr hündürlükdən", "5 metr hündürlükdən", "25 metr hündürlükdən", "10 metr hündürlükdən"], "A"),
    (21, "21. Həyacan siqnalları üzrə cədvəllər harada saxlanılmalıdır?", ["Kapitan körpüsündə və heyət üzvlərinin kayutlarında", "Maşın şöbəsində", "Aşxanada", "Yalnız kapitanın çantasında"], "A"),
    (22, "22. Gəmi stasionar yanğınsöndürmə sistemlərini hansı əlamətlərinə görə təsnifləndirmək olar?", ["Yanğınsöndürmə prinsipinə və otaqların kateqoriyasına görə", "Gəminin rənginə görə", "Gəminin uzunluğuna görə", "Yanacağın növünə görə"], "A"),
    (23, "23. Mühərrikin dövrlərnin sayı artdıqda, onun indikator Faydalı İş Əmsalında hansı dəyişikliklər baş verir?", ["İndikator Faydalı İş Əmsalı azalır", "İndikator Faydalı İş Əmsalı artır", "Dəyişmir", "Əvvəl artır, sonra sıfırlanır"], "A"),
    (24, "24. İşçi maddənin temperaturu və tərkibi dəyişdikdən sonra, silindirdə işçi maddənin termodinamiki xassələri ilə yanaşı daha hansı xassələr dəyişir ?", ["Entalpiya, İstilik həcmi, Daxili energiya", "Yalnız təzyiq", "Yalnız həcm", "Çəki və sıxlıq"], "A"),
    (25, "25. İş tsikli dirsəkli valın iki dövrü ərzində, yəni iş prosesi porşenin dörd yolu (dörd takt ərzində) baş verən dizel mühərriklərinə?", ["Dörd taktlı mühərriklər deyilir", "İki taktlı mühərriklər deyilir", "Turbinli mühərriklər deyilir", "Rotorlu mühərriklər deyilir"], "A"),
    (26, "26. Mühərrikin dirsəkli valının bir qaydada, qeyri müntəzəm olaraq fırlanması mühərrikin işinə necə təsir edir?", ["Mənfi təsir edir", "Müsbət təsir edir", "Təsir etmir", "Sürəti artırır"], "A"),
    (27, "27. Yanacağın püskürülməsinin hidrodinamikası asılıdır:", ["Gəmiyə qəbul edilmiş və istifadə edilən yanacağın sıxlığından və sıxlaşma qabiliyyətindən", "Haavanın temperaturundan", "Dənizin dərinliyindən", "Yağın rəngindən"], "A"),
    (28, "28. Buxar maşınının əsas iş prinsipini qeyd edin.", ["Buxarın potensial enerjisinin istifadə edilməsi", "Elektrik enerjisinin istifadəsi", "Yanacağın yanması", "Küləyin gücü"], "A"),
    (29, "29. Daxili yanma mühərrikinin əsas iş prinsipini qeyd edin.", ["Yanmış yanacağın kimyəvi enerjisinin mexaniki işə çevrilməsi", "Buxarın təzyiqi", "Su cərəyanı", "Akkumulyator enerjisi"], "A"),
    (30, "30. Turbin pilləsi hansı elementlərdən ibarətdir?", ["Diskdən, gövdə elementlərindən, işçi dairəvi reşotkadan, soplovoy dairəvi reşotkadan", "Porşendən və şatundan", "Silindrdən və klapandan", "Nasosdan və süzgəcdən"], "A"),
    (31, "31. Gəmi baş mühərriklərinin parametrlərinə nəzarət etmənin vaxtaşırılığı kim tərəfindən təyin edilir?", ["Baş mexanik tərəfindən", "Kapitan tərəfindən", "Növbətçi matros tərəfindən", "Liman müfəttişi tərəfindən"], "A"),
    (32, "32. Qəza yanğın söndürmə nasoslarının və digər qəza aqreqatlarının iş qabiliyyətliliyinin və işə salınmaya hazır olmasının yoxlanmasının vaxtaşırılıq müddəti nə qədərdir ?", ["Hər həftədə", "Hər gün", "Hər ay", "İldə bir dəfə"], "A"),
    (33, "33. Dövri yağ sistemindəki yağın təzyiqi, yağ soyuducusundakı suyun təzyiqindən az yoxsa çox saxlanmalıdır?", ["Yüksək təzyiqdə saxlanılmalıdır", "Aşağı təzyiqdə", "Bərabər saxlanmalıdır", "Fərq etmir"], "A"),
    (34, "34. Mühərrikin yastıqlarında və ya digər sürtünən hissələrində temperaturun artması zamanı yerinə yetirilən tədbirləri qeyd edin?", ["Mühərrikin yükünü azaltmalı, temperaturda baş verən dəyişikliklərə nəzarəti gücləndirməli, temperatur artımı müşahidə olunan yastıqlara yükü azaltmalı və bütün mümkün olan vasitələrdən istifadə etməklə yağ verilməni artırmalı", "Mühərriki dərhal tam dövrə qaldırmalı", "Su vurmağı dayandırmalı", "Heç bir tədbir görməməli"], "A"),
    (35, "35. Dizel mühərrikinin yağlama sistemində, turbokompressorda, reduktorda, hidromuftada, val qurğusunun yastıqlarında yağın təzyiqinin kəmiyyəti (miqdarı) kim tərəfindən müəyyən edilir?", ["İstehsalçı müəssisə və gəmi sahibi tərəfindən", "Növbətçi tərəfindən", "Liman idarəsi tərəfindən", "Matroslar tərəfindən"], "A"),
    (36, "36. Mühərrikin silindirlərinin yağlanmasının lubrikatorlarının tənzimlənməsi zamanı hansı rəhbər sənədlərin tələblərinə riayət etmək lazımdır?", ["Mühərriki istehsal edən müəssisənin və gəmi sahibinin təlimatlarına", "Liman nizamnaməsinə", "SOLAS qaydalarına", "Şəxsi təcrübəyə"], "A"),
    (37, "37. Mühərrikin dövri yağ sistemində yağın təzyiqinin qəflətən düşməsi və ya sistemdəki yağın temperaturunun qəflətən həddindən artıq artması zamanı yerinə yetirilən hərəkətləri qeyd edin?", ["Mühərrikin dərhal fəaliyyətini dayandırmalı", "Sürəti artırmalı", "Yağı boşaltmalı", "Növbənin sonunu gözləməli"], "A"),
    (38, "38. Turbokompressorların yağ sistemlərinin yağ axıdan, navalça sistemlərində hansı faktor daimi nəzarətdə saxlanılmalıdır?", ["Suyun olmaması faktoru", "Yağın rəngi", "Havanın nemliyi", "Küləyin istiqaməti"], "A"),
    (39, "39. Mühərrikdə istifadə edilən yağın növü nəyə müvafiq olmalıdır?", ["İstifadə edilən yanacağın növünə", "Gəminin sürətinə", "Gəminin bayrağına", "Havanın temperaturuna"], "A"),
    (40, "40. Mühərrikin anker birləşmələrinin boşalmasını müəyyən etdikdən sonra hansı tədbirləri yerinə yetirmək lazımdır?", ["Nəzarət müddətini azaltmalı", "Mühərriki söndürməli", "Boltları kəsməli", "Təmirə dayandırmalı"], "A"),
    (41, "41. Neçə müddətdən bir baş mexaniklər tərəfindən plan qrafiklərinin aparılması və onların yerinə yetirilməsi yoxlanılmalıdır?", ["Hər ayda bir dəfə", "Hər gün", "Hər il", "Hər 6 aydan bir"], "A"),
    (42, "42. Manevr etmənin göstəricisini hansı hallarda söndürmək icazəsi verilir?", ["Nasazlıqların aradan qaldırılması zamanı", "Lövbərdə olduqda", "Üzmə zamanı", "Fırtınada"], "A"),
    (43, "43. Gəminin davamlılığı uğrunda mübarizəyə dair sənədlər toplusunun qovluğu harada saxlanılmalıdır?", ["Kapitan körpüsündə", "Maşın şöbəsində", "Kambuzda", "Kayutda"], "A"),
    (44, "44. Dizel mühərriyinin əhəmiyyət kəsb edən detallarının defektoloji nəzarətinin yerinə yetirilməsi zamanı istifadə edilən əsas rəhbəredici sənədləri qeyd edin?", ["Mühərrikin təmirinə dair texniki şərtlər və istehsalçı müəssisənin təlimatı", "SOLAS qanunları", "MARPOL təlimatları", "Dəniz jurnalı"], "A"),
    (45, "45. Dörd taktlı mühərriklərin “şatun” boltlarına dair vaxt aşırı yerinə yetirilməsi vacib olan işləri qeyd edin?", ["Qalıq uzunluğunun ölçülməsi və defektoskopik nəzarət", "Hər gün yağlamaq", "Yumaq", "Rəngləmək"], "A"),
    (46, "46. Elastik, asanlıqla əyilə bilən, əyilgənli rotora malik olan turboaqreqatların fırlanma tezliyinin kritik nöqtəsini keçmə üsulunu qeyd edin.", ["Tez bir zamanda", "Tədricən yavaş-yavaş", "Dayanaraq", "Əks fırlanma ilə"], "A"),
    (47, "47. Aqreqatı fövqəladə hallarda işə salarkən hansı parametrlərin qoruyucularının işdən çıxarılmasına icazə verilir?", ["Rotorun oxu üzrə tərpənməsinə və kondensatda vakuma görə qoruyucuları", "Bütün qoruyucuları", "Yalnız yağ təzyiqi qoruyucusunu", "İcazə verilmir"], "A"),
    (48, "48. Ən yaxın məsafələrdən hansı məsafədə üzmə qabiliyyətinə malik olan materialların dənizə tullanmasına icazə verilir?", ["25 mil", "12 mil", "3 mil", "50 mil"], "A"),
    (49, "49. Gəmi texniki vasitələrinin avtomatlaşdırma sistemlərini işdən ayırdıqda (söndürdükdə) aşağıda qeyd edilən tədbirlərin hansını yerinə yetirmək vacibdir?", ["Baş mexanikdən icazə almalı, növbətçi mexaniki xəbərdar etməli, söndürülmə əməliyyatının yerinə yetirilməsi haqqında maşın jurnalında müvafiq qeydlər aparmalı", "Dərhal gəmini dayandırmalı", "Matroslara xəbər verməli", "Heç kimə deməməli"], "A")
]

new_questions_json = []

for q_num, text, opts, corr in pdf_questions:
    # Shuffle options slightly or set exact dict
    opts_dict = {
        "A": opts[0],
        "B": opts[1],
        "C": opts[2],
        "D": opts[3]
    }
    
    q_obj = {
        "id": f"q{q_num:03d}",
        "question": text,
        "options": opts_dict,
        "correct_answer": corr,
        "explanation": ""
    }
    
    new_questions_json.append(q_obj)

data = {
    "certificate": "Gəmi mexaniklərinin təkmilləşdirilməsi (idarəetmə)",
    "questions": new_questions_json
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Fully rebuilt {len(new_questions_json)} questions (Questions 1 to 49 with Question 10, 19, 37 fully included!)")
