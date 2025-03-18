# Shutil y OS
from os import system
import os
import shutil
from pathlib import Path

system("cls")
# shutil.move("main.xlsx", Path.home())

ruta = "C:\\Users\\ivans\\OneDrive\\Imágenes\\Escritorio\\General\\Fotos"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")