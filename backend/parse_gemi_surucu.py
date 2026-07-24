# -*- coding: utf-8 -*-
import fitz # PyMuPDF

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")

full_text = ""
for page_num in range(len(doc)):
    page = doc[page_num]
    full_text += f"\n--- PAGE {page_num+1} ---\n" + page.get_text()

with open("gemi_surucu_istismar_raw.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("First 1500 chars of extracted PDF:")
print(full_text[:1500])
