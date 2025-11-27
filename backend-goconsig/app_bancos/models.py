from django.db import models

class Banco(models.Model):
    codigo_banco = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    fator = models.DecimalField(max_digits=10, decimal_places=6)
    comissao_parceiro = models.DecimalField(max_digits=5, decimal_places=4)
