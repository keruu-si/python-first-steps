productos = {"manzana": 2000, "pan": 3500, "leche": 4200}

def mostrar_menu(productos):
    print("--- MENÚ DE PRODUCTOS ---")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")
    print("-------------------------")

mostrar_menu(productos)

producto_buscado = input("Escribe el nombre de un producto: ")

if producto_buscado in productos:
    print(f"El {producto_buscado} cuesta ${productos[producto_buscado]}")
else:
    print("Ese producto no está en el menú")