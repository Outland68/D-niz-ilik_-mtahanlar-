import os, fitz, docx, json, sys, re
from difflib import SequenceMatcher

sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari"
json_base = r"D:\Dənizçilik_İmtahanları\backend\static\questions"
backend_img_dir = r"D:\Dənizçilik_İmtahanları\backend\static\images"
frontend_img_dir = r"D:\Dənizçilik_İmtahanları\frontend\public\images"

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

# Map from JSON file to exact image dictionary {q_num: img_rel_url}
IMAGE_MAPS = {
    "xususi/elektron_x_rit_displeyinin_v_i_nformasiy.json": {
        # Page 1 img_p1_1.png is symbol FI (2) on page 1.
        # Page 2 img_p2_1.png is on page 2.
        # Page 4 img_p4_1.png, img_p4_2.png, img_p4_3.png, img_p4_4.png
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

print("Image map dictionary compiled.")
