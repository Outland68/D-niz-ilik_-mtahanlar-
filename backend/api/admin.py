from django.contrib import admin
from .models import Category, Certificate, QuestionReport, SiteVisit

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



@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ('user_display', 'ip_address', 'page_url', 'visited_at')
    list_filter = ('visited_at',)
    search_fields = ('ip_address', 'page_url', 'user__username')
    readonly_fields = ('user', 'ip_address', 'user_agent', 'page_url', 'visited_at')
    
    def user_display(self, obj):
        return obj.user.username if obj.user else 'Anonim'
    user_display.short_description = 'İstifadəçi'
    
    class Media:
        css = {'all': ('css/admin_custom.css',)}
