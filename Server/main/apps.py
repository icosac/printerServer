from django.apps import AppConfig

class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        with open("lock", "w") as f:
            f.write("a")
            f.close
