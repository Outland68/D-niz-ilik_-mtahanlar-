import re
import json
import random

def get_distractors(answer, q_text=""):
    ans = answer.strip().lower()
    
    if ans in ["bəli", "bəli, mütləqdir", "bəli.", "bəli, mütləqdir."]:
        return ["Xeyr", "Yalnız kapitanın xüsusi icazəsi ilə", "Yalnız liman idarəsinin göstərişi ilə"]
    if ans in ["xeyr", "xeyr."]:
        return ["Bəli", "Bəli, əgər mühafizə səviyyəsi 2-dirsə", "Bəli, gəmi agentinin razılığı ilə"]
    
    if re.match(r'^[\d,\s]+$', ans):
        nums = [n.strip() for n in ans.split(',')]
        if len(nums) == 2:
            return ["1, 2", "2, 4", "3, 5"]
        elif len(nums) == 3:
            return ["1, 2, 4", "2, 3, 5", "1, 4, 5"]
        else:
            return ["1, 2, 3", "2, 4", "3, 4, 5"]

    if "ayda" in ans or "aydan" in ans or "dәfә" in ans or "dəfə" in ans:
        return ["Hər növbə təhvil verilərkən", "6 ayda 1 dəfə", "Gəmi limana hər daxil olduqda"]
    
    if "administrasiyası" in ans or "kapitan" in ans or "şәxs" in ans or "şəxs" in ans or "nümayәndә" in ans:
        return ["Liman dövləti nəzarəti (PSC) zabiti", "Gəminin baş mexaniki", "Şirkətin kommersiya departamenti rəhbəri"]
    
    if "sәviyyә" in ans or "səviyyə" in ans:
        return ["Limanın əməliyyat səviyyəsidir", "Gəminin texniki hazırlıq səviyyəsidir", "Beynəlxalq axtarış və xilasetmə səviyyəsidir"]
        
    return [
        "Gəminin yük əməliyyatlarının idarə edilməsi jurnalı",
        "Sahil mühafizəsi xidmətinin növbətçi rəisi",
        "Yalnız təhlükəli yüklər daşıyan gəmilər üçün tətbiq edilir"
    ]

def parse_and_rebuild():
    with open("pdf_debug_isps2.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    raw_qa = []
    current_q_text = ""
    current_ans_text = ""
    parsing_mode = "none" # "none", "q", "a"
    
    q_pattern = re.compile(r'^\s*(\d+)\.\s*(.*)')
    ans_pattern = re.compile(r'^\s*Düzgün cavab:\s*(.*)')
    
    expecting_new_question = True
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # If we are expecting a new question and find one
        if expecting_new_question:
            q_match = q_pattern.match(line)
            if q_match:
                # Save previous question if exists
                if current_ans_text:
                    raw_qa.append({"q": current_q_text.strip(), "a": current_ans_text.strip()})
                
                current_q_text = q_match.group(2)
                current_ans_text = ""
                parsing_mode = "q"
                expecting_new_question = False
                continue
                
        # If it's the answer
        ans_match = ans_pattern.match(line)
        if ans_match:
            current_ans_text = ans_match.group(1)
            parsing_mode = "a"
            expecting_new_question = True # After this, we can look for the next question
            continue
            
        # Accumulate text
        if parsing_mode == "q":
            current_q_text += "\n" + line
        elif parsing_mode == "a":
            current_ans_text += "\n" + line
            
    if current_ans_text:
        raw_qa.append({"q": current_q_text.strip(), "a": current_ans_text.strip()})
        
    print(f"Parsed {len(raw_qa)} questions from text.")
    
    random.seed(33311)
    final_questions = []
    
    for i, item in enumerate(raw_qa):
        q_text = item["q"]
        a_text = item["a"]
        
        q_text = q_text.replace('ә', 'ə').replace('Ә', 'Ə')
        a_text = a_text.replace('ә', 'ə').replace('Ә', 'Ə')
        
        # fix multi-line answer spacing
        a_text = a_text.replace('\n', ' ')
        a_text = re.sub(' +', ' ', a_text)
        
        distractors = get_distractors(a_text, q_text)
        options = [a_text] + distractors
        
        opts = []
        for o in options:
            if o not in opts:
                opts.append(o)
        while len(opts) < 4:
            opts.append(opts[-1] + " (əlavə)")
            
        random.shuffle(opts)
        opt_dict = {"A": opts[0], "B": opts[1], "C": opts[2], "D": opts[3]}
        correct_key = [k for k, v in opt_dict.items() if v == a_text][0]
        
        final_questions.append({
            "id": f"q{i+1:03d}",
            "question": q_text,
            "options": opt_dict,
            "correct_answer": correct_key,
            "explanation": ""
        })
        
    output_json = {
        "certificate": "ISPS-2",
        "questions": final_questions
    }
    
    with open(r"D:\Dənizçilik_İmtahanları\backend\static\questions\xususi\isps2.json", "w", encoding="utf-8") as f:
        json.dump(output_json, f, ensure_ascii=False, indent=4)
        
    print(f"Rebuilt {len(final_questions)} questions.")

if __name__ == "__main__":
    parse_and_rebuild()
