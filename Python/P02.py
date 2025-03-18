# Proyecto 2
from os import system
system("cls")

Nombre = input("¿Cual es tu nombre?: ")
Dinero = input("¿cuanto has vendido en este mes?: ")
Comision = int(Dinero) + int(Dinero)*0.13

print(f"Hola {Nombre}, tu comisión es: {Comision} pesos")