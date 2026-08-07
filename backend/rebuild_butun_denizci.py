import json
import random
import os

def rebuild():
    random.seed(33308)
    
    with open('questions_parsed.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
        
    with open('distractors.json', 'r', encoding='utf-8') as f:
        distractors_dict = json.load(f)
        
    final_questions = []
    
    for idx, q_data in enumerate(questions):
        q_id = str(q_data['id'])
        question_text = q_data['q']
        correct_answer = q_data['a']
        
        dists = distractors_dict.get(q_id, [
            'müvafiq təhlükəsizlik qaydalarına əsasən',
            'qəza anında xüsusi təlimata uyğun olaraq',
            'gəmi kapitanının əlavə göstərişi ilə'
        ])
        
        options = [correct_answer] + dists
        random.shuffle(options)
        
        letters = ['A', 'B', 'C', 'D']
        options_dict = {}
        correct_letter = 'A'
        
        for i, opt in enumerate(options):
            options_dict[letters[i]] = opt
            if opt == correct_answer:
                correct_letter = letters[i]
        
        final_questions.append({
            'id': f'q{idx+1:03d}',
            'question': question_text,
            'options': options_dict,
            'correct_answer': correct_letter,
            'explanation': ''
        })
        
    final_json = {
        'certificate': 'bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat',
        'questions': final_questions
    }
    
    # Let's ensure output directory exists
    out_dir = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi'
    os.makedirs(out_dir, exist_ok=True)
    
    with open(r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\b_t_n_d_niz_il_r_n_t_hl_k_sizlik_zr_tan_.json', 'w', encoding='utf-8') as f:
        json.dump(final_json, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    rebuild()
