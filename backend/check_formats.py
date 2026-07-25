import os, fitz, docx, sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"

files = sorted(os.listdir(src_dir))

print(f"Total source files: {len(files)}")

for sf in files:
    path = os.path.join(src_dir, sf)
    print(f"\n==================================================")
    print(f"FILE: {sf}")
    if sf.endswith(".pdf"):
        doc = fitz.open(path)
        print(f"Pages: {len(doc)}")
        full_text = "\n".join([page.get_text() for page in doc])
        # sample text lines
        lines = [l.strip() for l in full_text.split('\n') if l.strip()]
        print(f"Total lines: {len(lines)}")
        print("First 10 lines:", lines[:10])
        has_duzgun = any("düzgün cavab" in l.lower() for l in lines)
        has_a = any(re.match(r'^[A-Da-d][\)\.]\s+', l) for l in lines)
        print(f"Format: Has 'Düzgün cavab': {has_duzgun}, Has 'A)': {has_a}")
    elif sf.endswith(".docx"):
        doc = docx.Document(path)
        lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        print(f"Total paragraphs: {len(lines)}")
        print("First 10 paragraphs:", lines[:10])
        has_duzgun = any("düzgün cavab" in l.lower() for l in lines)
        has_a = any(re.match(r'^[A-Da-d][\)\.]\s+', l) for l in lines)
        print(f"Format: Has 'Düzgün cavab': {has_duzgun}, Has 'A)': {has_a}")
