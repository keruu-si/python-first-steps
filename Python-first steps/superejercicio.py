
import os


os.makedirs("mis_archivos", exist_ok=True)

with open("mis_archivos/archivo1.txt", "w") as f:
    f.write("hola que tal pipoooooooooool")

with open("mis_archivos/archivo2.txt", "w") as f:
        f.write("hoy extraño mucho a Karen")

with open("mis_archivos/archivo3.txt", "w") as f:
      f.write("bueno, realmente extraño a Karen porque la quiero muchi")

archivos = os.listdir("mis_archivos")
print("archivos en la carpeta:")
for archivo in archivos:
      print(f"- {archivo}")

print(f"\nTotal de archivos: {len(archivos)}")