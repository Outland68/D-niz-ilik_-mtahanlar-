from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, CertificateViewSet, QuestionReportViewSet,
    login_view, register_view, verify_email_view, refresh_token_view, change_password_view,
    send_reset_code_view, verify_reset_code_view,
    logout_view, me_view, record_visit, get_site_visits
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'certificates', CertificateViewSet, basename='certificate')
router.register(r'reports', QuestionReportViewSet, basename='report')

urlpatterns = [
    path('', include(router.urls)),
    # Auth endpoints
    path('auth/login/', login_view, name='auth-login'),
    path('auth/register/', register_view, name='auth-register'),
    path('auth/verify-email/', verify_email_view, name='auth-verify-email'),
    path('auth/refresh/', refresh_token_view, name='auth-refresh'),
    path('auth/send-reset-code/', send_reset_code_view, name='auth-send-reset-code'),
    path('auth/verify-reset-code/', verify_reset_code_view, name='auth-verify-reset-code'),
    path('auth/logout/', logout_view, name='auth-logout'),
    path('auth/change-password/', change_password_view, name='auth-change-password'),
    path('auth/me/', me_view, name='auth-me'),
    path('record-visit/', record_visit, name='record-visit'),
    path('site-visits/', get_site_visits, name='site-visits'),
]
