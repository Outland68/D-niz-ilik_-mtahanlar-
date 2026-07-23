from rest_framework import serializers
from .models import Category, Certificate


class CertificateListSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = ['id', 'name', 'json_file', 'question_count']

    def get_question_count(self, obj):
        # Count from JSON file if it exists
        if obj.json_file:
            import json
            from django.conf import settings
            path = settings.QUESTIONS_DIR / obj.json_file
            try:
                with open(path, encoding='utf-8') as f:
                    data = json.load(f)
                return len(data.get('questions', []))
            except Exception:
                return 0
        return 0


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon_name', 'color']
