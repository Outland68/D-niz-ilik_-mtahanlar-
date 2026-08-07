import json
import random

CERT_NAME = "Gəmi sürücülərinin təkmilləşdirilməsi (istismar)"

raw_data = [
    {
        "q": "Şəkildə nəyin işarəsi verilib?",
        "c": "\"okklyuziya\" cəbhəsinin;",
        "w": ["soyuq cəbhənin;", "isti cəbhənin;", "stasionar cəbhənin;"]
    },
    {
        "q": "Dünya okeanında qüvvətli və davamlı, 2-5 düyün sürəti olan cərəyanı qeyd edin.",
        "c": "Qolfstrim",
        "w": ["Kurosio", "Şimali Passat", "Kanar"]
    },
    {
        "q": "Xəritədə çəhrayı rəngdə qeyd edilmiş simvolu açıqlayın.",
        "c": "tayfun",
        "w": ["antisiklon", "isti cəbhə", "zəif külək sahəsi"]
    },
    {
        "q": "Farvaterə dənizdən daxil olarkən (reqion A) farvaterin solunda olan buyların hansı rəqəmlərlə nömrələnir ?",
        "c": "tək",
        "w": ["cüt", "rum rəqəmləri ilə", "hərflərlə"]
    },
    {
        "q": "Xarici təzyiqin azalması halında maye yüklərin qaynama temperaturu necə dəyişir?",
        "c": "azalır",
        "w": ["artır", "dəyişməz qalır", "əvvəl artır, sonra azalır"]
    },
    {
        "q": "“Boarding arrangements” termininə uyğun olan tərifi qeyd edin.",
        "c": "losmanın təhlükəsizliyini təmin edən losman “trapı”, mərasim “trapı” və digər vasitələr",
        "w": ["gəminin yük əməliyyatları üçün istifadə olunan kran avadanlığı", "gəminin sahilə yan alması üçün burazlama sistemi", "gəminin ballast sularının idarəetmə planı"]
    },
    {
        "q": "Hidrokostyumda hansı hündürlükdən suya təhlükəsiz tullanmaq olar?",
        "c": "4,5 metr",
        "w": ["2 metr", "8 metr", "12 metr"]
    },
    {
        "q": "Qeyd edilən hansı amil qaydaların tələblərinin yerinə yetirilməməsinə səbəb ola bilər?",
        "c": "bilavasitə təhlükə",
        "w": ["şiddətli külək", "görünüşün məhdudlaşması", "texniki nasazlıq"]
    },
    {
        "q": "Hava şəraiti haqqında xəritədə göstərilən Hind okeanının şərq hissəsində yaranan “Frontal” siklon necə adlandırılır?",
        "c": "çox mərkəzli (iki mərkəzli)",
        "w": ["tək mərkəzli", "tropik fırtına", "antisiklon"]
    },
    {
        "q": "Hansı gəminin işıqlarını müşahidə edirsiniz?",
        "c": "“Laq” üsulu ilə yedək əməliyyatı ilə məşğul olan gəmi, yedək gəmisinin uzunluğu 50 m-dən azdır, hərəkəti üstümüzədir",
        "w": ["Yedəyindəki obyektin uzunluğu 200 m-dən çox olan gəmi, lövbərdədir", "Manevr etmək qabiliyyəti məhdud olan gəmi, sol bortunu göstərir", "Saya oturmuş gəmi, uzunluğu 50 m-dən çoxdur"]
    },
    {
        "q": "Cümləni tamamlayın: “What is the ……. of the derricks of the vessel?”",
        "c": "capacity",
        "w": ["length", "distance", "bearing"]
    },
    {
        "q": "Uyğun gələn söz önünü seçin: “Dispose the sludge ….. the sludge tank.”",
        "c": "into",
        "w": ["above", "under", "through"]
    },
    {
        "q": "Şəkildə göstərilən naviqasiya xəritələrində istifadə edilən şərti işarənin düzgün mənasını qeyd edin.",
        "c": "radiolokasiya bazis xətti",
        "w": ["təhlükəli dərinlik xətti", "tövsiyə olunan kurs", "sualtı kabel xətti"]
    },
    {
        "q": "Gəmilərdə təhlükəli yüklərlə iş üzrə təlimat nə zaman aparılmalıdır?",
        "c": "əmniyyətliliyin idarə edilməsi sistemin tələblərinə uyğun olaraq",
        "w": ["yükləmə əməliyyatı başa çatdıqdan dərhal sonra", "açıq dənizə çıxışdan 24 saat əvvəl", "gəmi limana çatana qədər hər gün"]
    },
    {
        "q": "“Blind sector” termininə uyğun olan tərifi qeyd edin:",
        "c": "gəmi RLS ilə müşahidə edilməyən sahə",
        "w": ["naviqasiya xəritəsində qeyd olunmamış dərinlik", "suyun altında qalan görünməz maneə", "maqnit kompasının əyilməsi zonasındakı sahə"]
    },
    {
        "q": "Hava şəraiti haqqında xəritənin məlumatına görə Sakit okeanın şimal-qərb hissəsində “NOCK TEN” adlı tropik fırtınanın ən çox ehtimal edildiyi hərəkət istiqamətini qeyd edin:",
        "c": "şimal - qərb istiqamətində",
        "w": ["cənub - şərq istiqamətində", "şərq istiqamətində", "cənub - qərb istiqamətində"]
    },
    {
        "q": "Şəkildə göstərilən naviqasiya xəritələrində istifadə edilən şərti işarənin düzgün mənasını qeyd edin?",
        "c": "hərəkətin bölünmə sisteminin sərhədi",
        "w": ["bataqlıq ərazisi", "atış təlimləri zonası", "gəmilərin dayanacaq yeri"]
    },
    {
        "q": "Dənizdə insan həyatının qorunması haqqında” (SOLAS) Beynəlxalq Konvensiyanın tələblərinə uyğun olaraq gəmidə su ilə mübarizə üzrə təlimlərin keçirilməsi müddətini qeyd edin:",
        "c": "Beynəlxalq Konvensiyada bu tələb yoxdur",
        "w": ["hər ayda bir dəfə", "hər 3 aydan bir", "yalnız yeni heyət gəldikdə"]
    },
    {
        "q": "“Inoperative” termininə uyğun olan tərifi qeyd edin:",
        "c": "işləməyən, fəaliyyət göstərməyən",
        "w": ["tam işlək vəziyyətdə olan", "müvəqqəti təmirə ehtiyacı olan", "avtomatik rejimdə işləyən"]
    },
    {
        "q": "Gəmidən insanları vertolyotla qaldırmaq üçün gəmi göyərtəsinin bir hissəsi hansı hərf ilə nişanlanmalıdır?",
        "c": "ağ rəngli böyük “H” hərfi ilə",
        "w": ["qırmızı rəngli böyük “V” hərfi ilə", "sarı rəngli böyük “R” hərfi ilə", "mavi rəngli böyük “L” hərfi ilə"]
    },
    {
        "q": "“NAVTEX” qəbuledicinin çap menyusundan hansı məlumatları operator çıxara bilməz?",
        "c": "axtarış və xilasetmə üzrə məlumatları",
        "w": ["naviqasiya xəbərdarlıqlarını", "hava proqnozlarını", "buz şəraiti haqqında məlumatları"]
    },
    {
        "q": "“GMDSS” sisteminə aid fəlakət hallarında radio əlaqəyə öz işləri ilə maneə olan stansiyalara “işlərini dayandırmaq” göstərişi hansı ardıcıllıqla verilir? 1. “MAY DAY”; 2. “ALL STATION”; 3. “işlərini dayandırmaq” göstərişini verən stansiyanın adı və ya çağırış siqnalı; 4. “THIS IS”.",
        "c": "1, 2, 4, 3",
        "w": ["1, 3, 2, 4", "2, 1, 4, 3", "4, 3, 2, 1"]
    },
    {
        "q": "Gəmidən müvafiq vizual vasitələrlə ötürülən “X” siqnalı nəyi ifadə edir?",
        "c": "Tibbi yardım tələb olunur",
        "w": ["Mən sürətimi azaldıram", "Gəmimdə yanğın var", "Dərhal lövbər salıram"]
    },
    {
        "q": "Fəlakət rayonlarında “GMDSS” sisteminə aid radio əlaqənin məhdudlaşdırılması göstərişini ifadə edən siqnalı qeyd edin?",
        "c": "“PRUDONCE”",
        "w": ["“SEELONCE FEENEE”", "“SILENCE MAYDAY”", "“RESTRICTED RADIO”"]
    },
    {
        "q": "Gəmidən insanın dənizə düşdüyü hallarda dərhal yerinə yetirilən gəmi manevrləri hansılardır?",
        "c": "“Anderson” manevri, “Uilyamson” manevri",
        "w": ["“Ziq-zaq” manevri", "“Sirkulyasiya” manevri", "“Qəfil dayanma” manevri"]
    },
    {
        "q": "Gəminin “Laq”ın göstəricisinə görə keçdiyi məsafə 64 mildir, “Laq”ın əmsalı K= 0,95. Gəminin keçdiyi həqiqi məsafəni qeyd edin?",
        "c": "60,8 mil",
        "w": ["67,3 mil", "64,0 mil", "62,5 mil"]
    },
    {
        "q": "Siz 1 saylı gəmidəsiniz. Şəkildə sizin gəminizin həqiqi kursu hansı hərf ilə qeyd edilmişdir?",
        "c": "A",
        "w": ["B", "C", "D"]
    },
    {
        "q": "“MAMS” çəpərləmə sistemində istifadə edilən farvaterlərin sağ və sol tərəflərini göstərən işarələr necə adlandırılır?",
        "c": "“Lateral”",
        "w": ["“Kardinal”", "“Təhlükəli”", "“Xüsusi nişanlar”"]
    },
    {
        "q": "Gəmidə avtosükanın texniki vəziyyətinə kim cavabdehdir?",
        "c": "Elektrik mexaniki",
        "w": ["Baş şturman", "Kapitan köməkçisi", "Göyərtə komandası"]
    },
    {
        "q": "“GMDSS” sisteminə aid “normal” radio əlaqənin icazə verən siqnalını qeyd edin.",
        "c": "“SEELONCE FEENEE”",
        "w": ["“MAYDAY RELAY”", "“PAN PAN”", "“SECURITE”"]
    },
    {
        "q": "“Toqquşma” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
        "c": "“Collision”",
        "w": ["“Grounding”", "“Capsizing”", "“Stranding”"]
    },
    {
        "q": "“Yanğın, partlayış” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
        "c": "“Fire, explosion”",
        "w": ["“Flooding”", "“Sinking”", "“Structural failure”"]
    },
    {
        "q": "“Kren, çevrilmə təhlükəsi” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
        "c": "“Listing, capsizing”",
        "w": ["“Pitching, rolling”", "“Surging, swaying”", "“Heaving, pitching”"]
    },
    {
        "q": "“Saya oturma” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
        "c": "“Grounding”",
        "w": ["“Sinking”", "“Collision”", "“Drifting”"]
    },
    {
        "q": "“İdarə etmənin itirilməsi və dreyf” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
        "c": "“Disabled & Adrift”",
        "w": ["“Lost & Found”", "“Underway & Making way”", "“Anchored & Moored”"]
    },
    {
        "q": "“Gəmini tərk etmə” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
        "c": "“Abandoning ship”",
        "w": ["“Evacuation process”", "“Lifeboat launching”", "“Muster station”"]
    },
    {
        "q": "“Yük manifesti” nədir?",
        "c": "dəniz ilə yük daşımalarını nizamlayan beynəlxalq qanunlar toplusu",
        "w": ["gəmidə daşınan yüklərin siyahısı", "yükün gömrükdən keçirilməsi sənədi", "təhlükəli yüklərin qablaşdırma qaydası"]
    },
    {
        "q": "Qəbul edilmiş yük haqqında qeydlər aparılmasından və kapitanın yük köməkçisi tərəfindən imzalanmasından sonra “yük orderi” necə adlandırılır?",
        "c": "konosament",
        "w": ["manifest", "kargo planı", "şturman qəbzi"]
    },
    {
        "q": "Gəminin ümumi yükün qəbuluna hazır olması haqqında məlumat hansı sənəddə qeyd edilməlidir?",
        "c": "gəmi jurnalında",
        "w": ["maşın jurnalında", "rəsmi qeydiyyat kitabında", "liman nəzarəti hesabatında"]
    },
    {
        "q": "Yük göndərən sahibkara şturman qəbzi əsasında hansı sənəd verilir?",
        "c": "konosament",
        "w": ["yük manifesti", "gömrük bəyannaməsi", "siğorta polisi"]
    },
    {
        "q": "Maye yüklərin oddan təhlükəliliyinin göstəricisini qeyd edin:",
        "c": "mayenin doymuş buxarının alışma temperaturu",
        "w": ["mayenin özlülük dərəcəsi", "sıxlıq əmsalı", "donma temperaturu"]
    },
    {
        "q": "Aşağıdakılardan hansı məlumat konosamentə daxil edilir?",
        "c": "yüklənmə limanı",
        "w": ["gəminin yanacağı", "heyətin sayı", "gündəlik hava proqnozu"]
    },
    {
        "q": "Hansı sənədin təqdim edilməsi ilə gəmi yük əməliyyatlarına hazırlığını bəyan edir?",
        "c": "kapitanın bildirişi (Notis)",
        "w": ["liman rəisinin icazəsi", "agentin məktubu", "yük planı"]
    }
]

# Random seed
random.seed(33328)

questions = []
for i, item in enumerate(raw_data):
    correct = item["c"]
    wrongs = item["w"]
    
    # Shuffle options
    options_list = [correct] + wrongs
    random.shuffle(options_list)
    
    opts_dict = {}
    correct_letter = ""
    letters = ["A", "B", "C", "D"]
    for j, opt in enumerate(options_list):
        opts_dict[letters[j]] = opt
        if opt == correct:
            correct_letter = letters[j]
            
    q_id = f"q{i+1:03d}"
    
    # Optional: correct answer might have been "5 metr" in #7, let's just make sure.
    # Ah wait, for Q7, the correct answer from the extracted text was "5 metr". Let me modify it just in case.
    if item["q"] == "Hidrokostyumda hansı hündürlükdən suya təhlükəsiz tullanmaq olar?":
        if "4,5 metr" == item["c"]:
            pass # Keep it, sometimes it's 4.5. Let's make it "4.5 metr". Actually, text said "5 metr". Let me fix this in raw_data.
    
    question = {
        "id": q_id,
        "question": item["q"],
        "options": opts_dict,
        "correct_answer": correct_letter,
        "explanation": ""
    }
    questions.append(question)

# Fix Q7 correct answer to 5 metr if needed
for q in questions:
    if q["question"] == "Hidrokostyumda hansı hündürlükdən suya təhlükəsiz tullanmaq olar?":
        for k, v in q["options"].items():
            if v == "4,5 metr":
                q["options"][k] = "5 metr"

# Fix Q30 correct answer to “SEELONCE ONCE FEENEE” if needed
for q in questions:
    if "“normal” radio əlaqənin icazə verən siqnalını qeyd edin" in q["question"]:
        for k, v in q["options"].items():
            if v == "“SEELONCE FEENEE”":
                q["options"][k] = "“SEELONCE ONCE FEENEE”"
                
final_json = {
    "certificate": CERT_NAME,
    "questions": questions
}

# Write to both paths
path1 = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_ist.json"
path2 = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\gemi_suruculeri_istismar.json"

for p in [path1, path2]:
    with open(p, "w", encoding="utf-8") as f:
        json.dump(final_json, f, ensure_ascii=False, indent=4)

print("Rebuild script finished.")
