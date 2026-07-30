import os, json, glob, shutil

questions_dir = r'D:\Dənizçilik_İmtahanları\backend\static\questions'
docs_dir = r'D:\Dənizçilik_İmtahanları\Ləyihənin İmtahan sorulari'

json_files = glob.glob(os.path.join(questions_dir, '**', '*.json'), recursive=True)

report = []
total_qs = 0
total_issues = 0

for fpath in json_files:
    fname = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception as e:
            report.append(f"❌ {fname}: INVALID JSON -> {e}")
            continue

    cert_name = data.get('certificate', fname)
    questions = data.get('questions', [])
    total_qs += len(questions)

    file_issues = []
    
    # Check each question
    for idx, q in enumerate(questions):
        q_id = q.get('id', f'q_{idx+1}')
        q_text = q.get('question', '')
        options = q.get('options', {})
        corr = q.get('correct_answer')
        img = q.get('image_url')

        # Rule 1: Must have question text
        if not q_text.strip():
            file_issues.append(f"  - [{q_id}] Question text is empty!")

        # Rule 2: Options must be dict or list with at least 4 items
        if isinstance(options, dict):
            if len(options) < 4:
                file_issues.append(f"  - [{q_id}] Less than 4 options in dict ({len(options)})")
            for letter in ['A', 'B', 'C', 'D']:
                if not options.get(letter, '').strip():
                    file_issues.append(f"  - [{q_id}] Option {letter} is empty or missing!")
            if corr not in ['A', 'B', 'C', 'D']:
                file_issues.append(f"  - [{q_id}] Invalid correct_answer letter: '{corr}'")
            elif not options.get(corr, '').strip():
                file_issues.append(f"  - [{q_id}] Correct answer '{corr}' points to an empty string!")

        elif isinstance(options, list):
            if len(options) < 4:
                file_issues.append(f"  - [{q_id}] Less than 4 options in list ({len(options)})")
            for o_idx, opt_str in enumerate(options[:4]):
                if not str(opt_str).strip():
                    file_issues.append(f"  - [{q_id}] Option index {o_idx} is empty!")
            if isinstance(corr, int):
                if not (0 <= corr < len(options)):
                    file_issues.append(f"  - [{q_id}] Out of bounds correct_answer index: {corr}")
            elif isinstance(corr, str) and corr in ['A', 'B', 'C', 'D']:
                corr_idx = ['A', 'B', 'C', 'D'].index(corr)
                if corr_idx >= len(options):
                    file_issues.append(f"  - [{q_id}] Correct answer '{corr}' out of bounds for options list!")
            else:
                file_issues.append(f"  - [{q_id}] Invalid correct_answer format: {corr}")

        else:
            file_issues.append(f"  - [{q_id}] Options is not a dict or list!")

        # Rule 3: Check image URL validity if present
        if img:
            # Map /images/... to public/images/...
            clean_img = img.lstrip('/')
            frontend_img = os.path.join(r'D:\Dənizçilik_İmtahanları\frontend\public', clean_img)
            backend_img = os.path.join(r'D:\Dənizçilik_İmtahanları\backend\static', clean_img.replace('images/', 'images/'))
            if not os.path.exists(frontend_img) and not os.path.exists(backend_img):
                file_issues.append(f"  - [{q_id}] Referenced image file does NOT exist: '{img}'")

    if file_issues:
        total_issues += len(file_issues)
        report.append(f"❌ {fname} ({cert_name}) - {len(file_issues)} ISSUES FOUND:")
        report.extend(file_issues)
    else:
        report.append(f"✅ {fname} ({cert_name}) - {len(questions)} questions 100% VALID!")

print("=== AUDIT SUMMARY ===")
print(f"Total files audited: {len(json_files)}")
print(f"Total questions audited: {total_qs}")
print(f"Total issues found: {total_issues}")
print("\nDetailed Report:\n")
for line in report[:50]: # Print first 50 lines
    print(line)

with open(r'D:\Dənizçilik_İmtahanları\backend\audit_full_report.txt', 'w', encoding='utf-8') as out:
    out.write("\n".join(report))
