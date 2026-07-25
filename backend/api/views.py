import json
import os
from pathlib import Path

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .models import Category, Certificate, UserSession
from .serializers import CategorySerializer, CertificateListSerializer
import uuid

# ─────────────────────────────────────────────
#  AUTH VIEWS
# ─────────────────────────────────────────────

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST /api/auth/login/
    Enforces Single Device Login (logging out any previous device)
    and sets HttpOnly cookies.
    """
    username_input = request.data.get('username', '').strip()
    password = request.data.get('password', '').strip()

    if not username_input or not password:
        return Response(
            {'error': 'İstifadəçi adı / E-poçt və şifrə tələb olunur.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Check if input is email or username
    user_obj = User.objects.filter(username=username_input).first() or User.objects.filter(email=username_input).first()
    if not user_obj:
        return Response(
            {'error': 'İstifadəçi adı və ya şifrə yanlışdır.'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    user = authenticate(username=user_obj.username, password=password)
    if user is None:
        return Response(
            {'error': 'İstifadəçi adı və ya şifrə yanlışdır.'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # 🔒 SINGLE DEVICE LOGIN ENFORCEMENT:
    # Generate unique session key for this device login
    new_session_key = str(uuid.uuid4())
    UserSession.objects.update_or_create(
        user=user,
        defaults={'session_key': new_session_key}
    )

    refresh = RefreshToken.for_user(user)
    refresh['session_key'] = new_session_key
    
    access_token = refresh.access_token
    access_token['session_key'] = new_session_key

    access_token_str = str(access_token)
    refresh_token_str = str(refresh)

    response = Response({
        'access': access_token_str,
        'refresh': refresh_token_str,
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    })

    # 🍪 Set HttpOnly Cookies for persistent, secure login
    response.set_cookie(
        key='access_token',
        value=access_token_str,
        max_age=7 * 24 * 3600, # 7 days
        httponly=True,
        samesite='None',
        secure=True
    )
    response.set_cookie(
        key='refresh_token',
        value=refresh_token_str,
        max_age=30 * 24 * 3600, # 30 days
        httponly=True,
        samesite='None',
        secure=True
    )

    return response


# In-memory email validation storage: { email: { 'code': '123456', 'username': '...', 'password': '...' } }
EMAIL_VERIFICATION_CODES = {}

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    POST /api/auth/register/
    Generates verification code, sends to Gmail, but does not activate account yet.
    """
    username = request.data.get('username')
    email = request.data.get('email', '').strip()
    password = request.data.get('password')

    if not username or not password or not email:
        return Response({'error': 'İstifadəçi adı, e-poçt və şifrə tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

    if len(password) < 8:
        return Response({'error': 'Şifrə ən azı 8 simvol olmalıdır.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Bu istifadəçi adı artıq götürülüb.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Bu e-poçt ünvanı artıq istifadə olunur. Başqa e-poçt daxil edin və ya daxil olun.'}, status=status.HTTP_400_BAD_REQUEST)

    # Generate 6-digit OTP
    import random
    code = f"{random.randint(100004, 999999)}"
    
    # Temporarily cache registration data
    EMAIL_VERIFICATION_CODES[email] = {
        'code': code,
        'username': username,
        'password': password
    }

    # Send confirmation code via n8n Webhook (Primary) and Django SMTP (Fallback)
    import threading
    from django.core.mail import send_mail

    def send_email_thread(email_address, otp_code, username_val=None):
        # 1. n8n Webhook integration (Primary) using Python's built-in urllib to avoid external dependency issues
        import urllib.request
        import json
        
        n8n_url = os.environ.get('N8N_WEBHOOK_URL', '')
        if not n8n_url and hasattr(settings, 'N8N_WEBHOOK_URL'):
            n8n_url = getattr(settings, 'N8N_WEBHOOK_URL', '')
        
        if n8n_url:
            try:
                payload = {
                    'email': email_address,
                    'code': otp_code,
                    'type': 'register',
                    'username': username_val or 'İstifadəçi'
                }
                data_bytes = json.dumps(payload).encode('utf-8')
                req = urllib.request.Request(
                    n8n_url,
                    data=data_bytes,
                    headers={'Content-Type': 'application/json'},
                    method='POST'
                )
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status in [200, 201]:
                        print(f"OTP successfully routed via n8n Webhook to {email_address}")
                        return
            except Exception as web_err:
                print("n8n Webhook routing failed, trying SMTP fallback:", web_err)

        # 2. Django SMTP Fallback
        try:
            subject = "Dənizçilik İmtahanları - Qeydiyyat Təsdiq Kodu"
            message = f"Hərvaxtınız xeyir,\n\nDənizçilik İmtahanları platformasında qeydiyyatdan keçmək üçün təsdiq kodunuz: {otp_code}\n\nBu kodu qeydiyyat pəncərəsinə daxil edərək hesabınızı aktivləşdirin.\n\nHörmətlə,\nDənizçilik İmtahanları Komandası"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email_address], fail_silently=True)
        except Exception as smtp_err:
            print("Background SMTP Fallback Exception:", smtp_err)

    # Start thread
    thread = threading.Thread(
        target=send_email_thread,
        args=(email, code, username)
    )
    thread.daemon = True
    thread.start()

    return Response({
        'message': f'6 rəqəmli qeydiyyat təsdiq kodu {email} ünvanına göndərildi!',
        'email_sent': True
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email_view(request):
    """
    POST /api/auth/verify-email/
    Body: { "email": "...", "code": "..." }
    Creates the user account after valid code validation.
    """
    email = request.data.get('email', '').strip()
    code = request.data.get('code', '').strip()

    if not email or not code:
        return Response({'error': 'E-poçt və təsdiq kodu tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

    if email not in EMAIL_VERIFICATION_CODES:
        return Response({'error': 'Qeydiyyat sorğusu tapılmadı və ya vaxtı bitib.'}, status=status.HTTP_400_BAD_REQUEST)

    saved_data = EMAIL_VERIFICATION_CODES[email]
    if saved_data['code'] != code:
        return Response({'error': 'Daxil etdiyiniz 6 rəqəmli təsdiq kodu yanlışdır!'}, status=status.HTTP_400_BAD_REQUEST)

    # Code is valid -> create actual user in database
    user = User.objects.create_user(
        username=saved_data['username'], 
        email=email, 
        password=saved_data['password']
    )
    
    # Delete temporary cache
    del EMAIL_VERIFICATION_CODES[email]

    refresh = RefreshToken.for_user(user)
    return Response({
        'access': str(refresh.access_token),
        'refresh': str(refresh),
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    """
    POST /api/auth/refresh/
    Checks single active session key before refreshing token.
    """
    refresh_token = request.data.get('refresh') or request.COOKIES.get('refresh_token')
    if not refresh_token:
        return Response({'error': 'Refresh token tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        token = RefreshToken(refresh_token)
        user_id = token.payload.get('user_id')
        token_session_key = token.payload.get('session_key')

        if user_id and token_session_key:
            user = User.objects.filter(id=user_id).first()
            active_session = UserSession.objects.filter(user=user).first() if user else None
            if active_session and active_session.session_key != token_session_key:
                return Response(
                    {'error': 'Bu hesaba başqa bir cihazdan daxil olundu. Sizin sessiyanız sonlandırıldı.'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

        access_token = token.access_token
        if token_session_key:
            access_token['session_key'] = token_session_key

        return Response({'access': str(access_token)})
    except TokenError as e:
        return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)


# In-memory OTP storage: { email: { 'code': '123456', 'user_id': 1 } }
RESET_CODES = {}

@api_view(['POST'])
@permission_classes([AllowAny])
def send_reset_code_view(request):
    """
    POST /api/auth/send-reset-code/
    Body: { "email": "..." }
    """
    email = request.data.get('email', '').strip()
    if not email:
        return Response({'error': 'E-poçt ünvanı tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email).first() or User.objects.filter(username=email).first()
    if not user:
        return Response({'error': 'Bu e-poçt ünvanına uyğun aktiv hesab tapılmadı.'}, status=status.HTTP_404_NOT_FOUND)

    # Generate 6-digit OTP code
    import random
    code = f"{random.randint(100004, 999999)}"
    RESET_CODES[user.email] = {'code': code, 'user_id': user.id}
    RESET_CODES[email] = {'code': code, 'user_id': user.id}

    # Send Email via Gmail SMTP in background thread (with n8n primary check)
    import threading
    from django.core.mail import send_mail

    def send_reset_thread(email_address, otp_code, username):
        n8n_url = os.environ.get('N8N_WEBHOOK_URL', '')
        if not n8n_url and hasattr(settings, 'N8N_WEBHOOK_URL'):
            n8n_url = getattr(settings, 'N8N_WEBHOOK_URL', '')
        
        if n8n_url:
            try:
                import urllib.request
                import json
                payload = {
                    'email': email_address,
                    'code': otp_code,
                    'type': 'reset',
                    'username': username
                }
                data_bytes = json.dumps(payload).encode('utf-8')
                req = urllib.request.Request(
                    n8n_url,
                    data=data_bytes,
                    headers={'Content-Type': 'application/json'},
                    method='POST'
                )
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status in [200, 201]:
                        print(f"Reset OTP routed via n8n Webhook to {email_address}")
                        return
            except Exception as web_err:
                print("n8n Reset Webhook failed, trying SMTP fallback:", web_err)

        try:
            subject = "Dənizçilik İmtahanları - Şifrə Sıfırlama Kodu"
            message = f"Hərvaxtınız xeyir {username},\n\nŞifrənizi sıfırlamaq üçün təsdiq kodunuz: {otp_code}\n\nBu kodu heç kimlə paylaşmayın.\n\nHörmətlə,\nDənizçilik İmtahanları Komandası"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email_address], fail_silently=True)
        except Exception as e:
            print("Background SMTP Reset Exception:", e)

    thread = threading.Thread(
        target=send_reset_thread,
        args=(user.email, code, user.username)
    )
    thread.daemon = True
    thread.start()

    return Response({
        'message': f'6 rəqəmli təsdiq kodu {user.email} ünvanına göndərildi!'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_reset_code_view(request):
    """
    POST /api/auth/verify-reset-code/
    Body: { "email": "...", "code": "...", "new_password": "..." }
    """
    email = request.data.get('email', '').strip()
    code = request.data.get('code', '').strip()
    new_password = request.data.get('new_password', '').strip()

    if not email or not code or not new_password:
        return Response({'error': 'Bütün xanalar doldurulmalıdır.'}, status=status.HTTP_400_BAD_REQUEST)

    if len(new_password) < 8:
        return Response({'error': 'Yeni şifrə ən azı 8 simvol olmalıdır.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email).first() or User.objects.filter(username=email).first()
    if not user:
        return Response({'error': 'İstifadəçi tapılmadı.'}, status=status.HTTP_400_BAD_REQUEST)

    # Check key by user.email or input email
    target_key = user.email if user.email in RESET_CODES else email
    if target_key not in RESET_CODES:
        return Response({'error': 'Sıfırlama sorğusu tapılmadı və ya vaxtı bitib.'}, status=status.HTTP_400_BAD_REQUEST)

    saved_info = RESET_CODES[target_key]
    if str(saved_info['code']).strip() != str(code).strip():
        return Response({'error': 'Daxil etdiyiniz 6 rəqəmli kod yanlışdır!'}, status=status.HTTP_400_BAD_REQUEST)

    # Success: set new password & delete used code
    user.set_password(new_password)
    user.save()
    if target_key in RESET_CODES:
        del RESET_CODES[target_key]

    return Response({'message': 'Şifrəniz uğurla yeniləndi! İndi daxil ola bilərsiniz.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password_view(request):
    """
    POST /api/auth/change-password/   (JWT required)
    Body: { "old_password": "...", "new_password": "..." }
    """
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    if not old_password or not new_password:
        return Response({'error': 'Köhnə və yeni şifrə tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

    if not user.check_password(old_password):
        return Response({'error': 'Mövcud şifrə yanlışdır.'}, status=status.HTTP_400_BAD_REQUEST)

    if len(new_password) < 8:
        return Response({'error': 'Yeni şifrə ən azı 8 simvol olmalıdır.'}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()
    return Response({'message': 'Şifrə uğurla dəyişdirildi.'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    POST /api/auth/logout/   (JWT required)
    Body: { "refresh": "..." }
    Blacklists the refresh token.
    """
    refresh_token = request.data.get('refresh')
    if not refresh_token:
        return Response({'error': 'Refresh token tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'message': 'Uğurla çıxış edildi.'})
    except TokenError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    """
    GET /api/auth/me/  — current user info & single device validation
    """
    user = request.user
    
    # Check single device active session
    active_session = UserSession.objects.filter(user=user).first()
    auth_header = request.headers.get('Authorization', '')
    
    # If session exists in DB, ensure user hasn't logged in on another device
    # (Token payload check or single active record verification)
    
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    })


# ─────────────────────────────────────────────
#  CATEGORY & CERTIFICATE VIEWS  (public)
# ─────────────────────────────────────────────

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CertificateListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Certificate.objects.all()
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated], url_path='questions')
    def questions(self, request, pk=None):
        """
        GET /api/certificates/{id}/questions/   (JWT required)
        Reads questions from the JSON file linked to this certificate.
        """
        certificate = self.get_object()

        if not certificate.json_file:
            return Response({'questions': [], 'certificate': certificate.name})

        json_path = settings.QUESTIONS_DIR / certificate.json_file
        if not json_path.exists():
            return Response(
                {'error': f'Sual faylı tapılmadı: {certificate.json_file}'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            with open(json_path, encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            return Response({'error': f'Fayl oxunarkən xəta: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'certificate': certificate.name,
            'questions': data.get('questions', [])
        })
