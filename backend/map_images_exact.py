# -*- coding: utf-8 -*-
import fitz # PyMuPDF

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf"
doc = fitz.open(pdf_path)

print("Mapping images to questions exactly from PDF geometry:")

# We inspect page by page where images physically sit relative to text blocks
for page_num, page in enumerate(doc):
    print(f"\n--- PAGE {page_num+1} ---")
    img_info = page.get_images(full=True)
    text_blocks = page.get_text("blocks")
    
    for i, img in enumerate(img_info):
        xref = img[0]
        # find image rects
        rects = page.get_image_rects(xref)
        for r in rects:
            print(f"Image {i+1} (xref {xref}) at Y=[{r.y0:.1f} .. {r.y1:.1f}]")
            # find closest text above and below
            text_above = [b[4].strip().replace('\n', ' ') for b in text_blocks if b[1] < r.y0]
            text_below = [b[4].strip().replace('\n', ' ') for b in text_blocks if b[1] >= r.y0]
            print(f"   Text above: {text_above[-1][:80] if text_above else 'None'}")
            print(f"   Text below: {text_below[0][:80] if text_below else 'None'}")
