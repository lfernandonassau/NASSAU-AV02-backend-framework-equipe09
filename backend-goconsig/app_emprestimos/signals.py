from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Simulacao
from app_historico.models import HistoricoSimulacao


@receiver(post_save, sender=Simulacao)
def criar_historico_para_simulacao(sender, instance: Simulacao, created, **kwargs):
    """Cria um registro de HistoricoSimulacao quando uma Simulacao é criada.

    Para satisfazer as constraints NOT NULL do modelo de histórico, 
    copiamos os campos da simulação no momento da criação.
    A representação REST evita duplicação expondo dados via nested serializers.
    """
    if created:
        HistoricoSimulacao.objects.create(
            cliente=instance.cliente,
            simulacao=instance,
            # copiar campos exigidos (NOT NULL)
            prazo=instance.prazo,
            margem_cliente=instance.margem_cliente,
            valor_liberado=instance.valor_liberado,
            parcela=instance.parcela,
            comissao_parceiro_valor=instance.comissao_parceiro_valor,
            # opcional: se desejar manter banco/parceiro, descomente conforme necessidade
            # banco=instance.banco,
            # parceiro=getattr(instance.cliente, 'parceiro', None),
        )
