from django.apps import AppConfig
import sys

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Always attempt to ensure superuser exists on startup
        try:
            from django.core.management import call_command
            call_command('create_admin')
        except Exception as e:
            print("Auto create_admin failed:", e)
