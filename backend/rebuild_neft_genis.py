import json
import re
import random
import os

SEED = 33316
random.seed(SEED)

PDF_TEXT_FILE = r'D:\Dənizçilik_İmtahanları\backend\pdf_debug_neft_genis.txt'
OUTPUT_JSON = r'D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\neft_tankerl_rind_geni.json'

def get_distractors():
    return {
        1: ["30 ppm", "50 ppm", "100 ppm"],
        2: ["qəti qadağandır", "yalnız liman rəhbərliyinin icazəsi ilə", "yalnız gündüz vaxtı icazə verilir"],
        3: ["2,3,4,5", "1,2,5", "1,3,4,5"],
        4: ["alışma temperaturuna görə 100 0C-dən yuxarı olan neft mәhsulları", "alışma temperaturuna görә 80 0C-dәn aşağı olan neft mәhsulları", "özlülüyü yüksək olan qalıq neft məhsulları"],
        5: ["manifoldun klapanı, boru kәmәrinin kәsәn klapanı, tankın klapanı", "boru kәmәrinin kәsәn klapanı, tankın klapanı, manifoldun klapanı", "tankın klapanı, manifoldun klapanı, boru kәmәrinin kәsәn klapanı"],
        6: ["10-15 dәqiqә", "60-90 dәqiqә", "5-10 dәqiqә"],
        7: ["5%-li", "10%-li", "0.5%-li"],
        8: ["şlanqın diametrinin 2 mislindәn az olmamalıdır", "şlanqın diametrinin 10 mislindәn az olmamalıdır", "şlanqın diametrinin 4 mislindәn az olmamalıdır"],
        9: ["Daşınan elektrik avadanlığı fasiləsiz işləməlidir", "Daşınan elektrik avadanlığı yalnız xüsusi izolyasiya ilə istifadə olunmalıdır", "Elektrik avadanlığının gərginliyi artırılmalıdır"],
        10: ["Alfa", "Çarli", "Qolf"],
        11: ["Yalnız xam neftlә yumanı saxlamaq", "Nasosların sürətini azaltmaq", "Əlavə ventilyatorları qoşub davam etmək"],
        12: ["2.5 dәfә", "3.0 dәfә", "1.0 dәfә"],
        13: ["Liman nəzarətçisinin icazəsi ilə mümkündür", "Xüsusi ehtiyat tәdbirlәri görərək icazә verilir", "Yalnız şlüz sistemlәrindәn istifadә edәrәk icazә verilir"],
        14: ["40-60", "120-140", "60-70"],
        15: ["Gәminin baş mühәrrikinin vә kömәkçi mexanizmlәrinin", "Bütün ballast nasoslarının vә boru kәmәrlәrinin", "İqlimlәndirmә vә ventilyasiya sistemlәrinin"],
        16: ["Tanklarda yükün temperaturunu tənzimləmək üçün", "Tankların daxilindəki maye səviyyəsini ölçmək üçün", "Köpük söndürmə sisteminin tәzyiqini saxlamaq üçün"],
        17: ["7.6 metr", "15.0 metr", "5.0 metr"],
        18: ["1 sistem", "2 sistem", "4 sistem"],
        19: ["açıq", "yarımaçıq", "avtomatik tәnzimlәnәn rejimdә"],
        20: ["Bütün növ plastik tullantıları", "Kimyәvi maddә qarışıqlı yuyucu suları", "İşlәnmiş sürtkü yağlarını"],
        21: ["Plastik qablaşdırmaları", "Sintetik kәndirlәri", "Bütün növ neft qalıqlarını"],
        22: ["1", "3", "4"],
        23: ["Gәminin hәrәkәt sürәtinә", "Sahildәn olan mәsafәyә", "Tullantının dәnizә axıdılma intensivliyinә"],
        24: ["Xüsusi ehtiyat tәdbirlәri ilә icazә verilir", "Yalnız gündüz vaxtı icazә verilir", "Liman kapitanının icazәsi ilә mümkündür"],
        25: ["Su çilәyici sistemdәn", "Köpüklә söndürmә sistemindәn", "Karbon qazı (CO2) sistemindәn"],
        26: ["1,4", "2,4,5", "3,4,5"],
        27: ["alışma temperaturuna görә 600 C-dәn aşağı olan neft mәhsulları", "buxarlanma qabiliyyәti yüksәk olan yüngül neft mәhsulları", "xüsusi çәkisi 0.8-dәn az olan mәhsullar"],
        28: ["2", "6", "8"],
        29: ["Yalnız qısa müddәtә icazә verilir", "Zәrәrçәkәn huşsuz olduqda mütlәqdir", "Gәmi kapitanının icazәsi ilә mümkündür"],
        30: ["açıq", "yarımaçıq", "ventilyasiya rejimindә"],
        31: ["2 dәfә", "3 dәfә", "10 dәfә"],
        32: ["850 C", "1000 C", "450 C"],
        33: ["2", "4", "5"],
        34: ["Zәrәrçәkәnin paltarını kәsib çıxarmaq vә buz qoymaq", "Yanıq nahiyәsinә yağ sürtmәk vә sarımaq", "Yaraya spirt vurub açiq saxlamaq"],
        35: ["1,2,3", "2,3", "4,5"],
        36: ["1-2 dәqiqә", "10-15 dәqiqә", "20-25 dәqiqә"],
        37: ["50-60", "90-100", "100-110"],
        38: ["5 m/s", "7 m/s", "10 m/s"],
        39: ["Nasosların sürәtini artırmaq, xәbәrdarlıq siqnalı vermәk", "Yalnız gәmi kapitanına mәruzә etmәk vә gözlәmәk", "Problemi tәkbaşına hәll etmәyә çalışmaq"],
        40: ["Yük tanklarında tәzyiqi", "İnert qazın vәziyyәtini", "Yükün temperaturunu vә sәviyyәsini"],
        41: ["4 kq/sm2", "12 kq/sm2", "15 kq/sm2"],
        42: ["1", "5", "7"],
        43: ["1", "2", "5"],
        44: ["Basma klapanı açıq, sovurucu klapanı bağlı", "Hәr iki klapan bağlı", "Hәr iki klapan açıq"],
        45: ["Boru kәmәrlәri", "Keser klapanlar", "Manifoldlar"],
        46: ["2", "3", "5"],
        47: ["Açıq dövrlü", "Birləşdirilmiş dövrlü", "Yarı-açıq dövrlü"],
        48: ["Zәrәrçәkәnә dәrhal su vermәk", "Zәrәrçәkәnә süni nәfәs vermәyә başlamaq (cərəyanı kəsmədən)", "Zәrәrçәkәni ayağa qaldırmağa çalışmaq"],
        49: ["Yuyucu maşınlar", "Yuyucu nasoslar", "Boru kәmәrlәri vә klapanlar"],
        50: ["1", "2", "4"],
        51: ["1", "2", "4"],
        52: ["Yük növünü dәyişәn zaman", "Qalın çöküntülәr tәmizlәnәn zaman", "Tәmirlә әlaqәdar tanklara daxil olmadan әvvәl"],
        53: ["İnert qazın istehsalı vә tәmizlәnmәsi prosesindә", "Xam neftlә yuma sisteminin avtomatik nәzarәtindә", "Buxar qayıtma sisteminin tәnzimlәnmәsindә"]
    }

def build():
    with open(PDF_TEXT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    # Regex to capture all questions
    matches = re.findall(r"(\d+)\.\s*(.*?)(?=\nDüzgün cavab:)(?:\nDüzgün cavab:\s*)(.*?)(?=\n\s*\n|\Z|\n\d+\.)", text, re.DOTALL)
    
    distractors = get_distractors()
    
    questions = []
    
    for m in matches:
        q_id = int(m[0])
        q_text = m[1].strip()
        correct = m[2].strip()
        
        q_distractors = distractors.get(q_id, ["D1", "D2", "D3"])
        
        options = [correct] + q_distractors
        random.shuffle(options)
        
        correct_letter = ""
        opt_dict = {}
        letters = ["A", "B", "C", "D"]
        for i, opt in enumerate(options):
            opt_dict[letters[i]] = opt
            if opt == correct:
                correct_letter = letters[i]
                
        questions.append({
            "id": f"q{q_id:03d}",
            "question": q_text,
            "options": opt_dict,
            "correct_answer": correct_letter,
            "explanation": ""
        })

    out_data = {
        "certificate": "Neft tankerlərində geniş proqram",
        "questions": questions
    }
    
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=4)
        
    print(f"Successfully wrote {len(questions)} questions to {OUTPUT_JSON}")

if __name__ == "__main__":
    build()
