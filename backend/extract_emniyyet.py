import fitz

pdf_path = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Gәmi әmniyyәtliyi üzrә Mәsul Şәxs.pdf"
out_path = r"D:\Dənizçilik_İmtahanları\backend\pdf_debug_emniyyet.txt"

try:
    doc = fitz.open(pdf_path)
    with open(out_path, "w", encoding="utf-8") as f:
        for page in doc:
            f.write(page.get_text())
    print("PDF extraction completed.")
except Exception as e:
    print(f"Error: {e}")
