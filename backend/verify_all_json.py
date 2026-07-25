import os, json, sys

sys.stdout.reconfigure(encoding='utf-8')

q_base = r"D:\Dənizçilik_İmtahanları\backend\static\questions"
b_img_base = r"D:\Dənizçilik_İmtahanları\backend\static"
f_img_base = r"D:\Dənizçilik_İmtahanları\frontend\public"

total_json_files = 0
total_questions = 0
image_references = 0
missing_images = 0
invalid_correct_answers = 0

for root, dirs, files in os.walk(q_base):
    for f in sorted(files):
        if f.endswith('.json'):
            total_json_files += 1
            path = os.path.join(root, f)
            rel = os.path.relpath(path, q_base)
            
            with open(path, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
                
            qs = data.get('questions', [])
            total_questions += len(qs)
            
            for idx, q in enumerate(qs, 1):
                opts = q.get('options', {})
                corr = q.get('correct_answer')
                
                if corr not in opts:
                    print(f"[{rel}] Q{idx} ({q.get('id')}): Invalid correct_answer '{corr}' not in options {list(opts.keys())}")
                    invalid_correct_answers += 1
                    
                img_url = q.get('image_url')
                if img_url:
                    image_references += 1
                    # strip leading slash
                    clean_rel = img_url.lstrip('/')
                    b_img_path = os.path.join(b_img_base, clean_rel)
                    f_img_path = os.path.join(f_img_base, clean_rel)
                    
                    b_exists = os.path.exists(b_img_path)
                    f_exists = os.path.exists(f_img_path)
                    
                    if not b_exists or not f_exists:
                        print(f"[{rel}] Q{idx} ({q.get('id')}): Missing image file '{img_url}' (Backend: {b_exists}, Frontend: {f_exists})")
                        missing_images += 1

print("\n================ Verification Summary ================")
print(f"Total JSON Files Verified: {total_json_files}")
print(f"Total Questions Verified: {total_questions}")
print(f"Total Image References Verified: {image_references}")
print(f"Missing Image Files: {missing_images}")
print(f"Invalid Correct Answer Keys: {invalid_correct_answers}")
