from django.db import models

class Parceiro(models.Model):
    matricula = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True, null=False, blank=True)
    endereco = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"