# -*- coding: utf-8 -*-
import fitz # PyMuPDF
import os

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi elektrik mexaniklərinin təkmilləşdirilməsi.pdf"
doc = fitz.open(pdf_path)

output_img_dir = r"D:\Dənizçilik_İmtahanları\frontend\public\images\gemi_elektrik"
os.makedirs(output_img_dir, exist_ok=True)

full_text = ""
for i, page in enumerate(doc):
    full_text += f"\n--- PAGE {i+1} ---\n" + page.get_text()
    
    # render page to image for visual verification
    pix = page.get_pixmap(dpi=150)
    pix.save(os.path.join(output_img_dir, f"page_{i+1}.png"))
    
    # extract raw images
    for img_idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        filename = f"img_p{i+1}_{img_idx+1}.{base_image['ext']}"
        filepath = os.path.join(output_img_dir, filename)
        with open(filepath, "wb") as f:
            f.write(base_image["image"])
        print(f"Page {i+1}: Extracted {filename}")

with open("gemi_elektrik_raw.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"\nTotal pages: {len(doc)}")
print("First 1500 chars of extracted text:")
print(full_text[:1500])
