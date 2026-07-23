# -*- coding: utf-8 -*-
import pypdf

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Yanginla_mubarize_test.pdf"
reader = pypdf.PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")

full_text = ""
for i, page in enumerate(reader.pages):
    full_text += f"\n--- PAGE {i+1} ---\n" + page.extract_text()

with open("yangin_extracted.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Saved first 500 chars sample:")
print(full_text[:500])
