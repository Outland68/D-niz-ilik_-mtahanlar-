import json
import random
import os

random.seed(33322)

questions_data = [
    {
        "q": "1. Mühafizə haqqında deklarasiyanı liman tərəfindən kim imzalamalıdır?",
        "a": "Limanın mühafizəyə məsul şəxsi və ya limanda mühafizəyə cavabdeh olan təşkilatın nümayəndəsi",
        "d": [
            "Limanın baş kapitanı və ya onun müavini",
            "Dövlət Gömrük Komitəsinin nümayəndəsi",
            "Nəqliyyat, Rabitə və Yüksək Texnologiyalar Nazirliyinin müfəttişi"
        ]
    },
    {
        "q": "2. Mühafizə üzrə tədbirlər görmək üçün yaxınlaşma farvateri liman vasitəsinin tərkibinə daxil edilə bilərmi?",
        "a": "Bəli",
        "d": [
            "Xeyr, yalnız liman akvatoriyası daxil edilir",
            "Yalnız fırtınalı hava şəraitində daxil edilir",
            "Yalnız hərbi gəmilərin girişi zamanı daxil edilir"
        ]
    },
    {
        "q": "3. Gəmilərin və liman vasitələrinin mühafizəsi üzrə Beynəlxalq Məcəllə neçənci ildə qüvvəyə minib?",
        "a": "01.07.2004",
        "d": [
            "01.01.2002",
            "11.09.2001",
            "12.12.2005"
        ]
    },
    {
        "q": "4. Dənizdə mühafizə səviyyəsinin artırılması üzrə xüsusi tədbirlər fəsli aşağıda göstərilənlərdən hansıdır?",
        "a": "XI-2 Fəsli",
        "d": [
            "IX Fəsil",
            "XI-1 Fəsli",
            "VII Fəsil"
        ]
    },
    {
        "q": "5. GLVM BM-nin yaranma səbəbi hansı hadisədir?",
        "a": "11.09.2001-ci il ABŞ-da törədilmiş terror aktı",
        "d": [
            "1912-ci ildə Titanik gəmisinin batması",
            "1989-cu ildə Exxon Valdez tankerinin qəzası",
            "1974-cü ildə SOLAS konvensiyasının qəbul edilməsi"
        ]
    },
    {
        "q": "6. Xarici dövlətin hökuməti onun limanlarına daxil olmaq niyyəti olan gəmilərdən girişə icazə almaq şərti kimi gəminin limanlara son neçə girişi haqqında məlumatları tələb edə bilər?",
        "a": "Liman vasitələrinə son 10 giriş",
        "d": [
            "Liman vasitələrinə son 5 giriş",
            "Liman vasitələrinə son 3 giriş",
            "Liman vasitələrinə son 12 giriş"
        ]
    },
    {
        "q": "7. Limanın mühafizəsinin qiymətləndirilməsi hansı sənədlə rəsmiləşdirilir?",
        "a": "Limanın mühafizəsinin qiymətləndirilməsi haqqında hesabat ilə",
        "d": [
            "Limanın təhlükəsizlik deklarasiyası ilə",
            "Gəmi jurnalı qeydləri ilə",
            "Limanın beynəlxalq yoxlama aktı ilə"
        ]
    },
    {
        "q": "8. Limanın mühafizə planı elektron şəklində saxlanılarkən onun qorunması üçün hansı mühafizə tədbirləri görülməlidir?",
        "a": "Məlumatın icazəsiz istifadəsinin, onun məhv edilməsinin və ya ona dəyişikliklərin edilməsinin qarşısının alınmasına yönəldilən prosedurları həyata keçirmək",
        "d": [
            "Yalnız çap versiyasını hazırlayıb seyfdə saxlamaq",
            "Faylı hər bir liman işçisinin elektron poçtuna göndərmək",
            "Məlumatları yalnız Beynəlxalq Dəniz Təşkilatının serverlərində saxlamaq"
        ]
    },
    {
        "q": "9. Gəminin mühafizə səviyyəsi limanın mühafizə səviyyəsindən yüksək ola bilərmi?",
        "a": "Yüksək ola bilər",
        "d": [
            "Xeyr, heç bir halda ola bilməz",
            "Yalnız liman rəhbərliyi icazə verdikdə ola bilər",
            "Səviyyələr mütləq şəkildə eyni olmalıdır"
        ]
    },
    {
        "q": "10. Mühafizə səviyyəsi 1- adi səviyyə dedikdə nə nəzərdə tutulur?",
        "a": "Riskin minimal səviyyəsidir",
        "d": [
            "Əlavə mühafizə tədbirlərinin tətbiq olunduğu səviyyədir",
            "Terror hadisəsinin gözlənildiyi yüksək səviyyədir",
            "Fövqəladə hallarda elan edilən ən yuxarı səviyyədir"
        ]
    },
    {
        "q": "11. Limanda mühafizə üzrə məşqlər ən azı neçə müddətdən bir keçirilməlidir?",
        "a": "3 ayda azı 1 dəfə",
        "d": [
            "1 ayda azı 1 dəfə",
            "6 ayda azı 1 dəfə",
            "12 ayda azı 1 dəfə"
        ]
    },
    {
        "q": "12. Limanda mühafizə üzrə təlimlər ən azı neçə müddətdən bir keçirilməlidir?",
        "a": "12 ayda azı bir dəfə",
        "d": [
            "6 ayda azı bir dəfə",
            "3 ayda azı bir dəfə",
            "24 ayda azı bir dəfə"
        ]
    },
    {
        "q": "13. Limana zəng vurub təhdid edən şəxslə telefonda necə danışmaq tövsiyyə olunur?",
        "a": "Zəng vuran şəxslə söhbəti maksimum uzatmaq və təmkinli danışmaq",
        "d": [
            "Dərhal telefonu qapatmaq və polisə zəng etmək",
            "Təhdid edən şəxsə qışqırmaq və xəbərdarlıq etmək",
            "Danışığı qısa tutub, yalnız adını soruşmaq"
        ]
    },
    {
        "q": "14. Bomba təhdidini qəbul etmiş liman əməkdaşının ilkin görəcəyi tədbir:",
        "a": "Zəngin vaxtını dərhal qeyd etməlidir",
        "d": [
            "Bütün liman işçilərini səsli həyəcan siqnalı ilə təxliyə etmək",
            "Limanın əsas qapılarını dərhal bağlamaq",
            "Gəmilərə dərhal limanı tərk etməyi əmr etmək"
        ]
    },
    {
        "q": "15. Mühafizə səviyyəsi 3 dedikdə hansı səviyyə nəzərdə tutulur?",
        "a": "Ən yüksək səviyyə",
        "d": [
            "Adi işçi səviyyə",
            "Minimal təhlükə səviyyəsi",
            "Orta mühafizə səviyyəsi"
        ]
    },
    {
        "q": "16. Limanda əlavə mühafizə tədbirlərinin görülməsi hansı mühafizə səviyyəsinə aiddir?",
        "a": "Yüksəldilmiş səviyyəyə",
        "d": [
            "Adi səviyyəyə",
            "Müstəsna səviyyəyə",
            "Aşağı səviyyəyə"
        ]
    },
    {
        "q": "17. Limanda xüsusi mühafizə tədbirlərinin görülməsi hansı mühafizə səviyyəsinə aiddir?",
        "a": "Müstəsna səviyyəyə",
        "d": [
            "Minimal səviyyəyə",
            "Yüksəldilmiş səviyyəyə",
            "Normal səviyyəyə"
        ]
    },
    {
        "q": "18. Müşayiət olunmayan baqaj dedikdə nə nəzərdə tutulur?",
        "a": "Yoxlama və ya baxış keçirilən yerdə müvafiq sərnişin və ya heyət üzvü ilə birgə olmur",
        "d": [
            "Tərkibində partlayıcı maddə olan xüsusi təhlükəli yüklər",
            "Gəmi kapitanının xüsusi nəzarəti altında olan rəsmi sənədlər",
            "Yalnız gömrük deklarasiyası olmayan mallar"
        ]
    },
    {
        "q": "19. Limanda mühafizənin və təhlükəsizliyin təmini üzrə tədbirlərin tətbiqini özündə qeyd edən sənəd necə adlanır?",
        "a": "Liman vasitələrinin mühafizə planı",
        "d": [
            "Gəminin təhlükəsizlik jurnalı",
            "Limanın fəaliyyət reyestri",
            "Liman akvatoriyasının nizamnaməsi"
        ]
    },
    {
        "q": "20. Hansı əşyalar stasionar metal detektorla müəyyən edilir?",
        "a": "Soyuq silahlar",
        "d": [
            "Narkotik və psixotrop maddələr",
            "Tezalışan kimyəvi mayelər",
            "Bioloji və zəhərli qazlar"
        ]
    },
    {
        "q": "21. Liman dövləti GLVM BM-nin tələblərinə uyğun olmayan gəmiyə hansı xüsusi tədbirləri tətbiq edə bilər?",
        "a": "Gəmiyə limana daxil olma icazəsi verilməyə bilər",
        "d": [
            "Gəminin kapitanını dərhal həbs edə bilər",
            "Gəmini dərhal müsadirə edə bilər",
            "Gəminin yükünü təmənnasız boşalda bilər"
        ]
    },
    {
        "q": "22. Mühafizə üzrə iki təlim arasındakı zaman müddəti hansı dövrü aşmamalıdır?",
        "a": "18 ayı",
        "d": [
            "6 ayı",
            "12 ayı",
            "24 ayı"
        ]
    },
    {
        "q": "23. Gəmilərin və liman vasitələrinin mühafizəsi üzrə beynəlxalq məcəllə hansı gəmilərə şamil edilir?",
        "a": "Registr tutumu 500 r/t və yuxarı, Beynəlxalq reyslər həyata keçirən yüksək sürətli yük gəmiləri daxil olmaqla yük gəmilərinə",
        "d": [
            "Yalnız 300 r/t qədər olan kiçik həcmli gəmilərə",
            "Daxili sularda hərəkət edən bütün balıqçı gəmilərinə",
            "Hərbi dəniz donanmasına aid olan gəmilərə"
        ]
    },
    {
        "q": "24. Məhdudlaşdırılmış giriş sahələri haqqında limanın hansı sənədində geniş şərh olunur?",
        "a": "Limanın mühafizə planında",
        "d": [
            "Gəminin sanitar-karantin rəyində",
            "Limanın yükləmə-boşaltma təlimatında",
            "Mühafizə deklarasiyasında"
        ]
    },
    {
        "q": "25. Aşağıda göstərilənlərdən hansılar şübhəli şəxslər kateqoriyasına aiddir?",
        "a": "Ünsiyyətdən yayınan şəxslər",
        "d": [
            "Baqajı çox olan sərnişinlər",
            "Limanda uzun müddət işləyən fəhlələr",
            "Gömrük bəyannaməsini gecikdirən şəxslər"
        ]
    },
    {
        "q": "26. Aşağıda göstərilənlərdən hansılar şübhəli şəxslər kateqoriyasına aiddir?",
        "a": "Mövsüm üzrə geyinməmiş şəxslər",
        "d": [
            "Gəmi forması geyinmiş heyət üzvləri",
            "Əlində kamera olan turistlər",
            "Sənədlərində xırda uyğunsuzluq olan sərnişinlər"
        ]
    },
    {
        "q": "27. XI-2 Fəsli neçə Qaydadan ibarətdir?",
        "a": "13 Qayda",
        "d": [
            "9 Qayda",
            "15 Qayda",
            "20 Qayda"
        ]
    },
    {
        "q": "28. XI-2 Fəslinin III Qaydası nədən bəhs edir?",
        "a": "Mühafizə səviyyələrinin tətbiqindən bəhs edir",
        "d": [
            "Gəminin tanınma nömrələrinin vurulmasından",
            "Gəmi xəbərdarlıq sistemlərinin quraşdırılmasından",
            "Mühafizə üzrə təlimatların tərtib edilməsindən"
        ]
    },
    {
        "q": "29. Liman vasitəsinin mühafizəsi aşağıdakılardan hansını nəzərdə tutur?",
        "a": "Yuxarıda qeyd olunanların hamısını",
        "d": [
            "Yalnız gəmi və liman heyətinin təhlükəsizliyini",
            "Gəmi yükünün gömrük yoxlamasını",
            "Mühafizə avadanlıqlarının texniki baxışını"
        ]
    },
    {
        "q": "30. Liman vasitəsinin mühafizəyə məsul şəxsinin vəzifə borclarını göstərin:",
        "a": "Liman vasitəsinin mühafizə planının qüvvəyə mindirilməsi və yerinə yetirilməsi",
        "d": [
            "Limanda yanğınsöndürmə avadanlıqlarının sınaqdan keçirilməsi",
            "Gəmilərin yüklənmə prosesinin qeydiyyatının aparılması",
            "Sərnişin biletlərinin yoxlanılması və qeydiyyatı"
        ]
    }
]

output_data = {
    "certificate": "Liman vasitələrinin mühafizəyə məsul",
    "questions": []
}

for i, q_data in enumerate(questions_data):
    options = [q_data["a"]] + q_data["d"]
    random.shuffle(options)
    
    correct_key = ""
    options_dict = {}
    letters = ["A", "B", "C", "D"]
    for j, opt in enumerate(options):
        options_dict[letters[j]] = opt
        if opt == q_data["a"]:
            correct_key = letters[j]
            
    q_id = f"q{i+1:03d}"
    
    output_data["questions"].append({
        "id": q_id,
        "question": q_data["q"],
        "options": options_dict,
        "correct_answer": correct_key,
        "explanation": ""
    })

os.makedirs(r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi", exist_ok=True)
output_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\liman_vasit_l_rinin_m_hafiz_y_m_sul.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

print(f"Generated {len(output_data['questions'])} questions and saved to {output_path}")
