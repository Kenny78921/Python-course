# Shutil y OS
from os import system
from datetime import datetime
from datetime import date
import datetime

import time

system("cls")

mi_hora = datetime.time(17,35,23)

mi_dia = datetime.date(2025,10,18)

nacimiento = date(1998, 8, 19)
vida = datetime.date.today() - nacimiento

print(mi_hora.hour)
print(mi_dia.day)

print(vida.days)

inicio_temporizador = time.time()
time.sleep(2)
fin_temporizador = time.time()
duracion = inicio_temporizador - fin_temporizador
print(duracion)