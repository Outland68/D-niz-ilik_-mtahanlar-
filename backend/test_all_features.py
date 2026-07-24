# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from api.models import Category, Certificate, UserSession

c1 = Client() # Device 1
c2 = Client() # Device 2

print("==================================================")
print("     COMPREHENSIVE BACKEND & SECURITY TESTS       ")
print("==================================================")

# 1. Test Categories Public Endpoint
res = c1.get('/api/categories/')
assert res.status_code == 200
categories = res.json()
print(f"✅ [1/9] GET /api/categories/ -> Status 200 | Total Categories: {len(categories)}")

# 2. Test Certificates Public Endpoint
res = c1.get('/api/certificates/')
assert res.status_code == 200
certificates = res.json()
print(f"✅ [2/9] GET /api/certificates/ -> Status 200 | Total Certificates: {len(certificates)}")

# 3. Test Register New User & Login with Email/Username
test_username = "test_captain_99"
test_email = "captain99@example.com"
test_password = "password123"

User.objects.filter(username=test_username).delete()

res = c1.post('/api/auth/register/', {'username': test_username, 'email': test_email, 'password': test_password}, content_type='application/json')
assert res.status_code == 201
print(f"✅ [3/9] POST /api/auth/register/ -> Status 201 | Registered user '{test_username}'.")

# 4. Login Device 1
res_dev1 = c1.post('/api/auth/login/', {'username': test_email, 'password': test_password}, content_type='application/json')
assert res_dev1.status_code == 200
dev1_data = res_dev1.json()
dev1_access = dev1_data['access']
print(f"✅ [4/9] POST /api/auth/login/ (Device 1) -> Status 200 | Device 1 logged in.")

# 5. Device 1 accesses protected questions (Should Succeed)
cert = Certificate.objects.exclude(json_file='').first()
assert cert is not None
res = c1.get(f'/api/certificates/{cert.id}/questions/', HTTP_AUTHORIZATION=f'Bearer {dev1_access}')
assert res.status_code == 200
print(f"✅ [5/9] GET /api/certificates/{cert.id}/questions/ (Device 1) -> Status 200 | Device 1 token valid.")

# 6. Login Device 2 on SAME account (Single Device Enforcement Test)
res_dev2 = c2.post('/api/auth/login/', {'username': test_username, 'password': test_password}, content_type='application/json')
assert res_dev2.status_code == 200
dev2_data = res_dev2.json()
dev2_access = dev2_data['access']
print(f"✅ [6/9] POST /api/auth/login/ (Device 2) -> Status 200 | Device 2 logged in on SAME account.")

# 7. Device 1 tries to access protected endpoint AFTER Device 2 logged in (Should FAIL 401)
res_dev1_retry = c1.get(f'/api/certificates/{cert.id}/questions/', HTTP_AUTHORIZATION=f'Bearer {dev1_access}')
assert res_dev1_retry.status_code == 401
print(f"✅ [7/9] Single Device Protection: Device 1 request rejected with Status 401 Unauthorized! (Device 1 kicked out).")

# 8. Device 2 tries to access protected endpoint (Should SUCCEED)
res_dev2_retry = c2.get(f'/api/certificates/{cert.id}/questions/', HTTP_AUTHORIZATION=f'Bearer {dev2_access}')
assert res_dev2_retry.status_code == 200
questions = res_dev2_retry.json()['questions']
print(f"✅ [8/9] Single Device Protection: Device 2 active session verified with Status 200 | {len(questions)} questions loaded.")

# 9. Verify questions structure (4 options A, B, C, D & correct answer)
q_sample = questions[0]
assert 'question' in q_sample
assert 'options' in q_sample
assert len(q_sample['options']) == 4
assert 'correct_answer' in q_sample
print(f"✅ [9/9] Question Structure Verified: 4 options (A,B,C,D) present with correct answer.")

print("\n🎉 ALL 9 SYSTEM & SECURITY TESTS PASSED 100% PERFECTLY! 🎉\n")
