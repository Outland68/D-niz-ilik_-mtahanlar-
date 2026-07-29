from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    category = models.ForeignKey(Category, related_name='certificates', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    json_file = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

# Model to enforce Single Device Login (Only 1 active session per user)
class UserSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='active_session')
    session_key = models.CharField(max_length=255, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session for {self.user.username}"

class QuestionReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    certificate_id = models.IntegerField()
    certificate_name = models.CharField(max_length=255)
    question_id = models.CharField(max_length=50)
    question_text = models.TextField()
    report_reason = models.TextField()
    status = models.CharField(max_length=20, default='pending') # pending, resolved, dismissed
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Report by {self.user.username if self.user else 'Guest'} on {self.certificate_name} (Sual: {self.question_id})"
