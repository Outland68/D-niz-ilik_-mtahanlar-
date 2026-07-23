# -*- coding: utf-8 -*-
import docx
import re
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings
from api.models import Certificate, Category

docx_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\DƏNİZÇİLƏR ÜÇÜN TƏHLÜKƏSİZLİK ÜZRƏ TANIŞLIQ VƏ İLKİN HAZIRLIQ TESTİ.docx"
doc = docx.Document(docx_path)

def is_paragraph_bold(p):
    bold_runs = [r for r in p.runs if r.bold and r.text.strip()]
    total_runs = [r for r in p.runs if r.text.strip()]
    if not total_runs:
        return False
    return len(bold_runs) == len(total_runs)

questions = []
current_q = None

for p in doc.paragraphs:
    text = p.text.strip()
    if not text:
        continue
    
    # Skip title
    if "Bütün dənizçilər üçün təhlükəsizlik" in text and not re.match(r'^\d+', text):
        continue
        
    q_match = re.match(r'^(\d+)[\.\)]\s*(.+)', text)
    opt_match = re.match(r'^([A-D])[\.\)]\s*(.+)', text)
    
    if q_match:
        q_num = int(q_match.group(1))
        q_title = q_match.group(2)
        current_q = {
            "id": f"q{q_num:03d}",
            "question_num": q_num,
            "question": q_title,
            "options": {},
            "correct_answer": None,
            "explanation": ""
        }
        questions.append(current_q)
    elif opt_match and current_q is not None:
        opt_key = opt_match.group(1)
        opt_val = opt_match.group(2)
        current_q["options"][opt_key] = opt_val
        
        if is_paragraph_bold(p):
            current_q["correct_answer"] = opt_key
    elif current_q is not None and not opt_match and not q_match:
        if current_q["options"]:
            last_opt = list(current_q["options"].keys())[-1]
            current_q["options"][last_opt] += " " + text
            if is_paragraph_bold(p):
                current_q["correct_answer"] = last_opt
        else:
            current_q["question"] += " " + text

# Clean temporary fields
for q in questions:
    del q["question_num"]

print(f"Total questions parsed: {len(questions)}")
missing = [q for q in questions if not q["correct_answer"]]
print(f"Questions missing answer: {len(missing)}")
if missing:
    for m in missing:
        print(f"Missing answer for: {m['id']} - {m['question']}")

output_dir = settings.QUESTIONS_DIR / 'xususi'
output_dir.mkdir(parents=True, exist_ok=True)
json_file_rel = 'xususi/tanisliq_ilkin_hazirliq.json'
json_path = output_dir / 'tanisliq_ilkin_hazirliq.json'

output_data = {
    "certificate": "Bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat",
    "questions": questions
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Saved to {json_path}")

# Update DB
category = Category.objects.get(name='Xüsusi hazırlıq şəhadətnamələri üzrə')
cert = Certificate.objects.filter(category=category, name__icontains='tənəffüs').first()

if not cert:
    cert = Certificate.objects.filter(category=category, name__icontains='tanışlıq').first()
if not cert:
    cert = Certificate.objects.filter(category=category, name__icontains='Safety familiarization').first()

if cert:
    cert.name = "Bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat"
    cert.json_file = json_file_rel
    cert.save()
    print(f"Updated Certificate: ID {cert.id} ('{cert.name}') -> json_file='{json_file_rel}'")
else:
    # Create if not exists
    cert = Certificate.objects.create(
        category=category,
        name="Bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat",
        json_file=json_file_rel
    )
    print(f"Created Certificate: ID {cert.id} ('{cert.name}') -> json_file='{json_file_rel}'")
