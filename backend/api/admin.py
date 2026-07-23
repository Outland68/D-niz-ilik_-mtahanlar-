from django.contrib import admin
from .models import Category, Certificate

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_name')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
