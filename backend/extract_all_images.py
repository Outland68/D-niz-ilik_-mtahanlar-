import os, fitz, docx, sys, json, shutil

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"
backend_img_dir = r"D:\Dənizçilik_İmtahanları\backend\static\images"
frontend_img_dir = r"D:\Dənizçilik_İmtahanları\frontend\public\images"

os.makedirs(backend_img_dir, exist_ok=True)
os.makedirs(frontend_img_dir, exist_ok=True)

# Define map from PDF filename to folder name
file_to_folder = {
    'Elektron Xəritə Displeyinin və İnformasiya Sistemlərinin İstismar Qaydaları.pdf': 'elektron_x_rit_displeyinin_v_i_nformasiy',
    'Gəmi elektrik mexaniklərinin təkmilləşdirilməsi.pdf': 'g_mi_elektrik_mexanikl_rinin_t_kmill_dir',
    'Gəmi mexaniklərinin təkmilləşdirilməsi (idarəetmə).pdf': 'g_mi_mexanikl_rinin_t_kmill_dirilm_si_id',
    'Gəmi mexaniklərinin təkmilləşdirilməsi (istismar səviyyəsində).pdf': 'g_mi_mexanikl_rinin_t_kmill_dirilm_si_is',
    'Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf': 'g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist',
    'Gəmidə tibbi nəzarət.pdf': 'g_mid_tibbi_n_zar_t',
    'Radar, avtomatik radar müşahidə vasitələri, kapitan körpüsü komandası və axtarış xilasetmə (idarəetmə səviyyəsində).pdf': 'radar_avtomatik_radar_m_ahid_vasit_l_ri_',
    'bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat.pdf': 'b_t_n_d_niz_il_r_n_t_hl_k_sizlik_zr_tan_'
}

extracted_summary = {}

for sf, folder in file_to_folder.items():
    path = os.path.join(src_dir, sf)
    if not os.path.exists(path):
        print(f"File not found: {sf}")
        continue
    
    b_target = os.path.join(backend_img_dir, folder)
    f_target = os.path.join(frontend_img_dir, folder)
    os.makedirs(b_target, exist_ok=True)
    os.makedirs(f_target, exist_ok=True)
    
    doc = fitz.open(path)
    extracted_summary[folder] = []
    
    for pno in range(len(doc)):
        page = doc[pno]
        ilist = page.get_images(full=True)
        for idx, img in enumerate(ilist, 1):
            xref = img[0]
            base_img = doc.extract_image(xref)
            image_bytes = base_img["image"]
            image_ext = base_img["ext"]
            
            fname = f"img_p{pno+1}_{idx}.{image_ext}"
            b_path = os.path.join(b_target, fname)
            f_path = os.path.join(f_target, fname)
            
            with open(b_path, "wb") as fp:
                fp.write(image_bytes)
            with open(f_path, "wb") as fp:
                fp.write(image_bytes)
                
            extracted_summary[folder].append({
                "page": pno + 1,
                "index": idx,
                "filename": fname,
                "ext": image_ext,
                "size": len(image_bytes)
            })

print("\n--- IMAGE EXTRACTION SUMMARY ---")
total_extracted = 0
for folder, imgs in extracted_summary.items():
    print(f"Folder '{folder}': {len(imgs)} images extracted.")
    total_extracted += len(imgs)
    for im in imgs:
        print(f"  - Page {im['page']}, Index {im['index']} -> {im['filename']} ({im['size']} bytes)")

print(f"\nTOTAL EXTRACTED IMAGES: {total_extracted}")
