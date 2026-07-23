import json
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

from .models import Category, Certificate
from .serializers import CategorySerializer, CertificateListSerializer


# ─────────────────────────────────────────────
#  AUTH VIEWS
# ─────────────────────────────────────────────

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST /api/auth/login/
    Body: { "username": "...", "password": "..." }
    Returns: { "access": "...", "refresh": "...", "user": { ... } }
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
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    POST /api/auth/register/
    Body: { "username": "...", "email": "...", "password": "..." }
    """
    username = request.data.get('username')
    email = request.data.get('email', '')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'İstifadəçi adı və şifrə tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

    if len(password) < 8:
        return Response({'error': 'Şifrə ən azı 8 simvol olmalıdır.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Bu istifadəçi adı artıq götürülüb.'}, status=status.HTTP_400_BAD_REQUEST)

    if email and User.objects.filter(email=email).exists():
        return Response({'error': 'Bu e-poçt ünvanı artıq istifadə olunur. Başqa e-poçt daxil edin və ya daxil olun.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
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
    Body: { "refresh": "..." }
    Returns: { "access": "..." }
    """
    refresh_token = request.data.get('refresh')
    if not refresh_token:
        return Response({'error': 'Refresh token tələb olunur.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        token = RefreshToken(refresh_token)
        return Response({'access': str(token.access_token)})
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

    # Send Email via Gmail SMTP
    from django.core.mail import send_mail
    subject = "Dənizçilik İmtahanları - Şifrə Sıfırlama Kodu"
    message = f"Hərvaxtınız xeyir {user.username},\n\nŞifrənizi sıfırlamaq üçün təsdiq kodunuz: {code}\n\nBu kodu heç kimlə paylaşmayın.\n\nHörmətlə,\nDənizçilik İmtahanları Komandası"
    
    try:
        send_mail(
            subject, 
            message, 
            settings.DEFAULT_FROM_EMAIL, 
            [user.email], 
            fail_silently=True
        )
    except Exception as e:
        print("Gmail SMTP Exception:", e)

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
    """GET /api/auth/me/  — current user info"""
    user = request.user
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
