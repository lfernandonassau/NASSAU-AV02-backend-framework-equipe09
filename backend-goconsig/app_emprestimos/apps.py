from django.apps import AppConfig


class EmprestimosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_emprestimos'

    def ready(self):
        # Importa os signals para conectar handlers post_save
        from . import signals  # noqa: F401
