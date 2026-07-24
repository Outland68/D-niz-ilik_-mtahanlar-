# -*- coding: utf-8 -*-
import fitz # PyMuPDF
import os

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf"
doc = fitz.open(pdf_path)

output_img_dir = r"D:\Dənizçilik_İmtahanları\frontend\public\images\gemi_surucu"
os.makedirs(output_img_dir, exist_ok=True)

extracted_images = []

for page_index in range(len(doc)):
    page = doc[page_index]
    image_list = page.get_images(full=True)
    print(f"Page {page_index+1} has {len(image_list)} images.")
    
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        filename = f"img_p{page_index+1}_{img_index+1}.{image_ext}"
        filepath = os.path.join(output_img_dir, filename)
        
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        
        print(f"Saved: {filename}")
