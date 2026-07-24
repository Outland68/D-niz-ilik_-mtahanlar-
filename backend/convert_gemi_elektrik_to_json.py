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

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi elektrik mexaniklərinin təkmilləşdirilməsi.pdf"
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

# Realistic electrical engineering distractors pool
distractors_pool = [
    "İşıq siqnalizasiya lövhəsində",
    "Gəmi jurnalının son səhifəsində",
    "0.5 Mom-dan az olmayan elektrik maşınlarında",
    "1.0 Mom müqavimət olduqda",
    "Hər 6 aydan bir",
    "Hər növbə dəyişikliyində",
    "5.00 %-dən çox olmadıqda",
    "0.50 %-dən çox olmadıqda",
    "0.10 %-dən az olduqda",
    "Hər iki tərəfdən 6 mil məsafədə",
    "Kapitan körpüsünün üstündə",
    "10 uzel",
    "12 uzel",
    "Baş mexanik və növbətçi mexanik",
    "Gəmi sahibi tərəfindən",
    "Liman müfəttişliyi tərəfindən",
    "10.0 Mom",
    "0.01 Mom",
    "Əqrəbli ampermertlə",
    "Rəqəmsal meqometr vasitəsilə",
    "3 saat",
    "12 saat",
    "24 saat",
    "Gəmi kapitanı",
    "İldə bir dəfə",
    "Hər fırtınadan sonra",
    "200 A",
    "500 A",
    "1500 A",
    "Dəyişməz qalır",
    "Azalar",
    "Sıfıra bərabər olar",
    "Elektromaqnit generatoru",
    "Dəniz su filtri",
    "İmpuls transformatoru"
]

final_questions = []

for item in raw_questions:
    q_num = item["num"]
    q_text = item["question"]
    correct_text = item["correct"]

    # Choose 3 suitable distractors distinct from correct_text
    candidates = [d for d in distractors_pool if d.lower() != correct_text.lower()]
    random.seed(q_num + 999)
    selected_distractors = random.sample(candidates, 3)

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

    q_obj = {
        "id": f"q{q_num:03d}",
        "question": f"{q_num}. {q_text}",
        "options": options_dict,
        "correct_answer": correct_key,
        "explanation": ""
    }

    # Question 35 contains warning sign diagram extracted from page 4 (img_p4_1.png)
    if q_num == 35:
        q_obj["image_url"] = "/images/gemi_elektrik/img_p4_1.png"

    final_questions.append(q_obj)

print(f"Generated {len(final_questions)} complete 4-option questions for Gəmi Elektrik Mexanikləri.")

output_dir = settings.QUESTIONS_DIR / 'xususi'
output_dir.mkdir(parents=True, exist_ok=True)
json_file_rel = 'xususi/gemi_elektrik_mexanikleri.json'
json_path = output_dir / 'gemi_elektrik_mexanikleri.json'

output_data = {
    "certificate": "Gəmi elektrik mexaniklərinin təkmilləşdirilməsi",
    "questions": final_questions
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Saved to {json_path}")

# Update DB
category = Category.objects.get(name='Xüsusi hazırlıq şəhadətnamələri üzrə')
cert = Certificate.objects.filter(category=category, name__icontains='elektrik').first()

if cert:
    cert.json_file = json_file_rel
    cert.save()
    print(f"Updated Certificate: ID {cert.id} ('{cert.name}') -> json_file='{json_file_rel}'")
else:
    cert = Certificate.objects.create(
        category=category,
        name="Gəmi elektrik mexaniklərinin təkmilləşdirilməsi",
        json_file=json_file_rel
    )
    print(f"Created Certificate: ID {cert.id} ('{cert.name}') -> json_file='{json_file_rel}'")
