import json
import random
import re

seed_val = 33307
random.seed(seed_val)

def load_data():
    with open('pdf_debug_liderlik.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    # Match "1. Question text\nDüzgün cavab: Answer text"
    pattern = re.compile(r'(\d+)\.\s+(.*?)\s+Düzgün cavab:\s+(.*?)(?=\n\n|\n\d+\.|$)', re.DOTALL)
    matches = pattern.findall(content)
    
    distractors_map = {
        1: ["01 yanvar 2010-cu il", "01 iyul 2014-cü il", "01 yanvar 2017-ci il"],
        2: ["DHDNÇ-78 Beynәlxalq Mәcәllәsinin A-I/1 vә A-I/2 bölmәlәri", "DHDNÇ-78 Beynәlxalq Mәcәllәsinin B-II/1 vә B-II/2 bölmәlәri", "DHDNÇ-78 Beynәlxalq Mәcәllәsinin A-IV/1 vә A-IV/2 bölmәlәri"],
        3: ["Yalnız sıravi heyәt üçün", "Gәmi aşpazları vә ofisiantlar üçün", "Yalnız sahil tәşkilatlarının rәhbәrlәri üçün"],
        4: ["12 avqust 1995-ci il", "18 oktyabr 1991-ci il", "28 may 1990-cı il"],
        5: ["01 yanvar 2005-ci il", "15 sentyabr 1998-ci il", "10 noyabr 2010-cu il"],
        6: ["Yalnız daxili sularda üzәn gәmilәrә", "Yalnız sәrnişin gәmilәrinә", "Yalnız hәrbi vә dövlәt tәyinatlı gәmilәrә"],
        7: ["4", "5", "8"],
        8: ["Liderlik qrupun qәrarlarını tәkbaşına qәbul etmәk sәlahiyyәtidir", "Liderlik dәnizçilik qanunlarının әzbәrlәnmәsi prosesidir", "Liderlik ancaq rәsmi vәzifә sәlahiyyәtlәrindәn istifadә edәrәk göstәrişlәr vermәkdir"],
        9: ["Fiziki güc tәtbiq etmәklә işlәri icra etmәk qabiliyyәti", "Yalnız gәmi sәnәdlәrinin qaydasında olması", "Rәhbәrliyin verdiyi göstәrişlәri şübhәsiz vә mexaniki icra etmәk vәrdişi"],
        10: ["Biliklәrin sınaqdan keçirilmәdәn qәbul edilmәsi", "Nәzәri mәlumatların әzbәrlәnmәsi", "Fiziki cәhәtdәn qüvvәtli olmaq"],
        11: ["Demokratik liderlik", "Xarizmatik liderlik", "Transformal liderlik"],
        12: ["Avtokratik liderlik", "Demokratik liderlik", "Xidmәtkar liderlik"],
        13: ["Komanda üzvlәri ilә qeyri-rәsmi görüşlәr keçirmәk vә motivasiya tәdbirlәri tәşkil etmәk", "Gәminin interyer dizaynını qәrarlaşdırmaq vә ya rәng seçimi etmәk", "Yalnız bәdii әdәbiyyat oxumaqla vaxt keçirmәk vә әylәncә proqramları tәrtib etmәk"],
        14: ["Bürokratik liderlik", "Avtokratik liderlik", "Tapşırıq yönümlü liderlik"],
        15: ["Avtokratik liderlik", "Bürokratik liderlik", "Müdaxilә etmәyәn liderlik"],
        16: ["Komanda üzvlәri tәcrübәsiz olduqda vә tәlimә ehtiyac duyduqda", "Fövqәladә hallar vә qәza şәraitindә tәcili qәrarlar qәbul edәrkәn", "Qaydalara ciddi riayәt tәlәb edәn tәhlükәli yük әmәliyyatları zamanı"],
        17: ["Xarizmatik liderlik", "İnsan yönümlü liderlik", "Demokratik liderlik"],
        18: ["Bürokratik liderlik", "Avtokratik liderlik", "Transakt liderlik"],
        19: ["Transformal liderlik", "Demokratik liderlik", "Xidmәtkar liderlik"],
        20: ["Bürokratik liderlik", "Transakt liderlik", "Avtokratik liderlik"],
        21: ["Avtokratik liderlik", "Xarizmatik liderlik", "Bürokratik liderlik"],
        22: ["Gәmi sahibi şirkәtin mühasibat uçotu vә vergi ödәnişlәri üzrә", "Liman işçilәrinin әmәkhaqqının verilmәsi üzrә", "Sahil nәqliyyat vasitәlәrinin tәhlükәsiz istismarı üzrә"],
        23: ["Gәminin ehtiyat hissәlәrinin sahil anbarında tәşkili", "Şirkәtin büdcә planlaşdırmasının aparılması", "Liman idarәetmә orqanlarının daxili qәrarlarının verilmәsi"],
        24: ["Bütün gәmi heyәtinә", "Yalnız sıravi heyәtә", "Tәcrübәdә olan tәlәbәlәrә"],
        25: ["Baş mexanik", "Kapitanın baş kömәkçisi", "Gәmi hәkimi"],
        26: ["Yalnız komanda heyәti", "Yalnız xilasedici qayıq heyәti", "Növbәdә olmayan bütün sıravi heyәt"],
        27: ["Dәrhal su ilә söndürmәyә başlamaq", "Yalnız qum vә köpükdәn istifadә etmәk", "Rәhbәrliyin gәlmәsini gözlәmәk"],
        28: ["Baş mexanik", "Kapitanın baş kömәkçisi", "Növbәtçi mexanik"],
        29: ["Baş mexanik, elektrik mexaniki, aşpaz vә matros", "İkinci kömәkçi, üçüncü mexanik vә mühәrrikçi", "Kapitan, gәmi hәkimi, radist vә ofisiant"],
        30: ["Qorxu", "Risk", "Tәhlükә"],
        31: ["Qәza nәticәsi", "Ekstrovertlik", "Fövqәladә vәziyyәt"],
        32: ["Yalnız iqtisadi itkilәr vә maliyyә kәsirlәri", "Gәminin sәnәdlәrinin itirilmәsi", "Gәminin sürәtinin azalması"],
        33: ["Tәsadüfi vә qanuni", "Böyük vә kiçik", "Gözlәnilәn vә gözlәnilmәyәn"],
        34: ["Hadisәnin nәticәsinin kәmiyyәti", "Dәyәn ziyanın mәblәği", "Zaman çәrçivәsinin ölçülmәsi"],
        35: ["Hadisә yerinin vizual müayinәsi", "Gәminin texniki baxışdan keçirilmәsi", "Sığorta şirkәtinә müraciәt edilmәsi"],
        36: ["Bazar qiymәtlәrinin dәyәrlәndirilmәsi", "Riskin yalnız sәnәdlәşdirilmәsi işi", "Yükün miqdarının ölçülmәsi"],
        37: ["2", "4", "5"],
        38: ["Fövqәladә hallar nazirliyinә tәcili mәlumat vermәk", "Bütün gәmi әmәliyyatlarını dәrhal dayandırmaq", "Qoruyucu geyimlәrin lәğv edilmәsi"],
        39: ["İşlәri dәrhal dayandırmaq vә gәmini tәrk etmәk", "Heç bir tәdbir görmәdәn işә davam etmәk", "Yalnız kapitanın әmrini yazılı olaraq gözlәmәk"],
        40: ["İşi yalnız günorta vaxtı davam etdirmәk olar", "Әlavә qoruyucu dәbilqә geyinmәklә işә davam etmәk olar", "Heç nәyә baxmayaraq planlaşdırılmış işә tәcili başlamaq"],
        41: ["Gәmidә yanğın, partlayış vә deşilmә", "Əsas mühәrrikin sındırılması, pәrvanәnin itirilmәsi", "Yükün sürüşmәsi vә gәminin aşması"],
        42: ["İşlәrin yalnız kapitan tәrәfindәn icra edilmәsi", "Mәsuliyyәtin tamamilә kәnar şәxslәrә verilmәsi", "Bütün qәrarların mәrkәzlәşdirilmәsi"],
        43: ["Açıq dialoqun dәstәklәnmәsi", "Mәlumat mübadilәsinin tәmin edilmәsi", "Әks-әlaqәnin qurulması"],
        44: ["Az hәrәkәtlilik vә stresli iş rejimi", "Qidalanma rejiminin pozulması", "Yuxusuzluq vә fasilәsiz uzunmüddәtli iş"],
        45: ["Dәnizçilәrin iş saatlarının tәnzimlәnmәsi sahәsinә", "Limanların idarә edilmәsi vә logistikaya", "Gәmilәrin dizaynı vә gәmiqayırma sahәsinә"],
        46: ["2", "3", "4"],
        47: ["Qarşıdakını dinlәmәdәn yalnız öz fikrini diktә etmәkdir", "Mәlumatı yazılı şәkildә heç bir izahatsız vermәkdir", "Yalnız yüksәk sәslә danışaraq әmr vermәkdir"],
        48: ["Eqoizm", "Laqeydlik", "İnadkarlıq"],
        49: ["İnsanlar liderә mәcburiyyәtdәn, menecerә isә hәvәslә tabe olurlar", "Lider vә menecer arasında heç bir fәrq yoxdur", "Liderlәr yalnız nәzәriyyәçi, menecerlәr isә yalnız praktikdir"],
        50: ["Hәr ikisini dәrhal işdәn azad etmәk", "Onlardan birinә әsaslı sәbәb olmadan töhmәt vermәk", "Münaqişәni görmәzdәn gәlib öz-özünә hәll olunmasını gözlәmәk"],
        51: ["BWM-2004", "SOLAS-74", "STCW-78"],
        52: ["İlhamlandırır, yenilikçidir, gәlәcәyә istiqamәtlәnmişdir", "Yalnız psixoloji dәstәk göstәrir, passivdir", "Komanda üzvlәri ilә hәmişә dostluq münasibәtlәri qurur vә tәlәbkar deyil"],
        53: ["İşçini cәzalandırmaq üçün istifadә olunan hüquqi aktlar", "Әmәkhaqqının kәsilmәsi qorxusu ilә işlәtmәk", "İşdәn kәnar әylәncә proqramları tәrtib etmәk"],
        54: ["İdarәetmәni yalnız kapitanın ixtiyarına buraxmaqdır", "Şirkәtin fәaliyyәtini tamamilә dayandırmaqdır", "Rәqib şirkәtlәrin planlarını kopyalamaqdır"],
        55: ["Cәzalandırma vә qorxutma", "Maaş kәsimi vә töhmәt", "Tәcrid etmә vә nәzarәt"],
        56: ["Әdalәtli qәrar qәbul etmәk", "Nümunәvi davranış nümayiş etdirmәk", "Mәsuliyyәti öz üzәrinә götürmәk"],
        57: ["Yalnız menecer xüsusiyyәtlәrinә malik olan, rәsmi vәzifәsindәn istifadә edәndir", "Yalnız lider olub şirkәtin qaydalarına mәhәl qoymayandır", "İşçilәrin hәr istәyini yerinә yetirәn şәxsdir"],
        58: ["MARPOL-73/78", "STCW-78", "MLC-2006"],
        59: ["Mükafatlandırma", "Әdalәtlilik", "Fikirlәrin qiymәtlәndirilmәsi"],
        60: ["Sıravi heyәt", "Liman idarәsi", "Beynәlxalq Әmәk Tәşkilatı"],
        61: ["Sülh müqavilәsidir", "Tәlim vә mәşqdir", "Beynәlxalq razılaşmadır"],
        62: ["Kompromis tapmaq", "Münaqişә tәrәflәri ilә fәrdi söhbәtlәr aparmaq", "Problemin mәnbәyini araşdırmaq"],
        63: ["Ortaq mәxrәcә gәlmәk", "Tәrәflәri sakitlәşdirmәk", "Konstruktiv dialoq qurmaq"],
        64: ["Yalnız kapitan vә komanda heyәtindәn", "Yalnız sahil işçilәri vә sıravi heyәtdәn", "Sәrnişinlәr vә texniki işçilәrdәn"],
        65: ["Matrosa", "Bosmana", "Gәmi hәkiminә"],
        66: ["Gәminin sürәtinә, limanların sayına", "Hava şәraitinә, suyun temperaturuna", "Yükün miqdarına, mühәrrikin gücünә"]
    }
    
    formatted_questions = []
    
    for match in matches:
        q_num = int(match[0])
        q_text = match[1].strip().replace('\n', ' ')
        q_text = re.sub(' +', ' ', q_text)
        correct_ans = match[2].strip().replace('\n', ' ')
        correct_ans = re.sub(' +', ' ', correct_ans)
        
        distractors = distractors_map.get(q_num, [f"Yanlış cavab 1 ({q_num})", f"Yanlış cavab 2 ({q_num})", f"Yanlış cavab 3 ({q_num})"])
        
        options_list = [correct_ans] + distractors
        random.shuffle(options_list)
        
        options_dict = {}
        correct_letter = ""
        letters = ['A', 'B', 'C', 'D']
        for i, opt in enumerate(options_list):
            options_dict[letters[i]] = opt
            if opt == correct_ans:
                correct_letter = letters[i]
                
        formatted_questions.append({
            "id": f"q{q_num:03d}",
            "question": q_text,
            "options": options_dict,
            "correct_answer": correct_letter,
            "explanation": ""
        })
        
    out_data = {
        "certificate": "Liderlik və birgə iş fəaliyyəti",
        "questions": formatted_questions
    }
    
    with open('static/questions/xususi/liderlik_v_birg_i_f_aliyy_ti.json', 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=4)
        
    print(f'Successfully generated json with {len(formatted_questions)} questions.')

if __name__ == '__main__':
    load_data()
