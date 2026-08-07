import fitz
import re
import json
import random

seed = 33320
random.seed(seed)

pdf_path = r'D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Kimyәvi maddә daşıyan tankerlәrdә yük әmәliyyatlarına dair geniş proqram üzrә hazırlıq.pdf'
json_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\kimy_vi_madd_da_yan_tankerl_rd_y_k_m_liy.json'

doc = fitz.open(pdf_path)
text = '\n'.join([page.get_text() for page in doc])

# Parse questions
# Pattern: number. question text \n Düzgün cavab: answer
# But sometimes there are options 1. 2. 3. between question and Düzgün cavab
pattern = re.compile(r'(\d+)\.\s+(.*?)\s+Düzgün cavab:\s+(.*?)(?=\n\d+\.|$)', re.DOTALL)
matches = pattern.findall(text)

print(f"Found {len(matches)} questions.")

distractors_pool = [
    "IBC Məcəlləsinin 15-ci fəslinin tələblərinə əsasən",
    "Yük tanklarının yuyulma təlimatına uyğun olaraq",
    "P&A (Prosedur və Təşkiletmə) Təlimat kitabçasına əsasən",
    "MARPOL Əlavə II tələblərinə riayət etməklə",
    "Kimyəvi yüklərin bir-birinə uyğunluğu cədvəlinə əsasən",
    "IGC Məcəlləsinə uyğun olaraq",
    "Yük sisteminin hidravlik sınaqdan keçirilməsi",
    "Tankın inert qazla təchiz olunması",
    "Deqazasiya əməliyyatı zamanı oksigenin yoxlanılması",
    "Tankın içərisindəki atmosferin zəhərlilik dərəcəsi",
    "Gəminin təhlükəsizlik idarəetmə sisteminə (SMS) əsasən",
    "Xüsusi kimyəvi geyim və qoruyucu vasitələrdən istifadə",
    "Qapalı məkana giriş proseduruna əsasən",
    "Yükləmə-boşaltma planının (Cargo Plan) təsdiqi",
    "Nasosların nominal işçi təzyiqi",
    "Buxar qayıtma sisteminin (Vapor Return System) işə salınması",
    "Gəmi-Sahil təhlükəsizlik yoxlama vərəqəsi (Ship/Shore Safety Checklist)",
    "Tankların ventilyasiya rejimi",
    "Zəhərli maye maddələrin (NLS) kateqoriyaları",
    "Antistatik tədbirlərin görülməsi",
    "Sərbəst səth effektinin (Free Surface Effect) nəzərə alınması",
    "Kofurdamların və ballast tanklarının yoxlanılması",
    "Tank yuma sularının (Slop) təhvil verilməsi qaydası",
    "Fövqəladə hallarda müdaxilə planı (SOPEP/SMPEP)",
    "Dəniz mühitinin çirklənməsinin qarşısının alınması"
]

questions = []

for idx, match in enumerate(matches):
    q_num = match[0]
    q_text = match[1].strip().replace('\n', ' ')
    # clean up extra spaces
    q_text = re.sub(r'\s+', ' ', q_text)
    correct = match[2].strip().replace('\n', ' ')
    correct = re.sub(r'\s+', ' ', correct)
    
    question_full = f"{q_num}. {q_text}"
    
    # get 3 unique distractors
    distractors = random.sample(distractors_pool, 3)
    while correct in distractors:
         distractors = random.sample(distractors_pool, 3)
         
    options_list = distractors + [correct]
    random.shuffle(options_list)
    
    opts = {
        "A": options_list[0],
        "B": options_list[1],
        "C": options_list[2],
        "D": options_list[3]
    }
    
    # find correct letter
    correct_letter = "A"
    for k, v in opts.items():
        if v == correct:
            correct_letter = k
            break
            
    q_obj = {
        "id": f"q{int(q_num):03d}",
        "question": question_full,
        "options": opts,
        "correct_answer": correct_letter,
        "explanation": ""
    }
    questions.append(q_obj)

output_json = {
    "certificate": "Kimyәvi maddә daşıyan tankerlәrdә yük әmәliyyatlarına dair geniş proqram üzrә hazırlıq",
    "questions": questions
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output_json, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(questions)} questions and saved to JSON.")
