from django.apps import AppConfig
from django.db.models.signals import post_save


class CustomAuthConfig(AppConfig):
    name = 'custom_auth'
