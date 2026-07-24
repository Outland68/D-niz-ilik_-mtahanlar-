# -*- coding: utf-8 -*-
import fitz # PyMuPDF
import os

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf"
doc = fitz.open(pdf_path)

output_dir = r"D:\Dənizçilik_İmtahanları\frontend\public\images\gemi_surucu"
os.makedirs(output_dir, exist_ok=True)

# Render pages to PNG images at 150 DPI to visually inspect exact questions
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    page_path = os.path.join(output_dir, f"page_{i+1}.png")
    pix.save(page_path)
    print(f"Rendered Page {i+1} -> {page_path}")
