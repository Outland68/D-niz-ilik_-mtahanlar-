import os, docx, json, sys, re
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

def parse_docx(docx_path):
    doc = docx.Document(docx_path)
    questions = []
    curr_q = None
    
    for para in doc.paragraphs:
        text = clean_text(para.text)
        if not text: continue
        
        # Check if question header e.g. "1. ..." or "1. ..."
        q_match = re.match(r'^\s*(\d+)\.\s*(.*)', text)
        opt_match = re.match(r'^\s*([A-Da-d])[\)\.]\s*(.*)', text)
        
        if q_match and not opt_match:
            if curr_q:
                questions.append(curr_q)
            q_num = int(q_match.group(1))
            q_text = q_match.group(2)
            curr_q = {
                'id': q_num,
                'question': q_text,
                'options': {},
                'correct_answer': None
            }
        elif opt_match and curr_q:
            opt_key = opt_match.group(1).upper()
            opt_text = opt_match.group(2)
            curr_q['options'][opt_key] = opt_text
            
            # Check if correct answer:
            # Bold check
            is_bold = any(r.bold for r in para.runs if r.text.strip())
            # Red color check
            is_red = any(r.font.color and r.font.color.rgb and r.font.color.rgb[0] > 150 for r in para.runs if r.text.strip())
            # Highlight check
            is_hl = any(r.font.highlight_color for r in para.runs if r.text.strip())
            
            if is_bold or is_red or is_hl:
                curr_q['correct_answer'] = opt_key
                
    if curr_q:
        questions.append(curr_q)
        
    return questions

# Audit DƏNİZÇİLƏR ÜÇÜN...docx
docx1 = os.path.join(src_dir, "DƏNİZÇİLƏR ÜÇÜN TƏHLÜKƏSİZLİK ÜZRƏ TANIŞLIQ VƏ İLKİN HAZIRLIQ TESTİ.docx")
qs_docx1 = parse_docx(docx1)
print(f"Parsed {len(qs_docx1)} questions from DƏNİZÇİLƏR ÜÇÜN...docx")

json1_p = os.path.join(json_base, "xususi/tanisliq_ilkin_hazirliq.json")
with open(json1_p, 'r', encoding='utf-8') as fp:
    jdata1 = json.load(fp)
jqs1 = jdata1.get('questions', [])

disc1 = []
for q in qs_docx1:
    qnum = q['id']
    if qnum <= len(jqs1):
        jq = jqs1[qnum - 1]
        src_corr = q['correct_answer']
        json_corr = jq.get('correct_answer')
        if src_corr != json_corr:
            disc1.append((qnum, json_corr, src_corr, q['question'], q['options']))

print(f"Discrepancies in tanisliq_ilkin_hazirliq.json: {len(disc1)}")
for d in disc1[:10]:
    print(f"  Q{d[0]}: JSON has '{d[1]}', DOCX has '{d[2]}' ({d[4].get(d[2]) if d[4] else ''})")
