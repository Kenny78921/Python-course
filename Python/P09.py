# P09
from os import system
import zipfile
from pathlib import Path
import re
import os
import pandas as pd
import time
import math
from datetime import datetime

system("cls")

ruta_dir = Path("C:\\Users\\ivans\\Downloads\\Carpeta_P09\\Mi_Gran_Directorio")
ruta_aux = Path("C:\\Users\\ivans\\Downloads\\Carpeta_P09\\Mi_Gran_Directorio\\Directorio_1\\Directorio_1A\\archivo3.txt")

# Leer instrucciones
"""ruta_descarga = Path("C:\\Users\\ivans\\Downloads\\Proyecto+Dia+9.zip")
ruta_carpeta = Path("C:\\Users\\ivans\\Downloads\\Carpeta_P09")
ruta_archivo = Path("C:\\Users\\ivans\\Downloads\\Carpeta_P09\\Instrucciones.txt")

if ruta_descarga.exists():
    print("Existe")
    if ruta_carpeta.exists():
        mi_zip = zipfile.ZipFile(ruta_descarga,"r")
        mi_zip.extractall(ruta_carpeta)
        mi_archivo_instrucciones = open(ruta_archivo, "r", encoding='utf-8')
        for x in mi_archivo_instrucciones:
            if x != "\n" :
                print(x)

            
    else:
        ruta_carpeta.mkdir()

else:
    print("No ta")"""
arch = []
num = []
total = 0
tiempo = 0
tiempo_i = time.time()


fecha = datetime.today().date()
fecha_arreglada = fecha.strftime("%d-%m-%Y")

for carpeta,subcarpetas,archivos in os.walk(ruta_dir):
    for x in archivos:
        if x.endswith(".txt"):
            ruta_archivo = Path(carpeta, x)
            archivo = open(ruta_archivo,"r",  encoding='utf-8')
            resultado = re.search(r"N\D{3}.\d{5}", archivo.readline())
            if resultado:
                arch.append(x)
                num.append(resultado.group())
                total +=1
tiempo_f = time.time()

tiempo = math.ceil(tiempo_f - tiempo_i)

print(f"Fecha de búsqueda: {fecha_arreglada}\n")

datos = {
    "Archivo": arch,
    "# Serie": num,
        }

df = pd.DataFrame(datos)
print(df)

print(f"\nNúmeros encontrados: {total}\nDuración de la búsqueda: {tiempo} segundos\n")
