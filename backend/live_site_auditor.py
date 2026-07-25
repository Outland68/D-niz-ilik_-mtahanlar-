import urllib.request
import json
import os

BASE_URL = 'https://d-niz-ilik-mtahanlar-1.onrender.com/api'

print("==================================================")
print("     LIVE PRODUCTION FULL EXAM AUDITOR            ")
print("==================================================")

# 1. Login as Auditor Test User
login_url = f"{BASE_URL}/auth/login/"
payload = json.dumps({"username": "auditor_test", "password": "Password123!"}).encode('utf-8')
req = urllib.request.Request(login_url, data=payload, headers={'Content-Type': 'application/json'}, method='POST')

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    token = data['access']
    print("✅ Live Production Login successful! Token acquired.")

# 2. Fetch all certificates
certs_url = f"{BASE_URL}/certificates/"
req = urllib.request.Request(certs_url)
with urllib.request.urlopen(req) as resp:
    certificates = json.loads(resp.read().decode('utf-8'))

print(f"📋 Found {len(certificates)} total certificates in production API.\n")

total_questions_tested = 0
certificates_with_issues = []

for cert in certificates:
    cert_id = cert['id']
    cert_name = cert['name']
    
    q_url = f"{BASE_URL}/certificates/{cert_id}/questions/"
    req = urllib.request.Request(q_url, headers={'Authorization': f'Bearer {token}'})
    
    try:
        with urllib.request.urlopen(req) as resp:
            q_data = json.loads(resp.read().decode('utf-8'))
            questions = q_data.get('questions', [])
            
            if not questions:
                # Certificate has no linked questions or empty file
                certificates_with_issues.append((cert_name, "Empty / No Questions Linked"))
                continue

            total_questions_tested += len(questions)
            issues_in_cert = []

            for idx, q in enumerate(questions):
                q_text = str(q.get('question', '')).strip()
                options = q.get('options', [])
                correct = q.get('correct_answer')
                img_url = q.get('image_url')

                # Check question
                if not q_text:
                    issues_in_cert.append(f"Q #{idx+1}: Empty question text")
                
                # Check options
                if not isinstance(options, list) or len(options) < 2:
                    issues_in_cert.append(f"Q #{idx+1}: Invalid options count ({len(options) if isinstance(options, list) else 0})")
                else:
                    for opt_i, opt_val in enumerate(options):
                        if not str(opt_val).strip():
                            issues_in_cert.append(f"Q #{idx+1}: Empty option at position {opt_i+1}")

                # Check correct answer index bounds
                if not isinstance(correct, int) or correct < 0 or correct >= len(options):
                    issues_in_cert.append(f"Q #{idx+1}: Invalid correct_answer index ({correct})")

            if issues_in_cert:
                certificates_with_issues.append((cert_name, f"{len(issues_in_cert)} question issues: {issues_in_cert[:3]}"))
            else:
                print(f"✅ [{cert_id}] {cert_name[:50]} -> {len(questions)} questions OK!")

    except Exception as e:
        certificates_with_issues.append((cert_name, f"HTTP Error / Failed to load: {e}"))

print("\n==================================================")
print(f"📊 SUMMARY: Tested {total_questions_tested} questions across {len(certificates)} certificates.")
print(f"Total problematic certificates: {len(certificates_with_issues)}")
print("==================================================")

for name, err in certificates_with_issues:
    print(f"⚠️ {name}: {err}")
