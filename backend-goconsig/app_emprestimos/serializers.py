from rest_framework import serializers
from decimal import Decimal
from app_emprestimos.models import Simulacao
from app_emprestimos.services import calcular_simulacao


class SimulacaoSerializer(serializers.ModelSerializer):
    parcela = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Simulacao
        fields = [
            "id",
            "cliente",
            "banco",
            "prazo",
            "margem_cliente",
            "valor_liberado",
            "parcela",
            "comissao_parceiro_valor",
        ]
        read_only_fields = [
            "prazo",
            "margem_cliente",
            "valor_liberado",
            "comissao_parceiro_valor",
        ]

    def create(self, validated_data):
        cliente = validated_data["cliente"]
        banco = validated_data["banco"]

        parcela = validated_data.get("parcela")
        parcela = Decimal(parcela) if parcela else None

        dados = calcular_simulacao(cliente, banco, parcela)

        validated_data.update(dados)
        return super().create(validated_data)
