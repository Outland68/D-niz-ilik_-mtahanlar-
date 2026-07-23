# -*- coding: utf-8 -*-
import fitz # PyMuPDF

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Yanginla_mubarize_test.pdf"
doc = fitz.open(pdf_path)

red_answers = []

for page_num in range(len(doc)):
    page = doc[page_num]
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if "lines" in b:
            for line in b["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    color = span["color"]
                    # Convert color int to hex RGB
                    r = (color >> 16) & 255
                    g = (color >> 8) & 255
                    b_val = color & 255
                    
                    # Check if predominantly red (r > 150 and g < 50 and b < 50)
                    if r > 150 and g < 80 and b_val < 80 and text:
                        print(f"P{page_num+1} RED: '{text}' (RGB: {r},{g},{b_val})")
