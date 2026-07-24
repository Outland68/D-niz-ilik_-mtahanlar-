# -*- coding: utf-8 -*-
import fitz

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    text_page = page.get_text("blocks")
    image_list = page.get_images(full=True)
    print(f"\n--- PAGE {page_num+1} ({len(image_list)} images) ---")
    for b in text_page:
        print(f"Block: {b[4].strip()[:100]}")
