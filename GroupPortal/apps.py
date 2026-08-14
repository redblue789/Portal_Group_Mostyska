from django.apps import AppConfig


class GroupportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GroupPortal'

    def ready(self):
        import GroupPortal.signals
