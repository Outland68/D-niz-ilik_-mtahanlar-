# -*- coding: utf-8 -*-
import docx

doc = docx.Document(r"C:\Users\Omer\Downloads\EIBM_Test (1).docx")

print("Checking tail paragraphs...")
for i, p in enumerate(doc.paragraphs[-30:]):
    if p.text.strip():
        print(f"P{i}: {p.text.strip()}")
