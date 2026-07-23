# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from api.models import Category, Certificate

# Category 2: Xüsusi hazırlıq şəhadətnamələri üzrə
category, created = Category.objects.get_or_create(
    name='Xüsusi hazırlıq şəhadətnamələri üzrə',
    defaults={'icon_name': 'FileBadge', 'color': 'bg-emerald-500/20 text-emerald-400'}
)

special_certificates = [
    "Safety familiarization basic training and instruction for all seafarers",
    "Gəmi sürücülərinin təkmilləşdirilməsi (istismar)",
    "Gəmi elektrik mexaniklərinin təkmilləşdirilməsi",
    "Gəmi mexaniklərinin təkmilləşdirilməsi (idarəetmə)",
    "Gəmi sürücülərinin təkmilləşdirilməsi (idarəetmə)",
    "Gəmi mexaniklərinin təkmilləşdirilməsi (istismar səviyyəsində)",
    "Əmniyyətli İdarəetmə Haqqında Beynəlxalq Məcəllə",
    "İzdihamın idarə olunması üzrə hazırlıq",
    "İnert qaz sistemi",
    "Yanğınla mübarizə geniş proqram üzrə",
    "Təhlükəli və zərərli yüklərin daşınması",
    "Sərnişinlərə bilavasitə xidmət göstərən heyət üyələri",
    "Sərnişinlərin, yükün və gəmi gövdəsinin təhlükəsizliyi üzrə hazırlıq",
    "Sürətli xilasetmə qayıq mütəxəssisi",
    "Sürətli olmayan xilasedici qayıqlar və sallar üzrə mütəxəssis",
    "Radar, avtomatik radar müşahidə vasitələri, kapitan körpüsü komandası və axtarış xilasetmə (idarəetmə səviyyəsində)",
    "Radar müşahidəsi və təsviri, avtomatik radar müşahidəsi vasitələrinin istismarı (istismar səviyyəsində)",
    "Qlobal Dəniz Fəlakət və Əmniyyətli Rabitə Sisteminin Ümumi Rayon Operatoru",
    "Neft və Kimyəvi-İlkin",
    "Neft tankerlərində-geniş",
    "Maşın şöbəsi resurslarının idarə olunması",
    "Liman vasitələrinin mühafizəyə məsul",
    "Liderlik və birgə iş fəaliyyəti",
    "Kimyəvi maddə daşıyan tankerlərdə yük əməliyyatlarına dair geniş proqram üzrə hazırlıq",
    "Kapitan Körpüsü Resurslarının İdarə Olunması",
    "ISPS-3",
    "ISPS-2",
    "ISPS-1",
    "Gəminin idarə olunması və manevr edilməsi",
    "Gəmi əmniyyətliyi üzrə Məsul Şəxs",
    "Gəmidə tibbi nəzarət",
    "Gəmidə ilk tibbi yardım",
    "Gəmi qazanalizatorları və onların istismarı",
    "Elektron Xəritə Displeyinin və İnformasiya Sistemlərinin İstismar Qaydaları",
    "Bütün dənizçilər üçün təhlükəsizlik üzrə tanışlıq, ilkin hazırlıq və təlimat",
    "Böhran zamanı idarəetmə və insan davranışı üzrə hazırlıq",
    "1000 volt və artıq olan gərginlik sistemlərinin təhlükəsiz istismarı və onlara texniki nəzarət",
    "Xam Neftlə Yuyulma Sistemi"
]

added_count = 0
for name in special_certificates:
    cert, cert_created = Certificate.objects.get_or_create(
        category=category,
        name=name
    )
    if cert_created:
        added_count += 1

print(f"Added {added_count} new certificates for 'Xüsusi hazırlıq şəhadətnamələri üzrə'. Total now: {Certificate.objects.filter(category=category).count()}")
