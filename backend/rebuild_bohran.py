import fitz
import json
import random
import re

import glob
pdf_path = glob.glob(r'D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari\*B*hran*zaman*.pdf')[0]
json_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\b_hran_zaman_idar_etm_v_insan_davran_zr_.json'

random.seed(33306)

doc = fitz.open(pdf_path)
text = ''.join([p.get_text() for p in doc])

# Fix page breaks and clean up spaces
text = re.sub(r'\n+', '\n', text)
questions_raw = re.split(r'\n(?=\d+\.)', '\n' + text)

valid_questions = []
for q_raw in questions_raw:
    if not re.match(r'\d+\.', q_raw):
        continue
    # Replace internal newlines for the question text itself, 
    match = re.search(r'(.*?)\nDüzgün cavab:\s*(.*)', q_raw.strip(), re.DOTALL | re.IGNORECASE)
    if match:
        q_text = match.group(1).replace('\n', ' ').strip()
        # Add space after dot if missing
        q_text = re.sub(r'^(\d+\.)([^\s])', r'\1 \2', q_text)
        ans_text = match.group(2).replace('\n', ' ').strip()
        valid_questions.append({
            "question": q_text,
            "correct": ans_text
        })

print(f"Extracted {len(valid_questions)} questions")

distractors_pool = [
    "Sərnişinləri qapalı yerlərdə kilidləmək",
    "Təşviş yaranmaması üçün siqnal verməmək",
    "Gəmi rəhbərliyinin əmrlərini gözləmədən suya atılmaq",
    "Rabitə avadanlığını söndürmək və radio sükutu saxlamaq",
    "Qəza barədə məlumatı sərnişinlərdən gizlətmək",
    "Bütün işıqları söndürərək insanların hərəkətini məhdudlaşdırmaq",
    "Xilasedici qayıqları tam dolmadan suya buraxmaq",
    "Kapitanın əmrini gözləmədən xilasetmə işlərinə başlamaq",
    "Panikaya düşən insanları fiziki güc tətbiq edərək sakitləşdirmək",
    "Təcrid olunmuş otaqlarda sərnişinləri nəzarətsiz qoymaq",
    "Qaydalara zidd olaraq özbaşına qərarlar qəbul etmək",
    "Fövqəladə hal zamanı yalnız heyət üzvlərinin xilasını təmin etmək",
    "Sərnişinlərin toplanış məntəqələrinə deyil, birbaşa qayıqlara getməsini tələb etmək",
    "Qəza zamanı fərdi xilasedici vasitələrdən istifadəni qadağan etmək",
    "Xəbərdarlıq siqnallarını qulaqardına vuraraq gündəlik işlərə davam etmək",
    "Təxliyə planını dəyişdirmək və alternativ lakin yoxlanılmamış yollarla hərəkət etmək",
    "Təxliyə yollarını bloklamaq və insanların hərəkətini əngəlləmək",
    "İnsanların qorxmaması üçün yalan məlumatlar vermək",
    "Siqnalizasiya sistemini bilərəkdən söndürmək",
    "Bütün sərnişinləri eyni vaxtda dar dəhlizlərə yönəltmək",
    "Xilasetmə əməliyyatını yalnız gündüz vaxtı həyata keçirmək",
    "Fövqəladə halda rabitə əlaqəsini kəsərək müstəqil fəaliyyət göstərmək",
    "Sərnişinlərin gəmi göyərtəsində sərbəst hərəkətinə icazə vermək",
    "Təxliyə zamanı liftlərdən kütləvi şəkildə istifadə etmək",
    "Qadın və uşaqların xilas edilməsini ən sona saxlamaq",
    "Heyət üzvlərinin panikada olan sərnişinlərlə mübahisə etməsi",
    "Toplanış məntəqələrində qeydiyyat aparmadan insanları qayıqlara mindirmək",
    "Gəmi kapitanının icazəsi olmadan ümumi həyəcan elan etmək",
    "Yalnız birinci dərəcəli sərnişinləri xilas etmək",
    "Gəmini dərhal tərk etmək və xilasedici jiletləri axtarmaq",
    "Gəmidəki bütün qida və su ehtiyatlarını dərhal məhv etmək",
    "Fövqəladə halda ancaq gəminin yükünü xilas etməyə çalışmaq",
    "Xilasedici salları gəmiyə möhkəm bağlamaq və buraxmamaq",
    "Təxliyə zamanı sərnişinlərin şəxsi əşyalarını daşımasına icazə vermək",
    "Xilasedici vasitələrin yoxlanılmasını qəza anına qədər təxirə salmaq"
]

out_data = {
    "certificate": "Böhran zamanı idarəetmə və insan davranışı üzrə hazırlıq",
    "questions": []
}

for i, q in enumerate(valid_questions):
    q_id = f"q{i+1:03d}"
    correct_ans = q['correct']
    
    available_distractors = [d for d in distractors_pool if d.lower().strip() != correct_ans.lower().strip()]
    wrong_options = random.sample(available_distractors, 3)
    
    options_list = [correct_ans] + wrong_options
    random.shuffle(options_list)
    
    labels = ['A', 'B', 'C', 'D']
    options_dict = {}
    correct_label = ''
    
    for label, opt in zip(labels, options_list):
        options_dict[label] = opt
        if opt == correct_ans:
            correct_label = label
            
    out_data['questions'].append({
        "id": q_id,
        "question": q['question'],
        "options": options_dict,
        "correct_answer": correct_label,
        "explanation": ""
    })

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

print("JSON successfully rebuilt and saved.")
