from docx import Document
import os

files = [f for f in os.listdir('.') if f.endswith('.docx')]
for f in files:
    print(f"\n{'='*20} {f} {'='*20}")
    doc = Document(f)
    text = [p.text for p in doc.paragraphs]
    full = '\n'.join(text)
    print(full[:3000])
