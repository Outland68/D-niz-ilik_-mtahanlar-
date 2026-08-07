import fitz

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Qlobal Dәniz Fәlakәt vә Әmniyyәtli Rabitә Sisteminin Ümumi Rayon Operatoru.pdf"
out_path = r"D:\Dənizçilik_İmtahanları\backend\pdf_debug_gmdss.txt"

doc = fitz.open(pdf_path)
text = ""
for page in doc:
    text += page.get_text()

with open(out_path, "w", encoding="utf-8") as f:
    f.write(text)
