import os, fitz, json, sys

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"
json_base = r"D:\Dənizçilik_İmtahanları\backend\static\questions"

mappings_to_verify = [
    ("Elektron Xəritə Displeyinin və İnformasiya Sistemlərinin İstismar Qaydaları.pdf", "xususi/elektron_x_rit_displeyinin_v_i_nformasiy.json"),
    ("Gəmi elektrik mexaniklərinin təkmilləşdirilməsi.pdf", "xususi/g_mi_elektrik_mexanikl_rinin_t_kmill_dir.json"),
    ("Gəmi mexaniklərinin təkmilləşdirilməsi (idarəetmə).pdf", "xususi/g_mi_mexanikl_rinin_t_kmill_dirilm_si_id.json"),
    ("Gəmi mexaniklərinin təkmilləşdirilməsi (istismar səviyyəsində).pdf", "xususi/g_mi_mexanikl_rinin_t_kmill_dirilm_si_is.json"),
    ("Gəmi sürücülərinin təkmilləşdirilməsi (istismar).pdf", "xususi/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist.json"),
    ("Gəmidə tibbi nəzarət.pdf", "xususi/g_mid_tibbi_n_zar_t.json"),
    ("Radar, avtomatik radar müşahidə vasitələri, kapitan körpüsü komandası və axtarış xilasetmə (idarəetmə səviyyəsində).pdf", "xususi/radar_avtomatik_radar_m_ahid_vasit_l_ri_.json"),
    ("bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat.pdf", "xususi/b_t_n_d_niz_il_r_n_t_hl_k_sizlik_zr_tan_.json")
]

for pdf_name, json_rel in mappings_to_verify:
    pdf_p = os.path.join(src_dir, pdf_name)
    json_p = os.path.join(json_base, json_rel)
    
    doc = fitz.open(pdf_p)
    with open(json_p, 'r', encoding='utf-8') as fp:
        jdata = json.load(fp)
    qs = jdata.get('questions', [])
    
    print(f"\n==================================================")
    print(f"PDF: {pdf_name}")
    print(f"JSON: {json_rel} ({len(qs)} questions)")
    
    for pno in range(len(doc)):
        page = doc[pno]
        ilist = page.get_images()
        if not ilist: continue
        
        # print text on page line by line
        lines = [line.strip() for line in page.get_text().split('\n') if line.strip()]
        print(f"\n--- Page {pno+1}: {len(ilist)} image(s) ---")
        for line in lines:
            if line[0].isdigit() and ('.' in line[:4] or ' ' in line[:4]):
                print(f"   Q line: {line}")
            elif any(w in line.lower() for w in ['şəkil', 'düzgün cavab', 'hansı', 'şəkildə']):
                print(f"   Text line: {line}")
