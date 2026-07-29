from django.contrib import admin
from .models import Category, Certificate, QuestionReport

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name')
    class Media:
        css = {'all': ('css/admin_custom.css',)}

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    class Media:
        css = {'all': ('css/admin_custom.css',)}

@admin.register(QuestionReport)
class QuestionReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate_name', 'question_id', 'user', 'status', 'created_at')
    list_filter = ('status', 'certificate_name', 'created_at')
    search_fields = ('question_text', 'report_reason', 'user__username', 'user__email')
    readonly_fields = ('created_at',)
    class Media:
        css = {'all': ('css/admin_custom.css',)}


