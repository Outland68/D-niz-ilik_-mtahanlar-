# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from api.models import Category, Certificate

# Clear existing to prevent duplicates
Category.objects.all().delete()

# Create Categories
c1 = Category.objects.create(name='Sıravi heyət hazırlığı üzrə', icon_name='Anchor', color='bg-blue-500/20 text-blue-400')
c2 = Category.objects.create(name='Xüsusi hazırlıq şəhadətnamələri üzrə', icon_name='FileBadge', color='bg-emerald-500/20 text-emerald-400')
c3 = Category.objects.create(name='Sertifikat diplom üzrə', icon_name='Award', color='bg-amber-500/20 text-amber-400')

# Dummy certificate with questions based on user's exact JSON layout
Certificate.objects.create(category=c1, name='Təməl Dənizçilik Sertifikatı', questions=[
    {
        "id": "q001",
        "category": "denizcilik-hukuku",
        "question": "Gəminin ön hissəsi necə adlanır?",
        "options": {
            "A": "Burun",
            "B": "Kıç",
            "C": "Gövdə",
            "D": "Lövbər"
        },
        "correct_answer": "A",
        "explanation": "Gəminin ön tərəfi Burun adlanır."
    }
])

print("Database seeded successfully with UTF-8 characters!")
