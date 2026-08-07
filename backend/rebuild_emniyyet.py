import json
import random
import re

text_path = r"D:\Dənizçilik_İmtahanları\backend\pdf_debug_emniyyet.txt"
json_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_mniyy_tliyi_zr_m_sul_xs.json"
seed_value = 33309
random.seed(seed_value)

isps_distractors_pool = [
    "ISPS Məcəlləsinə əsasən gəminin mühafizə planının yenilənməsi və yoxlanılması",
    "Gəmiyə giriş-çıxış nəzarətinin gücləndirilməsi və mühafizə səviyyəsi 2-nin tətbiqi",
    "Gəmi mühafizə həyəcanı sisteminin (SSAS) aktivləşdirilməsi və sınaqdan keçirilməsi",
    "Baqajların, yüklərin və gəmi ehtiyatlarının rentgen cihazı ilə yoxlanılması",
    "Gəminin qadağan olunmuş zonalarına (restricted areas) buraxılış rejiminin təmin edilməsi",
    "Mühafizə səviyyəsi 3 elan edildikdə liman rəhbərliyi ilə əlaqənin yaradılması",
    "Kontrabanda, silah və partlayıcı maddələrin axtarışının aparılması",
    "Gəminin mühafizə bəyannaməsinin (DoS) doldurulması və imzalanması",
    "Liman vasitələrinin mühafizə zabiti (PFSO) ilə koordinasiya",
    "Gəmi mühafizə təlimlərinin və məşqlərinin müntəzəm olaraq keçirilməsi",
    "Şübhəli şəxslərin müəyyən edilməsi və axtarış prosedurlarının tətbiqi",
    "Gəmiyə gələn ziyarətçilərin şəxsiyyət vəsiqələrinin qeydiyyata alınması",
    "Gəminin ətrafında və göyərtəsində patrul xidmətinin təşkil olunması",
    "Mühafizə avadanlıqlarının texniki xidməti və kalibrlənməsi",
    "Gəminin mühafizə qeydlərinin (security records) aparılması",
    "Dəniz quldurluğuna və silahlı hücumlara qarşı müdafiə tədbirləri",
    "Mühafizə səviyyəsi 1-də minimum təhlükəsizlik tədbirlərinin icrası",
    "Yük əməliyyatları zamanı kənar şəxslərin gəmiyə daxil olmasının qarşısının alınması",
    "Gəmi heyətinin mühafizə ilə bağlı vəzifələrinin bölüşdürülməsi",
    "Gəminin xarici işıqlandırmasının və nəzarət kameralarının yoxlanılması",
    "Mühafizə təhdidləri barədə bayraq dövlətinə hesabat verilməsi",
    "ISPS Məcəlləsinin tələblərinə uyğun olaraq daxili auditi həyata keçirmək",
    "Gəminin fiziki mühafizə sədlərinin möhkəmləndirilməsi",
    "Xidməti itlərin köməyi ilə narkotik və partlayıcı maddə axtarışı",
    "Liman ərazisindəki qeyri-qanuni fəaliyyətlərin monitorinqi",
    "Gəmi təhlükəsizlik zabitinin (SSO) liman yoxlamalarında iştirakı",
    "Mühafizə xidməti əməkdaşları ilə əlaqəli təlimlərin təşkili",
    "Gəminin yük manifestlərinin mühafizə baxımından təhlili",
    "Gəmiyə gətirilən poçt və bağlamaların xüsusi yoxlamadan keçirilməsi",
    "Kibertəhlükəsizlik və gəmi şəbəkələrinin kənar müdaxilədən qorunması"
]

with open(text_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

questions = []
current_q_text = ""
current_answer = ""
expected_q_num = 1
in_question = False
in_answer = False

for line in lines:
    line = line.strip()
    if not line:
        continue
    
    if line.startswith(f"{expected_q_num}.") and (in_answer or expected_q_num == 1):
        if expected_q_num > 1:
            questions.append({
                "id": f"q{expected_q_num-1:03d}",
                "q_text": current_q_text.strip(),
                "ans_text": current_answer.strip()
            })
            current_q_text = ""
            current_answer = ""
            
        current_q_text = line + "\n"
        in_question = True
        in_answer = False
        expected_q_num += 1
    elif line.startswith("Düzgün cavab:"):
        current_answer = line.replace("Düzgün cavab:", "").strip()
        in_question = False
        in_answer = True
    else:
        if in_question:
            current_q_text += line + "\n"
        elif in_answer:
            current_answer += " " + line

if expected_q_num > 1:
    questions.append({
        "id": f"q{expected_q_num-1:03d}",
        "q_text": current_q_text.strip(),
        "ans_text": current_answer.strip()
    })

out_questions = []
for idx, q in enumerate(questions):
    q_text = q['q_text']
    distractors = random.sample(isps_distractors_pool, 3)
    options_list = [q['ans_text']] + distractors
    random.shuffle(options_list)
    
    options_dict = {
        "A": options_list[0],
        "B": options_list[1],
        "C": options_list[2],
        "D": options_list[3]
    }
    
    correct_key = "A"
    for k, v in options_dict.items():
        if v == q['ans_text']:
            correct_key = k
            break
            
    out_questions.append({
        "id": q['id'],
        "question": q_text,
        "options": options_dict,
        "correct_answer": correct_key,
        "explanation": ""
    })

final_data = {
    "certificate": "Gəmi əmniyyətliyi üzrə Məsul Şəxs",
    "questions": out_questions
}

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False, indent=4)

print(f"Generated {len(out_questions)} questions in {json_path}")
