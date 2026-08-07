import json
import random
import os

SEED = 33310
random.seed(SEED)

def get_distractors(q_id):
    # Generating ISPS/maritime security specific distractors for each question based on ID
    distractors = {
        "1": ["10 qayda", "15 qayda", "20 qayda"],
        "2": ["2", "4", "5"],
        "3": ["Dərhal gəmi kapitanına xəbər vermədən şəxsi göyərtəyə buraxmaq", "Sənədləri yoxlamadan yalnız şifahi suallar vermək", "Gələn şəxsi birbaşa gəmi maşın şöbəsinə yönləndirmək"],
        "4": ["yüksək ola bilməz", "həmişə eyni olmalıdır", "liman rəisi tərəfindən qadağan edilir"],
        "5": ["gəminin təcili tərk edilməsi vəziyyətidir", "pirat hücumu ehtimalının çox yüksək olduğu səviyyədir", "beynəlxalq sularda mühafizənin dayandırılmasıdır"],
        "6": ["Birləşmiş Millətlər Təşkilatı", "Gəminin gəldiyi sonuncu liman rəhbərliyi", "Beynəlxalq Dəniz Təşkilatı (IMO)"],
        "7": ["gəmi sahibi tərəfindən", "liman nəzarəti (PSC) tərəfindən", "yerli polis orqanları tərəfindən"],
        "8": ["gəmi kapitanı tərəfindən", "liman rəisi tərəfindən", "dəniz Administrasiyası tərəfindən"],
        "9": ["Gəmini dərhal tərk etmək və xilasedici qayıqlara minmək", "Gəminin sürətini azaltmaq və piratlarla danışıqlara başlamaq", "Silahlı müqavimət göstərmək və atəş açmaq"],
        "10": ["yalnız şifahi kimliyini bildirməlidir", "heç bir yoxlama olmadan kapitanın icazəsini gözləməlidir", "çantasını göyərtədə qoyub gəmiyə daxil olmalıdır"],
        "11": ["Baltik dənizi, Şimal dənizi", "Aralıq dənizi, Qara dəniz", "Xəzər dənizi, Karib dənizi"],
        "12": ["6 ayda azı 1 dəfə", "hər ay azı 1 dəfə", "ildə azı 1 dəfə"],
        "13": ["Gəmi jurnalının içində", "Kayutada hər hansı bir şkafda", "Maşın şöbəsində"],
        "14": ["6 ayda ən azı bir dəfə", "3 ayda ən azı bir dəfə", "24 ayda ən azı bir dəfə"],
        "15": ["Gəminin yarısı yoxlanıldıqdan sonra", "Liman rəisi icazə verdikdən sonra", "Gəmi yola düşdükdən sonra"],
        "16": ["1 il", "3 il", "10 il"],
        "17": ["Narkotik maddəni dənizə atmaq", "Narkotik maddəni götürüb kapitana aparmaq", "Gəmi heyətindən gizlətmək və limanda polisə vermək"],
        "18": ["Baxış qrupunda 1 nəfər olmalıdır", "Baxış qrupunda bütün heyət iştirak etməlidir", "Baxış qrupunda 5 nəfərdən çox heyət üzvü olmalıdır"],
        "19": ["Dərhal telefonu söndürmək", "Təhdid edən şəxsi hədələmək", "Söhbəti kəsmək və polisi gözləmək"],
        "20": ["Gəmi rol cədvəlində", "Dənizçinin qeyd kitabçasında", "Yük planında"],
        "21": ["Müntəzəm olaraq gəmiyə gələn təchizatçılar", "Gəmi agentləri və liman işçiləri", "Sənədlərini vaxtında təqdim edən şəxslər"],
        "22": ["Gəminin heyət siyahısı", "Gəminin yanacaq ehtiyatı", "Gəminin hərəkət cədvəli"],
        "23": ["Yalnız tapançalar", "Su topları və səs qumbaraları", "Lazer silahları və qaz balonları"],
        "24": ["Gəmi maşın jurnalında", "Gəmi sanitariya jurnalında", "Yük əməliyyatları jurnalında"],
        "25": ["Adi səviyyə", "Müstəsna səviyyə", "Kritik səviyyə"],
        "26": ["Gəminin mövqeyini peyklə izləmə", "Gəmidə yanğın haqqında xəbərdarlıq", "Gəminin sualtı qayıqlarla əlaqəsi"],
        "27": ["Adi səviyyə", "Yüksəldilmiş səviyyə", "Aşağı səviyyə"],
        "28": ["Gəmi agenti", "Liman rəisi", "Böyük mexanik"],
        "29": ["Adi səviyyəyə", "Yüksəldilmiş səviyyəyə", "Bütün səviyyələrə"],
        "30": ["Kənar şəxsi gəmidən kənara çıxarmağa cəhd etmək", "Kənar şəxsdən gəmiyə niyə gəldiyini soruşmaq və buraxmaq", "Heç bir tədbir görməmək"],
        "31": ["Gəminin sürəti və koordinatları", "Heyət üzvlərinin maaşları", "Gəminin sonuncu dəfə boyanma tarixi"],
        "32": ["Gəmiyə məxsus qida ehtiyatları", "Gəmi kapitanının şəxsi əşyaları", "Heyət üzvlərinin daşıdığı əl çantaları"],
        "33": ["gündəlik, həftəlik, aylıq", "mövsümi, illik, onillik", "planlı, plansız, qəfil"],
        "34": ["1", "3", "4"],
        "35": ["1-ci düymə maşın şöbəsində, 2-ci düymə kambuzda", "Bütün düymələr gəmi kapitanının kayutasında", "1-ci düymə bosmanın kayutasında, 2-ci düymə nasosxanada"],
        "36": ["Gəmi agenti", "Liman nəzarətçisi", "Gəmi sahibi"],
        "37": ["Yalnız gəminin işçi dilində", "Yalnız ingilis dilində", "İngilis, rus və ya ərəb dillərində"],
        "38": ["Limanın kommersiya planı", "Limanın ekologiya planı", "Limanın sanitar mühafizə planı"],
        "39": ["Bəli", "Yalnız kapitanın icazəsi ilə", "Yalnız liman rəisinin icazəsi ilə"],
        "40": ["Aralıq dənizi və Qara dəniz", "Karib dənizi və Meksika körfəzi", "Şimal dənizi və Baltik dənizi"],
        "41": ["Partlayıcı maddələr", "Narkotik vasitələr", "Bioloji silahlar"],
        "42": ["Xeyr", "Yalnız limanda olarkən", "Yalnız dəniz administrasiyasının xüsusi icazəsi ilə"],
        "43": ["Gələn şəxsin yükünü daşımaq", "Gələn şəxsi birbaşa gəmi kapitanının yanına aparmaq", "Gələn şəxsin tibbi vəziyyətini yoxlamaq"],
        "44": ["Beynəlxalq Dəniz Təşkilatı (IMO)", "Liman nəzarəti (PSC)", "Yerli dəniz polisi"],
        "45": ["Gəminin mühafizəyə məsul şəxsi", "Böyük köməkçi", "Növbətçi matros"]
    }
    
    # We strip the "1. ", "2. " prefix to match the dict or just use index
    idx = q_id
    if str(idx) in distractors:
        return distractors[str(idx)]
    else:
        return ["Yanlış cavab 1 (ISPS)", "Yanlış cavab 2 (ISPS)", "Yanlış cavab 3 (ISPS)"]


def main():
    with open("isps_qa.json", "r", encoding="utf-8") as f:
        qa_pairs = json.load(f)
    
    questions = []
    
    for i, item in enumerate(qa_pairs):
        idx = i + 1
        q_text = item["q"].split(".", 1)[1].strip() if "." in item["q"][:4] else item["q"].strip()
        ans = item["a"].strip()
        
        distractors = get_distractors(idx)
        
        options_list = [ans] + distractors
        random.shuffle(options_list)
        
        options_dict = {}
        correct_letter = ""
        for j, letter in enumerate(["A", "B", "C", "D"]):
            options_dict[letter] = options_list[j]
            if options_list[j] == ans:
                correct_letter = letter
                
        questions.append({
            "id": f"q{idx:03d}",
            "question": q_text,
            "options": options_dict,
            "correct_answer": correct_letter,
            "explanation": ""
        })
        
    out_data = {
        "certificate": "ISPS-1",
        "questions": questions
    }
    
    out_path = r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\isps_1.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_data, f, ensure_ascii=False, indent=4)
        
    print(f"Generated {len(questions)} questions for ISPS-1 and saved to {out_path}.")

if __name__ == "__main__":
    main()
