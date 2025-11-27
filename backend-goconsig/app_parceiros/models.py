from django.db import models

class Parceiro(models.Model):
    matricula = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
