import re, json, random
random.seed(33301)

with open('pdf_debug_isps3.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

# Clean up page headers
txt = re.sub(r'\n--- PAGE \d+ ---\n', '\n', txt)

# Split by Question Number pattern
questions_raw = re.split(r'\n(?=\d+\.\s)', txt)

who_pool = [
    'Liman vasitəsinin mühafizəyə məsul şəxsi',
    'Gəmi kapitanı',
    'Gəmi sahibi',
    'Dövlət liman nəzarəti (PSC)',
    'Beynəlxalq Dəniz Təşkilatı (IMO)',
    'Şirkətin mühafizəyə məsul şəxsi (CSO)',
    'Gəminin mühafizəyə məsul şəxsi (SSO)',
    'Tanınmış mühafizə təşkilatı (RSO)',
    'Bayraq dövlətinin dəniz administrasiyası'
]

time_pool = [
    '3 aydan artıq olmayaraq',
    '6 ay ərzində',
    '1 il müddətinə',
    '5 ildən artıq olmayaraq',
    '12 ayda 1 dəfə',
    '3 ayda azı 1 dəfə',
    '6 ayda 1 dəfə',
    '24 saat ərzində',
    'Səfər başa çatana qədər'
]

general_pool = [
    'Gəminin mühafizə xəbərdaretmə sistemini (SSAS) aktivləşdirməklə',
    'Liman vasitəsinin mühafizə planına dəyişiklik etməklə',
    'Avtomatik İdentifikasiya Sistemini (AIS) söndürməklə',
    'Gəminin mühafizə səviyyəsini dərhal 3-ə qaldırmaqla',
    'Qapalı sahələrə girişə tam qadağa qoymaqla',
    'Mühafizə haqqında deklarasiyanı (DoS) ləğv etməklə',
    'Yük əməliyyatlarını tamamilə dayandırmaqla',
    'Gəminin fasiləsiz qeydiyyat jurnalında (CSR) qeyd aparmaqla',
    'Gəmi heyətinin sahilə çıxışını qadağan etməklə',
    'Gəminin yanğından mühafizə planını tətbiq etməklə',
    'Liman dövləti nəzarəti (PSC) tərəfindən yoxlama tələb etməklə',
    'Mühafizə üzrə təlimləri ayda iki dəfə keçirməklə',
    'Bütün ziyarətçiləri gəmidən kənarlaşdırmaqla',
    'Məhdudlaşdırılmış giriş zonalarının sayını azaltmaqla',
    'Xarici dövlət hökumətindən xüsusi icazə almaqla'
]

yes_no_pool = [
    'Bəli',
    'Xeyr',
    'Yalnız kapitanın yazılı icazəsi ilə',
    'Yalnız liman nəzarətinin göstərişi olduqda',
    'Mühafizə səviyyəsi 3 olduqda bəli',
    'Bəli, lakin yalnız gündüz vaxtı',
    'Xeyr, heç bir halda icazə verilmir'
]

combo_pool = ['1, 2', '1, 3', '2, 3', '1, 4', '2, 4', '3, 4', '1, 2, 3', '1, 3, 4', '2, 3, 4', '1, 4, 5', '2, 4, 5', '1, 2, 5']

out_questions = []
q_counter = 1

for q_raw in questions_raw:
    if 'Düzgün cavab:' not in q_raw:
        continue
    parts = q_raw.split('Düzgün cavab:')
    q_text = parts[0].strip()
    c_ans = parts[1].strip()
    
    q_text = re.sub(r'\s+', ' ', q_text).strip()
    c_ans = re.sub(r'\s+', ' ', c_ans).strip()
    
    m = re.match(r'^(\d+)\.', q_text)
    if not m:
        continue
    
    distractors = []
    c_ans_lower = c_ans.lower()
    
    if re.match(r'^[\d,\s]+$', c_ans):
        pool = [p for p in combo_pool if p != c_ans]
        distractors = random.sample(pool, 3)
    elif c_ans_lower in ['bəli', 'xeyr', 'bəli, mütləqdir']:
        pool = [p for p in yes_no_pool if p.lower() != c_ans_lower and p.lower() not in c_ans_lower]
        distractors = random.sample(pool, 3)
    elif 'kim' in q_text.lower():
        pool = [p for p in who_pool if p.lower() != c_ans_lower and p.lower() not in c_ans_lower]
        distractors = random.sample(pool, 3)
    elif any(w in c_ans_lower for w in ['ay', 'il', 'gün', 'saat', 'dəfə', 'müddət']):
        pool = [p for p in time_pool if p.lower() != c_ans_lower and p.lower() not in c_ans_lower]
        distractors = random.sample(pool, 3)
    else:
        pool = [p for p in general_pool if p.lower() != c_ans_lower and p.lower() not in c_ans_lower]
        distractors = random.sample(pool, 3)
        
    options_list = distractors + [c_ans]
    random.shuffle(options_list)
    
    letters = ['A', 'B', 'C', 'D']
    options_dict = {}
    correct_letter = ''
    
    for i in range(4):
        options_dict[letters[i]] = options_list[i]
        if options_list[i] == c_ans:
            correct_letter = letters[i]
            
    out_questions.append({
        'id': f'q{q_counter:03d}',
        'question': q_text,
        'options': options_dict,
        'correct_answer': correct_letter,
        'explanation': ''
    })
    q_counter += 1

final_json = {
    'certificate': 'ISPS-3',
    'questions': out_questions
}

with open('static/questions/xususi/isps_3.json', 'w', encoding='utf-8') as f:
    json.dump(final_json, f, ensure_ascii=False, indent=2)

print(f'Successfully wrote {len(out_questions)} questions to isps_3.json')
