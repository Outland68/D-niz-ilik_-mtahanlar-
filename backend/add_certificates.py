# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from api.models import Category, Certificate

category_name = 'Sertifikat diplom üzrə'
category = Category.objects.filter(name=category_name).first()

if not category:
    print(f"Kategori bulunamadı: {category_name}")
else:
    certificates_to_add = [
        "Axtarış xilasetmə əməliyyatların koordinasiyası (IAMSAR)",
        "Beynəlxalq dəniz hüququ",
        "Gəmilərin Toqquşmasının Qarşısını Alınmasına dair Beynalxalq Qaydalar (Colreg-72)",
        "Gəminin dayanaqlığı",
        "Gəminin idarə edilməsi",
        "Naviqasiya təhlükələrin çəpərlənmə sistemi (IALA)",
        "Radar ARPA",
        "Səfərin planlaşdırılması- Dənizçilik astronomiyası",
        "Səfərin planlaşdırılması-Meteorologiya",
        "Səfərin planlaşdırılması - Naviqasiya",
        "Yük əməliyyatları",
        "İngilis dili (göyərtə heyəti üçün)",
        "Gəmi energetik qurğuları və onların istismarı",
        "Gəmi konstruksiyası və Gəmi dayanıqlılığı",
        "Gəmi köməkçi buxar qazanları",
        "Gəmi köməkçi mexanizmləri",
        "Gəmi soyuducu qurğuları",
        "İngilis dili (maşın heyəti üçün)",
        "MARPOL 73-78",
        "Yanğından mühafizə və xilasedici vasitələr",
        "Aşağı elektrik gərginliyi sistemləri",
        "Baş mühərriklərin və köməkçi mexanizmlərin avtomatik idarəetmə sistemlərinin işinə nəzarət",
        "Bütün gəmidaxili rabitə sistemlərinin istismarı",
        "Elektrik generatorlarının və paylayıcı sistemlərinin istismarı",
        "Elektrik sistemlərinin və avadanlıqlarının xüsusiyyətləri",
        "Elektrik və elektron avadanlıqlarının istismarı və texniki xidmətin göstərilməsi",
        "Elektrik və elektron avadanlığın istismarı",
        "Elektrik və elektron nəzarət avadanlıqlarının idarəedilməsi",
        "Gəmi elektrik avadanlıqlarının istismarı",
        "Gəmi mexaniki qurğularının iş prinsipinə dair anlayışlar"
    ]

    count = 0
    for cert_name in certificates_to_add:
        # Check if it already exists to prevent duplicates
        if not Certificate.objects.filter(category=category, name=cert_name).exists():
            Certificate.objects.create(category=category, name=cert_name, questions=[])
            count += 1
            
    print(f"Toplam {count} adet sertifika '{category_name}' kategorisine eklendi!")
