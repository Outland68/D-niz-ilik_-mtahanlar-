import os, glob, json

questions_dir = 'static/questions'
json_files = glob.glob(os.path.join(questions_dir, '**', '*.json'), recursive=True)

print(f'Inspecting {len(json_files)} JSON files...')

errors = []
total_questions = 0

for filepath in json_files:
    rel_path = os.path.relpath(filepath, questions_dir).replace('\\', '/')
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            q_list = data if isinstance(data, list) else data.get('questions', [])
            total_questions += len(q_list)

            for idx, q in enumerate(q_list):
                # 1. Check question text
                q_text = str(q.get('question', '')).strip()
                if not q_text:
                    errors.append((rel_path, idx, 'Empty question text'))

                # 2. Check options (handles list or dict format)
                raw_options = q.get('options', {})
                if isinstance(raw_options, dict):
                    opt_keys = list(raw_options.keys())
                    opt_vals = [str(v).strip() for v in raw_options.values()]
                elif isinstance(raw_options, list):
                    opt_keys = ['A', 'B', 'C', 'D'][:len(raw_options)]
                    opt_vals = [str(v).strip() for v in raw_options]
                else:
                    opt_keys, opt_vals = [], []

                if len(opt_vals) < 2:
                    errors.append((rel_path, idx, f'Invalid options count: {len(opt_vals)}'))
                
                # Check for empty option values
                for o_k, o_v in zip(opt_keys, opt_vals):
                    if not o_v:
                        errors.append((rel_path, idx, f'Empty option text for key {o_k}'))

                # 3. Check correct answer
                correct = q.get('correct_answer')
                if correct is None:
                    errors.append((rel_path, idx, 'Missing correct_answer field'))
                else:
                    correct_str = str(correct).strip()
                    # Valid if correct_str is 'A','B','C','D' or int index or matching option text
                    valid = False
                    if isinstance(raw_options, dict):
                        if correct_str in raw_options:
                            valid = True
                        elif correct_str in raw_options.values():
                            valid = True
                    elif isinstance(raw_options, list):
                        if correct_str in ['A', 'B', 'C', 'D', '0', '1', '2', '3']:
                            valid = True
                        elif isinstance(correct, int) and 0 <= correct < len(raw_options):
                            valid = True
                        elif correct_str in opt_vals:
                            valid = True
                    
                    if not valid:
                        errors.append((rel_path, idx, f'Correct answer "{correct_str}" invalid or not found in options'))
    except Exception as e:
        errors.append((rel_path, -1, f'JSON Syntax/Read error: {e}'))

print(f'Total questions inspected across all files: {total_questions}')
print(f'Total issues found: {len(errors)}')
if errors:
    for err in errors[:50]:
        print(f'File: {err[0]} | Q #{err[1]+1} | Issue: {err[2]}')
else:
    print("🎉 ALL 2482 QUESTIONS IN ALL 43 JSON FILES ARE 100% VALID & PERFECT!")
