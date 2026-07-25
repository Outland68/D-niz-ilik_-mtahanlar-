from django.apps import AppConfig
import sys

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Only run during server start (not during manage.py commands like migrate/makemigrations)
        if 'runserver' in sys.argv or 'gunicorn' in sys.argv or 'wsgi' in sys.argv or 'uvicorn' in sys.argv:
            try:
                from django.core.management import call_command
                call_command('create_admin')
            except Exception as e:
                print("Auto create_admin failed:", e)
