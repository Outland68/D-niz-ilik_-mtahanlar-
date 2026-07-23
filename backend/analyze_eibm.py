# -*- coding: utf-8 -*-
import os
import docx

path = r"C:\Users\Omer\Downloads\EIBM_Test (1).docx"
doc = docx.Document(path)

print("Checking formatting & text sample...")
for i, p in enumerate(doc.paragraphs[:50]):
    text = p.text.strip()
    if not text:
        continue
    runs_info = []
    for r in p.runs:
        if r.text.strip():
            runs_info.append(f"['{r.text}' bold={r.bold} underline={r.underline} color={r.font.color.rgb if r.font and r.font.color else None}]")
    print(f"P{i}: {text}")
    if runs_info:
        print("   Runs:", " ".join(runs_info))
