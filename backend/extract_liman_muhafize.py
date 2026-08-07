import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Liman vasitәlәrinin mühafizәyә mәsul.pdf")
with open("pdf_debug_liman_muhafize.txt", "w", encoding="utf-8") as f:
    for page in doc:
        f.write(page.get_text())
