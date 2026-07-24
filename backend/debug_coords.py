# -*- coding: utf-8 -*-
import fitz # PyMuPDF

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    image_list = page.get_images(full=True)
    print(f"\n================ PAGE {page_num+1} ({len(image_list)} images) ================")
    
    # Get rects of images
    for img_idx, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        print(f"Img {img_idx+1}: xref={xref}, ext={base_image['ext']}, width={base_image['width']}, height={base_image['height']}")

    # Get text with coordinates
    blocks = page.get_text("blocks")
    for b in blocks:
        text = b[4].strip().replace('\n', ' ')
        if text:
            print(f"Text block [y0={b[1]:.1f}, y1={b[3]:.1f}]: {text[:120]}")
