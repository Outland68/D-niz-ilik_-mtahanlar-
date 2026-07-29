import json, os, shutil

json_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist.json'
backend_img_dir = r'D:\Dənizçilik_İmtahanları\backend\static\images\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist'
frontend_img_dir = r'D:\Dənizçilik_İmtahanları\frontend\public\images\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist'

os.makedirs(backend_img_dir, exist_ok=True)
os.makedirs(frontend_img_dir, exist_ok=True)

# Copy extracted page images with clear question names
extracted_dir = r'D:\Dənizçilik_İmtahanları\backend\static\images\gemi_idareetme_extracted'
if not os.path.exists(extracted_dir):
    extracted_dir = r'D:\Dənizçilik_İmtahanları\backend\static\images\gemi_suruculerinin_istismar'

image_mappings = {
    1: 'gemi_istismar_page_1_img_1.png',
    3: 'gemi_istismar_page_1_img_2.png',
    7: 'gemi_istismar_page_1_img_3.jpeg',
    9: 'gemi_istismar_page_2_img_1.png',
    10: 'gemi_istismar_page_2_img_2.jpeg',
    13: 'gemi_istismar_page_2_img_3.jpeg',
    17: 'gemi_istismar_page_3_img_1.png',
    18: 'gemi_istismar_page_3_img_2.jpeg',
    20: 'gemi_istismar_page_3_img_3.jpeg',
    21: 'gemi_istismar_page_3_img_4.jpeg',
    22: 'gemi_istismar_page_4_img_1.jpeg',
    23: 'gemi_istismar_page_4_img_2.jpeg',
    24: 'gemi_istismar_page_4_img_3.jpeg',
    27: 'gemi_istismar_page_5_img_1.jpeg',
    29: 'gemi_istismar_page_5_img_2.jpeg',
    30: 'gemi_istismar_page_5_img_3.jpeg'
}

# Copy images to backend and frontend
for q_num, src_file in image_mappings.items():
    src_path = os.path.join(extracted_dir, src_file)
    ext = os.path.splitext(src_file)[1]
    dest_filename = f'q_{q_num:03d}{ext}'
    
    dest_b = os.path.join(backend_img_dir, dest_filename)
    dest_f = os.path.join(frontend_img_dir, dest_filename)
    
    if os.path.exists(src_path):
        shutil.copy(src_path, dest_b)
        shutil.copy(src_path, dest_f)
        print(f"Copied image for Sual {q_num}: {dest_filename}")

# Update JSON file
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data.get('questions', [])

# Remove all existing image_url
for q in questions:
    if 'image_url' in q:
        del q['image_url']

# Assign correct image_url based on exact user directives & PDF matching
for q in questions:
    # Get question number from question text (e.g., "1. Şəkildə...")
    q_str = q.get('question', '').strip()
    q_num = None
    try:
        q_num = int(q_str.split('.')[0])
    except:
        pass

    if q_num in image_mappings:
        ext = os.path.splitext(image_mappings[q_num])[1]
        q['image_url'] = f"/images/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist/q_{q_num:03d}{ext}"
        print(f"✅ Linked Sual {q_num} -> {q['image_url']}")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("🎉 JSON successfully updated with perfect image mappings!")
