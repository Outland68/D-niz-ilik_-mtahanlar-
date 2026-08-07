import json
import random

json_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_id.json"
out_path = json_path

# Read existing JSON
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

random.seed(33327)

distractors_map = {
    "q001": [
        "buzun təbəqələşmə dərəcəsi",
        "buzun dreyf sürəti və istiqaməti",
        "buzun sıxılma ehtimalı"
    ],
    "q002": [
        "bəli, ancaq VHF əhatə dairəsində hədəflər aktiv rejimdə olduqda",
        "xeyr, çünki radio dalğaları optik görünüş xəttindən asılıdır",
        "bəli, lakin yalnız VTS mərkəzinin təkrar ötürücü stansiyaları vasitəsilə"
    ],
    "q003": [
        "sahildən 12 mil məsafədə, xüsusi zonalar xaricində hərəkət edərkən",
        "gəmidəki tullantı yandırıcısı (incinerator) nasaz olduqda",
        "xüsusi zonalarda yalnız qida tullantıları ilə qarışdırıldıqda"
    ],
    "q004": [
        "sahil dövlətinin daxili suları ilə ərazi sularını ayıran koordinat xətti",
        "eksklüziv iqtisadi zonanın daxili sərhədini müəyyən edən şərti xətt",
        "beynəlxalq boğazlarda ayrılmış hərəkət zolaqlarının mərkəzi xətti"
    ],
    "q005": [
        "Yalnız təhlükəli yüklər (IMDG Code) daşıyan xüsusi təyinatlı gəmilər üçün",
        "Limana giriş icazəsi istəyən bütün daxili və beynəlxalq gəmilər üçün",
        "Yalnız ISM məcəlləsinin tələblərinə uyğun gəlməyən riskli gəmilər üçün"
    ],
    "q006": [
        "gəminin fırlaq momenti (metasentrik hündürlüyü) kəskin şəkildə artır",
        "yırğalanma periodu kiçilir və gəmi ani olaraq tarazlığa qayıdır",
        "sərbəst səthlərin təsiri nəticəsində dalğaya qarşı müqavimət yüksəlir"
    ],
    "q007": [
        "Beynəlxalq tonaj şəhadətnaməsi (ITC-69)",
        "Gəmi konstruksiyasının təhlükəsizliyi haqqında şəhadətnamə",
        "Gəminin dənizə yararlılıq haqqında təsnifat cəmiyyətinin aktı"
    ],
    "q008": [
        "kapitanın qərarı ilə yalnız 3 nüsxədən ibarət olmaqla",
        "fraxt müqaviləsinə uyğun olaraq maksimum 5 orijinal nüsxə",
        "yük sahibinin tələbi əsasında qeyri-məhdud sayda, eyni seriya ilə"
    ],
    "q009": [
        "Azor adaları və Kanar adaları arasındakı antisiklon zonasında",
        "Nyufaundlend adasının cənub-şərq akvatoriyasında",
        "Süveyş kanalından Cəbəllütariq boğazına gedən yolda"
    ],
    "q010": [
        "genişlənən kvadrat axtarışı (Expanding square search)",
        "koordinatlı sektor axtarışı (Sector search)",
        "təqib edən axtarış modeli (Track line search)"
    ],
    "q011": [
        "yalnız STCW konvensiyasının VI fəslinə aid olan dənizçilərə",
        "ISM məcəlləsinə görə məsul olan bütün şirkət nümayəndələrinə",
        "yalnız qlobal dəniz fəlakət rabitəsi (GMDSS) operatorlarına"
    ],
    "q012": [
        "güclü qütb antisiklonu",
        "yerli termal qabarma tufanı",
        "genişmiqyaslı duman zolağının yaranması"
    ],
    "q013": [
        "gəminin qeydiyyatda olduğu Bayraq Dövləti İdarəsinə (Administration)",
        "yükün sığorta şirkətinə (P&I Club) və fraxtedənə",
        "təhlükəli yüklərin beynəlxalq dəniz qeydiyyatı mərkəzinə (IMDG Center)"
    ],
    "q014": [
        "gəminin eninə metasantr hündürlüyünün daim müsbət saxlanması ilə",
        "ballast sularının idarəetmə planına əsasən tankların doluluq səviyyəsi ilə",
        "yük markasının (Plimsoll line) batma səviyyəsinin yoxlanması ilə"
    ],
    "q015": [
        "Əlavə 1 (Neftlə çirklənmənin qarşısının alınması)",
        "Əlavə 4 (Gəmi çirkab suları ilə çirklənmənin qarşısının alınması)",
        "Əlavə 6 (Havanın gəmilər tərəfindən çirklənməsinin qarşısının alınması)"
    ],
    "q016": [
        "sərbəst səth effekti yaranmasın deyə bütün ballast tanklarını boşaltmaq",
        "baş mühərrikləri tam gücü ilə “arxaya” (Full Astern) rejimində işlətmək",
        "gəminin xilasedici vasitələrini suya salıb heyəti təcili təxliyə etmək"
    ],
    "q017": [
        "mən öz kursumu sağa (starboard) dəyişirəm",
        "mən hərəkət edə bilmirəm, mənə yol verin",
        "mən öz kursumu sola (port) dəyişirəm"
    ],
    "q018": [
        "sükan diametral müstəvidə (midships) və kurs 218º olsun",
        "sükan sol borta və gəmi sürəti 21.8 uzel olsun",
        "sağ borta tərəf yavaş-yavaş (slow ahead) 218 fırlanma ilə irəli"
    ],
    "q019": [
        "antisiklonik cərəyan modeli",
        "ekvatorial dumanlı front",
        "qütb hava kütlələrinin hərəkəti"
    ],
    "q020": [
        "2",
        "4",
        "qurğu ümumiyyətlə yanalma üçün deyil"
    ],
    "q021": [
        "buzun dreyf istiqamətini",
        "su səthinin donma temperaturunu",
        "buz kütləsinin qırılma ehtimalını"
    ],
    "q022": [
        "1-nömrəli hədəf",
        "3-nömrəli hədəf",
        "4-nömrəli hədəf"
    ],
    "q023": [
        "La-Manş boğazının qərb çıxışında",
        "Berinq dənizinin cənub hissəsində",
        "Madaqaskar adasının şərq sahillərində"
    ],
    "q024": [
        "my course over ground is zero, three, seven",
        "I am turning to starboard zero, three, seven",
        "my bearing to the target is zero, three, seven"
    ],
    "q025": [
        "yalnız 500 registr ton və artıq olan beynəlxalq səfər edən gəmilərdə",
        "sahilyanı sular daxilində (A1 rayonu) üzən bütün ticarət gəmilərində",
        "yalnız sərnişin və təhlükəli yük daşıyan ro-ro tipli gəmilərdə"
    ],
    "q026": [
        "Şimal koordinal buyu",
        "Şərq koordinal buyu",
        "Təhlükəsiz sular (Safe water) buyu"
    ],
    "q027": [
        "0° ön (Head on)",
        "180° arxa (Astern)",
        "90° sağ bort (Starboard beam)"
    ],
    "q028": [
        "manevr qabiliyyəti məhdud olan gəmi (RAM)",
        "sualtı əməliyyat və ya tral çəkən gəmi",
        "lövbərdə dayanaraq yük əməliyyatı edən gəmi"
    ],
    "q029": [
        "gəminin diametral müstəvisindən hər iki borta 135° olmaqla cəmi 270°",
        "yalnız sağ və sol bortlara 112,5° olmaqla ümumilikdə 225°",
        "bütün üfüq boyu 360° kəsintisiz sektor"
    ],
    "q030": [
        "hədəfin kursu 310°, sürəti 10 düyün",
        "hədəfin kursu 090°, sürəti 15 düyün",
        "hədəfin kursu 180°, sürəti 12 düyün"
    ],
    "q031": [
        "gəmi hərəkət edərkən mühərrik dayandıqda",
        "dar kanalda qarşıdan gələn gəmini xəbərdar etdikdə",
        "lövbərə qalxmazdan dərhal əvvəl xəbərdarlıq kimi"
    ],
    "q032": [
        "pelenq kəsişmə xətti (EBL)",
        "paralel indeks xətti (PI)",
        "hədəfin nisbi hərəkət vektoru (RM)"
    ],
    "q033": [
        "Şimal-qərbə",
        "Cənub-şərqə",
        "Cənub-qərbə"
    ],
    "q034": [
        "Rolks (Roller fairlead)",
        "Knext (Bollard)",
        "Klyuz (Hawsepipe)"
    ],
    "q035": [
        "“B”",
        "“D”",
        "“E”"
    ],
    "q036": [
        "Laylı-yağışlı buludlar (Nimbostratus)",
        "Topa-yağışlı buludlar (Cumulonimbus)",
        "Yüksək-qatlı buludlar (Altostratus)"
    ],
    "q037": [
        "Gəminin manevr qabiliyyəti məhduddur",
        "Gəmi sualtı kabellərin çəkilməsi ilə məşğuldur",
        "Gəmi minadan təmizləmə əməliyyatı həyata keçirir"
    ],
    "q038": [
        "Gəmi limana tam yan aldıqdan və mühərriklər dayandıqdan sonra",
        "Növbəti köməkçi körpüyə qalxdığı ilk anda",
        "Gəmi lövbər saldıqdan sonra kapitan körpünü tərk etdikdə"
    ],
    "q039": [
        "Kurs 218,0 °, sürət 12,5 düyün",
        "Kurs 038,0 °, sürət 0 düyün",
        "Kurs 180,0 °, sürət 15,0 düyün"
    ],
    "q040": [
        "hər səfərdən əvvəl liman nəzarəti tərəfindən",
        "hər 5 ildən bir gəminin sinif yenilənməsində",
        "hər 6 aydan bir xüsusi təsdiqlənmiş laboratoriyada"
    ],
    "q041": [
        "şərq tərəfdən",
        "qərb tərəfdən",
        "şimal tərəfdən"
    ],
    "q042": [
        "“MAYDAY”",
        "“SECURITE”",
        "“SILENCE FINI”"
    ],
    "q043": [
        "təcrid olunmuş təhlükə buyu",
        "sağ tərəf (starboard) lateral buyu",
        "təhlükəsiz su (safe water) buyu"
    ],
    "q044": [
        "90°",
        "60°",
        "45°"
    ],
    "q045": [
        "gəmidə gömrük və sərhəd yoxlaması aparılarkən",
        "gəmi təhlükəli yüklərlə əməliyyat apararkən",
        "gəmidə infeksion xəstəlik olmaması barədə karantin siqnalı verərkən"
    ],
    "q046": [
        "buyu sol bortda saxla",
        "buyu birbaşa diametral kəsikdə qarşıla",
        "buydan tamamilə uzaqlaş (clear the buoy)"
    ]
}

for item in data["questions"]:
    correct_letter = item["correct_answer"]
    correct_text = item["options"][correct_letter]
    
    qid = item["id"]
    if qid in distractors_map:
        d_list = distractors_map[qid][:3]
        all_options = [correct_text] + d_list
        random.shuffle(all_options)
        
        new_opts = {}
        letters = ["A", "B", "C", "D"]
        for i, val in enumerate(all_options):
            new_opts[letters[i]] = val
            if val == correct_text:
                item["correct_answer"] = letters[i]
        
        item["options"] = new_opts

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Rebuilt JSON for {len(data['questions'])} questions.")
