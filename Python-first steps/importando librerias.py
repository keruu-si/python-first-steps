import os
print(os.getcwd())
archivos = os.listdir(".")
print(archivos)
os.makedirs("nueva_carpeta", exist_ok=True)
import shutil
shutil.copy("notas.txt", "nueva_carpeta/notas_copia.txt")
shutil.move("nueva_carpeta/notas_copia.txt", "notas_copias.txt")
