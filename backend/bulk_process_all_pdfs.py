# -*- coding: utf-8 -*-
import fitz # PyMuPDF
import re
import json
import random
import os
import glob
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings
from api.models import Certificate, Category

# Distractors database for domain-accurate option generation
MARITIME_DISTRACTORS = [
    "bütün cavablar doğrudur",
    "bütün cavablar yanlışdır",
    "yalnız gəmi kapitanının yazılı icazəsi ilə",
    "baş mexanikin və növbətçi mexanikin nəzarəti altında",
    "xüsusi təyin olunmuş növbətçi şturman tərəfindən",
    "gəminin texniki sənədlərində göstərilmiş qaydada",
    "SOLAS Beynəlxalq Konvensiyasının tələblərinə uyğun olaraq",
    "MARPOL 73/78 Konvensiyasının V əlavəsinə əsasən",
    "GMDSS beynəlxalq radiorabitə nizamnaməsinə uyğun olaraq",
    "fırtınalı havada təxirə salınmaqla",
    "hər 6 aydan bir keçirilən təlimlərdə",
    "hər ayda bir dəfədən az olmayan müddətdə",
    "gəmi limana daxil olana qədər",
    "10 uzel sürətlə manevr etdikdə",
    "50 metr məsafədə dənizdə",
    "lövbər dayanacağı sahəsində",
    "şimal-şərq istiqamətində",
    "cənub-qərb dreyfi zamanı",
    "avtomatik rejimdə işləyərkən",
    "əllə idarəetmə rejiminə keçdikdə",
    "izolyasiya müqaviməti 0.5 Mom-dan yüksək olduqda",
    "gərginlik 220 V həddinə çatdıqda",
    "cərəyan şiddəti nominal dəyəri keçdikdə"
]

pdf_files = glob.glob(r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\*.pdf")
output_base_dir = settings.QUESTIONS_DIR / 'xususi'
output_base_dir.mkdir(parents=True, exist_ok=True)

frontend_img_base = r"D:\Dənizçilik_İmtahanları\frontend\public\images"
backend_img_base = settings.BASE_DIR / 'static' / 'images'

processed_certs = {}

for pdf_path in pdf_files:
    filename = os.path.basename(pdf_path)
    if filename.startswith("~$"):
        continue

    # Extract certificate clean title
    cert_name = filename.replace(".pdf", "").strip()
    
    # Safe slug for image directory and JSON filename
    slug = re.sub(r'[^a-zA-Z0-9_]', '_', cert_name.lower())
    slug = re.sub(r'_+', '_', slug).strip('_')[:40]
    
    json_filename = f"{slug}.json"
    json_path = output_base_dir / json_filename
    json_rel_path = f"xususi/{json_filename}"

    doc = fitz.open(pdf_path)

    # Prepare image export folders
    cert_frontend_img_dir = os.path.join(frontend_img_base, slug)
    cert_backend_img_dir = os.path.join(backend_img_base, slug)
    os.makedirs(cert_frontend_img_dir, exist_ok=True)
    os.makedirs(cert_backend_img_dir, exist_ok=True)

    page_images_map = {} # page_index -> list of saved relative image URLs

    for page_idx, page in enumerate(doc):
        image_list = page.get_images(full=True)
        page_images_map[page_idx] = []
        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            ext = base_image["ext"]
            
            img_name = f"img_p{page_idx+1}_{img_idx+1}.{ext}"
            
            # Save to frontend public/images/<slug>/
            with open(os.path.join(cert_frontend_img_dir, img_name), "wb") as f:
                f.write(img_bytes)
                
            # Save to backend static/images/<slug>/
            with open(os.path.join(cert_backend_img_dir, img_name), "wb") as f:
                f.write(img_bytes)
                
            rel_url = f"/images/{slug}/{img_name}"
            page_images_map[page_idx].append(rel_url)

    # Extract text and map questions
    raw_questions = []
    
    for page_idx, page in enumerate(doc):
        page_text = page.get_text()
        blocks = re.split(r'\n(?=\d+[\.\)]\s*)', page_text)
        page_imgs = page_images_map[page_idx]
        
        for block in blocks:
            block = block.strip()
            if not block:
                continue
            
            m = re.match(r'^(\d+)[\.\)]\s*(.*?)\s*Düzgün cavab:\s*(.*)', block, re.DOTALL)
            if m:
                q_num = int(m.group(1))
                q_text = re.sub(r'\s+', ' ', m.group(2)).strip()
                c_ans = re.sub(r'\s+', ' ', m.group(3)).strip()
                
                # Attach page image if question contains "şəkildə", "xəritədə", "baxın" or if images on page
                img_url = None
                if page_imgs and ("şəkil" in q_text.lower() or "xəritə" in q_text.lower() or "işarə" in q_text.lower() or "bax" in q_text.lower()):
                    img_url = page_imgs[0]
                elif page_imgs and len(blocks) <= len(page_imgs) + 2:
                    img_url = page_imgs[min(q_num - 1, len(page_imgs) - 1)]

                raw_questions.append({
                    "num": q_num,
                    "question": q_text,
                    "correct": c_ans,
                    "image_url": img_url
                })

    if not raw_questions:
        print(f"Skipping {filename} (no questions parsed)")
        continue

    # Build 4-option MCQs
    questions_list = []
    for item in raw_questions:
        q_num = item["num"]
        q_text = item["question"]
        c_ans = item["correct"]
        img_url = item["image_url"]

        # 3 Distractors
        candidates = [d for d in MARITIME_DISTRACTORS if d.lower() != c_ans.lower()]
        random.seed(q_num + len(filename) * 11)
        distractors = random.sample(candidates, 3)

        opts = [
            {"is_correct": True, "text": c_ans},
            {"is_correct": False, "text": distractors[0]},
            {"is_correct": False, "text": distractors[1]},
            {"is_correct": False, "text": distractors[2]}
        ]
        random.shuffle(opts)

        keys = ['A', 'B', 'C', 'D']
        options_dict = {}
        correct_key = None

        for idx, opt in enumerate(opts):
            k = keys[idx]
            options_dict[k] = opt["text"]
            if opt["is_correct"]:
                correct_key = k

        q_entry = {
            "id": f"q{q_num:03d}",
            "question": f"{q_num}. {q_text}",
            "options": options_dict,
            "correct_answer": correct_key,
            "explanation": ""
        }
        if img_url:
            q_entry["image_url"] = img_url

        questions_list.append(q_entry)

    # Save JSON
    output_data = {
        "certificate": cert_name,
        "questions": questions_list
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    processed_certs[cert_name] = json_rel_path
    print(f"[{len(questions_list)} Qs] Processed '{cert_name}' -> {json_rel_path}")

print(f"\nSuccessfully processed {len(processed_certs)} PDF certificates.")

# Update setup.py automatically to include all newly generated certificate JSONs
setup_path = settings.BASE_DIR / 'setup.py'
with open(setup_path, 'r', encoding='utf-8') as f:
    setup_code = f.read()

# Update special_certs dictionary in setup.py
for name, json_file in processed_certs.items():
    # Replace `"Name": None` or `"Name": "..."` with new json_file
    pattern = rf'"{re.escape(name)}"\s*:\s*(?:None|".*?")'
    replacement = f'"{name}": "{json_file}"'
    setup_code = re.sub(pattern, replacement, setup_code)

with open(setup_path, 'w', encoding='utf-8') as f:
    f.write(setup_code)

print("Updated setup.py with all certificate JSON file paths!")

# Run setup.py to seed database
import subprocess
subprocess.run(["python", "setup.py"], cwd=settings.BASE_DIR)
