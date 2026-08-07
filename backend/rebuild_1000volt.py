import re, json, random

seed = 33304
random.seed(seed)

with open('pdf_debug_1000volt.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for 1. Question \n Düzgün cavab: Answer
pattern = re.compile(r'(\d+)\.\s+(.*?)\n\s*Düzgün cavab:\s*(.*?)(?=\n\s*\d+\.\s+|\n--- PAGE|$)', re.DOTALL)
matches = pattern.findall(text)

distractors_pool = [
    "Qısaqapanma cərəyanı 10 kA-dan çox olduqda",
    "İzolyasiya müqaviməti 500 kOm-dan az olduqda",
    "Gərginlik 220 V dərəcəsinə düşdükdə",
    "Qoruyucu rölelərin həssaslığı artırıldıqda",
    "Torpaqlama konturu tam kəsildikdə",
    "Yalnız aşağı gərginlik şəbəkələrində",
    "Fazalararası gərginlik sıfıra bərabər olduqda",
    "Reaktiv güc itkiləri çox olduqda",
    "Şinlərarası məsafə 10 mm-dən az olduqda",
    "Elektrik mühərrikinin sürəti nominaldan az olduqda",
    "24 V qəza işıqlandırma sistemlərində",
    "Akkumulyator batareyaları tam boşaldıqda",
    "Gərginlik 380 V olduqda",
    "Tezlik 60 Hz-dən 50 Hz-ə dəyişdikdə",
    "Dəyişən cərəyan şəbəkələrində güc əmsalı aşağı olduqda",
    "Sabit cərəyan generatorunun maqnit sahəsi itdikdə",
    "Avtomatik açar termal yüklənmədən çıxdıqda",
    "Yalnız açıq havada quraşdırılmış transformatorlarda",
    "Cərəyan sızması 30 mA-dan çox olduqda",
    "Sinusoidal gərginlik rejimində",
    "Fazalararası müqavimət 0 olduqda",
    "Tranzistor tipli gücləndiricilərdə",
    "Transformator yağı həddindən artıq isindikdə",
    "Bütün fazalarda eyni zamanda qapanma baş verdikdə",
    "Sıxıcı kontaktların boşalması nəticəsində qığılcım yarandıqda",
    "Cərəyan transformatorunun ikinci dolağı açıq qaldıqda",
    "Neytral naqil tamamilə ayrıldıqda",
    "İzolyatorun üzərindəki çirklənmə dərəcəsi artdıqda",
    "Termiki dayanıqlılıq həddini aşdıqda",
    "Həddindən artıq gərginlik (ifrat gərginlik) yarandıqda",
    "Avtomatik idarəetmə dövrələrində nasazlıq yaranarsa",
    "Elektromaqnit induksiyası sıfıra düşərsə",
    "Kabelin xarici örtüyü mexaniki zədələndikdə",
    "Gərginlik transformatorunun sarğılarında qırılma olduqda",
    "Kontaktorda istilik itkisi çox olduqda",
    "Sinfinə görə IP22 mühafizə dərəcəsinə malik avadanlıqlarda",
    "Stator dolağında izolyasiya qatı nazildikdə",
    "Lokal topraqlama xətti mövcud olmadıqda",
    "Tezlik çeviricilərindəki tranzistorlar sıradan çıxdıqda",
    "Üçfazalı sistemdə asimmetriya 10%-i keçdikdə"
]

questions = []
for i, match in enumerate(matches):
    q_num, q_text, ans_text = match
    q_text = q_text.strip().replace('\n', ' ')
    q_text = re.sub(r'\s+', ' ', q_text)
    ans_text = ans_text.strip().replace('\n', ' ')
    ans_text = re.sub(r'\s+', ' ', ans_text)
    
    q_full = f"{q_num}. {q_text}"
    
    dists = random.sample(distractors_pool, 3)
    opts = [ans_text] + dists
    random.shuffle(opts)
    
    letters = ['A', 'B', 'C', 'D']
    options = {}
    correct_letter = 'A'
    for j, o in enumerate(opts):
        options[letters[j]] = o
        if o == ans_text:
            correct_letter = letters[j]
            
    questions.append({
        "id": f"q{int(q_num):03d}",
        "question": q_full,
        "options": options,
        "correct_answer": correct_letter,
        "explanation": ""
    })

output = {
    "certificate": "1000 volt və artıq olan gərginlik sistemlərinin təhlükəsiz istismarı və onlara texniki nəzarət",
    "questions": questions
}

with open(r'static\questions\xususi\1000_volt_v_art_q_olan_g_rginlik_sisteml.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
    
print(f"Total questions generated: {len(questions)}")
