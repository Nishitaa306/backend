# apps.py
from django.apps import AppConfig

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'  # Ensure this matches your app folder name

    def ready(self):
        import dashboard.signals  # Correct the import to 'dashboard.signals'
