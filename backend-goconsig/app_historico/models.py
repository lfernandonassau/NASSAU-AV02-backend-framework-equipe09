from django.db import models

from django.db import models

class HistoricoSimulacao(models.Model):
    cliente = models.ForeignKey(
        "app_usuarios.Cliente",
        on_delete=models.CASCADE,
        related_name="historicos"
    )

    Parceiros = models.ForeignKey(
        "app_parceiros.Parceiros",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historicos"
    )

    banco = models.ForeignKey(
        "app_bancos.Banco",
        on_delete=models.SET_NULL,
        null=True,
        related_name="historicos"
    )

    # valores congelados da simulação
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    margem = models.DecimalField(max_digits=10, decimal_places=2)
    fator_banco = models.DecimalField(max_digits=10, decimal_places=6)
    valor_liberado = models.DecimalField(max_digits=12, decimal_places=2)
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    prazo = models.IntegerField()

    # comissão
    percentual_comissao = models.DecimalField(max_digits=5, decimal_places=2)
    valor_comissao = models.DecimalField(max_digits=10, decimal_places=2)

    # controle
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Simulação {self.id} - {self.cliente.nome} - {self.banco.nome}"
