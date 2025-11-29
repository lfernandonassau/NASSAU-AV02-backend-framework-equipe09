from django.db import models
from app_usuarios.models import Cliente
from app_bancos.models import Banco

class Simulacao(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="simulacoes"
    )
    banco = models.ForeignKey(
        Banco,
        on_delete=models.CASCADE,
        related_name="simulacoes"
    )

    prazo = models.IntegerField(default=96)

    margem_cliente = models.DecimalField(max_digits=10, decimal_places=2)
    valor_liberado = models.DecimalField(max_digits=12, decimal_places=2)
    parcela = models.DecimalField(max_digits=10, decimal_places=2)
    comissao_parceiro_valor = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Simulação {self.id} - {self.cliente.nome}"



