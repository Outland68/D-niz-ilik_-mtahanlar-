from rest_framework import serializers
from .models import Category, Certificate, QuestionReport


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


class QuestionReportSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = QuestionReport
        fields = [
            'id', 'user', 'username', 'user_email', 'certificate_id', 
            'certificate_name', 'question_id', 'question_text', 
            'report_reason', 'status', 'created_at'
        ]
        read_only_fields = ['id', 'user', 'created_at']

