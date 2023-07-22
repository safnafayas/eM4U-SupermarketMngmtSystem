from django.apps import AppConfig
# from django.contrib.admin.apps import AdminConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

# class CustomAdminConfig(AdminConfig):
#     default_site = 'core.admin.CustomAdminSite'