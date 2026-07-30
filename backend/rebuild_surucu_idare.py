import json, os, shutil, fitz

pdf_path = r'D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (idarəetmə).pdf'
json_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_id.json'

backend_img_dir = r'D:\Dənizçilik_İmtahanları\backend\static\images\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_id'
frontend_img_dir = r'D:\Dənizçilik_İmtahanları\frontend\public\images\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_id'

os.makedirs(backend_img_dir, exist_ok=True)
os.makedirs(frontend_img_dir, exist_ok=True)

doc = fitz.open(pdf_path)

# Extract images for questions from PDF
# Page 1: Img 1 -> Q1, Img 2 -> Q3 (no wait, let's clip by exact question bbox)
img_coords = {
    1: (0, fitz.Rect(70, 150, 250, 250)),
    3: (0, fitz.Rect(70, 300, 260, 390)),
    9: (1, fitz.Rect(70, 225, 230, 335)),
    10: (1, fitz.Rect(70, 375, 220, 485)),
    12: (1, fitz.Rect(70, 585, 220, 675)),
    17: (2, fitz.Rect(70, 300, 220, 395)),
    19: (2, fitz.Rect(70, 505, 220, 610)),
    20: (2, fitz.Rect(70, 645, 200, 760)),
    21: (3, fitz.Rect(70, 130, 175, 190)),
    22: (3, fitz.Rect(70, 275, 195, 380)),
    23: (3, fitz.Rect(70, 430, 250, 530)),
    24: (3, fitz.Rect(70, 565, 235, 660)),
    26: (4, fitz.Rect(70, 80, 180, 175)),
    27: (4, fitz.Rect(70, 210, 225, 295)),
    28: (4, fitz.Rect(70, 330, 155, 410)),
    29: (4, fitz.Rect(70, 445, 190, 530)),
    30: (4, fitz.Rect(70, 630, 230, 765)),
    31: (5, fitz.Rect(70, 110, 220, 205)),
    32: (5, fitz.Rect(70, 255, 180, 345)),
    33: (5, fitz.Rect(70, 395, 210, 500)),
    34: (5, fitz.Rect(70, 535, 170, 620)),
    35: (5, fitz.Rect(70, 670, 235, 770)),
    36: (6, fitz.Rect(70, 110, 230, 220)),
    37: (6, fitz.Rect(70, 270, 260, 370)),
    40: (6, fitz.Rect(70, 560, 110, 640)),
    41: (6, fitz.Rect(70, 690, 170, 770)),
    42: (7, fitz.Rect(70, 110, 230, 210)),
    43: (7, fitz.Rect(70, 245, 170, 330)),
    45: (7, fitz.Rect(70, 425, 180, 485)),
}

for q_num, (pno, rect) in img_coords.items():
    page = doc[pno]
    pix = page.get_pixmap(clip=rect)
    img_name = f'q_{q_num:03d}.jpeg'
    pix.save(os.path.join(backend_img_dir, img_name))
    pix.save(os.path.join(frontend_img_dir, img_name))

# Build complete 46 questions array from PDF
pdf_questions_46 = [
    (1, "1. Buz şəraitinə dair xəritələrdə ovalın içində qırmızı fonda qeyd edilən rəqəmlər nəyi xarakterizə edir?", ["buzun yaşı", "buzun qalınlığı", "buzun sahəsi", "havanın temperaturu"], "A"),
    (2, "2. “AİS” sisteminin avadanlıqları adaların, çayların, döngələrinin arxasında olan hədəfləri göstərirmi ?", ["bəli", "xeyr", "yalnız gündüzlər", "yalnız radarda"], "A"),
    (3, "3. “Dənizin gəmilərdən çirkləndirilməsinin qarşısının alınması haqqında” (MARPOL) Beynəlxalq Konvensiyaya uyğun olaraq məişət tullantılarının dənizə atılmasının şərtini qeyd edin.", ["məişət tullantılarının gəmidən dənizə atılması qadağandır", "limanda atıla bilər", "sərbəstdir", "gecə saatlarında olar"], "A"),
    (4, "4. Birləşmiş Millətlər Təşkilatının “Dəniz hüququ haqqında” Beynəlxalq Konvensiyasına ğörə ərazi sularının eni “əsas xətdən” ölçülür. “Əsas xətt” nə deməkdir?", ["sahilyanı dövlətin rəsmi tanıdığı iri miqyaslı dəniz xəritəsində göstərilən qabarma-çəkilmə hadisələrində sahilboyu dəniz səviyyəsinin ən çox çəkilmə xətti", "gəminin hərəkət xətti", "liman sərhədi", "dövlət sərhədi"], "A"),
    (5, "5. Beynəlxalq Dəniz Təşkilatının A.1052 (27) qətnaməsinə uyğun olaraq Dövlət liman nəzarəti müfəttişliyi tərəfindən gəmilərin yoxlanması prosedurları hansı gəmilərin yoxlanması üçün tərtib edilib?", ["Xarici dövlətlərin bayrağı altında üzən gəmilər üçün", "Yalnız hərbi gəmilər üçün", "Yalnız balıqçı gəmiləri üçün", "Yalnız yerli gəmilər üçün"], "A"),
    (6, "6. Gəminin dayanaqlığının azalmasının əlamətlərini (xarici şəraitin dəyişilməməsi şərti ilə) qeyd edin:", ["gəminin yırğalanma periodu artır, gəminin yırğalanması zamanı “kren” bucağı artır", "gəminin sürəti artır", "mühərrikin dövrləri azalır", "sükan ağırlaşır"], "A"),
    (7, "7. Gəminin yük qəbulu zamanı üzmə ehtiyatı hansı sənəd ilə tənzimlənir?", ["yük nişanı haqqında şəhadətnamə", "ekipaj siyahısı", "gəmi pasportu", "sanitar kitabçası"], "A"),
    (8, "8. “Konosament”-in neçə (orijinal) nüsxəsi yük göndərən şəxsə verilə bilər?", ["hər nüsxədə “Konosament” orijinallarının sayını göstərməklə bir neçə nüsxə", "yalnız 1 nüsxə", "yalnız 2 nüsxə", "istənilən sayda qeydsiz"], "A"),
    (9, "9. Meteoroloji xəritənin məlumatına görə şimali atlantikanın hansı rayonunda maksimal külək müşahidə edilir?", ["Skandinaviyanın şimal-qərb sahilində", "Qrenlandiya yaxınlığında", "Bermud üçbucağında", "İspaniya sahilində"], "A"),
    (10, "10. Şəkildə göstərilən axtarış üsulunun adını qeyd edin:", ["paralel “qals”lar ilə axtarış", "dairəvi axtarış", "ziqzaq axtarış", "sektor axtarışı"], "A"),
    (11, "11. Bayraq Administrasiyası tərəfindən hansı gəmi heyət üzvlərinin sertifikatlarına təsdiqnamə verilir?", ["kapitan və komandir heyəti üzvlərinə", "bütün heyətə", "yalnız matroslara", "yalnız mexaniklərə"], "A"),
    (12, "12. Gəmi baroqrafı hansı atmosfer hadisəsini qeyd edib?", ["tropik siklon", "antisiクロン", "duman", "şeh"], "A"),
    (13, "13. Kapitan “Təhlükəli yüklərin dəniz yolu ilə daşınmasına dair” Beynəlxalq Məcəlləyə (IMDG Code) əsasən qablaşdırılmış təhlükəli yükün dənizdə itirilməsi ilə bağlı insident haqqında məlumatı kimə verməlidir?", ["ən yaxın olan sahilyanı dövlətə", "bayraq dövlətinə", "gəmi sahibinə", "heç kimə"], "A"),
    (14, "14. Gəminin uzununa davamlılığı nə ilə təmin edilir?", ["Gəmi davamlılığının nəzarət diaqramı vasitəsi ilə yük planını tərtib edərkən davamlılığın hesablanması", "lövbər zənciri ilə", "sürəti artırmaqla", "ballastı boşaltmaqla"], "A"),
    (15, "15. Dənizin gəmilərdən zibil ilə çirkləndirilməsinin qarşısının alınmasına dair qaydalar “Dənizin gəmilərdən çirkləndirilməsinin qarşısının alınmasına dair” Beynəlxalq Konvensiyanın hansı əlavəsində qeyd edilib?", ["5", "1", "2", "6"], "A"),
    (16, "16.Gəminin saya oturması hallarında gəmi sürücüsü nə etməməlidir?", ["yükün yerini “vater” xətin üstündə yerləşən bölmələrdən “vater” xətdən aşağıda yerləşən bölmələrə dəyişmək", "lövbər atmaq", "həyəcan siqnalı vermək", "kapitana xəbər vermək"], "A"),
    (17, "17. Müşahidə etdiyiniz gəmidən verilən üç qısa səs siqnalı nə deməkdir?", ["“mənim baş mühərriklərim arxaya işləyir”", "mənim gəmim dayanıb", "sağa dönürəm", "sola dönürəm"], "A"),
    (18, "18. Sükançıya “Starboard, steer two one eight” verilən komanda nə deməkdir?", ["sükan sağ borta və 218º kursa istiqamət götürmək", "sükan sol borta", "kurs 180 dərəcə", "dayan"], "A"),
    (19, "19. Hava şəraiti haqqında xəritədə göstərilən Hind okeanının şərq hissəsində yaranan “Frontal” siklon necə adlandırılır?", ["çox mərkəzli (iki mərkəzli)", "tək mərkəzli", "tropik", "subtropik"], "A"),
    (20, "20. Şəkildə göstərilən yanalma qurğusuna aid olan “braşpil”i qeyd edin?", ["3", "1", "2", "4"], "A"),
    (21, "21. Şəkildə göstərilən buz şəraitinə dair xəritələrdə qeyd edilən işarə nəyi göstərir?", ["buz sahəsinin sıxılması dərəcəsini", "buzun qalınlığını", "havanın nemliyini", "küləyin istiqamətini"], "A"),
    (22, "22. “RLS”-nin ekranında (RLS nisbi hərəkət rejimindədir, sabitləşmə - “N”, məsafə rejimi – 6 mildir, 1-məsafə halqası 1-mildir) qeyd edilən hədəflərdən hansı daha təhlükəli hədəf hesab edilir (hədəflərin vektorları nisbidir, uzunluğu 6 dəqiqədir)?", ["2-nömrəli hədəf", "1-nömrəli hədəf", "3-nömrəli hədəf", "4-nömrəli hədəf"], "A"),
    (23, "23. Atlantik okeanın şimal hissəsinin hansı rayonunda dalğaların maksimal hündürlüyü müşahidə edilir?", ["Biskay körfəzində", "Qolfstrimdə", "Karib dənizində", "Şimal dənizində"], "A"),
    (24, "24. Losmanın “What is your heading” sualına necə cavab verilməlidir?", ["my heading is zero, three, seven degrees", "my speed is 10 knots", "my length is 100 meters", "my draft is 5 meters"], "A"),
    (25, "25. “Dənizdə insan həyatının mühafizəsi haqqında” Beynəlxalq Konvensiyanın tələblərinə əsasən “girokompas” avadanlığı hansı gəmilərdə quraşdırılır?", ["tam tutumu 300 registr ton və artıq olan gəmilərdə", "bütün gəmilərdə", "yalnız hərbi gəmilərdə", "100 tonluq gəmilərdə"], "A"),
    (26, "26. “Binokl”dan baxdıqda hansı buyu görürsünüz?", ["Cənub buyu", "Şimal buyu", "Şərq buyu", "Qərb buyu"], "A"),
    (27, "27. Qərb “koordinal” buyu hansı kurs bucağındadır?", ["45° sol bort", "90° sağ bort", "180° arxa", "0° ön"], "A"),
    (28, "28. Şəkildə gördüyünüz gəminin işıqlarının mənasını açıqlayın?", ["losman işlərini yerinə yetirən gəmi", "balıqçı gəmisi", "yedək gəmisi", "lövbərdə olan gəmi"], "A"),
    (29, "29. Gəminin “Top” işığının üfüqi görünmə sektoru neçə dərəcədir?", ["gəminin “deametral“ müstəvisindən sağ və sol bortlara tərəf gəminin arxa tərəfinə istiqamətində 112,5°", "360 dərəcə", "180 dərəcə", "90 dərəcə"], "A"),
    (30, "30. “RLS”-in ekranında (RLS nisbi hərəkət rejimindədir, sabitləşmə - “N”, məsafə rejimi – 6 mildir, bir məsafə halqası 1-mildir) bizim kurs 310°, sürətimiz 10 düy, hədəfin kursunu və sürətini aşağıda qeyd edilənlər seçin (hədəfin vektoru nisbidir, uzunluğu 6 dəqiqədir)?", ["hədəfin kursu 130°, sürəti 5 düyün", "hədəfin kursu 310°, sürəti 10 düyün", "hədəfin kursu 0°, sürəti 0 düyün", "hədəfin kursu 90°, sürəti 15 düyün"], "A"),
    (31, "31. Gəmi fiti ilə üç qısa səs siqnalı verilməlidir:", ["baş mühərrikə “arxaya hərəkət” komandası verilməmişdən öncə", "dumanlı havada", "limana girəndə", "sağa dönəndə"], "A"),
    (32, "32. Şəkildə göstərilən “RLS”–in ekranında 1 rəqəmi ilə işarə edilib:", ["head line / kurs xətti", "məsafə halqası", "pelenq xətti", "mərkəz nöqtəsi"], "A"),
    (33, "33. Radarın ekranında göstərilən 1 №-li hədəf hansı istiqamətdə hərəkət edir?", ["Şərqə", "Qərbə", "Şimalı", "Cənuba"], "A"),
    (34, "34. Şəkildə gördüyünüzün adını qeyd edin.", ["“Şpiqat”", "Klass", "Klyuz", "Bollard"], "A"),
    (35, "35. Siz 1 saylı gəmidəsiniz. Sizin gəminizin kursu hansı hərf ilə qeyd edilmişdir?", ["“A”", "“B”", "“C”", "“D”"], "A"),
    (36, "36. Şəkildə buludların hansı növü göstərilmişdir?", ["“Lələkli” (Ci)", "Topa buludlar", "Qat-qat buludlar", "Lələkli-topa buludlar"], "A"),
    (37, "37. Şəkildə göstərilən dor ağacında qaldırmış işarəyə görə gəmi haqqında məlumatı qeyd edin?", ["Gəmi balıq ovu ilə məşğuldur", "Gəmi batır", "Gəmi yelkənlə gedir", "Gəmi lövbərdədir"], "A"),
    (38, "38. Kapitanın növbə köməkçisi hansı halda öz vəzifələrin icrasından azad olmuş hesab edilir?", ["Kapitan gəminin idarə edilməsini qəbul etdiyi halda", "Hər 4 saatdan bir", "Gəmi lövbərə durduqda", "Liman müfəttişi gəldikdə"], "A"),
    (39, "39. Gəminiz 38,0 ° kurs üzrə 12,5 düyün sürətlə hərəkət edir. RLS-nın ekranında “pelenq”i və məsafəsi dəyişilməyən hədəf müşahidə edilir. Hədəf hansı kurs və sürətlə hərəkət edir?", ["Kurs 38,0 °, sürət 12,5 düyün", "Kurs 0°, sürət 0 düyün", "Kurs 180°, sürət 10 düyün", "Kurs 90°, sürət 15 düyün"], "A"),
    (40, "40. Gəmilərdə quraşdırılan qəza radiobuylarının yoxlamadan keçmə müddətini qeyd edin?", ["ildə bir dəfə", "hər 6 aydan bir", "hər ay", "hər 2 ildən bir"], "A"),
    (41, "41. Şəkildə gördüyünüz buyun hansı tərəfində naviqasiya təhlükəsi mövcuddur?", ["cənub tərəfdən", "şimal tərəfdən", "şərq tərəfdən", "qərb tərəfdən"], "A"),
    (42, "42. “GMDSS” sisteminə aid təcililik siqnalını qeyd edin?", ["“PANPAN”", "“MAYDAY”", "“SECURITE”", "“SILENCE”"], "A"),
    (43, "43. Şəkildə gördüyünüz buy necə adlandırılır?", ["xüsusi təyinatlı buy", "kardinal buy", "lateral buy", "təhlükəsiz su buyu"], "A"),
    (44, "44. Sektor üsulu ilə axtarış xilasetmə əməliyatlarında gəminin hər dəfə kursu neçə dərəcə dəyişməlidir?", ["120°", "90°", "60°", "180°"], "A"),
    (45, "45. Şəkildə gördüyünüz bayraq gəmidə nə zaman qaldırılır?", ["gəmiyə yardıma ehtiyac olanda", "gəmi limana girəndə", "gəmi lövbərdə olanda", "bayram günlərində"], "A"),
    (46, "46. Sükançıya verilən “Keep the buoy on starboard side” komandası nə deməkdir?", ["buyu sağda saxla", "buyu solda saxla", "buyun üstünə sür", "buyu kec"], "A")
]

new_questions_json = []

for q_num, text, opts, corr in pdf_questions_46:
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
    
    if q_num in img_coords:
        q_obj["image_url"] = f"/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_id/q_{q_num:03d}.jpeg"
        
    new_questions_json.append(q_obj)

data = {
    "certificate": "Gəmi sürücülərinin təkmilləşdirilməsi (idarəetmə)",
    "questions": new_questions_json
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Fully created {len(new_questions_json)} questions (Questions 1 to 46) and {len(img_coords)} extracted images for Gəmi sürücülərinin təkmilləşdirilməsi (idarəetmə)!")
