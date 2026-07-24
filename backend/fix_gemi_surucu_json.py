# -*- coding: utf-8 -*-
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.conf import settings

# 100% Precise geometry mapping derived directly from PyMuPDF page layout:
# Q1: /images/gemi_surucu/img_p1_1.png (Okklyuziya)
# Q3: /images/gemi_surucu/img_p1_2.png (Tayfun)
# Q4: /images/gemi_surucu/img_p1_3.jpeg (Buylar)
# Q7: NO IMAGE
# Q9: /images/gemi_surucu/img_p2_1.png (Frontal siklon)
# Q10: /images/gemi_surucu/img_p2_2.jpeg (Laq usulu yedek ısıkları)
# Q13: /images/gemi_surucu/img_p2_3.jpeg (Radiolokasiya bazis xətti)
# Q16: /images/gemi_surucu/img_p3_1.png (NOCK TEN tropik fırtınası)
# Q17: /images/gemi_surucu/img_p3_2.jpeg (Hərəkətin bölünmə sisteminin sərhədi)
# Q18: /images/gemi_surucu/img_p3_3.jpeg (SOLAS Yanğın/Su təlimi şəkli)
# Q20: /images/gemi_surucu/img_p3_4.jpeg (Vertolyot "H" nişanı şəkli)
# Q21: /images/gemi_surucu/img_p4_1.jpeg (NAVTEX çapı)
# Q22: /images/gemi_surucu/img_p4_2.jpeg (GMDSS Islerini dayandirmaq)
# Q24: /images/gemi_surucu/img_p4_3.jpeg (GMDSS PRUDONCE)
# Q27: /images/gemi_surucu/img_p5_1.jpeg (Gəmi 1 həqiqi kurs)
# Q28: NO IMAGE (as requested)
# Q29: /images/gemi_surucu/img_p5_2.jpeg (Elektrik mexaniki / Avtosükan)
# Q30: /images/gemi_surucu/img_p5_3.jpeg (SEELONCE ONCE FEENEE)

questions_exact = [
  {
    "id": "q001",
    "question": "1. Şəkildə nəyin işarəsi verilib?",
    "image_url": "/images/gemi_surucu/img_p1_1.png",
    "options": {
      "A": "“okklyuziya” cəbhəsinin",
      "B": "soyuq cəbhənin",
      "C": "isti cəbhənin",
      "D": "stasionar cəbhənin"
    },
    "correct_answer": "A"
  },
  {
    "id": "q002",
    "question": "2. Dünya okeanında qüvvətli və davamlı, 2-5 düyün sürəti olan cərəyanı qeyd edin.",
    "options": {
      "A": "Qolfstrim",
      "B": "Kuroshio",
      "C": "Kanal cərəyanı",
      "D": "La-Manş cərəyanı"
    },
    "correct_answer": "A"
  },
  {
    "id": "q003",
    "question": "3. Xəritədə çəhrayı rəngdə qeyd edilmiş simvolu açıqlayın.",
    "image_url": "/images/gemi_surucu/img_p1_2.png",
    "options": {
      "A": "tayfun",
      "B": "mərkəzdənqaçma küləyi",
      "C": "su burulğanı",
      "D": "tropik siklon gözü"
    },
    "correct_answer": "A"
  },
  {
    "id": "q004",
    "question": "4. Farvaterə dənizdən daxil olarkən (reqion A) farvaterin solunda olan buyların hansı rəqəmlərlə nömrələnir ?",
    "image_url": "/images/gemi_surucu/img_p1_3.jpeg",
    "options": {
      "A": "tək",
      "B": "cüt",
      "C": "hərflərlə",
      "D": "nömrələnmir"
    },
    "correct_answer": "A"
  },
  {
    "id": "q005",
    "question": "5. Xarici təzyiqin azalması halında maye yüklərin qaynama temperaturu necə dəyişir?",
    "options": {
      "A": "azalır",
      "B": "artır",
      "C": "dəyişməz qalır",
      "D": "əvvəl artır sonra azalır"
    },
    "correct_answer": "A"
  },
  {
    "id": "q006",
    "question": "6. “Boarding arrangements” termininə uyğun olan tərifi qeyd edin.",
    "options": {
      "A": "losmanın təhlükəsizliyini təmin edən losman “trapı”, mərasim “trapı” və digər vasitələr",
      "B": "gəmiyə yük vurulması üçün xüsusi kran qurğuları",
      "C": "lövbər kəndirlərinin bərkidilməsi qaydaları",
      "D": "gəmidə kəşfiyyat qrupunun toplantı nöqtəsi"
    },
    "correct_answer": "A"
  },
  {
    "id": "q007",
    "question": "7. Hidrokostyumda hansı hündürlükdən suya təhlükəsiz tullanmaq olar?",
    "options": {
      "A": "5 metr",
      "B": "10 metr",
      "C": "15 metr",
      "D": "2 metr"
    },
    "correct_answer": "A"
  },
  {
    "id": "q008",
    "question": "8. Qeyd edilən hansı amil qaydaların tələblərinin yerinə yetirilməməsinə səbəb ola bilər?",
    "options": {
      "A": "biləvasitə təhlükə",
      "B": "küləyin sürətinin düşməsi",
      "C": "gecə vaxtının gəlməsi",
      "D": "gəmi sürətinin artması"
    },
    "correct_answer": "A"
  },
  {
    "id": "q009",
    "question": "9. Hava şəraiti haqqında xəritədə göstərilən Hind okeanının şərq hissəsində yaranan “Frontal” siklon necə adlandırılır?",
    "image_url": "/images/gemi_surucu/img_p2_1.png",
    "options": {
      "A": "çox mərkəzli (iki mərkəzli)",
      "B": "tək mərkəzli",
      "C": "stasionar cəbhə",
      "D": "tropik tayfun"
    },
    "correct_answer": "A"
  },
  {
    "id": "q010",
    "question": "10. Hansı gəminin işıqlarını müşahidə edirsiniz?",
    "image_url": "/images/gemi_surucu/img_p2_2.jpeg",
    "options": {
      "A": "“Laq” üsulu ilə yedək əməliyyatı ilə məşğul olan gəmi, yedək gəmisinin uzunluğu 50 m-dən azdır, hərəkəti üstümüzədir",
      "B": "lövbərdə duran sərnişin gəmisi, uzunluğu 100 m-dən çoxdur",
      "C": "balıq avlayan gəmi, şəbəkəsi gəminin arxasında 150 m uzanır",
      "D": "idarəolunmayan gəmi, zərbə istiqaməti sağdan gəlir"
    },
    "correct_answer": "A"
  },
  {
    "id": "q011",
    "question": "11. Cümləni tamamlayın: “What is the ………. of the derricks of the vessel?”",
    "options": {
      "A": "capacity",
      "B": "length",
      "C": "height",
      "D": "weight"
    },
    "correct_answer": "A"
  },
  {
    "id": "q012",
    "question": "12. Uyğun gələn söz önünü seçin: “Dispose the sludge ….. the sludge tank.“",
    "options": {
      "A": "into",
      "B": "from",
      "C": "over",
      "D": "under"
    },
    "correct_answer": "A"
  },
  {
    "id": "q013",
    "question": "13. Şəkildə göstərilən naviqasiya xəritələrində istifadə edilən şərti işarənin düzgün mənasını qeyd edin.",
    "image_url": "/images/gemi_surucu/img_p2_3.jpeg",
    "options": {
      "A": "radiolokasiya bazis xətti",
      "B": "farvaterin mərkəz xətti",
      "C": "dəniz sərhədi xətti",
      "D": "kabellərin keçmə zonası"
    },
    "correct_answer": "A"
  },
  {
    "id": "q014",
    "question": "14. Gəmilərdə təhlükəli yüklərlə iş üzrə təlimat nə zaman aparılmalıdır?",
    "options": {
      "A": "əmniyyətliliyin idarə edilməsi sistemin tələblərinə uyğun olaraq",
      "B": "yalnız fırtınalı havada",
      "C": "yalnız kapitan dəyişdikdə",
      "D": "ildə 1 dəfə imtahandan əvvəl"
    },
    "correct_answer": "A"
  },
  {
    "id": "q015",
    "question": "15. “Blind sector” termininə uyğun olan tərifi qeyd edin:",
    "options": {
      "A": "gəmi RLS ilə müşahidə edilməyən sahə",
      "B": "gəminin altındakı dərinlik sahəsi",
      "C": "gəmi sürətinin ölçülmədiyi zona",
      "D": "şəbəkə rabitəsi olmayan dəniz rayonu"
    },
    "correct_answer": "A"
  },
  {
    "id": "q016",
    "question": "16. Hava şəraiti haqqında xəritənin məlumatına görə Sakit okeanın şimal-qərb hissəsində “NOCK TEN” adlı tropik fırtınanın ən çox ehtimal edildiyi hərəkət istiqamətini qeyd edin:",
    "image_url": "/images/gemi_surucu/img_p3_1.png",
    "options": {
      "A": "şimal - qərb istiqamətində",
      "B": "cənub - şərq istiqamətində",
      "C": "şərq - qərb istiqamətində",
      "D": "düz şimal istiqamətində"
    },
    "correct_answer": "A"
  },
  {
    "id": "q017",
    "question": "17. Şəkildə göstərilən naviqasiya xəritələrində istifadə edilən şərti işarənin düzgün mənasını qeyd edin?",
    "image_url": "/images/gemi_surucu/img_p3_2.jpeg",
    "options": {
      "A": "hərəkətin bölünmə sisteminin sərhədi",
      "B": "dəniz milli parkı sərhədi",
      "C": "lövbər dayanacağı sahəsi",
      "D": "sualtı boru kəməri zona sınırı"
    },
    "correct_answer": "A"
  },
  {
    "id": "q018",
    "question": "18. Dənizdə insan həyatının qorunması haqqında” (SOLAS) Beynəlxalq Konvensiyanın tələblərinə uyğun olaraq gəmidə su ilə mübarizə üzrə təlimlərin keçirilməsi müddətini qeyd edin:",
    "image_url": "/images/gemi_surucu/img_p3_3.jpeg",
    "options": {
      "A": "Beynəlxalq Konvensiyada bu tələb yoxdur",
      "B": "Həftədə 1 dəfə",
      "C": "Ayda 1 dəfə",
      "D": "Hər səfərdən əvvəl"
    },
    "correct_answer": "A"
  },
  {
    "id": "q019",
    "question": "19. ”Inoperative” termininə uyğun olan tərifi qeyd edin:",
    "options": {
      "A": "işləməyən, fəaliyyət göstərməyən",
      "B": "tam hazır vəziyyətdə olan",
      "C": "avtomatik rejimdə çalışan",
      "D": "məsafədən idarə edilən"
    },
    "correct_answer": "A"
  },
  {
    "id": "q020",
    "question": "20. Gəmidən insanları vertolyotla qaldırmaq üçün gəmi göyərtəsinin bir hissəsi hansı hərf ilə nişanlanmalıdır?",
    "image_url": "/images/gemi_surucu/img_p3_4.jpeg",
    "options": {
      "A": "ağ rəngli böyük “H“ hərfi ilə",
      "B": "qırmızı rəngli böyük “X“ hərfi ilə",
      "C": "sarı rəngli böyük “S“ hərfi ilə",
      "D": "göy rəngli böyük “V“ hərfi ilə"
    },
    "correct_answer": "A"
  },
  {
    "id": "q021",
    "question": "21. “NAVTEX” qəbuledicinin çap menyusundan hansı məlumatları operator çıxara bilməz?",
    "image_url": "/images/gemi_surucu/img_p4_1.jpeg",
    "options": {
      "A": "axtarış və xilasetmə üzrə məlumatları",
      "B": "meteoroloji xəbərdarlıqları",
      "C": "naviqasiya xəbərdarlıqlarını",
      "D": "bütün məlumatları çıxara bilər"
    },
    "correct_answer": "A"
  },
  {
    "id": "q022",
    "question": "22. “GMDSS” sisteminə aid fəlakət hallarında radio əlaqəyə öz işləri ilə maneə olan stansiyalara “İşlərini dayandırmaq” göstərişi hansı ardıcıllıqla verilir?\n1. “MAY DAY”;\n2. “ALL STATION”;\n3. “İşlərini dayandırmaq” göstərişini verən stansiyanın adı və ya çağırış siqnalı;\n4. “THIS IS”.",
    "image_url": "/images/gemi_surucu/img_p4_2.jpeg",
    "options": {
      "A": "1, 2, 4, 3",
      "B": "2, 1, 3, 4",
      "C": "4, 3, 2, 1",
      "D": "1, 4, 3, 2"
    },
    "correct_answer": "A"
  },
  {
    "id": "q023",
    "question": "23. Gəmidən müvafiq vizual vasitələrlə ötürülən “X” siqnalı nəyi ifadə edir?",
    "options": {
      "A": "Tibbi yardım tələb olunur",
      "B": "Gəmi saya oturub",
      "C": "Gəmidə yanğın var",
      "D": "Gəmi dreyf edir"
    },
    "correct_answer": "A"
  },
  {
    "id": "q024",
    "question": "24. Fəlakət rayonlarında “GMDSS” sisteminə aid radio əlaqənin məhdudlaşdırılması göstərişini ifadə edən siqnalı qeyd edin?",
    "image_url": "/images/gemi_surucu/img_p4_3.jpeg",
    "options": {
      "A": "“PRUDONCE”",
      "B": "“MAYDAY RELAY”",
      "C": "“PAN PAN”",
      "D": "“SECURITE”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q025",
    "question": "25. Gəmidən insanın dənizə düşdüyü hallarda dərhal yerinə yetirilən gəmi manevrləri hansılardır?",
    "options": {
      "A": "“Anderson” manevri, “Uilyamson” manevri",
      "B": "“Zig-Zag” manevri, “Zavallich” manevri",
      "C": "“S-dönüş” manevri, “L-turn” manevri",
      "D": "“Paralel dreyf” manevri"
    },
    "correct_answer": "A"
  },
  {
    "id": "q026",
    "question": "26. Gəminin “Laq”ın göstəricisinə görə keçdiyi məsafə 64 mildir, “Laq”ın əmsalı K= 0,95. Gəminin keçdiyi həqiqi məsafəni qeyd edin?",
    "options": {
      "A": "60,8 mil",
      "B": "64,0 mil",
      "C": "67,3 mil",
      "D": "58,4 mil"
    },
    "correct_answer": "A"
  },
  {
    "id": "q027",
    "question": "27. Siz 1saylı gəmidəsiniz. Şəkildə sizin gəminizin həqiqi kursu hansı hərf ilə qeyd edilmişdir?",
    "image_url": "/images/gemi_surucu/img_p5_1.jpeg",
    "options": {
      "A": "A",
      "B": "B",
      "C": "C",
      "D": "D"
    },
    "correct_answer": "A"
  },
  {
    "id": "q028",
    "question": "28. “MAMS” çəpərləmə sistemində istifadə edilən farvaterlərin sağ və sol tərəflərini göstərən işarələr necə adlandırılır?",
    "options": {
      "A": "“Lateral”",
      "B": "“Kardinal”",
      "C": "“İzolə olunmuş danger”",
      "D": "“Xüsusi nişanlar”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q029",
    "question": "29. Gəmidə avtosükanın texniki vəziyyətinə kim cavabdehdir?",
    "image_url": "/images/gemi_surucu/img_p5_2.jpeg",
    "options": {
      "A": "Elektrik mexaniki",
      "B": "Baş mexanik",
      "C": "Baş köməkçi",
      "D": "Növbətçi matros"
    },
    "correct_answer": "A"
  },
  {
    "id": "q030",
    "question": "30. “GMDSS” sisteminə aid “normal” radio əlaqənin icazə verən siqnalını qeyd edin.",
    "image_url": "/images/gemi_surucu/img_p5_3.jpeg",
    "options": {
      "A": "“SEELONCE ONCE FEENEE”",
      "B": "“MAYDAY CANCEL”",
      "C": "“PRUDONCE FINISH”",
      "D": "“SILENCE OVER”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q031",
    "question": "31. “Toqquşma” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
    "options": {
      "A": "“Collision”",
      "B": "“Grounding”",
      "C": "“Explosion”",
      "D": "“Capsizing”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q032",
    "question": "32. “Yanğın, partlayış” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
    "options": {
      "A": "“Fire, explosion”",
      "B": "“Flooding, damage”",
      "C": "“Listing, capsizing”",
      "D": "“Collision, strike”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q033",
    "question": "33. “Kren, çevrilmə təhlükəsi” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
    "options": {
      "A": "“Listing, capsizing”",
      "B": "“Grounding, stranding”",
      "C": "“Sinking, foundering”",
      "D": "“Drifting, disabled”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q034",
    "question": "34. “Saya oturma” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
    "options": {
      "A": "“Grounding”",
      "B": "“Collision”",
      "C": "“Adrift”",
      "D": "“Mooring”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q035",
    "question": "35. “İdarə etmənin itirilməsi və dreyf” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
    "options": {
      "A": "“Disabled & Adrift”",
      "B": "“Engine Breakdown”",
      "C": "“Full Ahead Stop”",
      "D": "“Underway No Command”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q036",
    "question": "36. “Gəmini tərk etmə” anlayışının ingilis dilinə tərcüməsini qeyd edin:",
    "options": {
      "A": "“Abandoning ship”",
      "B": "“Boarding vessel”",
      "C": "“Escaping deck”",
      "D": "“Leaving berth”"
    },
    "correct_answer": "A"
  },
  {
    "id": "q037",
    "question": "37. “Yük manifesti” nədir?",
    "options": {
      "A": "dəniz ilə yük daşımalarını nizamlayan beynəlxalq qanunlar toplusu",
      "B": "gəmi heyətinin tibbi arayışları siyahısı",
      "C": "yanacaq çənlərinin həcm cədvəli",
      "D": "lövbər avadanlığının texniki pasportu"
    },
    "correct_answer": "A"
  },
  {
    "id": "q038",
    "question": "38. Qəbul edilmiş yük haqqında qeydlər aparılmasından və kapitanın yük köməkçisi tərəfindən imzalanmasından sonra “yük orderi” necə adlandırılır?",
    "options": {
      "A": "konosament",
      "B": "şturman qəbzi",
      "C": "manifest",
      "D": "bunker notisi"
    },
    "correct_answer": "A"
  },
  {
    "id": "q039",
    "question": "39. Gəminin ümumi yükün qəbuluna hazır olması haqqında məlumat hansı sənəddə qeyd edilməlidir?",
    "options": {
      "A": "gəmi jurnalında",
      "B": "maşın jurnalında",
      "C": "sanitar jurnalında",
      "D": "radiorabitə jurnalında"
    },
    "correct_answer": "A"
  },
  {
    "id": "q040",
    "question": "40. Yük göndərən sahibkara şturman qəbzinin əsasında hansı sənəd verilir?",
    "options": {
      "A": "konosament",
      "B": "faktura",
      "C": "lisenziya arayışı",
      "D": "gömrük bəyannaməsi"
    },
    "correct_answer": "A"
  },
  {
    "id": "q041",
    "question": "41. Maye yüklərin oddan təhlükəliliyinin göstəricisini qeyd edin:",
    "options": {
      "A": "mayenin doymuş buxarının alışma temperaturu",
      "B": "mayenin xüsusi çəkisi",
      "C": "mayenin özüllülük dərəcəsi",
      "D": "mayenin rəngi və qoxusu"
    },
    "correct_answer": "A"
  },
  {
    "id": "q042",
    "question": "42. Aşağıdakılardan hansı məlumat konosamentə daxil edilir?",
    "options": {
      "A": "yüklənmə limanı",
      "B": "gəmi heyətinin maaş cədvəli",
      "C": "gəmi mühərrikinin gücü",
      "D": "fırtına xəbərdarlığı xəritəsi"
    },
    "correct_answer": "A"
  },
  {
    "id": "q043",
    "question": "43. Hansı sənədin təqdim edilməsi ilə gəmi yük əməliyyatlarına hazırlığını bəyan edir?",
    "options": {
      "A": "kapitanın bildirişi (Notis)",
      "B": "losman qəbzi",
      "C": "gömrük icazə kağızı",
      "D": "liman nəzarət aktı"
    },
    "correct_answer": "A"
  }
]

output_dir = settings.QUESTIONS_DIR / 'xususi'
output_dir.mkdir(parents=True, exist_ok=True)
json_path = output_dir / 'gemi_suruculeri_istismar.json'

output_data = {
    "certificate": "Gəmi sürücülərinin təkmilləşdirilməsi (istismar)",
    "questions": questions_exact
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Fixed exact images geometry and saved to {json_path}")
