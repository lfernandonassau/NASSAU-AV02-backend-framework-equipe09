from django.db import models
from app_usuarios.models import Cliente
from app_bancos.models import Banco
from app_parceiros.models import Parceiro
from app_emprestimos.models import Simulacao


class HistoricoSimulacao(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="historicos"
    )

    parceiro = models.ForeignKey(
        Parceiro,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historicos"
    )

    banco = models.ForeignKey(
        Banco,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historicos"
    )

    simulacao = models.ForeignKey(
        Simulacao,
        on_delete=models.CASCADE,
        related_name="historico_registros",
        null=True,
        blank=True
    )

    # Dados copiados da simulação
    prazo = models.IntegerField()
    margem_cliente = models.DecimalField(max_digits=10, decimal_places=2)
    valor_liberado = models.DecimalField(max_digits=12, decimal_places=2)
    parcela = models.DecimalField(max_digits=10, decimal_places=2)
    comissao_parceiro_valor = models.DecimalField(max_digits=12, decimal_places=2)

    # Controle
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Histórico - Cliente: {self.cliente.nome} - {self.data_registro}"

    
    
