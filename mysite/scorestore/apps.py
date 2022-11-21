from django.apps import AppConfig

# Регистрация приложения Scorestore
class ScorestoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scorestore'
    verbose_name = 'Магазин за очки'
