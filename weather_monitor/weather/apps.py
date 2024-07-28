from django.apps import AppConfig

class WeatherConfig(AppConfig):
    name = 'weather'

    def ready(self):
        from .tasks import start
        start()
