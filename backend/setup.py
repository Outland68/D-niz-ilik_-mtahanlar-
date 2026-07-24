# -*- coding: utf-8 -*-
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth.models import User
from api.models import Category, Certificate

# ── 1. Create superuser if not exists ──────────────────
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Superuser created: admin / admin123")
else:
    print("Superuser 'admin' already exists.")

# ── 2. Re-seed categories ──────────────────────────────
Category.objects.all().delete()
c1 = Category.objects.create(name='Sıravi heyət hazırlığı üzrə',           icon_name='Anchor',    color='bg-blue-500/20 text-blue-400')
c2 = Category.objects.create(name='Xüsusi hazırlıq şəhadətnamələri üzrə',  icon_name='FileBadge', color='bg-emerald-500/20 text-emerald-400')
c3 = Category.objects.create(name='Sertifikat diplom üzrə',                 icon_name='Award',     color='bg-amber-500/20 text-amber-400')
print("Categories seeded.")

# ── 3. Xüsusi hazırlıq şəhadətnamələri üzrə (Category 2) ──
special_certs = {
    "Safety familiarization basic training and instruction for all seafarers": "xususi/safety_familiarization_en.json",
    "Gəmi sürücülərinin təkmilləşdirilməsi (istismar)": "xususi/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist.json",
    "Gəmi elektrik mexaniklərinin təkmilləşdirilməsi": "xususi/g_mi_elektrik_mexanikl_rinin_t_kmill_dir.json",
    "Gəmi mexaniklərinin təkmilləşdirilməsi (idarəetmə)": "xususi/g_mi_mexanikl_rinin_t_kmill_dirilm_si_id.json",
    "Gəmi sürücülərinin təkmilləşdirilməsi (idarəetmə)": "xususi/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist.json",
    "Gəmi mexaniklərinin təkmilləşdirilməsi (istismar səviyyəsində)": "xususi/g_mi_mexanikl_rinin_t_kmill_dirilm_si_is.json",
    "Əmniyyətli İdarəetmə Haqqında Beynəlxalq Məcəllə": "xususi/mniyy_tli_i_dar_etm_haqq_nda_beyn_lxalq_.json",
    "İzdihamın idarə olunması üzrə hazırlıq": "xususi/i_zdiham_n_idar_olunmas_zr_haz_rl_q.json",
    "İnert qaz sistemi": "xususi/inert_qaz_sistemi.json",
    "Yanğınla mübarizə geniş proqram üzrə": "xususi/yanginla_mubarize_genis.json",
    "Təhlükəli və zərərli yüklərin daşınması": "xususi/t_hl_k_li_v_z_r_rli_y_kl_rin_da_nmas.json",
    "Sərnişinlərə bilavasitə xidmət göstərən heyət üyələri": "xususi/s_rni_inl_r_bilavasit_xidm_t_g_st_r_n_he.json",
    "Sərnişinlərin, yükün və gəmi gövdəsinin təhlükəsizliyi üzrə hazırlıq": "xususi/s_rni_inl_rin_y_k_n_v_g_mi_g_vd_sinin_t_.json",
    "Sürətli xilasetmə qayıq mütəxəssisi": "xususi/s_r_tli_xilasetm_qay_q_m_t_x_ssisi.json",
    "Sürətli olmayan xilasedici qayıqlar və sallar üzrə mütəxəssis": "xususi/s_r_tli_olmayan_xilasedici_qay_qlar_v_sa.json",
    "Radar, avtomatik radar müşahidə vasitələri, kapitan körpüsü komandası və axtarış xilasetmə (idarəetmə səviyyəsində)": "xususi/radar_avtomatik_radar_m_ahid_vasit_l_ri_.json",
    "Radar müşahidəsi və təsviri, avtomatik radar müşahidəsi vasitələrinin istismarı (istismar səviyyəsində)": "xususi/radar_m_ahid_si_v_t_sviri_avtomatik_rada.json",
    "Qlobal Dəniz Fəlakət və Əmniyyətli Rabitə Sisteminin Ümumi Rayon Operatoru": "xususi/qlobal_d_niz_f_lak_t_v_mniyy_tli_rabit_s.json",
    "Neft və Kimyəvi-İlkin": "xususi/neft_v_kimy_vi_i_lkin.json",
    "Neft tankerlərində-geniş": "xususi/neft_tankerl_rind_geni.json",
    "Maşın şöbəsi resurslarının idarə olunması": "xususi/ma_n_b_si_resurslar_n_n_idar_olunmas.json",
    "Liman vasitələrinin mühafizəyə məsul": "xususi/liman_vasit_l_rinin_m_hafiz_y_m_sul.json",
    "Liderlik və birgə iş fəaliyyəti": "xususi/liderlik_v_birg_i_f_aliyy_ti.json",
    "Kimyəvi maddə daşıyan tankerlərdə yük əməliyyatlarına dair geniş proqram üzrə hazırlıq": "xususi/kimy_vi_madd_da_yan_tankerl_rd_y_k_m_liy.json",
    "Kapitan Körpüsü Resurslarının İdarə Olunması": "xususi/kapitan_k_rp_s_resurslar_n_n_i_dar_olunm.json",
    "ISPS-3": "xususi/isps_3.json",
    "ISPS-2": "xususi/isps2.json",
    "ISPS-1": "xususi/isps_1.json",
    "Gəminin idarə olunması və manevr edilməsi": "xususi/g_minin_idar_olunmas_v_manevr_edilm_si.json",
    "Gəmi əmniyyətliyi üzrə Məsul Şəxs": "xususi/g_mi_mniyy_tliyi_zr_m_sul_xs.json",
    "Gəmidə tibbi nəzarət": "xususi/g_mid_tibbi_n_zar_t.json",
    "Gəmidə ilk tibbi yardım": "xususi/g_mid_ilk_tibbi_yard_m.json",
    "Gəmi qazanalizatorları və onların istismarı": "xususi/g_mi_qazanalizatorlar_v_onlar_n_istismar.json",
    "Elektron Xəritə Displeyinin və İnformasiya Sistemlərinin İstismar Qaydaları": "xususi/elektron_x_rit_displeyinin_v_i_nformasiy.json",
    "Bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat": "xususi/tanisliq_ilkin_hazirliq.json",
    "Böhran zamanı idarəetmə və insan davranışı üzrə hazırlıq": "xususi/b_hran_zaman_idar_etm_v_insan_davran_zr_.json",
    "1000 volt və artıq olan gərginlik sistemlərinin təhlükəsiz istismarı və onlara texniki nəzarət": "xususi/1000_volt_v_art_q_olan_g_rginlik_sisteml.json",
    "Xam Neftlə Yuyulma Sistemi": "xususi/xam_neftl_yuyulma_sistemi.json"
}

for name, json_file in special_certs.items():
    Certificate.objects.create(category=c2, name=name, json_file=json_file)

print(f"Xüsusi hazırlıq şəhadətnamələri üzrə: {len(special_certs)} certificates seeded.")

# ── 4. Sertifikat diplom üzrə (Category 3) ──
cert_map = {
    "Axtarış xilasetmə əməliyyatların koordinasiyası (IAMSAR)":                                                    None,
    "Beynəlxalq dəniz hüququ":                                                                                      None,
    "Gəmilərin Toqquşmasının Qarşısını Alınmasına dair Beynalxalq Qaydalar (Colreg-72)":                           "certdip/colreg_72.json",
    "Gəminin dayanaqlığı":                                                                                          None,
    "Gəminin idarə edilməsi":                                                                                       None,
    "Naviqasiya təhlükələrin çəpərlənmə sistemi (IALA)":                                                           None,
    "Radar ARPA":                                                                                                   None,
    "Səfərin planlaşdırılması- Dənizçilik astronomiyası":                                                          None,
    "Səfərin planlaşdırılması-Meteorologiya":                                                                       None,
    "Səfərin planlaşdırılması - Naviqasiya":                                                                       None,
    "Yük əməliyyatları":                                                                                            None,
    "İngilis dili (göyərtə heyəti üçün)":                                                                         None,
    "Gəmi energetik qurğuları və onların istismarı":                                                               None,
    "Gəmi konstruksiyası və Gəmi dayanıqlılığı":                                                                   None,
    "Gəmi köməkçi buxar qazanları":                                                                                None,
    "Gəmi köməkçi mexanizmləri":                                                                                    None,
    "Gəmi soyuducu qurğuları":                                                                                      None,
    "İngilis dili (maşın heyəti üçün)":                                                                            None,
    "MARPOL 73-78":                                                                                                 "certdip/marpol_73_78.json",
    "Yanğından mühafizə və xilasedici vasitələr":                                                                  None,
    "Aşağı elektrik gərginliyi sistemləri":                                                                        None,
    "Baş mühərriklərin və köməkçi mexanizmlərin avtomatik idarəetmə sistemlərinin işinə nəzarət":                 None,
    "Bütün gəmidaxili rabitə sistemlərinin istismarı":                                                             None,
    "Elektrik generatorlarının və paylayıcı sistemlərinin istismarı":                                              None,
    "Elektrik sistemlərinin və avadanlıqlarının xüsusiyyətləri":                                                   None,
    "Elektrik və elektron avadanlıqlarının istismarı və texniki xidmətin göstərilməsi":                            None,
    "Elektrik və elektron avadanlığın istismarı":                                                                   None,
    "Elektrik və elektron nəzarət avadanlıqlarının idarəedilməsi":                                                 None,
    "Gəmi elektrik avadanlıqlarının istismarı":                                                                    None,
    "Gəmi mexaniki qurğularının iş prinsipinə dair anlayışlar":                                                    None,
}

for name, json_file in cert_map.items():
    Certificate.objects.create(category=c3, name=name, json_file=json_file)

print(f"Sertifikat diplom üzrə: {len(cert_map)} certificates seeded.")
print("\nDone!")
