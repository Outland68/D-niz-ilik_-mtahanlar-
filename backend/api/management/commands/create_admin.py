import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates an initial Superuser for production automatically if not exists'

    def handle(self, *args, **options):
        username = os.environ.get('SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('SUPERUSER_EMAIL', 'admin@denizcilik.com')
        password = os.environ.get('SUPERUSER_PASSWORD', 'Admin123456!')

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' successfully created!"))
        else:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' updated with new password!"))
