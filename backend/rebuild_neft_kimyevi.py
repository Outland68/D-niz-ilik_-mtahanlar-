import json
import random
import re

random.seed(33317)

def main():
    text = '\n' + open('pdf_debug_neft_kimyevi.txt', 'r', encoding='utf-8').read()

    questions_data = []

    distractors_map = {
        1: ['4', '8', '12'],
        2: ['7.6 metr', '15.0 metr', '2.0 metr'],
        3: ['5', '15', '20'],
        4: ['Su keçirməyən', 'Yanğına davamlı', 'Toz keçirməyən'],
        5: ['Gəminin sürətinə', 'Sahildən olan məsafəyə', 'Boşaldılan suyun həcminə'],
        6: ['2', '4', '5'],
        7: ['Qadağandır', 'Tövsiyə olunur', 'Yalnız fırtınalı havada tələb olunur'],
        8: ['Yuyucu şlanqı yuma magistralına birləşdirmək, maşınkanı şlanqa bağlamaq, tanka salmaq', 'Tanka salmaq, maşınkanı bağlamaq, təzyiq vermək', 'Maşınkanı yoxlamaq, tanka salmaq, şlanqı magistrala bağlamaq'],
        9: ['İnert qazının xaric olunması üçün', 'Yük tanklarında təzyiqi tənzimləmək üçün', 'Tankların havalandırılmasını sürətləndirmək üçün'],
        10: ['Su buraxmayan', 'Qaz keçirməyən', 'Partlayışa davamlı'],
        11: ['0.95 %', '0.85 %', '0.90 %'],
        12: ['0.15 metr', '0.35 metr', '0.50 metr'],
        13: ['5%', '11%', '21%'],
        14: ['Tankın klapanı, manifoldun klapanı, boru kəmərinin kəsən klapanı', 'Boru kəmərinin kəsən klapanı, tankın klapanı, manifoldun klapanı', 'Tankın klapanı, boru kəmərinin kəsən klapanı, manifoldun klapanı'],
        15: ['Yükün sıxlığını ölçmək üçün', 'Tanklarda inert qazın səviyyəsini yoxlamaq üçün', 'Tankların dibindəki çöküntünü təmizləmək üçün'],
        16: ['Nasos bölməsində', 'Yük idarəetmə otağında', 'Açıq göyərtədə manifoldun yanında'],
        17: ['3 m/s', '5 m/s', '7 m/s'],
        18: ['Böyüktonajlı tankerlərin', 'Kimyəvi tankerlərin', 'Qazdaşıyan gəmilərin'],
        19: ['Kiçiktonajlı tankerlərin', 'Böyüktonajlı tankerlərin', 'Supertankerlərin'],
        20: ['2-ci sinif böyük tankerlərin', 'Orta tonajlı tankerlərin', 'Kiçiktonajlı kimyəvi tankerlərin'],
        21: ['1,2,3', '1,3,5', '2,4,5'],
        22: ['2', '4', '5'],
        23: ['6 aydan az olmayaraq', '3 aydan az olmayaraq', '24 aydan az olmayaraq'],
        24: ['200C', '250C', '100C'],
        25: ['2500 m3', '3000 m3', '500 m3'],
        26: ['Mərkəzi sinir sisteminin zədələnməsinə', 'Dəri xərçənginə', 'Sümük toxumasının zəifləməsinə'],
        27: ['Yük tankındakı oksigenin miqdarını', 'İnert qazının təzyiqini', 'H2S qazının konsentrasiyasını'],
        28: ['2', '4', '5'],
        29: ['2', '4', '5'],
        30: ['Tankları yumaq üçün', 'İnert qazı təmizləmək üçün', 'Manifoldda sızıntıları yoxlamaq üçün'],
        31: ['Odadavamlı', 'Qaz keçirməyən', 'Su buraxmayan'],
        32: ['Tankın atmosferində oksigenin həcmi 11 % təşkil edirsə', 'Tankın atmosferində oksigenin həcmi 21 % təşkil edirsə', 'Tankın atmosferində karbohidrogen 1 %-dən aşağıdırsa'],
        33: ['20000 m3', '40000 m3', '50000 m3'],
        34: ['3', '4', '5'],
        35: ['2', '4', '5'],
        36: ['Boru kəmərləri', 'Klapanlar', 'Manifoldlar'],
        37: ['1.5 metr', '2.0 metr', '0.50 metr'],
        38: ['1250 m3', '5000 m3', '1000 m3'],
        39: ['Zərərçəkəni dərhal isti suya salmaq', 'Süni nəfəs vermək və ürək masajı etmək', 'Zərərçəkənə çoxlu maye içirtmək'],
        40: ['1-ci sinif böyük tankerlərin', 'Ortatonajlı tankerlərin', 'Supertankerlərin'],
        41: ['1-ci sinif böyük tankerlərin', '2-ci sinif böyük tankerlərin', 'Kiçiktonajlı tankerlərin'],
        42: ['Böyüktonajlı tankerlərin', 'Ortatonajlı tankerlərin', 'Kiçiktonajlı tankerlərin'],
        43: ['1 m/s', '3 m/s', '12 m/s'],
        44: ['24 saat', '6 saat', '48 saat'],
        45: ['Yükün adı və sıxlığı', 'Tankın həcmi və maksimal təzyiqi', 'Son yoxlama tarixi'],
        46: ['İnertləşdirmə prinsipi ilə', 'Təzyiqi azaltma prinsipi ilə', 'Kimyəvi reaksiya prinsipi ilə'],
        47: ['Yükləmə sürətini artırmaq üçün', 'Tanklarda havalandırmanı təmin etmək üçün', 'İnert qazını paylamaq üçün'],
        48: ['1,2,3', '2,3,4', '1,3,4,5'],
        49: ['A, B, C', 'X, Y, Z', 'M, N, O'],
        50: ['Yalnız dərinin qızarması və qaşınma', 'Hərarətin kəskin artması və əzələ ağrıları', 'Görmə qabiliyyətinin qısa müddətli itməsi'],
        51: ['Karbohidrogenin miqdarı çox olduqda', 'H2S qazının miqdarı çox olduqda', 'Statik elektrik yarandıqda'],
        52: ['Nasosların həddən artıq qızmasının qarşısını almaq üçün', 'Yük tanklarında təzyiqin kəskin artmasının qarşısını almaq üçün', 'Boru kəmərlərində hidravlik zərbələrin qarşısını almaq üçün'],
        53: ['30000 m3', '20000 m3', '40000 m3'],
        54: ['8 % olmalıdır', '11 % olmalıdır', '21 % olmalıdır'],
        55: ['0.1 L-dən çox olmamalıdır', '0.3 L-dən çox olmamalıdır', '0.5 L-dən çox olmamalıdır'],
        56: ['MARPOL-73/78 Əlavə 2', 'SOLAS-74 Fəsil II-2', 'STCW Kodeksi'],
        57: ['Yalnız neft məhsulları daşıyan gəmi', 'Mayeləşdirilmiş qaz daşıyan gəmi', 'Quru yükləri və kimyəvi maddələri eyni vaxtda daşıyan gəmi'],
        58: ['2', '3', '5'],
        59: ['A,B,C,D', 'X,Y,Z', 'I,II,III'],
        60: ['2', '4', '5']
    }

    for i in range(1, 61):
        start_str = f'\n{i}.'
        start_idx = text.find(start_str)
        if start_idx == -1:
            print(f'Missing start {i}')
            continue
        
        ans_idx = text.find('Düzgün cavab:', start_idx)
        
        if i < 60:
            next_idx = text.find(f'\n{i+1}.', ans_idx)
            if next_idx == -1:
                chunk = text[start_idx:]
            else:
                chunk = text[start_idx:next_idx]
        else:
            chunk = text[start_idx:]
            
        ans_idx_local = chunk.find('Düzgün cavab:')
        question_text = chunk[len(start_str):ans_idx_local].strip()
        ans_text = chunk[ans_idx_local+len('Düzgün cavab:'):].strip()
        
        question_text = re.sub(r'\s+', ' ', question_text)
        ans_text = re.sub(r'\s+', ' ', ans_text)

        dists = distractors_map.get(i, ['Distractor 1', 'Distractor 2', 'Distractor 3'])
        opts = [ans_text] + dists
        random.shuffle(opts)
        
        correct_letter = chr(65 + opts.index(ans_text))
        
        q_obj = {
            'id': f'q{i:03d}',
            'question': question_text,
            'options': {
                'A': opts[0],
                'B': opts[1],
                'C': opts[2],
                'D': opts[3]
            },
            'correct_answer': correct_letter,
            'explanation': ''
        }
        questions_data.append(q_obj)

    if len(questions_data) != 60:
        print('Error parsing! Got:', len(questions_data))
    else:
        data = {
            "certificate": "Neft və Kimyəvi-İlkin",
            "questions": questions_data
        }

        with open(r'static/questions/xususi/neft_v_kimy_vi_i_lkin.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print('Successfully wrote JSON with 60 questions.')

if __name__ == '__main__':
    main()
