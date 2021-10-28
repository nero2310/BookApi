from django.apps import AppConfig


class GoogleBookApiConfig(AppConfig):
    name = 'google_book_api'

    def ready(self):
        from . import signals