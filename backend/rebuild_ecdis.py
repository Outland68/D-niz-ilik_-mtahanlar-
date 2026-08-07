import json
import random
import os

random.seed(33313)

questions_data = [
    {
        "id": "q001",
        "question": "Bir dəqiqə ərzində 50-60 işıltı hansı işığa aiddir?",
        "correct": "Tez-tez işıltılı işıq",
        "wrong": ["Qrup işıltılı işıq", "Mürəkkəb qrup işıltılı işıq", "Fasiləsiz sabit işıq"]
    },
    {
        "id": "q002",
        "question": "Beynəlxalq şərti işarə (FI (2)) hansı işığa aiddir?",
        "correct": "Qrup işıltılı işığına",
        "wrong": ["Davamlı işıltılı işığına", "Tez-tez işıltılı işığına", "Tək-tək işıltılı işığına"]
    },
    {
        "id": "q003",
        "question": "Beynəlxalq şərti işarə “Q” hansı işığa aiddir?",
        "correct": "Tez-tez işıltılı işığına",
        "wrong": ["Sabit davamlı işığa", "Qrup işıltılı işığına", "İzo-faza işığına"]
    },
    {
        "id": "q004",
        "question": "Beynəlxalq şərti işarə “Q (9) L FI” hansı işığa aiddir?",
        "correct": "Qrup tez-tez davamlı işıltı işığına",
        "wrong": ["Mürəkkəb qrup tez-tez işıltılı işığa", "Fasiləli qrup işıltılı işığa", "Davamlı qrup işıltılı işığa"]
    },
    {
        "id": "q005",
        "question": "“İşığın rəngi - Qırmızı, xüsusiyyəti - FI 3s” hansı işarəyə aiddir?",
        "correct": "Lateral işarə, farvaterin (kanalın) sağ tərəfi buyu",
        "wrong": ["Kardinal işarə, məni şimal tərəfdən keç buyu", "Təhlükəsiz sular işarəsi", "Xüsusi təyinatlı təhlükə işarəsi"]
    },
    {
        "id": "q006",
        "question": "“İşığın rəngi – Ağ, xüsusiyyəti – Q” hansı işarəyə aiddir?",
        "correct": "Kardinal işarə, məni şimal tərəfdən keç buyu",
        "wrong": ["Kardinal işarə, məni cənub tərəfdən keç buyu", "Lateral işarə, farvaterin sol tərəfi buyu", "Tək yerləşən təhlükəni göstərən işarə"]
    },
    {
        "id": "q007",
        "question": "“İşığın rəngi – Ağ, xüsusiyyəti – Q (6) L FI 15s” hansı işarəyə aiddir?",
        "correct": "Kardinal işarə, məni cənub tərəfdən keç buyu",
        "wrong": ["Kardinal işarə, məni şimal tərəfdən keç buyu", "Kardinal işarə, məni şərq tərəfdən keç buyu", "Kardinal işarə, məni qərb tərəfdən keç buyu"]
    },
    {
        "id": "q008",
        "question": "“İşığın rəngi – Ağ, xüsusiyyəti – FI (2) 5s” hansı işarəyə aiddir?",
        "correct": "Kiçik ölçülü tək-tək yerləşən təhlükəni göstərən işarə",
        "wrong": ["Təhlükəsiz sular işarəsi, ox boyu hərəkət buyu", "Xüsusi təyinatlı sahəni göstərən işarə", "Yeni təhlükəni göstərən buy"]
    },
    {
        "id": "q009",
        "question": "“İşığın rəngi – Sarı, xüsusiyyəti – FI 5s” hansı işarəyə aiddir?",
        "correct": "Xüsusi təyinatlı təhlükə işarəsi",
        "wrong": ["Tək yerləşən kiçik ölçülü təhlükə işarəsi", "Lateral işarə, farvaterin sol tərəfi buyu", "Təhlükəsiz sular işarəsi"]
    },
    {
        "id": "q010",
        "question": "Buya aid olan top fiquru: Buyun boyalanmasını göstərin.",
        "correct": "Yaşıl Qırmızı Yaşıl",
        "wrong": ["Qırmızı Yaşıl Qırmızı", "Sarı Qara Sarı", "Qara Sarı Qara"]
    },
    {
        "id": "q011",
        "question": "Buya aid olan top fiquru: buyun boyalanmasını göstərin.",
        "correct": "Sarı Qara Sarı",
        "wrong": ["Qara Sarı Qara", "Qara Sarı", "Sarı Qara"]
    },
    {
        "id": "q012",
        "question": "Beynəlxalq tələblərə görə «ECDIS» -in əsas komplektlərinə hansı naviqasiya sistemləri mütləq qoşulmalıdırlar?",
        "correct": "Gəminin yerini təyin etmək üçün sistem, girokompas, laq",
        "wrong": ["Radar, AIS, exolot", "NAVTEX, Inmarsat, maqnit kompas", "AIS, laq, VDR (Reys məlumat qeydiyyatçısı)"]
    },
    {
        "id": "q013",
        "question": "Kartoqrafik sistemindən istifadə edərkən, Beynəlxalq tələblərə görə, gəmidə hansı sənədlər olmalıdır?",
        "correct": "Nümunənin bəyənmə şəhadətnaməsi, naviqasiya düzəlişləri üçün müqavilə, müvafiq sənədi, texniki rəhbər sənədi",
        "wrong": ["Gəminin dənizə yararlılıq şəhadətnaməsi, ekoloji sənədlər", "Heyətin diplomları, sağlamlıq sertifikatları", "Sığorta sənədləri, gəmi jurnalı, radiostansiya jurnalı"]
    },
    {
        "id": "q014",
        "question": "Beynəlxalq şərti işarə “FI” hansı işığa aiddir?",
        "correct": "İşıltılı işığa",
        "wrong": ["Davamlı işığa", "Fasiləli işığa", "İzo-faza işığına"]
    },
    {
        "id": "q015",
        "question": "Beynəlxalq şərti işarə “L FI” hansı işığa aiddir?",
        "correct": "Davamlı işıltılı işığa",
        "wrong": ["Qısa işıltılı işığa", "Qrup işıltılı işığa", "Tez-tez işıltılı işığa"]
    },
    {
        "id": "q016",
        "question": "Beynəlxalq şərti işarə “Q (9)” hansı işığa aiddir?",
        "correct": "Qrup tez-tez işıltılı işığa",
        "wrong": ["Davamlı işıltılı işığa", "Mürəkkəb qrup işıltılı işığa", "Tək-tək işıltılı işığa"]
    },
    {
        "id": "q017",
        "question": "Beynəlxalq şərti işarə “FI (2+1)” hansı işığa aiddir?",
        "correct": "Mürəkkəb qrup işıltılı işığa",
        "wrong": ["Tez-tez işıltılı işığa", "Fasiləsiz işıltılı işığa", "Qrup tez-tez işıltılı işığa"]
    },
    {
        "id": "q018",
        "question": "“İşığın rəngi - Qırmızı, xüsusiyyəti - FI (2+1) 9s” hansı işarəyə aiddir?",
        "correct": "Lateral işarə, əsas farvater sağdadır buyu",
        "wrong": ["Lateral işarə, əsas farvater soldadır buyu", "Kardinal işarə, məni şimalda saxla", "Tək yerləşən təhlükə işarəsi"]
    },
    {
        "id": "q019",
        "question": "“İşığın rəngi – Ağ, xüsusiyyəti – Q (3) 10s” hansı işarəyə aiddir?",
        "correct": "Kardinal işarə, məni qərbdə saxla",
        "wrong": ["Kardinal işarə, məni şərqdə saxla", "Kardinal işarə, məni cənubda saxla", "Kardinal işarə, məni şimalda saxla"]
    },
    {
        "id": "q020",
        "question": "“İşığın rəngi – Ağ, xüsusiyyəti – Q (9) 15s” hansı işarəyə aiddir?",
        "correct": "Kardinal işarə, məni şərqdə saxla",
        "wrong": ["Kardinal işarə, məni qərbdə saxla", "Kardinal işarə, məni cənubda saxla", "Lateral işarə, kanalın sol tərəfi"]
    },
    {
        "id": "q021",
        "question": "Gəmilərdə hansı elektron kartoqrafik sistemləri istifadə olunur?",
        "correct": "RCDS, ECS, ECDİS",
        "wrong": ["GMDSS, AIS, VDR", "GPS, GLONASS, Galileo", "ARPA, Radar, Navtex"]
    },
    {
        "id": "q022",
        "question": "Elektron xəritələrin üçüncü miqyaslar diapazonunun təyinatı nədir?",
        "correct": "Sahilboyu (sahili görmə zonasında və ya məhdudlaşmış naviqasiya şəraitlərində keçidin təmin edilməsi)",
        "wrong": ["Xülasə (okeanlarda üzmənin planlaşdırılması)", "Planlar (limanlarda manevr edilməsi)", "General (əsas elektron xəritələrdə keçid)"]
    },
    {
        "id": "q023",
        "question": "Elektron xəritələrin ikinci miqyas diapazonunun təyinatı nədir?",
        "correct": "General (əsas elektron xəritələrdə keçidinin təmin edilməsi)",
        "wrong": ["Sahilboyu (sahili görmə zonasında naviqasiya)", "Hövzələr (limanların akvatoriyasında hərəkət)", "Planlar (yanalma zamanı üzgüçülük)"]
    },
    {
        "id": "q024",
        "question": "Elektron xəritələrin dördüncü miqyaslar diapazonunun təyinatı nədir?",
        "correct": "Sahilə yaxınlaşmalar (sahilə yaxınlaşmanın təmin edilməsi)",
        "wrong": ["Xülasə (okean üzgüçülüyü)", "General (açıq dənizdə keçid)", "Planlar (yanalma əməliyyatları)"]
    },
    {
        "id": "q025",
        "question": "Elektron xəritələrin beşinci miqyas diapazonunun təyinatı nədir?",
        "correct": "Hövzələr (limanların akvatoriyasında, buxtalarda, hövzələrdə v.s. hərəkətin təmin edilməsi)",
        "wrong": ["Sahilboyu (sahili görmə zonasında keçid)", "Xülasə xəritələri (marşrutun planlaşdırılması)", "Sahilə yaxınlaşmalar (sahilə yaxınlaşmanın təmin edilməsi)"]
    },
    {
        "id": "q026",
        "question": "Elektron xəritələrin altıncı miqyas diapazonunun təyinatı nədir?",
        "correct": "Planlar (yanalma zamanı və limandan çıxan zaman üzgüçülüyün eləcə də təhlükəsizliyin təmin edilməsi)",
        "wrong": ["Hövzələr (limanların akvatoriyasında hərəkət)", "General (əsas elektron xəritələrdə keçid)", "Sahilboyu (məhdudlaşmış naviqasiya şəraitində)"]
    },
    {
        "id": "q027",
        "question": "Elektron naviqasiya xəritələri Beynəlxalq Hidroqrafiya Təşkilatının (İHO) hansı standartında olmalıdırlar?",
        "correct": "S-57",
        "wrong": ["S-52", "S-63", "S-100"]
    },
    {
        "id": "q028",
        "question": "Elektron naviqasiya xəritələri haqqında olan məlumat qutusunun adı neçə simvoldan ibarətdir?",
        "correct": "8",
        "wrong": ["6", "10", "12"]
    },
    {
        "id": "q029",
        "question": "Elektron naviqasiya xəritələri haqqında olan məlumat qutusunun adındakı “PP” simvolların açıqlaması nədir?",
        "correct": "İstehsal edən ölkənin kodu",
        "wrong": ["Xəritənin miqyas kodu", "Xəritənin yenilənmə tarixi kodu", "Nəşr olunan ilin kodu"]
    },
    {
        "id": "q030",
        "question": "Elektron naviqasiya xəritələri haqqında olan məlumat qutusunun adındakı “S” simvolunun açıqlaması nədir?",
        "correct": "Miqyaslar sırasının kodu",
        "wrong": ["İstehsal edən ölkənin kodu", "Xəritənin təhlükəsizlik kodu", "Xəritə nömrəsinin seriyası"]
    },
    {
        "id": "q031",
        "question": "Miqyaslar sırasının kodu neçə diapazondan ibarətdir?",
        "correct": "6",
        "wrong": ["4", "8", "10"]
    },
    {
        "id": "q032",
        "question": "Elektron naviqasiya xəritələri haqqında olan məlumat qutusunun simvolu göstərilənlərdən hansıdır?",
        "correct": "PPSCCCCC",
        "wrong": ["SSPPCCCC", "CCCCPPSP", "PPCCCCCC"]
    },
    {
        "id": "q033",
        "question": "Elektron naviqasiya xəritələrinin korrekturası rəhbər sənədi hansı servis dərəcələrini təyin edir?",
        "correct": "Vaxt cədvəlinə əsasən servis, tələblə servis, fövqəladə servis",
        "wrong": ["Gündəlik servis, həftəlik servis, aylıq servis", "Avtomatik servis, yarı-avtomatik servis, əl ilə servis", "Lokal servis, regional servis, qlobal servis"]
    },
    {
        "id": "q034",
        "question": "Elektron naviqasiya xəritələrinin korrektura etmə üsullarının kateqoriyası hansıdır?",
        "correct": "Əl ilə korrektura və avtomatik korrektura",
        "wrong": ["Yalnız avtomatik korrektura", "Yalnız əl ilə korrektura", "Peyk vasitəsilə və radiostansiya vasitəsilə korrektura"]
    },
    {
        "id": "q035",
        "question": "Buyun göstərilən top fiquru işarəsini izah edin.",
        "correct": "Məni cənubda saxla, işıq - Ağ, boyalanma - qara sarı, xüsusiyyət - Q",
        "wrong": ["Məni şimalda saxla, işıq - Ağ, boyalanma - qara sarı, xüsusiyyət - Q", "Məni şərqdə saxla, işıq - Sarı, boyalanma - qara sarı, xüsusiyyət - Q(3)", "Məni qərbdə saxla, işıq - Qırmızı, boyalanma - qara sarı, xüsusiyyət - Q(9)"]
    },
    {
        "id": "q036",
        "question": "Buyun göstərilən top fiquru işarəsini izah edin.",
        "correct": "Məni şərq tərəfdən keç, işıq - Ağ, boyalanma - qara sarı qara, xüsusiyyət - Q (3) 10s",
        "wrong": ["Məni qərb tərəfdən keç, işıq - Ağ, boyalanma - sarı qara sarı, xüsusiyyət - Q (9) 15s", "Məni cənub tərəfdən keç, işıq - Ağ, boyalanma - sarı qara, xüsusiyyət - Q (6) L Fl 15s", "Məni şimal tərəfdən keç, işıq - Ağ, boyalanma - qara sarı, xüsusiyyət - Q"]
    },
    {
        "id": "q037",
        "question": "Şəkildəki top fiquru olan buyun tam xarakteristikasını göstərin.",
        "correct": "Boyalanma - qara qır qara, işıq - Ağ, xüsusiyyət - FI (2) 5s. Kiçik ölçülü təhlükələrin çəpərlənməsi buyu, hər tərəfdən keçmək olar. Təhlükənin üstündə qoyulur",
        "wrong": ["Boyalanma - qırmızı ağ qırmızı, işıq - Ağ, xüsusiyyət - Iso 5s. Təhlükəsiz sular işarəsi", "Boyalanma - sarı qara sarı, işıq - Ağ, xüsusiyyət - Q (9). Kardinal işarə", "Boyalanma - yaşıl qırmızı yaşıl, işıq - Yaşıl, xüsusiyyət - Fl(2+1). Lateral işarə"]
    },
    {
        "id": "q038",
        "question": "Buyun göstərilən top fiquru işarəsini izah edin.",
        "correct": "Məni şərqdə saxla. İşıq - Ağ, boyalanma - sarı qara sarı, xüsusiyyət - Q (9) 15s",
        "wrong": ["Məni qərbdə saxla. İşıq - Ağ, boyalanma - sarı qara sarı, xüsusiyyət - Q (9) 15s", "Məni cənubda saxla. İşıq - Ağ, boyalanma - sarı qara, xüsusiyyət - Q (6) L Fl 15s", "Məni şimalda saxla. İşıq - Ağ, boyalanma - qara sarı, xüsusiyyət - Q"]
    },
    {
        "id": "q039",
        "question": "Lateral işarələr hansı buylardan ibarətdir?",
        "correct": "kanal buyları, farvaterin tərəfini göstərən buylar",
        "wrong": ["təhlükəni tək-tək çəpərləyən buylar, kardinal buylar", "xüsusi təyinatlı buylar, yeni təhlükə buyları", "təhlükəsiz sular buyları, liman giriş buyları"]
    },
    {
        "id": "q040",
        "question": "Lateral işarələr neçə buydan ibarətdir?",
        "correct": "4",
        "wrong": ["2", "6", "8"]
    },
    {
        "id": "q041",
        "question": "BMXA (MAMC) sisteminə görə A və B reqionları nə ilə fərqlənir?",
        "correct": "Buyların rənginə görə",
        "wrong": ["Buyların top fiqurlarına görə", "Buyların işıq xüsusiyyətinə görə", "Buyların ölçüsünə görə"]
    },
    {
        "id": "q042",
        "question": "Kardinal işarələr neçə buydan ibarətdir?",
        "correct": "4",
        "wrong": ["2", "6", "8"]
    },
    {
        "id": "q043",
        "question": "Elektron xəritələr hansı formatda olur?",
        "correct": "Rastr və vektor",
        "wrong": ["Yalnız vektor formatda", "Yalnız rastr formatda", "PDF və JPEG formatında"]
    },
    {
        "id": "q044",
        "question": "Beynəlxalq tələblərinə görə ECDİS -in komplektinə əlavə olaraq hansı naviqasiya avadanlıqları qoşulmalıdır?",
        "correct": "Radar (ARPA), Exolot, AIS, NAVTEX",
        "wrong": ["GMDSS, Inmarsat-C, MF/HF radio", "VDR, SSAS, EPIRB", "SART, BNWAS, maqnit kompas"]
    },
    {
        "id": "q045",
        "question": "Elektron naviqasiya xəritələrinin korrekturası Beynəlxalq Hidroqrafiya Təşkilatının (IHO) tələblərinə görə hansı standarlarda aparılır?",
        "correct": "S-52",
        "wrong": ["S-57", "S-63", "S-100"]
    },
    {
        "id": "q046",
        "question": "Elektron xəritələrin nömrələnməsində Azərbaycanın kodu necə göstərilir?",
        "correct": "7A",
        "wrong": ["AZ", "99", "4J"]
    },
    {
        "id": "q047",
        "question": "Elektron naviqasiya xəritələrində ümumi (General) xəritələrin miqyas diapozonu neçədir?",
        "correct": "1:2 250 000 – 1:300 001",
        "wrong": ["1:300 000 – 1:80 001", "1:80 000 – 1:20 001", "1:20 000 – 1:4 001"]
    },
    {
        "id": "q048",
        "question": "Elektron naviqasiya xəritələrində sahilboyu xəritələrin miqyas diapozonu neçədir?",
        "correct": "1:300 000 – 1:80 001",
        "wrong": ["1:2 250 000 – 1:300 001", "1:80 000 – 1:20 001", "1:20 000 – 1:4 001"]
    },
    {
        "id": "q049",
        "question": "Beynəlxalq səviyyədə Elektron Naviqasiya xəritələrinin standartlarа uyğun hazırlanmasına və istifadəsinə hansı təşkilatlar nəzarət edir?",
        "correct": "IMO və IHO",
        "wrong": ["ITU və WMO", "IALA və ICS", "IMSO və IHO"]
    },
    {
        "id": "q050",
        "question": "Elektron naviqasiya xəritələrində xülasə xəritələrin miqyas diapozonu neçədir?",
        "correct": "1 : 2 250 000-dən kiçik",
        "wrong": ["1:2 250 000 – 1:300 001", "1:300 000 – 1:80 001", "1:4000-dən böyük"]
    }
]

output_json = {
    "certificate": "Elektron Xəritə Displeyinin və İnformasiya Sistemlərinin İstismar Qaydaları",
    "questions": []
}

for q in questions_data:
    options = [q["correct"]] + q["wrong"]
    random.shuffle(options)
    opt_dict = {}
    correct_key = ""
    for idx, opt in enumerate(options):
        letter = chr(65 + idx)
        opt_dict[letter] = opt
        if opt == q["correct"]:
            correct_key = letter
            
    output_json["questions"].append({
        "id": q["id"],
        "question": q["question"],
        "options": opt_dict,
        "correct_answer": correct_key,
        "explanation": ""
    })

output_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\elektron_x_rit_displeyinin_v_i_nformasiy.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_json, f, ensure_ascii=False, indent=4)
print("Rebuild complete. Total questions:", len(output_json["questions"]))
