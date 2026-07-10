import csv

with open('ventasu.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Producto", "Cantidad", "Precio"])
        escritor.writerow(["Manzanas", 10, 2000])
        escritor.writerow(["Pan", 5, 3500])
        escritor.writerow(["Leche", 8, 4200])

with open("ventasu.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["Producto"], fila["Cantidad"], fila["Precio"])

import pandas as pd
datos = pd.read_csv("ventasu.csv")
print(datos)
print(datos["Producto"])
filtrado = datos[datos["Cantidad"] > 5]
print(filtrado)
datos ["total"] = datos["Cantidad"] * datos["Precio"]
print(datos)
datos.to_excel("ventas_procesadas.xlsx", index=False)
