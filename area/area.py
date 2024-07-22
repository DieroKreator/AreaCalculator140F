import math

# 2.1 - Criar 3 funções para serem alvo dos testes de unidade.
def calcular_area_de_um_cubo(num1):
    areaCubo = num1 ** 3
    return areaCubo

def calcular_area_de_um_paralelogramo(base, altura):
    areaParalelogramo = base * altura
    return areaParalelogramo

def calcular_area_de_uma_piramide(base, altura):
    m = base / 2

    apotema = math.sqrt((base / 2) ** 2 + altura ** 2)

    area_face_lateral = (apotema * base) / 2

    at_faces_laterais = 4 * area_face_lateral

    area_base_piramide = base ** 2

    area_total_piramide = at_faces_laterais + area_base_piramide 
    
    return area_total_piramide