import fitz

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gəmi mexaniklərinin təkmilləşdirilməsi (idarəetmə).pdf"
out_path = r"D:\Dənizçilik_İmtahanları\backend\pdf_debug_mexanik_idareetme.txt"

doc = fitz.open(pdf_path)
with open(out_path, "w", encoding="utf-8") as f:
    for page in doc:
        f.write(page.get_text())
