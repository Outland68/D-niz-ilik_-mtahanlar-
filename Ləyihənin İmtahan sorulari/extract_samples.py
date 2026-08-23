import os
from docx import Document
from pypdf import PdfReader

# List files in current directory
files = [f for f in os.listdir('.') if f.lower().endswith(('.pdf','.docx'))]
files.sort()

# Read first DOCX
docx_files = [f for f in files if f.endswith('.docx')]
pdf_files = [f for f in files if f.endswith('.pdf')]

if docx_files:
    f = docx_files[0]
    print(f"=== DOCX: {f} ===")
    try:
        doc = Document(f)
        text = []
        for para in doc.paragraphs:
            text.append(para.text)
        full = '\n'.join(text)
        print(full[:2000])
        print("...")
    except Exception as e:
        print(f"Error: {e}")

if pdf_files:
    f = pdf_files[0]
    print(f"\n=== PDF: {f} ===")
    try:
        reader = PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        print(text[:2000])
        print("...")
    except Exception as e:
        print(f"Error: {e}")
