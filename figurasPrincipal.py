import pandas as pd
import math
from funciones import triangulo, rectangulo, circulo

dataFile = pd.read_csv("figuras.csv")

print("Procesando figuras ...\n")

areas = []
perimetros = []

for index, row in dataFile.iterrows():

    if row['FIGURA'] == 't':
        print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
        area = triangulo(row['MEDIDA1'],row['MEDIDA2'])
    elif row['FIGURA'] == 'r':
        print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
        area = rectangulo(row['MEDIDA1'],row['MEDIDA2'])
    elif row['FIGURA'] == 'c':
        print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
        area = circulo(row['MEDIDA1'], row['MEDIDA2'])

            

       
