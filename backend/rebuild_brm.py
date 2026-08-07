import json
import random

seed = 33314
random.seed(seed)

distractors = [
    ["Mən yalnız şifrəli dənizçi cədvəlindən istifadə edəcəyəm", "Mən beynəlxalq dəniz bayraqlarını istifadə edəcəyəm", "Mən fərdi şirkət sözlüyündən istifadə edəcəyəm"],
    ["Sizin sürətiniz nə qədərdir?", "Siz hansı limana gedirsiniz?", "Sizin yükünüzün növü nədir?"],
    ["Hədəf tamamilə təhlükəsizdir, manevrə ehtiyac yoxdur", "Gəmi sürətini dərhal artırmalıdır", "Hədəfin dreyf etdiyi ehtimal olunur"],
    ["HP = 150.00", "HP = 270.00", "HP = 180.00"],
    ["HP = 185.00", "HP = 85.00", "HP = 355.00"],
    ["Dəniz mühitinin mühafizəsi məcəlləsində", "Gəmi jurnalı təlimatlarında", "Dənizdə Toqquşmaların Qarşısının Alınması Qaydalarında"],
    ["2", "3", "5"],
    ["00 – 3600 sağ bortdan", "00 – 900 sağ və sol bortdan", "00 – 2700 saat əqrəbi istiqamətində"],
    ["Ümumgəmiyə (naviqasiya) və maşın bölməsinə yalnız kapitan rəhbərlik edir", "Naviqasiyaya və maşına növbətçi matros rəhbərlik edir", "Bütün gəmi xidmətlərinə yalnız baş köməkçi rəhbərlik edir"],
    ["Yalnız dənizdə hərəkət növbəçəkməsi", "Yalnız limanda dayanacaq növbəçəkməsi", "Yük əməliyyatları və təmir növbəçəkməsi"],
    ["Mən kursumu sağ tərəfə dəyişirəm", "Mən sürətimi azaldıram", "Mən maşını dayandırıram"],
    ["HP = 345.00", "HP = 15.00", "HP = 255.00"],
    ["Gəmi kapitanının sərəncamlar jurnalı ilə", "Maşın jurnalının qeydləri ilə", "Manevr elementləri cədvəli ilə"],
    ["Növbəni qəbul edən köməkçi dəniz paltarında olmadıqda", "Növbəni qəbul edən köməkçinin dəniz rütbəsi aşağı olduqda", "Növbə dəyişməsi vaxtından 5 dəqiqə gecikdikdə"],
    ["HP = 195.00", "HP = 157.00", "HP = 171.00"],
    ["Körpücükdə hava temperaturunu yoxlamaq üçün", "Küləyin gücünü və dreyfi təyin etmək üçün", "Gəminin sürətini hesablamaq üçün"],
    ["KB = 1000 sağ bort", "KB = 800 sol bort", "KB = 800 sağ bort"],
    ["Kompaniyanın daxili reqlament sənədlərində yazılır", "Beynəlxalq dəniz hüququ nizamnaməsində göstərilir", "Maşın jurnalında qeyd olunur"],
    ["KB = 1810 sol bort", "KB = 1950 sağ bort", "KB = 1710 sol bort"],
    ["Gəminin sürətindən və dreyfdən", "Küləyin istiqamətindən və gücündən", "Kompensator maqnitlərinin yaşından"],
    ["Görünüş şərtlərini və hava vəziyyətini", "Hərəkət intensivliyini və naviqasiya təhlükələrini", "Gəminin texniki vəziyyətini və avadanlıqlarını"],
    ["Hər dəfə limana daxil olduqda", "Yalnız fırtınalı havadan sonra", "Gəmi ekvatoru keçdikdə"],
    ["200-dən az, 1200-dən çox", "450-dən az, 900-dən çox", "600-dən az, 1800-dən çox"],
    ["30 dəqiqə", "1 saat", "24 saat"],
    ["24 saat", "48 saat", "6 saat"],
    ["100", "200", "350"],
    ["5 mildən az", "3 mildən az", "2 mildən az"],
    ["Mənim gəmim lövbərdə dayanmışdır", "Mənim gəmim saya oturmuşdur", "Mənim gəmim manevr edə bilmir, amma maşın işləyir"],
    ["Mən kursumu sol tərəfə dəyişəcəyəm", "Mən sürəti azaldacağam", "Mən arxaya hərəkət edəcəyəm"],
    ["Havanın temperaturundan və rütubətdən", "Gəminin sürətindən və yükləməsindən", "Bələdçinin peşəkarlığından"],
    ["Gəmilər bu rayona daxil olub lövbər sala bilər", "Gəmilər yalnız gündüz vaxtı burdan keçə bilər", "Gəmilər bu rayonda sürəti azaltmalıdır"],
    ["e=10 metr", "e=15 metr", "e=2 metr"],
    ["Gəmi şirkətinin dəniz təhlükəsizliyi müfəttişi", "Liman kapitanlığı ofisi", "Gəmi həkimi və bosman"],
    ["Mənim sağ tərəfimdən keçməyin", "Mənim gəmimə 1 mildən çox yaxınlaşmayın", "Mənim qarşımdan keçməyin"],
    ["Yalnız gündüz vaxtı", "Yalnız hərəkət zamanı, dayanacaqda yox", "Gündüz saat 08:00-dan 20:00-a qədər"],
    ["KB = 80.00 sol bort", "KB = 94.00 sağ bort", "KB = 268.00 sol bort"],
    ["Gəmi kapitanı", "Liman idarəsi", "Sahil mühafizə xidməti"],
    ["Hava şəraiti çox yaxşı olduqda", "Avtopilot tam işlək vəziyyətdə olduqda", "Xəritədə mövqe qeyd edildikdən sonra qısa müddətə"],
    ["Hər 3 gündən bir", "Yalnız limana yaxınlaşarkən", "Reys başlamazdan əvvəl bir dəfə"],
    ["Növbəni təhvil verdikdən sonra", "Yalnız xüsusi təhlükəli zonalarda", "Həftədə bir dəfə ümumi iclasda"],
    ["Bir obyektin məsafəsi və pelenqi ilə", "Obyektin kölgəsinin uzunluğu ilə", "Təqribi vizual hesablama ilə"],
    ["Yalnız mühərriklər tam arxaya işə salınır", "Gəmi heyəti dərhal gəmini tərk edir", "Bütün anbarlardakı su dərhal dənizə atılır"],
    ["Yalnız sürəti artırıb təhlükəli zonadan tez çıxır", "Körpüdəki bütün işıqları yandırır ki, kənardan görünsün", "Sadəcə avtopilotu söndürüb əllə idarəetməyə keçir"],
    ["Etməməlidir, radar enerjiyə qənaət üçün söndürülməlidir", "Yalnız gecə vaxtı istifadə etməlidir", "Yalnız kapitan icazə verdikdə istifadə etməlidir"],
    ["Təmir edilə bilən və edilə bilməyən qəzalar", "Ağır və yüngül texniki nasazlıqlar", "Şəxsi heyətin qəzası və yükün zədələnməsi"],
    ["Bəli, tam azad edir, çünki kapitan ali rəhbərdir", "Xeyr, ancaq hava şəraiti pis olduqda azad edir", "Yalnız kapitan öz köməkçisinə yazılı icazə verdikdə azad edir"],
    ["Etməməlidir, yalnız kapitanın birbaşa göstərişi ilə olar", "Yalnız baş köməkçi kapitan körpüsündə olduqda", "Sadəcə fövqəladə siqnal chalındıqda edə bilər"]
]

with open('pdf_debug_brm.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

questions_parsed = []
q_id = 1
current_q = ''
current_a = ''
in_q = False
in_a = False

for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith(str(q_id) + '.') or (q_id > 9 and line.startswith(str(q_id) + ' .')): 
        if current_q:
            questions_parsed.append({'q': current_q.strip(), 'a': current_a.strip()})
        current_q = line
        current_a = ''
        in_q = True
        in_a = False
        q_id += 1
    elif line.startswith('Düzgün cavab:'):
        current_a = line.replace('Düzgün cavab:', '').strip()
        in_a = True
        in_q = False
    elif in_q:
        current_q += ' ' + line
    elif in_a:
        current_a += ' ' + line
if current_q:
    questions_parsed.append({'q': current_q.strip(), 'a': current_a.strip()})

output_questions = []
for i, parsed in enumerate(questions_parsed):
    correct = parsed['a']
    wrong_options = distractors[i]
    
    all_opts = [correct] + wrong_options
    random.shuffle(all_opts)
    
    opts_dict = {}
    correct_letter = ''
    letters = ['A', 'B', 'C', 'D']
    for idx, opt in enumerate(all_opts):
        opts_dict[letters[idx]] = opt
        if opt == correct:
            correct_letter = letters[idx]
            
    q_dict = {
        "id": f"q{i+1:03d}",
        "question": parsed['q'],
        "options": opts_dict,
        "correct_answer": correct_letter,
        "explanation": ""
    }
    output_questions.append(q_dict)

final_data = {
    "certificate": "Kapitan Körpüsü Resurslarının İdarə Olunması",
    "questions": output_questions
}

target_file = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\kapitan_k_rp_s_resurslar_n_n_i_dar_olunm.json'

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print('Success')
