from django.db import models
from decimal import Decimal
from app_parceiros.models import Parceiro

class Cliente(models.Model):
    parceiro = models.ForeignKey(
        Parceiro,
        on_delete=models.CASCADE,
        related_name="clientes"
    )
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def margem(self):
        return self.salario * Decimal("0.35")

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
    
    def __str__(self):
        return self.nome.__str__()
