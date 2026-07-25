import os
import glob
import fitz # PyMuPDF
import docx
import json

source_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"
json_dir = r"D:\Dənizçilik_İmtahanları\backend\static\questions"

source_files = glob.glob(os.path.join(source_dir, "*.*"))
print(f"Total source document files found: {len(source_files)}")

# Check PDF images count
total_images = 0
for sf in source_files:
    if sf.endswith(".pdf"):
        doc = fitz.open(sf)
        for page in doc:
            images = page.get_images()
            if images:
                total_images += len(images)
                print(f"Found {len(images)} image(s) in PDF: {os.path.basename(sf)}")
    elif sf.endswith(".docx"):
        doc = docx.Document(sf)
        # Check inline shapes/images in docx
        inline_imgs = [rel for rel in doc.part.rels.values() if "image" in rel.target_ref]
        if inline_imgs:
            total_images += len(inline_imgs)
            print(f"Found {len(inline_imgs)} image(s) in DOCX: {os.path.basename(sf)}")

print(f"\nTotal embedded images found across all source files: {total_images}")
