import pandas as pd

datos_ventas = {
    'Producto' : ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audifonos'],
    'Cantidad' : [3, 10, 5, 2 , 8],
    'Precio' : [15000, 2500, 8000, 12000, 3000]
} 

df = pd.DataFrame(datos_ventas)
df.to_csv("ventas.csv", index=False)
print("Archivo ventas.csv creado correctamente.")

print("\n Para instalar las librerias necesarias ejecuta:")
print("pip install pandas openpyxl")

df_ventas = pd.read_csv("ventas.csv")

df_ventas['Total'] = df_ventas['Cantidad'] * df_ventas['Precio']
print("\n Datos con columna 'total':")
print(df_ventas)

df_filtrado = df_ventas[df_ventas['Total'] > 20000]
print("\n Productos con total mayor a $20000:")
print(df_filtrado)

df_filtrado.to_excel("reporte_ventas.xlsx", index=False)
print("\n Archivo 'reporte_ventas.xlsx' creado correctamente.")

print("\n RESUMEN FINAL:")
print(f"Total de productos: {len(df_ventas)}")
print(f"Productos con total > $20000: {len(df_filtrado)}")
print(f"Total en ventas: ${df_ventas['Total'].sum():,.0f}")

