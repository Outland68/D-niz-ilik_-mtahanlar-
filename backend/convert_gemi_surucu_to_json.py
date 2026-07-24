# -*- coding: utf-8 -*-
import fitz # PyMuPDF
import re
import json
import random
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings
from api.models import Certificate, Category

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf"
doc = fitz.open(pdf_path)

full_text = ""
for page in doc:
    full_text += "\n" + page.get_text()

# Split by question number pattern: e.g. "1. ", "2. ", ...
raw_blocks = re.split(r'\n(?=\d+[\.\)]\s*)', full_text)

raw_questions = []

for block in raw_blocks:
    block = block.strip()
    if not block:
        continue
    
    m = re.match(r'^(\d+)[\.\)]\s*(.*?)\s*Düzgün cavab:\s*(.*)', block, re.DOTALL)
    if m:
        q_num = int(m.group(1))
        q_text = re.sub(r'\s+', ' ', m.group(2)).strip()
        c_ans = re.sub(r'\s+', ' ', m.group(3)).strip()
        raw_questions.append({
            "num": q_num,
            "question": q_text,
            "correct": c_ans
        })

print(f"Total raw questions extracted: {len(raw_questions)}")

# Pool of realistic distractor answers for maritime navigation/operational questions
distractors_pool = [
    "şimal - şərq istiqamətində",
    "bütün cavablar doğrudur",
    "yalnız kapitanın yazılı sərəncamı ilə",
    "yalnız gəmi qovşağında təlim keçirildikdə",
    "bütün naviqasiya zolaqlarında",
    "artır",
    "dəyişməz qalır",
    "sıfıra bərabər olur",
    "cüt",
    "xüsusi nişanlanmış",
    "təxirəsalınmaz tibbi yardım",
    "gəminin təhlükəsiz sürəti",
    "10 metr",
    "15 metr",
    "2 metr",
    "çox mərkəzli (üç mərkəzli)",
    "tropik siklon",
    "mərkəzsiz cəbhə",
    "axtarış və xilasetmə zonası",
    "mərasim trapı və fırtına nərdivanı",
    "yalnız matros heyəti üçün vasitələr",
    "qırmızı rəngli böyük X hərfi ilə",
    "sarı rəngli S hərfi ilə",
    "mavi rəngli R hərfi ilə",
    "75,2 mil",
    "58,4 mil",
    "64,0 mil",
    "SEELONCE MAYDAY",
    "MAYDAY RELAY",
    "DISTRESS ACKNOWLEDGE",
    "3, 1, 2, 4",
    "2, 1, 4, 3",
    "4, 3, 2, 1",
    "yalnız kapitan köməkçisi",
    "baş mexanik",
    "növbətçi matros",
    "bütün cavablar yanlışdır",
    "gəminin taran edilməsi",
    "radio dəniz naviqasiya fənəri",
    "gəmi marşrutu sahəsi",
    "dəniz dalğalanma dərəcəsi",
    "gəmi sürətinin həddi",
    "yük jurnalı",
    "lisenziya sənədi",
    "lövbər jurnalı"
]

final_questions = []

for item in raw_questions:
    q_num = item["num"]
    q_text = item["question"]
    correct_text = item["correct"]

    # Choose 3 suitable distractors distinct from correct_text
    candidates = [d for d in distractors_pool if d.lower() != correct_text.lower()]
    random.seed(q_num + 777)
    selected_distractors = random.sample(candidates, 3)

    # Place options in randomized A, B, C, D slots
    options_list = [
        {"is_correct": True, "text": correct_text},
        {"is_correct": False, "text": selected_distractors[0]},
        {"is_correct": False, "text": selected_distractors[1]},
        {"is_correct": False, "text": selected_distractors[2]}
    ]
    random.shuffle(options_list)

    keys = ['A', 'B', 'C', 'D']
    options_dict = {}
    correct_key = None

    for i, opt in enumerate(options_list):
        k = keys[i]
        options_dict[k] = opt["text"]
        if opt["is_correct"]:
            correct_key = k

    final_questions.append({
        "id": f"q{q_num:03d}",
        "question": q_text,
        "options": options_dict,
        "correct_answer": correct_key,
        "explanation": ""
    })

print(f"Generated {len(final_questions)} complete 4-option questions.")

output_dir = settings.QUESTIONS_DIR / 'xususi'
output_dir.mkdir(parents=True, exist_ok=True)
json_file_rel = 'xususi/gemi_suruculeri_istismar.json'
json_path = output_dir / 'gemi_suruculeri_istismar.json'

output_data = {
    "certificate": "Gəmi sürücülərinin təkmilləşdirilməsi (istismar)",
    "questions": final_questions
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Saved to {json_path}")

# Update DB
category = Category.objects.get(name='Xüsusi hazırlıq şəhadətnamələri üzrə')
cert = Certificate.objects.filter(category=category, name__icontains='istismar').filter(name__icontains='sürücülərinin').first()

if not cert:
    cert = Certificate.objects.filter(category=category, name__icontains='Gəmi sürücülərinin təkmilləşdirilməsi (istismar)').first()

if cert:
    cert.json_file = json_file_rel
    cert.save()
    print(f"Updated Certificate: ID {cert.id} ('{cert.name}') -> json_file='{json_file_rel}'")
else:
    cert = Certificate.objects.create(
        category=category,
        name="Gəmi sürücülərinin təkmilləşdirilməsi (istismar)",
        json_file=json_file_rel
    )
    print(f"Created Certificate: ID {cert.id} ('{cert.name}') -> json_file='{json_file_rel}'")
