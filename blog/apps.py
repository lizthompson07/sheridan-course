"""App configuration"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """defaults for app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
