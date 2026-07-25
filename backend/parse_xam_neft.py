import fitz, json, re, os

pdf_path = r'D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\Xam Neftlə Yuyulma Sistemi.pdf'
json_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\xam_neftl_yuyulma_sistemi.json'

doc = fitz.open(pdf_path)
full_text = ""
for page in doc:
    full_text += page.get_text() + "\n"

# Parse questions from text
blocks = re.split(r'\n(?=\d+\.\s)', full_text)
questions = []

for b in blocks:
    lines = [l.strip() for l in b.split('\n') if l.strip()]
    if not lines:
        continue
    m = re.match(r'^(\d+)\.\s*(.*)', lines[0])
    if not m:
        continue
    q_num = m.group(1)
    q_title = lines[0]
    
    # Collect options and correct answer
    opts = {}
    correct = "A"
    
    # Simple regex match for A), B), C), D) or lines
    opt_matches = re.findall(r'([A-D])[\)\.]\s*(.*?)(?=(?:[A-D][\)\.]|$))', b, re.DOTALL)
    if opt_matches:
        for letter, val in opt_matches:
            opts[letter] = val.strip().replace('\n', ' ')
    
    ans_match = re.search(r'Düzgün cavab:\s*([A-D])', b, re.IGNORECASE)
    if ans_match:
        correct = ans_match.group(1).upper()

print(f"Extracted blocks from PDF...")
