import pytest

from area.area import calcular_area_de_um_cubo, calcular_area_de_uma_piramide
from utils.utils import ler_csv


# 2.2 - Criar 2 testes de unidade simples  (um positivo e um negativo) baseados em valores fixos para a função de cálculo da área do cubo
def test_positivo_calcular_area_de_um_cubo():
    num1 = 3
    resultado_esperado = 27
    resultado_obtido = calcular_area_de_um_cubo(num1)

    assert resultado_esperado == resultado_obtido

def test_negativo_calcular_area_de_um_cubo_():
    num1 = 3
    resultado_esperado = 29
    resultado_obtido = calcular_area_de_um_cubo(num1)

    assert resultado_esperado == resultado_obtido

# 2.3 - Criar um teste de unidade com um arquivo CSV de pelo menos 3 valores como massa de teste, 
#       sendo pelo menos 1 teste positivo e 2 testes negativos, para a função de cálculo da área da pirâmide
@pytest.mark.parametrize('base, altura, resultado_esperado',
                            ler_csv('./fixtures/massa_area_piramide.csv')
                        )
def test_calcular_area_de_uma_piramide_csv(base, altura, resultado_esperado):

    resultado_obtido = calcular_area_de_uma_piramide(float(base), float(altura))

    assert float(resultado_esperado) == resultado_obtido