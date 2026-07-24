# -*- coding: utf-8 -*-
import fitz
import os
import glob

pdf_files = glob.glob(r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\*.pdf")

for pdf_path in pdf_files:
    filename = os.path.basename(pdf_path)
    if filename.startswith("~$"):
        continue
    doc = fitz.open(pdf_path)
    img_count = 0
    for page in doc:
        img_count += len(page.get_images(full=True))
    print(f"[{'HAS IMAGES' if img_count > 0 else 'NO IMAGES '}] ({img_count} imgs, {len(doc)} pgs) -> {filename}")
