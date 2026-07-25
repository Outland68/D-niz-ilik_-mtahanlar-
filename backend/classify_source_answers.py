import os, fitz, docx, sys, json

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"
files = sorted(os.listdir(src_dir))

for sf in files:
    path = os.path.join(src_dir, sf)
    print(f"\n==================================================")
    print(f"FILE: {sf}")
    if sf.endswith(".pdf"):
        doc = fitz.open(path)
        duzgun_count = 0
        red_spans = 0
        bold_spans = 0
        underlined_spans = 0
        
        for page in doc:
            text = page.get_text()
            if "düzgün cavab" in text.lower():
                duzgun_count += 1
            
            blocks = page.get_text("dict")["blocks"]
            for b in blocks:
                for line in b.get("lines", []):
                    for span in line.get("spans", []):
                        color = span.get("color", 0)
                        r = (color >> 16) & 255
                        g = (color >> 8) & 255
                        b_val = color & 255
                        flags = span.get("flags", 0)
                        
                        if r > 150 and g < 50 and b_val < 50:
                            red_spans += 1
                        if flags & 2 or "bold" in span.get("font", "").lower():
                            bold_spans += 1
                            
        print(f"PDF Stats: 'Düzgün cavab' count: {duzgun_count}, Red spans: {red_spans}, Bold spans: {bold_spans}")
    elif sf.endswith(".docx"):
        doc = docx.Document(path)
        bold_runs = sum(1 for p in doc.paragraphs for r in p.runs if r.bold)
        red_runs = sum(1 for p in doc.paragraphs for r in p.runs if r.font.color and r.font.color.rgb and r.font.color.rgb[0] > 150)
        duzgun_count = sum(1 for p in doc.paragraphs if "düzgün cavab" in p.text.lower())
        print(f"DOCX Stats: 'Düzgün cavab' count: {duzgun_count}, Red runs: {red_runs}, Bold runs: {bold_runs}")
