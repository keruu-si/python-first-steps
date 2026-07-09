try: 
    numero = int(input("dame un numero: "))
    resultado = 10 / numero
    print(f"el resultado es: {resultado}")
except ValueError:
    print("por favor, introduce un numero valido")
except ZeroDivisionError:
    print("no se puede dividir entre cero")