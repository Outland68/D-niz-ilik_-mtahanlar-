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

        # Fix Certificate json_file mappings in database if needed
        try:
            from .models import Certificate
            cert = Certificate.objects.filter(name__icontains='Gəmi sürücülərinin təkmilləşdirilməsi (idarəetmə)').first()
            if cert and cert.json_file != 'xususi/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_id.json':
                cert.json_file = 'xususi/g_mi_s_r_c_l_rinin_t_kmill_dirilm_si_id.json'
                cert.save()
                print("✅ Auto-corrected Certificate 5513 json_file mapping to idare.json!")
        except Exception as err:
            print("Auto cert sync failed:", err)

