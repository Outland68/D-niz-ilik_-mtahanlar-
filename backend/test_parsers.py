import os, fitz, docx, json, sys, re
from difflib import SequenceMatcher

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"
json_base = r"D:\Dənizçilik_İmtahanları\backend\static\questions"

def clean_text(s):
    if not s: return ""
    s = s.replace('\xa0', ' ').replace('\u200b', '').strip()
    s = re.sub(r'\s+', ' ', s)
    return s

def norm_az(s):
    if not s: return ""
    s = clean_text(s).lower()
    s = s.replace('ә', 'ə').replace('i̇', 'i')
    return s

def similarity(a, b):
    a_clean = norm_az(a)
    b_clean = norm_az(b)
    if not a_clean or not b_clean: return 0.0
    if a_clean == b_clean: return 1.0
    if a_clean in b_clean or b_clean in a_clean: return 0.9
    return SequenceMatcher(None, a_clean, b_clean).ratio()

# Test 1: PDF with Düzgün cavab: <text>
def parse_pdf_duzgun_cavab(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = "\n".join([page.get_text() for page in doc])
    
    # Split text into question blocks based on regex \n\s*\d+\.\s+
    # Find all question match spans
    matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\.\s+', full_text))
    questions = []
    
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i+1 < len(matches) else len(full_text)
        q_num = int(matches[i].group(1))
        block = full_text[start:end].strip()
        
        # Look for Düzgün cavab:
        parts = re.split(r'Düzgün\s+cavab\s*:\s*', block, flags=re.IGNORECASE)
        if len(parts) >= 2:
            q_text = clean_text(parts[0])
            # remove question number prefix from q_text
            q_text = re.sub(r'^\s*\d+\.\s*', '', q_text)
            ans_text = clean_text(parts[1].split('\n\n')[0].split('\n1000')[0])
            # clean trailing numbers or next questions if any
            ans_text = re.sub(r'\s*\d+\.\s+.*$', '', ans_text, flags=re.DOTALL).strip()
            questions.append((q_num, q_text, ans_text))
            
    return questions

# Test 1 run
pdf1 = os.path.join(src_dir, '1000 volt vә artıq olan gәrginlik sistemlәrinin tәhlükәsiz istismarı vә onlara texniki nәzarәt.pdf')
qs1 = parse_pdf_duzgun_cavab(pdf1)
print(f"Test 1 parsed {len(qs1)} questions from 1000 volt...pdf")
print("Sample Q1:", qs1[0])
print("Sample Q2:", qs1[1])

# Audit against JSON
with open(os.path.join(json_base, 'xususi/1000_volt_v_art_q_olan_g_rginlik_sisteml.json'), 'r', encoding='utf-8') as fp:
    jdata1 = json.load(fp)
jqs1 = jdata1.get('questions', [])

discrepancies = []
for q_num, q_text, ans_text in qs1:
    if q_num <= len(jqs1):
        jq = jqs1[q_num - 1]
        j_opts = jq.get('options', {})
        # Find which option best matches ans_text
        best_opt = None
        best_score = 0.0
        for opt_key, opt_val in j_opts.items():
            score = similarity(ans_text, opt_val)
            if score > best_score:
                best_score = score
                best_opt = opt_key
                
        curr_correct = jq.get('correct_answer')
        if best_opt and curr_correct != best_opt:
            discrepancies.append((q_num, curr_correct, best_opt, ans_text, j_opts.get(best_opt)))

print(f"Discrepancies found in 1000 volt...json correct_answers: {len(discrepancies)}")
for d in discrepancies[:10]:
    print(f"  Q{d[0]}: JSON has '{d[1]}', but source 'Düzgün cavab: {d[3]}' matches option '{d[2]}' ({d[4]})")

