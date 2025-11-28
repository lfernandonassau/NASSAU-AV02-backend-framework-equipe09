from decimal import Decimal, ROUND_HALF_UP


def calcular_simulacao(cliente, banco, parcela_desejada=None):
    # 1) Margem do cliente (35% do salário)
    margem_cliente = (cliente.salario * Decimal("0.35")).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    # 2) Se não mandar parcela → usa margem total
    parcela = parcela_desejada or margem_cliente

    # Parcela mínima é 50 reais
    if parcela < Decimal("50.00"):
        parcela = Decimal("50.00")

    # Parcela não pode ultrapassar a margem
    if parcela > margem_cliente:
        parcela = margem_cliente

    # 3) Dados do banco
    fator = banco.fator
    comissao = banco.comissao_parceiro

    # 4) Valor liberado
    valor_liberado = (parcela / fator).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    # 5) Comissão para o parceiro
    comissao_valor = (valor_liberado * comissao).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    return {
        "prazo": 96,
        "margem_cliente": margem_cliente,
        "valor_liberado": valor_liberado,
        "parcela": parcela,
        "comissao_parceiro_valor": comissao_valor,
    }
