from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import UserSession

class SingleDeviceJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication class that validates if the JWT token's session_key
    matches the single active UserSession record in the database.
    If another device logs into the same account, old tokens are instantly invalidated.
    """
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            # Check HttpOnly cookies if header is missing
            raw_token = request.COOKIES.get('access_token')
        else:
            raw_token = self.get_raw_token(header)

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)

        # Enforce single device active session
        token_session_key = validated_token.get('session_key')
        active_session = UserSession.objects.filter(user=user).first()

        if active_session and token_session_key and active_session.session_key != token_session_key:
            raise AuthenticationFailed(
                'Bu hesaba başqa bir cihazdan daxil olundu. Sizin sessiyanız sonlandırıldı.',
                code='single_device_logout'
            )

        return (user, validated_token)
