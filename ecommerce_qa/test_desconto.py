import pytest
from desconto import calcular_desconto


def test_compra_abaixo_de_100():
    assert calcular_desconto(99.99, "COMUM") == 0.0


def test_compra_exatamente_100():
    assert calcular_desconto(100, "COMUM") == 10.0


def test_compra_entre_100_e_500():
    assert calcular_desconto(300, "COMUM") == 30.0


def test_compra_exatamente_500():
    assert calcular_desconto(500, "COMUM") == 100.0


def test_compra_acima_de_500():
    assert calcular_desconto(1000, "COMUM") == 200.0


def test_vip_abaixo_de_100():
    assert calcular_desconto(50, "VIP") == 2.5


def test_vip_exatamente_100():
    assert calcular_desconto(100, "VIP") == 15.0


def test_vip_entre_100_e_500():
    assert calcular_desconto(300, "VIP") == 45.0


def test_vip_exatamente_500():
    assert calcular_desconto(500, "VIP") == 125.0


def test_vip_acima_de_500():
    assert calcular_desconto(1000, "VIP") == 200.0


def test_vip_minusculo():
    assert calcular_desconto(300, "vip") == 45.0


def test_vip_misto():
    assert calcular_desconto(300, "Vip") == 45.0


def test_cliente_comum():
    assert calcular_desconto(300, "COMUM") == 30.0


def test_teto_de_200():
    assert calcular_desconto(2000, "COMUM") == 200.0


def test_desconto_exatamente_200():
    assert calcular_desconto(1000, "COMUM") == 200.0


def test_valor_zero():
    assert calcular_desconto(0, "COMUM") == 0.0


def test_valor_negativo():
    assert calcular_desconto(-100, "COMUM") == 0.0


def test_valor_como_texto():
    assert calcular_desconto("500", "COMUM") == 0.0


def test_valor_none():
    assert calcular_desconto(None, "COMUM") == 0.0


def test_cliente_none():
    assert calcular_desconto(300, None) == 30.0


def test_cliente_desconhecido():
    assert calcular_desconto(300, "OUTRO") == 30.0


def test_valor_decimal():
    assert calcular_desconto(199.99, "COMUM") == 20.0