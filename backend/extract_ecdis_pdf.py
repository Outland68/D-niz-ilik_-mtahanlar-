import fitz
import sys

pdf_path = "D:\\Dənizçilik_İmtahanları\\Ləyihənin İmtahan sorulari\\Elektron Xəritə Displeyinin və İnformasiya Sistemlərinin İstismar Qaydaları.pdf"
out_path = "D:\\Dənizçilik_İmtahanları\\backend\\pdf_debug_ecdis.txt"

try:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("PDF extraction complete")
except Exception as e:
    print(f"Error: {e}")
