# Proyecto 8
import P08_1
import time
from os import system

system("cls")

variable_while = 0
a = P08_1.generador_turno("perfumeria")
b = P08_1.generador_turno("Farmacia")
c = P08_1.generador_turno("Cosmética")

def funcion_area(area):
    if area == "1":
        system("cls")
        turno_perfumes = next(a)
        print(f"{turno_perfumes}-Perfumería")
        
    elif area == "2":
        system("cls")
        turno_farmacia = next(b)
        print(f"{turno_farmacia}-Farmacia")

    elif area == "3":
        system("cls")
        turno_cosmetica = next(c)
        print(f"{turno_cosmetica}-Cosmética")

    elif area == "#":
        system("cls")
        print("Hasta la proxima")
        time.sleep(2)
        variable_while = 1
        return variable_while

    else:
        system("cls")
        print("Ingrese un valor valido")
        time.sleep(2)
        system("cls")
    
    if area != "#":
        variable_while = 0
        
    return variable_while

while variable_while == 0:
    variable_while = funcion_area(input("¿A donde desea ir?\n1. Perfumería\n2. Farmacia\n3. Cosmética\n#. Finalizar\n\n"))

