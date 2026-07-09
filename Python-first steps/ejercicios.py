edad = int(input("¿cuantos años tienes?"))

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13 and edad < 18:
    print("Eres adolescente")
else:
    print("Eres menor")