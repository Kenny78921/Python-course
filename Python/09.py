# Rutas
import os
ruta = os.chdir("C:\\Users\\ivans\\OneDrive\\Imágenes\\Escritorio\\General\\Universidad\\Cursos\\Curso Power BI")

archivo = open("Texto.txt", "w+")

archivo.write("Hola")

archivo = open("Texto.txt", "r")

texto = archivo.readline()
print(texto)

from pathlib import Path
carpeta = Path("C:\\Users\\ivans\\OneDrive\\Imágenes\\Escritorio\\General\\Universidad\\Cursos\\Curso Power BI")
archivo_1 = carpeta / "text.txt"

ruta = Path(Path.home(), "Paises", "Mexico", "Texto_M.txt")
archivo_abierto = open(ruta)
print(archivo_abierto.readline())

ruta = Path(Path.home(), "Paises", "USA", "Texto_U.txt")
archivo_abierto = open(ruta)
print(archivo_abierto.readline())

ruta = Path(Path.home(), "Paises", "USA", "Texto_U2.txt")
archivo_abierto = open(ruta)
print(archivo_abierto.readline())

ruta = Path(Path.home(), "Paises", "Canada", "Texto_C.txt")
archivo_abierto = open(ruta)
print(archivo_abierto.readline())