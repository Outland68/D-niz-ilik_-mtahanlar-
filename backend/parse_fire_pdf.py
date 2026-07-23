# -*- coding: utf-8 -*-
import os
from pypdf import PdfReader

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Yanginla_mubarize_test.pdf"
reader = PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")

text_full = []
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"--- PAGE {i+1} ---")
    print(text[:500])
    text_full.append(text)

with open(r"D:\Dənizçilik_İmtahanları\backend\extracted_fire_pdf.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(text_full))

print("Saved extracted text to extracted_fire_pdf.txt")
