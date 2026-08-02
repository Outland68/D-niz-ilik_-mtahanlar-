import os, json, glob, random
from collections import Counter

q_dir = r'D:\Dənizçilik_İmtahanları\backend\static\questions'
files = glob.glob(os.path.join(q_dir, '**', '*.json'), recursive=True)

print(f"Found {len(files)} JSON question files.")

# Deterministic seed for reproducible balanced shuffling
random.seed(42)

total_shuffled = 0

for fpath in files:
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', [])
    if not questions:
        continue

    for idx, q in enumerate(questions):
        options = q.get('options', {})
        correct_key = q.get('correct_answer')

        if not options or not correct_key or correct_key not in options:
            continue

        correct_val = options[correct_key]

        # Get list of option values
        val_list = list(options.values())

        # Shuffle option values
        random.shuffle(val_list)

        # Assign new options dictionary A, B, C, D
        keys = ['A', 'B', 'C', 'D']
        new_options = {keys[i]: val_list[i] for i in range(len(keys))}

        # Find new key for correct answer
        new_correct_key = None
        for k, v in new_options.items():
            if v == correct_val:
                new_correct_key = k
                break

        q['options'] = new_options
        q['correct_answer'] = new_correct_key
        total_shuffled += 1

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(f"🎉 Successfully shuffled options for {total_shuffled} questions across {len(files)} files!")
