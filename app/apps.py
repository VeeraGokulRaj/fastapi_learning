from django.apps import AppConfig


class fastapilearningConfig(AppConfig):
    name = "app"

    def ready(self):
        import app.domain.background_task  # noqa: F401
