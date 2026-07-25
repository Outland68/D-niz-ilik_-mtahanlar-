import os, fitz, docx, json, sys, re, shutil
from difflib import SequenceMatcher

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"
json_base = r"D:\Dənizçilik_İmtahanları\backend\static\questions"
backend_img_base = r"D:\Dənizçilik_İmtahanları\backend\static\images"
frontend_img_base = r"D:\Dənizçilik_İmtahanları\frontend\public\images"

def clean_text(s):
    if not s: return ""
    s = str(s).replace('\xa0', ' ').replace('\u200b', '').strip()
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

# Dynamically map all 39 files in src_dir to target JSON files
all_src_files = os.listdir(src_dir)

all_json_files = []
for root, dirs, files in os.walk(json_base):
    for f in files:
        if f.endswith('.json'):
            all_json_files.append(os.path.relpath(os.path.join(root, f), json_base).replace('\\', '/'))

SOURCE_TO_JSON = {}

for sf in all_src_files:
    sn = norm_az(sf).replace('.pdf', '').replace('.docx', '').strip()
    matched_jsons = []
    
    for jf in all_json_files:
        full_jp = os.path.join(json_base, jf)
        with open(full_jp, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            ctitle = norm_az(d.get('certificate', ''))
        j_short = os.path.basename(jf).replace('.json', '')
        
        if (sn in ctitle or ctitle in sn or j_short in sn) and not ('colreg' in jf or 'marpol' in jf):
            matched_jsons.append(jf)
            
    if 'safety familiarization' in sn:
        matched_jsons = ['xususi/safety_familiarization_en.json']
    elif 'dənizçilər üçün təhlükəsizlik' in sn or 'bütün dənizçilər' in sn:
        matched_jsons = ['xususi/b_t_n_d_niz_il_r_n_t_hl_k_sizlik_zr_tan_.json', 'xususi/tanisliq_ilkin_hazirliq.json']
    elif 'eibm' in sn or 'əmniyyətli idarəetmə' in sn:
        matched_jsons = ['special/eibm.json', 'xususi/mniyy_tli_i_dar_etm_haqq_nda_beyn_lxalq_.json']
    elif 'yanginla_mubarize' in sn:
        matched_jsons = ['xususi/yanginla_mubarize_genis.json']
    elif 'gəmi elektrik mexaniklərinin' in sn:
        matched_jsons = ['xususi/g_mi_elektrik_mexanikl_rinin_t_kmill_dir.json', 'xususi/gemi_elektrik_mexanikleri.json']
    elif 'gəmi sürücülərinin təkmilləşdirilməsi' in sn:
        matched_jsons = ['xususi/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist.json', 'xususi/gemi_suruculeri_istismar.json']

    SOURCE_TO_JSON[sf] = matched_jsons

# Image assignments per JSON file
JSON_IMAGE_ASSIGNMENTS = {
    "xususi/elektron_x_rit_displeyinin_v_i_nformasiy.json": {
        2: "/images/elektron_x_rit_displeyinin_v_i_nformasiy/img_p1_1.png",
        14: "/images/elektron_x_rit_displeyinin_v_i_nformasiy/img_p2_1.png",
        33: "/images/elektron_x_rit_displeyinin_v_i_nformasiy/img_p4_1.png",
        34: "/images/elektron_x_rit_displeyinin_v_i_nformasiy/img_p4_2.png",
        35: "/images/elektron_x_rit_displeyinin_v_i_nformasiy/img_p4_3.png",
        36: "/images/elektron_x_rit_displeyinin_v_i_nformasiy/img_p4_4.png"
    },
    "xususi/g_mi_elektrik_mexanikl_rinin_t_kmill_dir.json": {
        37: "/images/g_mi_elektrik_mexanikl_rinin_t_kmill_dir/img_p4_1.png"
    },
    "xususi/gemi_elektrik_mexanikleri.json": {
        37: "/images/g_mi_elektrik_mexanikl_rinin_t_kmill_dir/img_p4_1.png"
    },
    "xususi/g_mi_mexanikl_rinin_t_kmill_dirilm_si_id.json": {
        13: "/images/g_mi_mexanikl_rinin_t_kmill_dirilm_si_id/img_p2_1.jpeg",
        22: "/images/g_mi_mexanikl_rinin_t_kmill_dirilm_si_id/img_p3_1.jpeg",
        23: "/images/g_mi_mexanikl_rinin_t_kmill_dirilm_si_id/img_p3_2.jpeg"
    },
    "xususi/g_mi_mexanikl_rinin_t_kmill_dirilm_si_is.json": {
        20: "/images/g_mi_mexanikl_rinin_t_kmill_dirilm_si_is/img_p3_1.jpeg",
        21: "/images/g_mi_mexanikl_rinin_t_kmill_dirilm_si_is/img_p3_2.jpeg"
    },
    "xususi/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist.json": {
        1: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p1_1.png",
        3: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p1_3.jpeg",
        9: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p2_1.png",
        10: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p2_2.jpeg",
        13: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p2_3.jpeg",
        16: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p3_1.png",
        17: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p3_3.jpeg",
        23: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p4_1.jpeg",
        27: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p5_1.jpeg"
    },
    "xususi/gemi_suruculeri_istismar.json": {
        1: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p1_1.png",
        3: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p1_3.jpeg",
        9: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p2_1.png",
        10: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p2_2.jpeg",
        13: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p2_3.jpeg",
        16: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p3_1.png",
        17: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p3_3.jpeg",
        23: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p4_1.jpeg",
        27: "/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/img_p5_1.jpeg"
    },
    "xususi/g_mid_tibbi_n_zar_t.json": {
        97: "/images/g_mid_tibbi_n_zar_t/img_p14_1.jpeg"
    },
    "xususi/radar_avtomatik_radar_m_ahid_vasit_l_ri_.json": {
        9: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p1_1.jpeg",
        10: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p2_1.jpeg",
        11: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p2_2.jpeg",
        12: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p2_3.jpeg",
        13: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p2_4.jpeg",
        14: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p3_1.jpeg",
        15: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p3_2.jpeg",
        34: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p5_1.jpeg",
        35: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p5_2.jpeg",
        36: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p5_3.jpeg",
        37: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p5_4.jpeg",
        38: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p6_1.jpeg",
        39: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p6_2.jpeg",
        50: "/images/radar_avtomatik_radar_m_ahid_vasit_l_ri_/img_p7_1.jpeg"
    },
    "xususi/b_t_n_d_niz_il_r_n_t_hl_k_sizlik_zr_tan_.json": {
        12: "/images/b_t_n_d_niz_il_r_n_t_hl_k_sizlik_zr_tan_/img_p2_1.jpeg"
    },
    "xususi/tanisliq_ilkin_hazirliq.json": {
        12: "/images/b_t_n_d_niz_il_r_n_t_hl_k_sizlik_zr_tan_/img_p2_1.jpeg"
    }
}

def parse_docx_file(docx_path):
    doc = docx.Document(docx_path)
    questions = {}
    curr_q = None
    
    for para in doc.paragraphs:
        text = clean_text(para.text)
        if not text: continue
        
        q_match = re.match(r'^\s*(\d+)\.\s*(.*)', text)
        opt_match = re.match(r'^\s*([A-Da-d])[\)\.]\s*(.*)', text)
        
        if q_match and not opt_match:
            if curr_q:
                questions[curr_q['id']] = curr_q
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
            
            is_bold = any(r.bold for r in para.runs if r.text.strip())
            is_red = any(r.font.color and r.font.color.rgb and r.font.color.rgb[0] > 150 for r in para.runs if r.text.strip())
            is_hl = any(r.font.highlight_color for r in para.runs if r.text.strip())
            
            if is_bold or is_red or is_hl:
                curr_q['correct_answer'] = opt_key
                
    if curr_q:
        questions[curr_q['id']] = curr_q
        
    return questions

def parse_pdf_file(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = "\n".join([page.get_text() for page in doc])
    
    matches = list(re.finditer(r'(?:^|\n)\s*(\d+)\.\s+', full_text))
    questions = {}
    
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i+1 < len(matches) else len(full_text)
        q_num = int(matches[i].group(1))
        block = full_text[start:end].strip()
        
        parts = re.split(r'Düzgün\s+cavab\s*:\s*', block, flags=re.IGNORECASE)
        if len(parts) >= 2:
            q_text = clean_text(parts[0])
            q_text = re.sub(r'^\s*\d+\.\s*', '', q_text)
            ans_text = clean_text(parts[1].split('\n\n')[0])
            ans_text = re.sub(r'\s*\d+\.\s+.*$', '', ans_text, flags=re.DOTALL).strip()
            
            opts = {}
            opt_matches = list(re.finditer(r'(?:^|\n)\s*([A-Da-d])[\)\.]\s*(.*)', q_text))
            if opt_matches:
                for om in opt_matches:
                    opts[om.group(1).upper()] = clean_text(om.group(2))
                q_text = q_text[:opt_matches[0].start()].strip()
                
            questions[q_num] = {
                'id': q_num,
                'question': q_text,
                'options': opts,
                'correct_answer_text': ans_text
            }
        else:
            q_text = clean_text(block)
            q_text = re.sub(r'^\s*\d+\.\s*', '', q_text)
            questions[q_num] = {
                'id': q_num,
                'question': q_text,
                'options': {},
                'correct_answer_text': None
            }
            
    return questions

# Run Master Audit & Fix
print("Starting Master Audit across all 39 source files...\n")

total_sources_processed = 0
total_json_files_updated = 0
total_answers_corrected = 0
total_images_assigned = 0
total_images_cleaned = 0

audit_log = []

for sf, target_jsons in SOURCE_TO_JSON.items():
    src_path = os.path.join(src_dir, sf)
    if not os.path.exists(src_path):
        print(f"WARNING: Source file missing: {sf}")
        continue
        
    total_sources_processed += 1
    
    if sf.endswith(".docx"):
        src_questions = parse_docx_file(src_path)
    elif sf.endswith(".pdf"):
        src_questions = parse_pdf_file(src_path)
    else:
        continue
        
    for rel_json in target_jsons:
        json_path = os.path.join(json_base, rel_json)
        if not os.path.exists(json_path):
            print(f"WARNING: Target JSON missing: {rel_json}")
            continue
            
        with open(json_path, 'r', encoding='utf-8') as fp:
            jdata = json.load(fp)
            
        jqs = jdata.get('questions', [])
        file_modified = False
        img_map_for_file = JSON_IMAGE_ASSIGNMENTS.get(rel_json, {})
        
        for idx, jq in enumerate(jqs, 1):
            q_id = jq.get('id', f'q{idx:03d}')
            
            # 1. Audit Image URL
            expected_img = img_map_for_file.get(idx)
            curr_img = jq.get('image_url')
            
            if expected_img:
                if curr_img != expected_img:
                    jq['image_url'] = expected_img
                    file_modified = True
                    total_images_assigned += 1
                    audit_log.append(f"[{rel_json}] Q{idx} ({q_id}): Assigned image_url -> {expected_img}")
            else:
                if curr_img is not None:
                    # Remove invalid or outdated image assignment
                    del jq['image_url']
                    file_modified = True
                    total_images_cleaned += 1
                    audit_log.append(f"[{rel_json}] Q{idx} ({q_id}): Removed invalid image_url '{curr_img}'")
                    
            # 2. Audit Correct Answer
            src_q = src_questions.get(idx)
            if src_q:
                # If DOCX source with explicit correct_answer key ('A', 'B', 'C', 'D')
                if src_q.get('correct_answer'):
                    src_ans_key = src_q['correct_answer']
                    if jq.get('correct_answer') != src_ans_key:
                        audit_log.append(f"[{rel_json}] Q{idx} ({q_id}): Corrected answer from '{jq.get('correct_answer')}' to '{src_ans_key}' (Source DOCX)")
                        jq['correct_answer'] = src_ans_key
                        file_modified = True
                        total_answers_corrected += 1
                        
                # If PDF source with Düzgün cavab: <text>
                elif src_q.get('correct_answer_text'):
                    ans_text = src_q['correct_answer_text']
                    j_opts = jq.get('options', {})
                    
                    # Find option key matching ans_text best
                    best_opt = None
                    best_score = 0.0
                    for opt_k, opt_v in j_opts.items():
                        score = similarity(ans_text, opt_v)
                        if score > best_score:
                            best_score = score
                            best_opt = opt_k
                            
                    if best_opt and best_score >= 0.65:
                        if jq.get('correct_answer') != best_opt:
                            audit_log.append(f"[{rel_json}] Q{idx} ({q_id}): Corrected answer from '{jq.get('correct_answer')}' to '{best_opt}' (Düzgün cavab text: '{ans_text}')")
                            jq['correct_answer'] = best_opt
                            file_modified = True
                            total_answers_corrected += 1

        if file_modified:
            total_json_files_updated += 1
            with open(json_path, 'w', encoding='utf-8') as fp:
                json.dump(jdata, fp, ensure_ascii=False, indent=2)
            print(f"UPDATED: {rel_json}")
        else:
            print(f"NO CHANGES NEEDED: {rel_json}")

print("\n================ Master Audit Summary ================")
print(f"Total Source Files Processed: {total_sources_processed}")
print(f"Total JSON Files Updated: {total_json_files_updated}")
print(f"Total Correct Answer Values Fixed: {total_answers_corrected}")
print(f"Total Images Assigned to Questions: {total_images_assigned}")
print(f"Total Erroneous Images Cleaned: {total_images_cleaned}")
print("\n--- Audit Log Highlights (First 40) ---")
for log_entry in audit_log[:40]:
    print("  *", log_entry)
