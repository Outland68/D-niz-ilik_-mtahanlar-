import json
import random

questions_data = [
    {
        'q': 'Gəminin elektrik sxemlərində və elektrik avadanlıqlarında həyata keçirilmiş dəyişikliklər haqqında məlumatlar harada öz əksini tapmalıdır?',
        'a': 'Gəminin texniki sənədlərində',
        'd': ['Baş mühərrikin formulyarında', 'Gündəlik maşın jurnalında', 'Elektrik təhlükəsizliyi jurnalında']
    },
    {
        'q': 'Cərəyanla qurutma, izolyasiyasının müqavimətinin neçə Mom olan elektrik maşınlarında həyata keçirilməsinə icazə verilir?',
        'a': '0.1 Mom-dan az olmayan elektrik maşınlarında',
        'd': ['0.5 Mom-dan az olmayan elektrik maşınlarında', '1.0 Mom-dan az olmayan elektrik maşınlarında', '0.01 Mom-dan az olmayan elektrik maşınlarında']
    },
    {
        'q': 'Akkumulyator batareyalarında keçirilən texniki baxışların mütəmadilik, dövrilik müddətini qeyd edin?',
        'a': 'Hər ayda bir dəfədən az olmayan müddət ərzində',
        'd': ['Hər həftə bir dəfədən az olmayan müddət ərzində', 'Altı ayda bir dəfədən az olmayan müddət ərzində', 'Hər üç aydan bir dəfədən az olmayan müddət ərzində']
    },
    {
        'q': 'Tullantılara nəzarət olunmayan rayonlarda tərkibində kükürdün faiz miqdarı neçə faizdən az və ya çox olduqda həmin yanacaqdan istifadə etməyə icazə verilir?',
        'a': '3.50-dən çox olmadıqda',
        'd': ['1.50-dən çox olmadıqda', '4.50-dən çox olmadıqda', '2.00-dən çox olmadıqda']
    },
    {
        'q': 'Tullantılara nəzarət rayonlarından keçid zamanı tərkibində neçə faiz kükürd olan yanacaqdan istifadə edilməsinə icazə verilir?',
        'a': '1.00 %-dən çox olmayan',
        'd': ['0.50 %-dən çox olmayan', '0.10 %-dən çox olmayan', '2.50 %-dən çox olmayan']
    },
    {
        'q': 'Ən yaxın sahildən 12 mil məsafədə olduqda MARPOL-73/78 BK-nın V əlavəsinə əsasən nələrin dənizə tullanmasına icazə verilir?',
        'a': 'Dondurulmuş halda balıq, ət, digər qida məhsulları və xırdalanmış ərzaq tullantıları',
        'd': ['Gəminin təmizlənməsi zamanı yaranan plastik tullantılar', 'Sürtkü yağları və neft qalıqları', 'Qablaşdırma materialları və kağız tullantıları']
    },
    {
        'q': 'Əl yanğın xəbərdarlıq edicilər harada yerləşdirilməlidirlər?',
        'a': 'Hər bir yanğın zonasında',
        'd': ['Yalnız baş mühərrik otağında', 'Yalnız gəmi kapitanının körpücüyündə', 'Qorunan sahələrdən kənarda, açıq göyərtədə']
    },
    {
        'q': 'Növbətçi qayıq hansı sürətlə manevr etmək imkanlarına malik olmalıdır?',
        'a': '6 uzel',
        'd': ['12 uzel', '4 uzel', '8 uzel']
    },
    {
        'q': 'Gəmidə təmir işləri yerinə yetirildiyi zaman yanğın təhlükəsizliyinin təmin olunmasına kim cavabdehdir?',
        'a': 'Gəmi təmiri müəssisəsi',
        'd': ['Baş mexanik', 'Növbətçi mexanik', 'Gəminin kapitanı']
    },
    {
        'q': 'Gəminin heyət üzvlərindən hansı vəzifəli şəxs gəminin bütün mexaniki qurğularının texniki vasitələrini və gövdə konstruksiyalarını rəhbər heyət üzvləri arasında təhkimatlar üzrə bölüşdürür?',
        'a': 'Baş mexanik',
        'd': ['Kapitan', 'Baş köməkçi', 'Elektrik mexaniki']
    },
    {
        'q': 'Gəminin qəzaya uğraması nəticəsində heyət üzvünün əmlakına zərər dəydikdə və ya əmlak itirildikdə, məhv olduqda həmin ziyan heyət üzvünə kim tərəfindən ödənilməlidir?',
        'a': 'Sığorta şirkəti tərəfindən',
        'd': ['Gəmi sahibi tərəfindən', 'Liman rəhbərliyi tərəfindən', 'Kadrlar şöbəsi tərəfindən']
    },
    {
        'q': '“Transducer” sözünün düzgün tərcüməsini qeyd edin?',
        'a': 'Ötürücü cihaz',
        'd': ['Transformator', 'Tranzistor', 'Düzləndirici']
    },
    {
        'q': '“Sea-chest” sözünün düzgün tərcüməsini qeyd edin?',
        'a': 'Kinqston',
        'd': ['Dəniz sandığı', 'Su pompası', 'Hava kompressoru']
    },
    {
        'q': '“Seal” sözünün düzgün tərcüməsini qeyd edin?',
        'a': 'Kipləndirici, salnik',
        'd': ['Qoruyucu örtük', 'Sızdırmazlıq klapanı', 'Elektrik izolyasiyası']
    },
    {
        'q': '“Assembly” sözünün düzgün tərcüməsini qeyd edin?',
        'a': 'Yığmaq, montaj etmək',
        'd': ['Sökmək, demontaj etmək', 'Yoxlamaq, test etmək', 'Tənzimləmək, kalibrləmək']
    },
    {
        'q': 'Baş paylayıcı lövhədə quraşdırılmış voltmetrlər nəyi göstərir?',
        'a': 'Xəttdə olan cərəyan gərginliyini',
        'd': ['Generatordan keçən cərəyan şiddətini', 'Şəbəkənin aktiv gücünü', 'Fazalararası müqaviməti']
    },
    {
        'q': 'Orqanizmdən keçən 50 Hz tezliklə, dəyişən elektrik cərəyanı hansı ölçüdə olduqda insan onu hiss etmiş olur?',
        'a': '1.1 mA',
        'd': ['10 mA', '50 mA', '0.1 mA']
    },
    {
        'q': 'Cərəyan göstəricisinin əvəzinə nəzarət elektrik lampasından istifadə etmək olarmı?',
        'a': 'Qətiyyən olmaz',
        'd': ['Yalnız fövqəladə hallarda olar', 'Kapitanın icazəsi ilə olar', 'Yalnız alçaq gərginliklərdə olar']
    },
    {
        'q': 'Dəyişən cərəyanlı elektromaqnitin lövbərinin ilişməsi nəyə səbəb ola bilər?',
        'a': 'Elektromaqnitin sarğısının yanmasına',
        'd': ['Generatorda tezliyin artmasına', 'İzolyasiya müqavimətinin yüksəlməsinə', 'Şəbəkədə gərginliyin düşməsinə']
    },
    {
        'q': 'Gəmi şəraitində möhürlərin çıxarılması, nəzarət ölçü cihazlarının açılması və təmir edilməsi gəmi heyət üzvlərindən kimin nəzarəti altında həyata keçirilməlidir?',
        'a': 'Kapitanın növbə köməkçisinin',
        'd': ['Baş mexanikin', 'Elektrik mexanikinin', 'Növbətçi motorçunun']
    },
    {
        'q': 'Cərəyanın güc transformatorunun paralel iş rejiminə ardıcıl olaraq düzgün qoşulma qaydasını qeyd edin:',
        'a': 'Paralel qoşulma öncə birinci, sonra isə ikinci şəbəkədən qoşulmaqla həyata keçirilir',
        'd': ['Eyni vaxtda hər iki şəbəkədən qoşulur', 'Paralel qoşulma ancaq yüksək gərginlik tərəfdən aparılır', 'Əvvəlcə neytral xətt, sonra isə fazalar qoşulur']
    },
    {
        'q': 'İstismarda olan yarımkeçirici dəyişdiricilərin izolyasiyasının normal müqavimətini qeyd edin?',
        'a': '1.0 Mom',
        'd': ['0.5 Mom', '5.0 Mom', '10.0 Mom']
    },
    {
        'q': 'Uzun müddət istismar edilməyən elektrik cihazlarının dövri texniki baxışlarının keçirilməsi və yoxlanması hansı müddətlərdə həyata keçirilir?',
        'a': 'Bir ayda bir dəfədən az olmayaraq',
        'd': ['Altı ayda bir dəfədən az olmayaraq', 'Hər həftə bir dəfə', 'Üç ayda bir dəfədən az olmayaraq']
    },
    {
        'q': 'Qoruyucu qurğunun işə düşməsi nəticəsində iş rejimindən çıxarılan və ya çıxardılan mexanizmin (qurğunun) avtomatik və ya məsafədən işə salınması üçün nə etmək lazım olduğunu qeyd edin:',
        'a': 'Əl vasitəsi ilə qoruyucu qurğunu əvvəlki vəziyyətə gətirmək',
        'd': ['İdarəetmə pultundan siqnalı sıfırlamaq', 'Şəbəkə gərginliyini kəsib yenidən vermək', 'Avtomatik açarı birbaşa dövrədən xaric etmək']
    },
    {
        'q': 'Nəzarət Məlumat Ölçü Sistemlərinin (MÖS) kanalının funksiyası nədən ibarətdir?',
        'a': 'Nəzarət edilən parametrlərin normadan kənara çıxdığı hallarda işıq siqnallarının formalaşdırılması',
        'd': ['Mexanizmlərin avtomatik işə salınması və dayandırılması', 'Elektrik enerjisinin paylanmasına nəzarət', 'Generatorda yaranan sinxronizasiya xətalarının düzəldilməsi']
    },
    {
        'q': 'Danışıq aparatlarının quraşdırılması zaman hansı tədbirləri həyata keçirmək lazımdır?',
        'a': 'Mexanizmlərin işləməsi zaman yaxşı eşitmə imkanlarının təmin edilməsi',
        'd': ['Cihazların mühərrik otağından tamamilə izolyasiya edilməsi', 'Yalnız baş mexanikin otağına qoşulmasının təmin edilməsi', 'Kabellərin yüksək gərginlikli xətlərlə birgə çəkilməsi']
    },
    {
        'q': 'Aşağıda qeyd edilənlərdən hansı cihazdan istifadə edərək Avtomatik İdarəetmə Sistemlərində gərginliyin ölçülməsi yerinə yetirilə bilər?',
        'a': 'Elektron voltmetrdən və ya yüksək çıxış müqaviməti olan əqrəbli voltmetrdən istifadə edərək',
        'd': ['Megometrdən və ya ommetrdən istifadə edərək', 'Alçaq çıxış müqaviməti olan rəqəmsal ampermetrdən istifadə edərək', 'Cərəyan transformatorundan istifadə edərək']
    },
    {
        'q': 'Dəyişən cərəyanlı gəmi elektroenergetik sistemlərinin paylama şəbəkələrinin bütün şaxələrində hansı növ qoruma quraşdırılmalıdır?',
        'a': 'Həddindən artıq yüklənmədən və qısa qapanmadan',
        'd': ['Yalnız gərginlik düşməsindən', 'Yalnız tezliyin artmasından', 'Yalnız fazalararası asimmetriyadan']
    },
    {
        'q': 'Avral siqnalizasiyanın işinin hansı müddətlərdə yoxlanması gərəkdir?',
        'a': 'Gəmi səfərə çıxmazdan öncə və hər 10 gündən bir',
        'd': ['Gəmi limana çatdıqda və hər 30 gündən bir', 'Hər növbə dəyişimində', 'Yalnız həyəcan siqnalı verildikdə']
    },
    {
        'q': 'İşləmək bacarığının (qabiliyyətinin) itirilməsinə nəzarət siqnalizasiyası hansı növ gəmilərdə quraşdırılır?',
        'a': 'Maşın bölməsində növbəçəkmə bir nəfər tərəfindən aparılan və maşın bölməsində növbəçəkmə xidməti aparılmayan gəmilərdə',
        'd': ['Yalnız sərnişin gəmilərində', 'Yalnız təhlükəli yük daşıyan tankerlərdə', 'Bütün tip hərbi gəmilərdə']
    },
    {
        'q': 'Yük əməliyyatları zaman tryumlarda işıqların yandırılıb söndürülməsinə və tryum işıqlarının istifadəsinə nəzarət kim tərəfindən həyata keçirilir?',
        'a': 'Gəmi kapitanının növbə köməkçisi tərəfindən',
        'd': ['Elektrik mexaniki tərəfindən', 'Bosman tərəfindən', 'Baş mexanik tərəfindən']
    },
    {
        'q': 'Gəminin akkumulyator batareyalarının qidalandırılmasına dair başqa bir özəl, xüsusi göstəriş olmadığı təqdirdə (akkumulyatorların nominal həcmi miqdarına bərabər olan 0.25 A-saat cərəyanla) normal qidalandırılması hansı müddətlərdə həyata keçirilməlidir?',
        'a': '6 saat',
        'd': ['10 saat', '12 saat', '24 saat']
    },
    {
        'q': 'Akumulyator batareyalarının sürətləndirilmiş qidalandırılmasını (normal qidalandırma cərəyan şiddətindən iki dəfə çox cərəyan şiddəti ilə) neçə saat ərzində yerinə yetirmək lazımdır?',
        'a': '3 ssat',
        'd': ['1 saat', '6 saat', '8 saat']
    },
    {
        'q': 'Gəmidə gəmi elektrik avadanlıqlarının, habelə ehtiyat hissələrinin sərf edilməsinin və qalıqlarının qeydiyyatı aparılmalıdır. Bu qeydiyyat kitablarının formasını və qaydalarını kim müəyyən edir?',
        'a': 'Gəmi sahibi',
        'd': ['Dəniz Administrasiyası', 'Baş mexanik', 'Klassifikasiya Cəmiyyəti']
    },
    {
        'q': 'Gəmidə istismara yararlı və saz vəziyyətdə olan elektrik avadanlıqlarını və qurğularını istismara hazırlanmasına və istismar edilməsinə icazə verilir. Nasaz olan elektrik avadanlıqlarının üzərində asılan xəbərdarlıq lövhələri hansı məzmunlu olmalıdırlar?',
        'a': 'Nasazlıq var. İşə salmaq qəti qadağandır',
        'd': ['Təmir gözlənilir. İdarə pultuna yaxınlaşmayın', 'Ehtiyat hissə. İstifadəsi məhduddur', 'Nasazlıq var. Yalnız təcili hallarda qoşun']
    },
    {
        'q': 'Nə üçün düzləndiricinin çıxışına paralel olaraq, fırçasız generatorun rotorunun üzərində varistor birləşdirilir?',
        'a': 'Yarımkeçirici düzləndiricinin elektrik cərəyanından qorunması üçün',
        'd': ['Generatorda tezliyi sabit saxlamaq üçün', 'Fırçaların qığılcım verməsinin qarşısını almaq üçün', 'Rotorun qızmasının qarşısını almaq üçün']
    },
    {
        'q': 'Generatorların texniki baxışlarının orta hesabla keçirilmə müddətlərini qeyd edin:',
        'a': '6-12 ay',
        'd': ['1-3 ay', '2-4 il', 'Hər səfərdən sonra']
    },
    {
        'q': 'Paylayıcı lövhələr bağlanılmalıdır?',
        'a': 'Az gərginlikli elektrik paylayıcılarının qapılarını bağlamaq üçün təyin edilmiş açarlardan fərqli olan, xüsusi açarla',
        'd': ['Standart asma qıfılla və açarı baş mexanikdə saxlanmaqla', 'Avtomatik kilidləmə sistemi ilə', 'Yalnız rezin izolyasiyalı bağlayıcılarla']
    },
    {
        'q': 'Lokal şəbəkə və kompüterlər arasında ikipanelli məlumat mübadiləsini təmin etmək üçün istifadə edilir:',
        'a': 'Şəbəkə adapteri',
        'd': ['Prosessor', 'Qidalanma bloku', 'Keş yaddaşı']
    },
    {
        'q': 'Kompüter sistem və şəbəkələrində istifadə edilən “Protokol” sözü nə deməkdir?',
        'a': 'Kompüter sistem və şəbəkələrində eyni səviyyədə, lakin müxtəlif şəbəkələrdə yerləşən məlumatların mübadiləsinin formatını və prosedurlarını nizama (müəyyən qaydaya) salan qaydalar məcmusudur',
        'd': ['Qonşu şəbəkə qovşaqları arasındakı fiziki bağlantını təmin edən kabellər sistemidir', 'Şəbəkədə məlumatların şifrələnməsini və təhlükəsizliyini təmin edən proqram təminatıdır', 'İstismar zamanı avadanlıqlarda yaranan xətaların qeydiyyat jurnalının formasıdır']
    },
    {
        'q': 'Kompüter sistem və şəbəkələrində istifadə edilən “Interfeys” sözü nə deməkdir?',
        'a': 'Kompüter sistem və şəbəkələrində qonşu səviyyələrdə, lakin eyni şəbəkədə yerləşən məlumatların mübadiləsinin formatını və prosedurlarını nizama (müəyyən qaydaya) salan qaydalar məcmusudur',
        'd': ['Yalnız şəbəkə istifadəçilərinin giriş hüquqlarını təyin edən qaydalardır', 'İki fərqli əməliyyat sistemi arasında məlumatı ötürən xüsusi proqramdır', 'Tətbiqlərin yaddaş resurslarına birbaşa çıxışını məhdudlaşdıran sistem xidmətidir']
    },
    {
        'q': 'Registrin qaydalarına əsasən gəmi sinxron maşınlarında hava zazorlarında qeyri müntəzəmliyin aralıqlarının kəmiyyətinin qiyməti nə qədər təşkil edir?',
        'a': 'Orta aralığa nisbətdə ± 10%',
        'd': ['Orta aralığa nisbətdə ± 5%', 'Orta aralığa nisbətdə ± 15%', 'Orta aralığa nisbətdə ± 20%']
    },
    {
        'q': 'Fırçalı və kontakt üzüklü sinxron generatorlarda kontakt üzüklərinin qütblərinin dəyişdirilməsi hansı səbəblərdən yerinə yetirilir?',
        'a': 'Üzüklərin yeyilməsinin müntəzəm şəkildə, bərabər səviyyədə həyata keçməsinin təmin edilməsi üçün',
        'd': ['Fırçaların qığılcımlanmasının qarşısının tam alınması üçün', 'Çıxış gərginliyinin fazalarının dəyişdirilməsi üçün', 'Rotorun tezliyinin sabitləşdirilməsi üçün']
    },
    {
        'q': 'Üç fazalı asinxron elektrik mühərrikinin nominal cərəyan şiddəti 200A bərabərdir. Yüklənmədən birbaşa şəbəkəyə qoşulma zamanı cərəyan sıçrayışı neçə amper təşkil edəcək?',
        'a': '1000 A',
        'd': ['400 A', '600 A', '2000 A']
    },
    {
        'q': 'Üç fazalı asinxron elektrik mühərriki nominal cərəyanlı yüklə işləyir. Bu zaman qəflətən bir faza qırılır. Elektrik mühərrikinin istehlak etdiyi cərəyan necə dəyişəcək?',
        'a': 'Artacaq',
        'd': ['Azalacaq', 'Sıfıra bərabər olacaq', 'Dəyişməz qalacaq']
    },
    {
        'q': 'Sinxron elektrik mühərrikinin cərəyan gərginliyi 10 % azaldıqda mühərrikin dövrlər sayı nə cür dəyişir?',
        'a': 'Dəyişməz olaraq sabit qalır',
        'd': ['10 % azalır', '10 % artır', 'Sürətlə sıfıra düşür']
    },
    {
        'q': 'Özü havalandırılan elektrik mühərrikini xaricdən, asılı olmayan üfürmə ilə təchiz etsək onun daimi qızma saatı nə cür dəyişəcəkdir?',
        'a': 'Azalacaq',
        'd': ['Artacaq', 'Dəyişməz qalacaq', 'Mühərrik dərhal yanacaq']
    }
]

extracted_data = json.load(open('extracted_q.json', encoding='utf-8'))

output_json = {
    'certificate': 'Gəmi elektrik mexaniklərinin təkmilləşdirilməsi',
    'questions': []
}

random.seed(33324)

for i, ext in enumerate(extracted_data):
    normalized_ext_a = " ".join(ext['a'].split())
    manual_q = next((q for q in questions_data if " ".join(q['a'].split()) == normalized_ext_a), None)
    if manual_q is None:
        print(f"Error finding manual question for: {ext['a']}")
        continue
        
    opts = [ext['a']] + manual_q['d']
    random.shuffle(opts)
    
    options_dict = {'A': opts[0], 'B': opts[1], 'C': opts[2], 'D': opts[3]}
    correct_key = [k for k, v in options_dict.items() if v == ext['a']][0]
    
    output_json['questions'].append({
        'id': f"q{(i+1):03d}",
        'question': ext['q'],
        'options': options_dict,
        'correct_answer': correct_key,
        'explanation': ''
    })

file1 = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mi_elektrik_mexanikl_rinin_t_kmill_dir.json"
file2 = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\gemi_elektrik_mexanikleri.json"

with open(file1, "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=4, ensure_ascii=False)

with open(file2, "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=4, ensure_ascii=False)

print("Rebuilt successfully.")
