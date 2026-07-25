import os
import glob
import json
import re

questions_dir = r"D:\Dənizçilik_İmtahanları\backend\static\questions"
json_files = glob.glob(os.path.join(questions_dir, "**", "*.json"), recursive=True)

print(f"Inspecting syntax & character formatting in {len(json_files)} JSON files...")

fix_count = 0

def clean_syntax(text):
    if not isinstance(text, str):
        return text
    
    original = text
    
    # Fix broken encoding sequences / typos
    replacements = {
        'tәlәblәrinә': 'tələblərinə',
        'әsasәn': 'əsasən',
        'dәnizә': 'dənizə',
        'tәrkibindә': 'tərkibində',
        'nә qәdәr': 'nə qədər',
        'icazә': 'icazə',
        'üzәrindә': 'üzərində',
        'işlәk': 'işlək',
        'vәziyyәtdә': 'vəziyyətdə',
        'tәsdiqlәyәn': 'təsdiqləyən',
        'çәkisi': 'çəkisi',
        'mәhsulları': 'məhsulları',
        'görә': 'görə',
        'Gәmidәn-gәmiyә': 'Gəmidən-gəmiyə',
        'ötürmә': 'ötürmə',
        'әyilmә': 'əyilmə',
        'Gәmi-Sahil': 'Gəmi-Sahil',
        'vәrәqi': 'vərəqi',
        'rayonunda': 'rayonunda',
        'barәsindә': 'barəsində',
        'nәyi': 'nəyi',
        'nәzәrdә': 'nəzərdə',
        'Daşınan': 'Daşınan',
        'kabellәri': 'kabelleri',
        'şәbәkәdәn': 'şəbəkədən',
        'әmәliyyatı': 'əməliyyatı',
        'çıxarsa': 'çıxarsa',
        'nә etmәk': 'nə etmək',
        'Boşaltmanı': 'Boşaltmanı',
        'xam neftlә': 'xam neftlə',
        'yumanı': 'yumanı',
        'sınağı': 'sınağı',
        'tәzyiqi': 'təzyiqi',
        'işçi tәzyiqdәn': 'işçi təzyiqdən',
        'neçә dәfә': 'neçə dəfə',
        'ölçülmәsinә': 'ölçülməsinə',
        'nümunәlәrin': 'nümunələrin',
        'götürülmәsinә': 'götürülməsinə',
        'görә yük': 'görə yük',
        'borta qәdәr': 'borta qədər',
        'mәsafә': 'məsafə',
        'neçә әsas': 'neçə əsas',
        'yüklәmә': 'yükləmə',
        'xәtti': 'xətti',
        'istifadә': 'istifadə',
        'Yüklәmә': 'Yükləmə',
        'әvvәl': 'əvvəl',
        'yollu': 'yollu',
        'vәziyyәtdә': 'vəziyyətdə',
        'Neçә növ': 'Neçə növ',
        'qazayırıcı': 'qazayırıcı',
        'әlavәsinin': 'əlavəsinin',
        'tәlәblәrinә': 'tələblərinə',
        'xüsusi rayonlardan': 'xüsusi rayonlardan',
        'kәnarda': 'kənarda',
        'tәrkibindә': 'tərkibində',
        'tullayarkәn': 'tullayarkən',
        'nәyә': 'nəyə',
        'riayәt': 'riayət',
        'vacib deyil': 'vacib deyil',
        'Әtraf mühitin': 'Ətraf mühitin',
        'İnertizә': 'İnertizə',
        'xәbərdarlığı': 'xəbərdarlığı',
        'әmәliyyatların': 'əsasən',
        'keçirilmәsi': 'keçirilməsi',
        'qarşısını': 'qarşısını',
        'sistemdәn': 'sistemdən',
        'istifadә': 'istifadə',
        'görә': 'görə',
        'uçmayan': 'uçmayan',
        'aiddir': 'aiddir',
        'әn azı': 'ən azı',
        'yanğın': 'yanğın',
        'әleyhinә': 'əleyhinə',
        'nәzәrdә tutulub': 'nəzərdə tutulub',
        'әmәliyyatları': 'əməliyyatları',
        'vәziyyәtdә': 'vəziyyətdə',
        'cırılma sınağı': 'cırılma sınağı',
        'tәzyiqi': 'təzyiqi',
        'neçә dәfә': 'neçə dəfə',
        'girişindә': 'girişində',
        'neçә dәrәcәdәn': 'neçə dərəcədən',
        'görә': 'görə',
        'zәrәrli': 'zərəli',
        'tәhlükәli': 'təhlükəli',
        'm/s': 'm/s',
        'mәrhәlәsindә': 'mərhələsində',
        'axar sürәti': 'axar sürəti',
        'әmәliyyatları': 'əməliyyatları',
        'tәdbirlәr': 'tədbirlər',
        'görülmәlidir': 'görülməlidir',
        'terminal nümayәndәlәrinә': 'terminal nümayəndələrinə',
        'xәbәr': 'xəbər',
        'kәmәrlәrindә': 'kəmərlərində',
        'tәzyiq': 'təzyiq',
        'sәviyyәsinin': 'səviyyəsinin',
        'ölçülmәsinin': 'ölçülməsinin',
        'neçә әsas': 'neçə əsas',
        'üsulu': 'üsulu',
        'qurudulması': 'qurudulması',
        'tәmizlәnmәsi': 'təmizlənməsi',
        'neçә üsuldan': 'neçə üsuldan',
        'istifadә': 'istifadə',
        'boşaltmazdan': 'boşaltmazdan',
        'әvvәl': 'əvvəl',
        'klapanları': 'klapanları',
        'vәziyyәtdә': 'vəziyyətdə',
        'yuyulmasında': 'yuyulmasında',
        'hansı üsullardan': 'hansı üsullardan',
        'yuma': 'yuma',
        'nә daxil deyil': 'nə daxil deyil',
        'yuyulması': 'yuyulması',
        'neçә üsuldan': 'neçə üsuldan',
        'nә zaman zәruri': 'nə zaman zəruri',
        'Tәmirdәn': 'Təmirdən',
    }
    
    # Replace Cyrillic 'ә' (U+04D9) and 'Ә' (U+04D8) with Latin Azerbaijani 'ə' and 'Ə'
    text = text.replace('\u04d9', 'ə').replace('\u04d8', 'Ə')
    
    # Clean double spaces
    text = re.sub(r' +', ' ', text).strip()
    
    return text

for filepath in json_files:
    modified = False
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    q_list = data if isinstance(data, list) else data.get('questions', [])
    for q in q_list:
        # Clean question
        if 'question' in q:
            cleaned_q = clean_syntax(q['question'])
            if cleaned_q != q['question']:
                q['question'] = cleaned_q
                modified = True
        
        # Clean options
        if 'options' in q:
            opts = q['options']
            if isinstance(opts, dict):
                for k, v in opts.items():
                    cleaned_v = clean_syntax(v)
                    if cleaned_v != v:
                        opts[k] = cleaned_v
                        modified = True
            elif isinstance(opts, list):
                for idx, v in enumerate(opts):
                    cleaned_v = clean_syntax(v)
                    if cleaned_v != v:
                        opts[idx] = cleaned_v
                        modified = True

    if modified:
        fix_count += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cleaned Azerbaijani syntax characters (Cyrillic 'ә' -> Latin 'ə' & double space cleanup) across {fix_count} JSON files!")
