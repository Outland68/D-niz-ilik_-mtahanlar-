# -*- coding: utf-8 -*-
import fitz # PyMuPDF
import re
import json
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings
from api.models import Certificate, Category

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Yanginla_mubarize_test.pdf"
doc = fitz.open(pdf_path)

# Extract paragraphs and detect red answers
questions = []
current_q = None

for page_num in range(len(doc)):
    page = doc[page_num]
    blocks = page.get_text("dict")["blocks"]
    
    for b in blocks:
        if "lines" not in b:
            continue
        for line in b["lines"]:
            line_text = ""
            is_line_red = False
            for span in line["spans"]:
                t = span["text"]
                line_text += t
                color = span["color"]
                r = (color >> 16) & 255
                g = (color >> 8) & 255
                b_val = color & 255
                if r > 150 and g < 80 and b_val < 80 and t.strip():
                    is_line_red = True
            
            line_text = line_text.strip()
            if not line_text:
                continue
            
            # Skip page headers / title
            if "Yanğınla mübarizə geniş proqram" in line_text or "Düzgün cavablar" in line_text or "--- PAGE" in line_text:
                continue
            
            q_match = re.match(r'^(\d+)[\.\)]\s*(.+)', line_text)
            opt_match = re.match(r'^([A-D])[\.\)]\s*(.+)', line_text)
            
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
                if is_line_red:
                    current_q["correct_answer"] = opt_key
            elif current_q is not None and not opt_match and not q_match:
                # Continuation of question or option
                if current_q["options"]:
                    # Last option continuation
                    last_opt = list(current_q["options"].keys())[-1]
                    current_q["options"][last_opt] += " " + line_text
                    if is_line_red:
                        current_q["correct_answer"] = last_opt
                else:
                    # Question continuation
                    current_q["question"] += " " + line_text

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
json_file_rel = 'xususi/yanginla_mubarize_genis.json'
json_path = output_dir / 'yanginla_mubarize_genis.json'

output_data = {
    "certificate": "Yanğınla mübarizə (geniş proqram üzrə)",
    "questions": questions
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Saved to {json_path}")

# Update DB
category = Category.objects.get(name='Xüsusi hazırlıq şəhadətnamələri üzrə')
cert = Certificate.objects.filter(category=category, name__icontains='Yanğınla mübarizə (geniş').first()

if not cert:
    cert = Certificate.objects.filter(category=category, name__icontains='Yanğınla mübarizə').first()

if cert:
    cert.json_file = json_file_rel
    cert.save()
    print(f"Updated Certificate: ID {cert.id} ('{cert.name}') -> json_file='{json_file_rel}'")
else:
    print("Certificate not found in DB!")
