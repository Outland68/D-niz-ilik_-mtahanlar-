# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from api.models import Category, Certificate

c = Client()

print("==================================================")
print("       BACKEND AUTOMATED INTEGRATION TESTS        ")
print("==================================================")

# 1. Test Categories Public Endpoint
res = c.get('/api/categories/')
assert res.status_code == 200
categories = res.json()
print(f"✅ [1/7] GET /api/categories/ -> Status 200 | Total Categories: {len(categories)}")

# 2. Test Certificates Public Endpoint
res = c.get('/api/certificates/')
assert res.status_code == 200
certificates = res.json()
print(f"✅ [2/7] GET /api/certificates/ -> Status 200 | Total Certificates: {len(certificates)}")

# 3. Test Register New User
test_username = "test_sailor_99"
test_email = "sailor99@example.com"
test_password = "password123"

# Cleanup if exists
User.objects.filter(username=test_username).delete()

res = c.post('/api/auth/register/', {'username': test_username, 'email': test_email, 'password': test_password}, content_type='application/json')
assert res.status_code == 201
reg_data = res.json()
assert 'access' in reg_data
access_token = reg_data['access']
print(f"✅ [3/7] POST /api/auth/register/ -> Status 201 | Registered user '{test_username}', received JWT token.")

# 4. Test Login User
res = c.post('/api/auth/login/', {'username': test_username, 'password': test_password}, content_type='application/json')
assert res.status_code == 200
login_data = res.json()
assert 'access' in login_data
print(f"✅ [4/7] POST /api/auth/login/ -> Status 200 | Login successful.")

# 5. Test Protected Questions Endpoint without Token (expect 401)
cert = Certificate.objects.exclude(json_file='').first()
assert cert is not None
res = c.get(f'/api/certificates/{cert.id}/questions/')
assert res.status_code == 401
print(f"✅ [5/7] GET /api/certificates/{cert.id}/questions/ (No Token) -> Status 401 Unauthorized (Security Protected).")

# 6. Test Protected Questions Endpoint WITH JWT Token (expect 200)
res = c.get(f'/api/certificates/{cert.id}/questions/', HTTP_AUTHORIZATION=f'Bearer {access_token}')
assert res.status_code == 200
questions_data = res.json()
assert 'questions' in questions_data
print(f"✅ [6/7] GET /api/certificates/{cert.id}/questions/ (With JWT Token) -> Status 200 | Certificate: '{cert.name}' | Questions loaded: {len(questions_data['questions'])}")

# 7. Test Gmail OTP Reset Flow
res = c.post('/api/auth/send-reset-code/', {'email': test_email}, content_type='application/json')
assert res.status_code == 200
send_data = res.json()
otp_code = send_data.get('dev_code')
print(f"✅ [7a/7] POST /api/auth/send-reset-code/ -> Status 200 | Generated OTP Code: {otp_code}")

new_pass = "newpassword123"
res = c.post('/api/auth/verify-reset-code/', {'email': test_email, 'code': otp_code, 'new_password': new_pass}, content_type='application/json')
assert res.status_code == 200
print(f"✅ [7b/7] POST /api/auth/verify-reset-code/ -> Status 200 | Password successfully reset with OTP!")

# Login with new password to verify
res = c.post('/api/auth/login/', {'username': test_username, 'password': new_pass}, content_type='application/json')
assert res.status_code == 200
print(f"✅ [7c/7] Verified login with NEW password -> Status 200 OK.")

print("\n🎉 ALL BACKEND & SECURITY TESTS PASSED SUCCESSFULLY! 🎉\n")
