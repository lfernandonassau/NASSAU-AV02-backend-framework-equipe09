from rest_framework import serializers
from .models import HistoricoSimulacao
from app_usuarios.models import Cliente
from app_emprestimos.models import Simulacao


class ClienteNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf']


class SimulacaoNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulacao
        fields = [
            'id', 'prazo', 'margem_cliente', 'valor_liberado', 'parcela', 'comissao_parceiro_valor', 'banco'
        ]


class HistoricoSimulacaoSerializer(serializers.ModelSerializer):
    cliente = ClienteNestedSerializer(read_only=True)
    simulacao = SimulacaoNestedSerializer(read_only=True)

    class Meta:
        model = HistoricoSimulacao
        fields = ['id', 'cliente', 'simulacao', 'data_registro']
        read_only_fields = fields

    def create(self, validated_data):
        raise serializers.ValidationError("Criação de histórico via API não permitida; este endpoint é apenas para leitura.")