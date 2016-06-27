from django.apps import AppConfig
from django.db.models.signals import post_save


class CustomAuthConfig(AppConfig):
    name = 'custom_auth'

    def ready(self):
        from custom_auth.models import CustomUser
        from custom_auth.signals import create_user
        post_save.connect(create_user, sender=CustomUser)
