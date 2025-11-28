from rest_framework import serializers
from .models import Simulacao

class SimulacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulacao
        fields = ['cliente', 'banco', 'prazo', 'margem_cliente', 'valor_liberado', 'parcela', 'comissao_parceiro_valor']