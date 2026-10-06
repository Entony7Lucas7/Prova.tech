def calcular_desconto(valor_compra, tipo_cliente):
    if not isinstance(valor_compra, (int, float)) or valor_compra <= 0:
        return 0.0

    desconto = 0

    if 100 <= valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20

    if isinstance(tipo_cliente, str) and tipo_cliente.strip().upper() == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

    if valor_desconto > 200:
        valor_desconto = 200.0

    return round(valor_desconto, 2)
