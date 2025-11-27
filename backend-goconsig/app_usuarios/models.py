from django.db import models
from app_parceiros.models import Parceiros
from decimal import Decimal

class Cliente(models.Model):
    Parceiros = models.ForeignKey(Parceiros, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def margem(self):
        return self.salario * Decimal("0.35")
