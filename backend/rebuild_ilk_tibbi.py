import random
import re
import json
import os

random.seed(33305)

with open('pdf_debug_ilk_tibbi.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'^\s*(\d+)\.\s*(.*?)\n\s*Düzgün cavab:\s*(.*?)(?=\n\s*\d+\.|\Z)', re.DOTALL | re.MULTILINE)
matches = pattern.findall(text)

distractors_pool = [
    'Zərərçəkənə isti su içirtmək və ayağa qaldırmaq',
    'Yaraya isti kompres qoymaq və masaj etmək',
    'Zədələnmiş nahiyəni spirtlə silmək və açıq saxlamaq',
    'Dərhal antibiotik və güclü ağrıkəsici həblər vermək',
    'Zərərçəkəni ayağa qaldırmaq və gəzdirmək',
    'Yanıq nahiyəsinə yağ, maz və ya spirt çəkmək',
    'Sınmış sümüyü yerinə salmağa çalışmaq',
    'Zəhərlənmə zamanı süni qusdurma yaratmaq və qan almaq',
    'Qanayan nahiyəni ürək səviyyəsindən aşağı salmaq',
    'Turniketi 3 saatdan çox fasiləsiz saxlamaq',
    'Yaranın içərisini yodla yumaq və pambıq qoymaq',
    'Boğulan şəxsə isti vanna qəbul etdirmək',
    'Döş qəfəsinə isti su şüşəsi qoymaq',
    'Huşsuz xəstənin ağzına su tökmək'
]

def generate_distractors(q_text, ans_text):
    ans = ans_text.lower()
    q = q_text.lower()
    
    if '12-16' in ans: return ['20-25 dәfә', '5-8 dәfә', '30-40 dәfә']
    if '3-4' in ans: return ['1-2 sm', '7-8 sm', '10-12 sm']
    if '90' in ans: return ['45 dərəcə', '15 dərəcə', '180 dərəcə']
    if '39-40' in ans: return ['36-37 °C', '35-36 °C', '41-42 °C']
    if '16-18' in ans: return ['10-12', '25-30', '35-40']
    if '120/80' in ans: return ['90/60', '160/100', '200/120']
    if '5 litr' in ans: return ['2-3 litr', '7-8 litr', '10 litr']
    if '4-5' in ans: return ['10-15 dәq', '20-30 dәq', '1-2 saat']
    if '1-2' in ans:
        if 'dәq' in ans: return ['5-10 dәq', '15-20 dәq', '30 dәqiqədən sonra']
        if 'l' in ans: return ['3-4 L', '5-6 L', '0.5 L']
    if '75-80' in ans: return ['50-60', '100-120', '130-150']
    if '2' in ans and len(ans) < 3: return ['3', '4', '5']
    if '1, 5-2' in ans.replace(' ', ''): return ['0.5 L', '3-4 L', '5 L']
    
    if 'bazu' in ans and 'arteriya' in ans: return ['Bud arteriyasını', 'Yuxu arteriyasını', 'Bilək venasını']
    if 'bud' in ans and 'arteriya' in ans: return ['Bazu arteriyasını', 'Yuxu arteriyasını', 'Dirsək venasını']
    if 'yuxu arteriyası' in ans: return ['Bazu arteriyasını sıxmaqla', 'Bud arteriyasını sıxmaqla', 'Aortanı sıxmaqla']
    if 'kapilyar' in ans: return ['Venoz qanaxma', 'Arterial qanaxma', 'Daxili qanaxma']
    if 'venoz' in ans: return ['Arterial', 'Kapilyar', 'Daxili']
    if 'arterial' in ans: return ['Venoz', 'Kapilyar', 'Daxili']
    if 'orta dirsәk venası' in ans: return ['Ayaq venası', 'Boyun venası', 'Bazu arteriyası']
    if 'dәri altına' in ans or 'dәrialtı' in q: return ['Venadaxili', 'Əzələdaxili', 'Sümükdaxili']
    if 'venadaxili' in ans: return ['Dərialtı', 'Əzələdaxili', 'Sümükdaxili']
    if 'saidin içәri sәthindә' in ans: return ['Budun ön səthində', 'Qarnın alt hissəsində', 'Kürək nahiyəsində']
    
    if 'a-vi/4' in ans: return ['A-II/1', 'A-III/2', 'A-V/3']
    if 'okluzion' in ans: return ['Sıxıcı sarğı', 'Spika sarğısı', 'Dezmo sarğısı']
    if 'nitroqliserin' in ans: return ['Ağrıkəsici iynə vurmaq', 'Aspirin udmaq', 'Süni nəfəs vermək']
    if 'döş sümüyünün' in ans: return ['Qarın boşluğunun mərkəzinə', 'Döş qəfəsinin yuxarı 1/3 hissəsinə', 'Kürək sümüyünün üzərinə']
    if 'torpağa basdırmaq' in ans: return ['Cərəyan mənbəyindən ayırmaq', 'Ürək masajı etmək', 'Süni nəfəs vermək']
    if 'cәrәyanın tәsirini kәsmәk' in ans: return ['Dərhal ürək masajına başlamaq', 'Zərərçəkənin üzərinə su tökmək', 'Həkim gələnə qədər gözləmək']
    if 'zәdәli qola' in ans: return ['Köynək əvvəl sağlam qola geyindirilir', 'Hər iki qola eyni vaxtda geyindirilir', 'Paltar ümumiyyətlə geyindirilməməlidir']
    if 'aclıq' in ans: return ['Bol maye və isti yemək verilməsi', 'Mədəni yumaq və qusdurmaq', 'Qarına isti qrelka qoymaq']
    if 'buz qoymaq' in ans or 'soyuq kompres' in ans: return ['İsti kompres qoymaq və masaj etmək', 'Spirtlə silmək və yod çəkmək', 'Sıxıcı turniket qoymaq']
    
    if 'yarımoturaq' in ans: return ['Tam arxası üstə uzadılmış vəziyyətdə', 'Qarnı üstə uzadılmış vəziyyətdə', 'Böyrü üstə uzadılmış vəziyyətdə']
    if 'arxası üstә' in ans: return ['Qarnı üstə', 'Böyrü üstə', 'Yarımoturaq']
    if 'böyrü üstә' in ans: return ['Qarnı üstə', 'Arxası üstə', 'Yarımoturaq']
    if 'qarnı üstә' in ans: return ['Böyrü üstə', 'Arxası üstə', 'Yarımoturaq']

    if 'al qırmızı' in ans: return ['Tünd albalı rəngdə olması', 'Qanın qara rəngdə olması', 'Açıq çəhrayı rəngdə olması']
    if 'tünd' in ans and 'qırmızı' in ans: return ['Al qırmızı rəngdə olması', 'Qanın qara rəngdə olması', 'Açıq çəhrayı rəngdə olması']
    
    if 'yaradan yuxarı' in ans: return ['Yaradan aşağı hissədə jqut bağlamaqla', 'Yaranın tam üzərinə jqut bağlamaqla', 'Jqutsuz sadəcə pambıq qoymaqla']
    
    opts = random.sample(distractors_pool, 3)
    return opts

final_questions = []
for i, m in enumerate(matches):
    qid = f'q{i+1:03d}'
    q_text = m[1].replace('\n', ' ').strip()
    q_text = re.sub(' +', ' ', q_text)
    ans_text = m[2].replace('\n', ' ').strip()
    ans_text = re.sub(' +', ' ', ans_text)
    
    distractors = generate_distractors(q_text, ans_text)
    
    options = [ans_text] + distractors
    random.shuffle(options)
    
    letters = ['A', 'B', 'C', 'D']
    opts_dict = {}
    correct_letter = ''
    for j, opt in enumerate(options):
        opts_dict[letters[j]] = opt
        if opt == ans_text:
            correct_letter = letters[j]
            
    final_questions.append({
        'id': qid,
        'question': q_text,
        'options': opts_dict,
        'correct_answer': correct_letter,
        'explanation': ''
    })

out_data = {
    'certificate': 'Gəmidə ilk tibbi yardım',
    'questions': final_questions
}

target_path = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\g_mid_ilk_tibbi_yard_m.json'
os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=4)

print(f'Successfully rebuilt json target! Wrote {len(final_questions)} questions.')
