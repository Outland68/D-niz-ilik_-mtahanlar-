import json
import re
import random

random.seed(33303)

with open('pdf_debug_tibbi_nezaret.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix newline split in answer prefix and page boundaries
text = re.sub(r'Düzgün\s+cavab:', 'Düzgün cavab:', text)
text = re.sub(r'--- PAGE \d+ ---', '', text)

questions_data = []
matches = list(re.finditer(r'(?m)^(\d+)\.\s*(.*?)\s*Düzgün cavab:\s*(.*?)(?=\n\s*\d+\.|\Z)', text, re.DOTALL))

for m in matches:
    q_id = int(m.group(1))
    q_text = m.group(2).strip().replace('\n', ' ')
    a_text = m.group(3).strip().replace('\n', ' ')
    
    questions_data.append({
        'id': f"q{q_id:03d}",
        'question_text': f"{q_id}. {q_text}",
        'answer_text': a_text
    })

print(f"Extracted {len(questions_data)} questions.")

pools = {
    'qanaxma': ["Yaraya isti kompres qoymaq", "Zərərçəkənə çoxlu maye içirtmək", "Turnanı 3 saatdan çox saxlamaq", "Yaranı spirtlə yumaq", "Qanayan hissəni aşağı salmaq", "Yaraya açıq sarğı qoymaq"],
    'yanıq': ["Yanıq yerinə bitki yağı çəkmək", "Suluqları deşmək", "Yanıq səthinə yod sürtmək", "Yaraya pambıq qoymaq", "Spirtlə təmizləmək"],
    'sınıq': ["Sınmış sümüyü yerinə salmağa çalışmaq", "Sınıq yerinə isti qoymaq", "Xəstəni yeritməyə cəhd etmək", "Ağrıkəsici vermədən sümüyü düzəltmək"],
    'huş': ["Ağzına soyuq su tökmək", "Başının altına hündür yastıq qoymaq", "Xəstəni dərhal oturtmaq", "Süni tənəffüs vermədən masaj etmək"],
    'donma': ["Donmuş nahiyəni isti su ilə yumaq", "Oduza yaxınlaşdırmaq", "Qarla ovxalamaq", "Suluqları partlatmaq"],
    'zəhərlənmə': ["Xəstəyə isti çay vermək", "Gözləri spirtlə yumaq", "Xəstəni isti yorğana bükmək", "Aspirin vermək"],
    'general': ["Xəstəyə sakitləşdirici vermək", "Yalnız kapitanın icazəsi ilə yardım etmək", "Gəmi aptekçisini gözləmək", "Gündə 3 dəfə antibiotik vermək", "Damardaxili iynə vurmaq", "Dərhal əməliyyat etmək", "Xəstəni izolyatora yerləşdirmək", "Yaraya yod sürtmək", "Şin qoymadan xəstəni köçürmək"]
}

def get_distractors(q_text):
    text_lower = q_text.lower()
    selected_pool = []
    if 'qanaxma' in text_lower or 'qan' in text_lower:
        selected_pool.extend(pools['qanaxma'])
    if 'yanıq' in text_lower or 'termiki' in text_lower:
        selected_pool.extend(pools['yanıq'])
    if 'sınıq' in text_lower or 'sümük' in text_lower:
        selected_pool.extend(pools['sınıq'])
    if 'huş' in text_lower or 'reanimasiya' in text_lower or 'nəbz' in text_lower:
        selected_pool.extend(pools['huş'])
    if 'donma' in text_lower or 'soyuq' in text_lower or 'hipotermiya' in text_lower:
        selected_pool.extend(pools['donma'])
    if 'zəhərlənmə' in text_lower or 'turşu' in text_lower or 'qələvi' in text_lower:
        selected_pool.extend(pools['zəhərlənmə'])
    
    if len(selected_pool) < 3:
        selected_pool.extend(pools['general'])
        
    random.shuffle(selected_pool)
    return selected_pool[:3]

final_questions = []
for q in questions_data:
    correct = q['answer_text']
    distractors = get_distractors(q['question_text'])
    
    options_list = [correct] + distractors
    random.shuffle(options_list)
    
    correct_letter = ""
    options_dict = {}
    letters = ['A', 'B', 'C', 'D']
    
    for i, opt in enumerate(options_list):
        options_dict[letters[i]] = opt
        if opt == correct:
            correct_letter = letters[i]
            
    final_questions.append({
        "id": q['id'],
        "question": q['question_text'],
        "options": options_dict,
        "correct_answer": correct_letter,
        "explanation": ""
    })

json_data = {
    "certificate": "Gəmidə tibbi nəzarət",
    "questions": final_questions
}

out_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mid_tibbi_n_zar_t.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("JSON saved successfully.")
