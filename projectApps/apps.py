from django.apps import AppConfig


class ProjectappsConfig(AppConfig):
    name = 'projectApps'

    def ready(self):
        import projectApps.signals
