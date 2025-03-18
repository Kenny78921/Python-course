# zip
from os import system
import zipfile
from pathlib import Path

system("cls")

ruta = Path(Path.home(), "Carpeta_aux")
ruta_z = Path(Path.home(), "Carpeta_aux", "Archivo.zip")
ruta_a = Path(Path.home(), "Carpeta_aux", "a.txt")
ruta_b = Path(Path.home(), "Carpeta_aux", "b.txt")
print(ruta)

mi_zip = zipfile.ZipFile(ruta_z,"w")

mi_zip.write(ruta_a, arcname="a.txt")
mi_zip.write(ruta_b, arcname="b.txt")

mi_zip.close()