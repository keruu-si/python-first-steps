gastos = []

def agregar_gasto(gastos, descripcion, monto):
    gastos.append({"descripcion": descripcion, "monto": monto})

def mostrar_gastos(gastos):
    if not gastos:
        print("no hay gastos registrados.")
    else: 
        for i, gasto in enumerate(gastos, 1):
            print(f"{i}. {gasto['descripcion']} - ${gasto['monto']:.2f}")

def calcular_total(gastos):
    total = 0 
    for gasto in gastos:
        total += gasto['monto']
    return total

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar gasto")
    print("2. Ver todos los gastos")
    print("3. Ver total gastado")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        descripcion = input("Descripcion del gasto: ")
        while True:
            try:
                monto = float(input("Monto del gasto: "))
                if monto < 0:
                    print("El monto no puede ser negativo. Intente nuevamente.")
                    continue
                agregar_gasto(gastos, descripcion, monto)
                print(f"gasto '{descripcion}' agregado correctamente.")
                break
            except ValueError:
                print("Error: Debes ingresar un numero valido para el monto.")
    elif opcion == "2":
        mostrar_gastos(gastos)
    elif opcion == "3":
        total = calcular_total(gastos)
        print(f"Total gastado: ${total:.2f}")
    elif opcion == "4":
        print("hasta luego!")
        break
    else:
        print("Opcion no valida")
