import fitz
import sys

def extract_pdf():
    doc = fitz.open(r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\ISPS2.pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    
    with open(r"D:\Dənizçilik_İmtahanları\backend\pdf_debug_isps2.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    extract_pdf()
