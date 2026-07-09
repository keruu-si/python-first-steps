try:
    numero = int(input("Ingresa un número para dividir 100: "))
    resultado = 100 / numero
    print(f"100 dividido entre {numero} es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except ValueError:
    print("Error: Debes ingresar un número válido")
    