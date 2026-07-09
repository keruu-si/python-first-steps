with open("notas.txt", "w") as archivo:
    archivo.write("holaaai, welcome to wild rift:\n")
    archivo.write("python es un lenguaje de programacion muy bueno\n")

with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

    with open("notas.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())