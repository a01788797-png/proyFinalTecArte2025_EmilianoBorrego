import math
def triangulo(MEDIDA1, MEDIDA2):
    MEDIDA1 = float(MEDIDA1)
    MEDIDA2 = float(MEDIDA2)
    area = (MEDIDA1 * MEDIDA2) / 2
    print(area)
def rectangulo(MEDIDA1, MEDIDA2):
    MEDIDA1 = float(MEDIDA1)
    MEDIDA2 = float(MEDIDA2)
    area = MEDIDA1 * MEDIDA2
    print(area)
def circulo(MEDIDA1, MEDIDA2):
    MEDIDA1 = float(MEDIDA1)
    area = (math.pi * MEDIDA1) ** 2
    print(area)
