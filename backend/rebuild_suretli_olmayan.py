import json
import random
import os

def rebuild():
    random.seed(33302)
    
    with open("parsed_qs.json", "r", encoding="utf-8") as f:
        parsed_qs = json.load(f)
        
    out_json = {
        "certificate": "Sürәtli olmayan xilasedici qayıqlar vә sallar üzrә mütәxәssis",
        "questions": []
    }
    
    for i, q in enumerate(parsed_qs):
        correct = q['a']
        d1 = q['d1']
        d2 = q['d2']
        d3 = q['d3']
        
        opts = [correct, d1, d2, d3]
        random.shuffle(opts)
        
        options_dict = {}
        correct_letter = "A"
        letters = ["A", "B", "C", "D"]
        for j, opt in enumerate(opts):
            options_dict[letters[j]] = opt
            if opt == correct:
                correct_letter = letters[j]
                
        out_json["questions"].append({
            "id": f"q{i+1:03d}",
            "question": q['q'],
            "options": options_dict,
            "correct_answer": correct_letter,
            "explanation": ""
        })
        
    out_path = r"static\questions\xususi\s_r_tli_olmayan_xilasedici_qay_qlar_v_sa.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out_json, f, ensure_ascii=False, indent=2)
        
    print("Rebuild complete. Wrote", len(out_json["questions"]), "questions.")

if __name__ == "__main__":
    rebuild()
