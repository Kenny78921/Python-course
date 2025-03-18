# Proyecto 4
from os import system
from random import *

system("cls")

print('A ver, ' + input('¿Cual es tu nombre?: ') + ' he pensado un número entre 1 y 100, y tienes solo 6 intentos para adivinar cuál crees que es el número')
numero_elegido = 2 #randint(1,100)
i = 0
lista_numeros = []

variable = 0

while i < 6 and i >= 0:

    Numero_pensado = input(f"Es tu intento numero {i} de adivinar, elige sabiamente: ")
    Numero_pensado = int(Numero_pensado)
    system("cls")

    if Numero_pensado < 1 or Numero_pensado > 100:
        print("\nHas elegido un número que no está permitido.\n")
    elif Numero_pensado < numero_elegido:
        print("\nElegiste un numero más bajo que el pensado.\n")
    elif Numero_pensado > numero_elegido:
        print("\nElegiste un numero más alto que el pensado.\n")
    else:
        print("Adivinaste el número.\n")
        i = -5
        print(lista_numeros)
        
    if i != -5:
        #2 Agregar una lista para identificar la posicion del numero
        lista_numeros.append(numero_elegido)
        lista_numeros.append(Numero_pensado)
        
        for j in range(len(lista_numeros) - 1):
            if lista_numeros[j] == "x":
                num = j
                lista_numeros.pop(num)

        lista_numeros.sort()

        for k in range(len(lista_numeros)):
            if lista_numeros[k] == numero_elegido:
                lista_numeros[k] = "x"

        print(f"{lista_numeros}\n")    
        i+=1

if i >= 5:
    system("cls")
    print(lista_numeros)
    print(f"\nEl número era {numero_elegido}\n")   