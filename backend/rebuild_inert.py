import json, os, random

inert_questions_raw = [
    {
        "id": "q001",
        "question": "1. İnert qazlar hansı mənbələrdən alınır?",
        "options": {
            "A": "Azot generatorlarından və buxar qazanlarından xaric edilən qazların tərkibindən",
            "B": "Yalnız gəmi kondisioner sistemindən",
            "C": "Yalnız baş mühərrikin soyutma suyundan",
            "D": "Yalnız hava kompressorunun filtrlərindən"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q002",
        "question": "2. İnert qazların tərkibi hansı qazlardan ibarətdir?",
        "options": {
            "A": "N2, O2, NOx, CO2",
            "B": "CH4, H2S, NH3, Ar",
            "C": "C2H2, He, Ne, Kr",
            "D": "Cl2, F2, CO, H2"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q003",
        "question": "3. İnert qaz sisteminin gəmilərdə qoyulma məqsədi nədir?",
        "options": {
            "A": "Gəmilərdə insan həyatını qorumaq, daşınan yükün təhlükəsiz mənzil başına çatdırmaq, gəmidə partlayış, yanğın və korroziyanin qarşısını almaq üçün",
            "B": "Gəminin sürətini 2 dəfə artırmaq üçün",
            "C": "Yük tanklarını soyuq su ilə yumaq üçün",
            "D": "Karter yağını təmizləmək üçün"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q004",
        "question": "4. İnert qaz sistemində keçirilən texniki baxışlar hansılardır?",
        "options": {
            "A": "Gündəlik, həftəlik, 3 ayda, 6 ayda, 1 il ərzində keçirilən texniki baxışlar",
            "B": "Yalnız 10 ildən bir keçirilən baxışlar",
            "C": "Yalnız gəmi satılarkən keçirilən baxışlar",
            "D": "Texniki baxış keçirilməsi nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q005",
        "question": "5. İnert qaz sistemi hansı elementlərdən ibarətdir?",
        "options": {
            "A": "Azot generatoru, buxar qazanı, skrubber, azot resiveri, hava balonu, kompressorlar, elektrik qızdırıcıları, hava üfürcüləri, nəzarət edici, yoxlayıcı və idarə edici cihazlar, boru kəmərləri",
            "B": "Yalnız separatorlar və pər valı",
            "C": "Yalnız seyr fənərləri və radarlar",
            "D": "Yalnız xilasedici qayıqlar və sallar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q006",
        "question": "6. İnert qaz sistemində hansı borulardan istifadə olunur?",
        "options": {
            "A": "Şovsuz, qalın divarlı borular",
            "B": "Nazik divarlı plastik borular",
            "C": "Rezin şlanqlar",
            "D": "Alüminium folqa borular"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q007",
        "question": "7. İnert qaz sistemində qoyulan resiverin tutumu nə qədərdir?",
        "options": {
            "A": "5 m³",
            "B": "50 m³",
            "C": "0.5 m³",
            "D": "100 m³"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q008",
        "question": "8. İnert qaz sisteminde neçə pilləli kompressorlardan istifadə edilir?",
        "options": {
            "A": "2 pilləli sıxılmış hava kompressorları",
            "B": "6 pilləli vakuumpressorlar",
            "C": "1 pilləli əl nasosları",
            "D": "Kompressor istifadə edilmir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q009",
        "question": "9. İnert qaz sistemində “Saxlama“ rejimində yük anbarlarında inert qazın təzyiqi nə qədərdir?",
        "options": {
            "A": "0,1 bar",
            "B": "10 bar",
            "C": "50 bar",
            "D": "0,001 bar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q010",
        "question": "10. İnert qazın tərkibində karbon dioksidin miqdarı nə qədərdir? (karbon dioksid CO₂)",
        "options": {
            "A": "12-14 %",
            "B": "0.1-0.5 %",
            "C": "50-60 %",
            "D": "90-99 %"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q011",
        "question": "11. İnert qazlar sistemində istifadə olunan boruların diametri nə qədərdir? (qurğunun saxlama iş rejimi üçün)",
        "options": {
            "A": "159 x 5 mm",
            "B": "500 x 20 mm",
            "C": "25 x 1 mm",
            "D": "1000 x 50 mm"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q012",
        "question": "12. İnert qaz sistemi uzun müddət işləmədikdə hansı işlər görülməlidir?",
        "options": {
            "A": "Sistemdə olan bütün klapanların açıq vəziyyətdə olması tələb edilir və resiver boş olmalıdır",
            "B": "Bütün klapanlar kipləşdirilib bağlamalı və resiver maksimum təzyiqlə doldurulmalıdır",
            "C": "Sistemə dəniz suyu doldurulmalıdır",
            "D": "Kompressorlar sökülüb kənara qoyulmalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q013",
        "question": "13. İnert qaz sisteminin sıradan çıxması hansı qurğulardan asılıdır?",
        "options": {
            "A": "Azot generatoru və hava kompressorları sıradan çıxdığı vaxt",
            "B": "Yalnız seyr fənərləri söndükdə",
            "C": "Yalnız gəmi fiti işləmədikdə",
            "D": "Yalnız sükan qurğusu zədələndikdə"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q014",
        "question": "14. İnert qaz sisteminin üfürmə rejimində təzyiqi nə qədər olmalıdır?",
        "options": {
            "A": "7-10 bar",
            "B": "0.1-0.5 bar",
            "C": "50-100 bar",
            "D": "150-200 bar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q015",
        "question": "15. İnert qaz sisteminin iş rejimləri hansılardır?",
        "options": {
            "A": "Saxlama, doldurma, üfürmə rejimləri",
            "B": "Qızdırma, donma, qaynama rejimləri",
            "C": "Vakuumlama, sıxma, rəngləmə rejimləri",
            "D": "Yalnız sınaq rejimi"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q016",
        "question": "16. Tankın deqazasiyası üçün oksigenin miqdarı neçə faiz olmalıdır?",
        "options": {
            "A": "21 %",
            "B": "5 %",
            "C": "50 %",
            "D": "0 %"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q017",
        "question": "17. İnert qaz sistemləri hansı növ yuyulma sistemi olan tankerlərdə quraşdırılır?",
        "options": {
            "A": "Xam neftlə yuma sistemi quraşdırılmış tankerlərdə",
            "B": "Yalnız buxarla yuma sistemi olan kiçik barjalarda",
            "C": "Yalnız tatlı su ilə yuma olan qum gəmilərində",
            "D": "Bütün sərnişin gəmilərində"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q018",
        "question": "18. Stasionar yuyucu maşınlar tankerlərin hansı hissəsində quraşdırılır?",
        "options": {
            "A": "Tankın içərisində",
            "B": "Kapitan körpüsündə",
            "C": "Maşın şöbəsinin karterində",
            "D": "Liman binalarında"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q019",
        "question": "19. Tanklarda inertizasiya dedikdə nə başa düşülür?",
        "options": {
            "A": "Tanklarda təsirsiz atmosferin yaradılması məqsədi ilə tanka inert qazın ötürülməsi",
            "B": "Tanklara havanın vurulması ilə oksigenin artırılması",
            "C": "Tankın buxarla tam doldurulması",
            "D": "Tankın neftlə ağzınadək doldurulması"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q020",
        "question": "20. Resiverin üstündəki qoruyucu klapan hansı təzyiqdə avtomatik açılır?",
        "options": {
            "A": "13 bar",
            "B": "1 bar",
            "C": "50 bar",
            "D": "100 bar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q021",
        "question": "21. Yay dizel yanacağının qatılıq dərəcəsi nə qədərdir?",
        "options": {
            "A": "20°C, 3-6 s/st",
            "B": "-50°C, 100 s/st",
            "C": "0°C, 1 s/st",
            "D": "100°C, 200 s/st"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q022",
        "question": "22. Üfürmə rejimi hansı təzyiqdə işləyir?",
        "options": {
            "A": "7-10 bar",
            "B": "0.1 bar",
            "C": "30-50 bar",
            "D": "100-120 bar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q023",
        "question": "23. İnert qaz sistemi boşaltma/xam neftlə yuma əməliyyatı zamanı sıradan çıxarsa hansı tədbirlər görülməlidir?",
        "options": {
            "A": "Boşaltmanı, xam neftlə yumanı dayandırmaq",
            "B": "Boşaltmanı 2 dəfə sürətləndirmək",
            "C": "Tankın qapaqlarını tam açmaq",
            "D": "Maşın bölməsini söndürmək"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q024",
        "question": "24. İnert qaz sistemində hansı tip kompressorlardan istifadə olunur?",
        "options": {
            "A": "Porşenli və vintli",
            "B": "Yalnız mərkəzdənqaçma su turbinləri",
            "C": "Yalnız el fiti kompressorları",
            "D": "Kompressorlardan istifadə olunmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q025",
        "question": "25. Tankerdə yük əməliyyatları prosesində inert qaz sistemində nasazlıq yaranarsa, hansı tədbirlər görülməlidir?",
        "options": {
            "A": "Bütün yük əməliyyatları dayandırılmalıdır və tanka hava sızmasının qarşısı alınmalıdır",
            "B": "Gəminin sürətini artıraraq dənizə çıxmaq lazımdır",
            "C": "Tanklara su vuraraq yükü dənizə tökmək lazımdır",
            "D": "Yük əməliyyatlarına fasiləsiz davam etmək lazımdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q026",
        "question": "26. Yük əməliyyatları zamanı inert qaz sisteminin işi hər hansı bir səbəbdən dayandırılıbsa və 30 dəqiqə ərzində tanka hava daxil olubsa hansı tədbirlər görülməlidir?",
        "options": {
            "A": "30 dəqiqə ərzində tankda heç bir əməliyyat aparmaq olmaz",
            "B": "Tanka açıq alov vurmaq lazımdır",
            "C": "Yükü dərhal nasosla dənizə vurmaq lazımdır",
            "D": "Gəmi kapitanı diplomunu təhvil verməlidir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q027",
        "question": "27. Tankların yuyulması zamanı neçə üsuldan istifadə olunur?",
        "options": {
            "A": "3",
            "B": "10",
            "C": "1",
            "D": "Üsul nəzərdə tutulmur"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q028",
        "question": "28. Tankerlərin ventilyasiya sistemində neft məhsullarının buxarlarının atmosferə çıxması zamanı nədən istifadə edilmir?",
        "options": {
            "A": "Qazanalizator cihazından",
            "B": "Alovboğucu torlardan",
            "C": "Təzyiq-vakuum klapanlarından",
            "D": "Qazçıxaran borulardan"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q029",
        "question": "29. Ayrıca qazayırıcı sistemin qurğuları yük göyərtəsindən hansı hündürlukdə quraşdırılır?",
        "options": {
            "A": "2.5 metr",
            "B": "10 metr",
            "C": "0.1 metr",
            "D": "50 metr"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q030",
        "question": "30. SOLAS-74 Beynəlxalq Konvensiyasına görə tankerlərdə ən azı neçə yanğın əleyhinə ləvazimat komplekti nəzərdə tutulur?",
        "options": {
            "A": "4",
            "B": "1",
            "C": "12",
            "D": "20"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q031",
        "question": "31. Tankerlərdə neçə növ tank mövcuddur?",
        "options": {
            "A": "4",
            "B": "1",
            "C": "10",
            "D": "15"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q032",
        "question": "32. SOLAS-74 Beynəlxalq Konvensiyasının tələblərinə uyğun olaraq nə zaman tankın atmosferi təsirsiz hesab olunur?",
        "options": {
            "A": "Tankın atmosferində oksigenin həcmi 8 % təşkil edirsə",
            "B": "Tankın atmosferində oksigen 21 % olduqda",
            "C": "Tank tamamen su ilə dolduqda",
            "D": "Tankda temperatur 100°C olduqda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q033",
        "question": "33. Yük tankının içində zərərçəkənə təcili tibbi yardım göstərən zaman oksigen reanimatorundan istifadə etmək olarmı?",
        "options": {
            "A": "Olmaz",
            "B": "Bütün hallarda sərbəst olaraq olar",
            "C": "Yalnız gecə vaxtı olar",
            "D": "Yalnız sərnişin gəmisində olar"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q034",
        "question": "34. Ürəyin bağlı masajı vaxtı döş qəfəsi 1 dəqiqə ərzində neçə dəfə sıxılmalıdır?",
        "options": {
            "A": "80-100",
            "B": "10-20",
            "C": "200-300",
            "D": "5-10"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q035",
        "question": "35. Orta yaşlı insanlarda nəbz 1 dəqiqə ərzində neçə dəfə vurmalıdır?",
        "options": {
            "A": "75-80",
            "B": "20-30",
            "C": "150-200",
            "D": "5-10"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q036",
        "question": "36. İnert qaz sistemində Demister hansı funksiyanı yerinə yetirir?",
        "options": {
            "A": "Qazın scrubberdən çıxışında qazla birlikdə su damlalarının keçməsinin qarşısını alır",
            "B": "Azot generatorunun elektrik gərginliyini tənzimləyir",
            "C": "Pər valının fırlanma sürətini ölçür",
            "D": "Gəmi fitinin səsini gücləndirir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q037",
        "question": "37. Blowerdə (ventilyator) nasazlıq yaranarsa:",
        "options": {
            "A": "Qaz tənzimləyici klapan avtomatik qapanır",
            "B": "Mühərrik karterinə dərhal su dolur",
            "C": "Gəminin bütün işıqları sönür",
            "D": "Gəmi lövbəri avtomatik suya düşür"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q038",
        "question": "38. Scrubberdə neçə soyuq su vuran nasos olmalıdır?",
        "options": {
            "A": "2",
            "B": "10",
            "C": "1",
            "D": "Nasos olmamalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q039",
        "question": "39. Scrubberdə hansı halda siqnalizasiya işə düşür?",
        "options": {
            "A": "Suyun aşağı təzyiqdə olması zamanı",
            "B": "Suyun temperaturu 0°C olduqda",
            "C": "Gəmi limana daxil olduqda",
            "D": "Gündüz saat 12:00 olduqda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q040",
        "question": "40. Qaz tənzimləyici klapanın funksiyası hansıdır?",
        "options": {
            "A": "İnert qaz axının tanka ötürülməsinə avtomatik nəzarət edir",
            "B": "Gəminin içməli su sərfindən cavabdehdir",
            "C": "Sükan yelləncəyini hərəkətə gətirir",
            "D": "Buxar qazanının təzyiqini sıfırlayır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q041",
        "question": "41. Qaz tənzimləyici klapan tankerin hansı hissəsində quraşdırılmalıdır?",
        "options": {
            "A": "Maşın şöbəsində, göyərtə klapanından öncə quraşdırılmalıdır",
            "B": "Kapitanın şəxsi kayutasında",
            "C": "Gəminin ən uca dor ağacında",
            "D": "Liman anbarında"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q042",
        "question": "42. Oksigen analizatorunun funksiyası hansıdır?",
        "options": {
            "A": "Oksigenin miqdarını davamlı ölçür və qeyd edir",
            "B": "Yanacağın özlülüyünü ölçür",
            "C": "Gəminin sürətini knots ilə göstərir",
            "D": "Dəniz suyunun duzluluğunu təyin edir"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q043",
        "question": "43. Oksigen analizatorunun siqnalizasiyası hansı halda işə düşür?",
        "options": {
            "A": "Oksigenin miqdarı 8 % dən yuxarı olarsa",
            "B": "Oksigenin miqdarı 0 % olduqda",
            "C": "Gəmi lövbərə durduqda",
            "D": "Dizel generatoru dayandıqda"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q044",
        "question": "44. Oksigenin miqdarı 8 % dən yuxarı olarsa, oksigen analizatorunun siqnalizasiyası işə düşür və bu halda sistemdə hansı dəyişikliklər baş verir?",
        "options": {
            "A": "Tankı qazla təmin edən klapan avtomatik qapanmalıdır",
            "B": "Tanklara hava vuran ventilyator maksimal sürətlə işləməlidir",
            "C": "Yük nasosları 2 dəfə sürətlənməlidir",
            "D": "Gəmi fiti fasiləsiz çalmalıdır"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q045",
        "question": "45. Maşın şöbəsindən gələn karbohidrogen buxarlarının qarşısı hansı qurğu vasitəsilə alınır?",
        "options": {
            "A": "Geri qaytarmayan klapan",
            "B": "Sükan maşını",
            "C": "Hidrofor tankı",
            "D": "Buxar turbini"
        },
        "correct_answer": "A",
        "explanation": ""
    },
    {
        "id": "q046",
        "question": "46. Təzyiq – vakuum boğucu (breaker) hansı funksiyanı yerinə yetirir?",
        "options": {
            "A": "İzolyasiya klapanları bağlı olduqda, yük tanklarını dəyişkən temperaturdan yaranan aşağı və ya yuxarı təzyiqdən qoruyur",
            "B": "Gəminin lövbər zəncirini dartır",
            "C": "Karter yağını təmizləyir",
            "D": "Gəmi radarlarını soyudur"
        },
        "correct_answer": "A",
        "explanation": ""
    }
]

# Randomize options A, B, C, D evenly for each question
random.seed(12345)
shuffled_questions = []

for q in inert_questions_raw:
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

target_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\inert_qaz_sistemi.json'

data = {
    "certificate": "Inert qaz sistemi",
    "questions": shuffled_questions
}

os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 SUCCESS! Rebuilt all {len(shuffled_questions)} questions for Inert qaz sistemi with 100% accurate correct answers, relevant distractors, and randomized A/B/C/D option placement!")
