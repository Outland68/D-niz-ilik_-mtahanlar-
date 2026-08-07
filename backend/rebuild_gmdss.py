import json
import random
import os

SEED = 33318
random.seed(SEED)

questions_data = [
    {
        "q": "VHF-radiostansiyası ilә DSC rejimindә verilmiş yanlış fәlakәt siqnalı hansı kanalda lәğv edilir?",
        "a": "16 Ch",
        "d": ["70 Ch", "13 Ch", "06 Ch"]
    },
    {
        "q": "SART-ın açıqlamasını göstәrin:",
        "a": "Radiolokasiya cavabvericisi",
        "d": ["Peyk rabitә terminalı", "Qısa dalğalı ötürücü cihaz", "Avtomatik identifikasiya sistemi"]
    },
    {
        "q": "HF- nin açıqlamasını göstәrin:",
        "a": "Qısa dalğalar",
        "d": ["Ultra qısa dalğalar", "Uzun dalğalar", "Santimetr dalğalar"]
    },
    {
        "q": "MF-nin açıqlamasını göstәrin:",
        "a": "Ara dalğalar",
        "d": ["Qısa dalğalar", "Millimetr dalğalar", "Mikrodalğalar"]
    },
    {
        "q": "Heç bir stansiya tәrәfindәn DSC fәlakət siqnalı tәsdiq olunmadıqda nә edir?",
        "a": "3,5-4,5 dәqiqәdәn bir avtomatik tәkrar olunur",
        "d": ["10 dәqiqәdәn bir tәkrar olunur", "Cihaz avtomatik sönür", "1 saatdan sonra yenidәn göndәrilir"]
    },
    {
        "q": "DSC-nin açıqlamasını göstәrin:",
        "a": "Rәqәmsal seçilmә çağırışı",
        "d": ["Peyk rabitә sistemi", "Avtomatik qәza ötürücüsü", "Uzaq mәsafәli radar siqnalı"]
    },
    {
        "q": "EPİRB-nin açıqlamasını göstәrin:",
        "a": "Qәza radiobuyu",
        "d": ["Gәmi daxili rabitә sistemi", "Radiolokasiya transponderi", "Naviqasiya mәlumatları qәbuledicisi"]
    },
    {
        "q": "VHF-nin açıqlamasını göstәrin:",
        "a": "Ultra qısa dalğalar",
        "d": ["Ara dalğalar", "Qısa dalğalar", "Uzun dalğalar"]
    },
    {
        "q": "“Listing” hansı fәlakәt növünә aid olunur?",
        "a": "Gәminin tәhlükәli kreni (meyililik)",
        "d": ["Gәmidә yanğın", "Gәminin saya oturması", "Suyun gәmiyә dolması"]
    },
    {
        "q": "“Undesignated” hansı fәlakәt növünә aid olunur?",
        "a": "Tәyin olunmamış",
        "d": ["Dәnizә adam düşmәsi", "Gәminin batması", "Quldur hücumu"]
    },
    {
        "q": "“Abandoning ship” hansı fәlakәt növünә aid olunur?",
        "a": "Gәminin tәrk edilmәsi",
        "d": ["Gәminin toqquşması", "Mühәrrikin sıradan çıxması", "Sükandakı nasazlıq"]
    },
    {
        "q": "Sәfәrә çıxmazdan әvvәl GMDSS operatoru nәyi mütlәq yoxlamalıdır?",
        "a": "Bütün radio avadanlığı vә ehtiyat enerji mәnbәlәri",
        "d": ["Yalnız VHF radiostansiyası", "Yalnız SART vә EPIRB cihazları", "Gәminin naviqasiya işıqları"]
    },
    {
        "q": "MMSI abreviaturasını açıqlayın:",
        "a": "Dәniz mobil servis identifikasiya nömrәsi",
        "d": ["Qlobal dәniz rabitә kodu", "Peyk naviqasiya nömrәsi", "Gәmi reyestrinin seriyası"]
    },
    {
        "q": "MMSI nömrәsini birinci üç rәqәmi nәyi göstәrir?",
        "a": "Milli mәnsubiyyәtin kodu",
        "d": ["Gәminin tonnajı", "Gәmi sahibinin kodu", "İstehsalçı şirkәtin nömrәsi"]
    },
    {
        "q": "Fәlakәt zamanı radioәlaqənin aparılması üçün mәslәhәt görülәn rejim hansıdır?",
        "a": "Radiotelefon rabitəsi",
        "d": ["Teleqraf rabitәsi", "Yalnız DSC vasitәsilә", "Teleks rejimi"]
    },
    {
        "q": "VHF radiostansiyalar radio dalğalarının hansı diapazonunda işlәyirlәr?",
        "a": "Ultra qısa dalğalar",
        "d": ["Ara dalğalar", "Qısa dalğalar", "Mikrodalğalar"]
    },
    {
        "q": "VHF-dә Fәlakәt,Tәcili vә Çağırış beynәlxalq kanalı hansıdır?",
        "a": "16 Ch",
        "d": ["70 Ch", "13 Ch", "06 Ch"]
    },
    {
        "q": "16 kanalın tezliyi hansıdır?",
        "a": "156.8 MHs",
        "d": ["156.3 MHs", "156.525 MHs", "2182 KHs"]
    },
    {
        "q": "Aşağıda sadalananlardan hansı “Dupleks”kanalı hesab olunur?",
        "a": "Qәbulun vә ötürülmәnin müxtәlif tezlikli kanal",
        "d": ["Qәbulun vә ötürülmәnin eyni tezlikli kanal", "Yalnız qәbul edәn kanal", "Yalnız ötürücü kanal"]
    },
    {
        "q": "Gәmilәr arası dәnizdә üzmәnin tәhlükәsizliyi haqqında mәlumatın ötürülmәsi hansı kanalda aparılır?",
        "a": "13 Ch",
        "d": ["16 Ch", "70 Ch", "09 Ch"]
    },
    {
        "q": "Aşağıda sadalananlardan hansı “Simpleks” kanalı hesab olunur?",
        "a": "Qәbulun vә ötürülmənin eyni tezlikli kanal",
        "d": ["Qәbulun vә ötürülmәnin müxtәlif tezlikli kanal", "Yalnız qәbul edәn kanal", "Yalnız ötürücü kanal"]
    },
    {
        "q": "VHF radiostansiyalar DSC radionövbәsini hansı kanalda aparılır?",
        "a": "70 Ch",
        "d": ["16 Ch", "13 Ch", "06 Ch"]
    },
    {
        "q": "“Collision” hansı fәlakәt növünә aid olunur?",
        "a": "Gәminin toqquşması",
        "d": ["Gәmidә partlayış", "Gәminin saya oturması", "Gәminin batması"]
    },
    {
        "q": "MF diapazonunda Fәlakәt, Tәcili vә Çağırış beynәlxalq kanalı hansıdır?",
        "a": "2182 KHs",
        "d": ["2187.5 KHs", "2174.5 KHs", "156.8 MHs"]
    },
    {
        "q": "MF/HF radiostansiyanın hәftәlik testi kimin ünvanına göndәrilir?",
        "a": "Yalnız sahil radiostansiyasının ünvanına",
        "d": ["Bütün gәmilәrә", "Xilasetmә mәrkәzlәrinә (RCC)", "Hәr hansı bir gәmiyә"]
    },
    {
        "q": "Sәrnişin gәmilәrdә VHF qәza radiostansiyalarının minimal sayı nә qәdәr olmalıdır?",
        "a": "3 әdәd",
        "d": ["1 әdәd", "2 әdәd", "4 әdәd"]
    },
    {
        "q": "300 r/t olan gәmilәrdә qәza VHF radio stansiyalarının minimal sayı nә qәdәr olmalıdır?",
        "a": "2 әdәd",
        "d": ["1 әdәd", "3 әdәd", "4 әdәd"]
    },
    {
        "q": "SART-ın tәyinatı nədir?",
        "a": "Yerinin tәyin edilmәsi üçün",
        "d": ["Sәs rabitәsi yaratmaq", "Gәminin sürәtini tәyin etmәk", "Hava haqqında mәlumat almaq"]
    },
    {
        "q": "Şüalanma rejimindә SART-ın iş vaxtı nә qәdәrdir?",
        "a": "8 saat",
        "d": ["24 saat", "48 saat", "96 saat"]
    },
    {
        "q": "Gözlәmә rejimindә SART-ın iş vaxtı neçә saatdır?",
        "a": "96 saat",
        "d": ["48 saat", "72 saat", "120 saat"]
    },
    {
        "q": "SART haqqında sәhv müddәanı göstәrin:",
        "a": "Korpusu göy rәngdә olmalıdır",
        "d": ["Radiolokasiya ekranda nöqtәlәr seriyası yaradır", "9 GHz tezliyindә işlәyir", "Su keçirmәz olmalıdır"]
    },
    {
        "q": "Xilasetmә avadanlıqlarından hansı fәlakәtin yerinin koordinatlarını ötürür?",
        "a": "EPİRB",
        "d": ["SART", "VHF qәza radiostansiyası", "NAVTEX"]
    },
    {
        "q": "Hansı vasitә EPİRB–nin gәmidәn avtomatik ayrılmasını tәmin edir?",
        "a": "Hidrostat",
        "d": ["Maqnit qıfıl", "Elektrik mühәrrik", "Mexaniki ling"]
    },
    {
        "q": "Gәminin radioavadanlığı hansı SART-ın siqnalını aşkar edir?",
        "a": "Radiolokasiya stansiyası",
        "d": ["AIS stansiyası", "GPS qәbuledicisi", "Inmarsat terminalı"]
    },
    {
        "q": "Hansı anda SART ötürmәyә başlayır ?",
        "a": "İş rejiminә salındıqdan vә radiolokasiya stansiya tәrafindәn şüalanmasından sonra",
        "d": ["Suya düşәn kimi dәrhal", "Gәmi kreni 45 dәrәcә olduqda", "EPIRB işә düşdükdәn sonra"]
    },
    {
        "q": "VHF qәza radiostansiyasının batareyasının gözlәmә rejimindә iş vaxtı neçә saatdır?",
        "a": "72 Saat",
        "d": ["24 Saat", "48 Saat", "96 Saat"]
    },
    {
        "q": "Neçә metr dәrinlikdә hidrostat EPIRB-ni gәmidәn avtomatik ayrılır?",
        "a": "10 m-ә qәdәr",
        "d": ["2 m-ә qәdәr", "15 m-ә qәdәr", "20 m-dәn çox"]
    },
    {
        "q": "Sadalanlardan hansı doğrudur?",
        "a": "EPIRB gәmidәn avtomatik ayrıldıkdan sonra işә düşmәlidir",
        "d": ["EPIRB gәmiyә bәrkidilmiş vәziyyәtdә siqnal verir", "EPIRB yalnız әllә işә salına bilәr", "EPIRB yalnız VHF siqnalı vasitәsilә aktivlәşir"]
    },
    {
        "q": "EPIRB-nin şüalanma rejimi neçә saatdır?",
        "a": "48 saat",
        "d": ["24 saat", "72 saat", "96 saat"]
    },
    {
        "q": "EPIRB-nin siqnalını hansı avadanlıq qәbul edir?",
        "a": "KOSPAS-SARSAT sisteminin peyklәri",
        "d": ["Inmarsat peyklәri", "Gәminin radiolokasiya stansiyası", "NAVTEX stansiyaları"]
    },
    {
        "q": "LEOSAR (Aşağı orbitalı peyklәr) tәrәfindәn EPİRB-nin koordinatlarının dәqiq tәyin edilmәsi neçә kilometrdir?",
        "a": "12-17 km",
        "d": ["1-5 km", "20-30 km", "50 km-dәn çox"]
    },
    {
        "q": "KOSPAS-SARSAT sistemindә GEOSAR (geostasionar peyklәr) tәrәfindәn EPİRB-dәn fәlakәt signalının RCC (xilasetmә koordinasiya mәrkәzinә) çatdırılması neçə dəqiqə ərzində təmin edilir?",
        "a": "2-5 dәqiqә",
        "d": ["10-15 dәqiqә", "30 dәqiqә", "1 saat"]
    },
    {
        "q": "NAVTEX sisteminin tәyinatı:",
        "a": "Dәnizdә üzmәnin tәhlükәsizliyi üzrә informasiyanın gәmilәrә ötürülmәsi üçün",
        "d": ["Gәmilәr arası sәsli rabitәni tәmin etmәk", "Fәlakәt siqnalını peyklәrә göndәrmәk", "Gәminin radardakı mövqeyini göstәrmәk"]
    },
    {
        "q": "Fәlakәt zamanı kömәyә aid olmayan danışıqların dayandırılması әmri aşağıdakı hansı ifadә ilә işarәlәrinir?",
        "a": "SEELONCE MAYDAY",
        "d": ["SEELONCE FEENEE", "PRUDONCE", "SILENCE DISTRESS"]
    },
    {
        "q": "INMARSAT sistemindә hansı peyk aid deyil",
        "a": "LEOSAR",
        "d": ["IOR (Hind okeanı regionu)", "AOR-E (Atlantik okeanının şәrq regionu)", "POR (Sakit okean regionu)"]
    },
    {
        "q": "Radio avadanlığının ehtiyat enerji qida mәnbәlәrinә hansı aiddir?",
        "a": "Akumulyator",
        "d": ["Əsas generator", "Kömәkçi dizel-generator", "Külәk turbini"]
    },
    {
        "q": "AIS stansiyası ilә hansı mәlumat növlәri ötürülür?",
        "a": "Statik, dinamik vә sәfәr mәlumatları",
        "d": ["Yalnız naviqasiya xәbәrdarlıqları", "Qlobal hava proqnozları", "Fәlakәt vә tәcili rabitә xәtti"]
    },
    {
        "q": "Gәminin AIS stansiyası nә vaxt qoşulmuş vәziyyәtdә olmalıdır?",
        "a": "Daimi",
        "d": ["Yalnız lövbәrdә olduqda", "Yalnız fırtınalı havada", "Yalnız limana daxil olduqda"]
    },
    {
        "q": "Fәlakәtə aid olan mәlumatlar vә ya danışıqlar hansı sözlә işarәlәnir?",
        "a": "MAYDAY",
        "d": ["PAN PAN", "SECURITE", "DISTRESS"]
    },
    {
        "q": "Fəlakətin qısa və tam formatları arasındakı fərq nədədir?",
        "a": "Fəlakətin növünün göstərilməsində",
        "d": ["Göndərilmə tezliyinin seçimində", "İstifadә olunan peyk növündә", "Koordinatların formatında"]
    }
]

questions = []
for i, item in enumerate(questions_data):
    options = [item["a"]] + item["d"]
    random.shuffle(options)
    
    correct_idx = options.index(item["a"])
    correct_letter = chr(65 + correct_idx)
    
    q_dict = {
        "id": f"q{i+1:03d}",
        "question": item["q"],
        "options": {
            "A": options[0],
            "B": options[1],
            "C": options[2],
            "D": options[3]
        },
        "correct_answer": correct_letter,
        "explanation": ""
    }
    questions.append(q_dict)

output_data = {
    "certificate": "Qlobal Dəniz Fəlakət və Ǝmniyyətli Rabitə Sisteminin Ümumi Rayon Operatoru",
    "questions": questions
}

output_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\qlobal_d_niz_f_lak_t_v_mniyy_tli_rabit_s.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

print(f"Generated {len(questions)} questions in {output_path}")
