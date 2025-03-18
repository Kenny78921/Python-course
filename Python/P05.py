# Proyecto 5
import random

from os import system
system("cls")

#2 Declaracion de variables globales
vidas = 5

#2 Selección de palabra
#lista_de_palabras = ["manzana", "banana", "cereza", "uva", "fresa", "mango", "naranja", "pera", "piña", "sandia", "melon", "frambuesa", "mora", "arándano", "aguacate", "coco", "higo", "lima", "limon", "mandarina", "maracuya", "papaya", "platano", "granada", "pomelo", "toronja", "nispero", "ciruela", "durazno", "albaricoque", "nectarina", "zarzamora", "guanabana", "tamarindo", "litchi", "kiwi", "papaya", "platano"]
lista_de_palabras = ["lulu", "nami", "soraka", "janna", "yuumi", "sona", "milio"]
palabra_elegida = list(random.choice(lista_de_palabras))
#1 Funcion para cambiar letras por "_"
def función_conversion(palabra_elegida):
    palabra_convertida = palabra_elegida[:]

    for num in range(len(palabra_convertida)):
        palabra_convertida[num] = "_"

    return palabra_convertida


#1 Funcion para verificar si la letra esta dentro de la lista
def funcion_verificacion(letra_seleccionada, palabra_elegida, palabra_convertida):
    if  letra_seleccionada_l == palabra_elegida:
        for i in range(len(palabra_elegida)):
            palabra_convertida[i] = letra_seleccionada_l[i]
    else:
        if palabra_elegida.count(letra_seleccionada) == 0:
            print(f" \nLa letra: '{letra_seleccionada}', no se encuentra en la palabra")

        elif palabra_elegida.count(letra_seleccionada) == 1:
            print(f" \nLa letra: '{letra_seleccionada}', se encuentra {palabra_elegida.count(letra_seleccionada)} vez en la palabra")
            for i in range(len(palabra_elegida)):
                if palabra_elegida[i] == letra_seleccionada_l[0]:
                    palabra_convertida[i] = letra_seleccionada_l[0]

        elif palabra_elegida.count(letra_seleccionada) > 1:
            print(f" \nLa letra: '{letra_seleccionada}', se encuentra {palabra_elegida.count(letra_seleccionada)} veces en la palabra")
            for i in range(len(palabra_elegida)):
                if palabra_elegida[i] == letra_seleccionada_l[0]:
                    palabra_convertida[i] = letra_seleccionada_l[0]

    print(f" \n{palabra_convertida}\n")
    return palabra_convertida

#1 Funcion para verificar las vidas
def funcion_vidas(vidas,palabra_convertida, palabra_convertida_p):
    if palabra_convertida == palabra_convertida_p:
        vidas-=1
    else:
        vidas = vidas
    return vidas

#3 Inicio programa
palabra_convertida = función_conversion(palabra_elegida)
print(f"\n{palabra_convertida}")

while vidas > 0:
    letra_seleccionada = input(f"Vidas restantes: {vidas}, ingresa una letra: ")
    system("cls")
    letra_seleccionada = letra_seleccionada.lower()
    letra_seleccionada_l = list(letra_seleccionada.lower())
    palabra_convertida_p = palabra_convertida[:]
    palabra_convertida = funcion_verificacion(letra_seleccionada, palabra_elegida, palabra_convertida)
    if "_" in palabra_convertida:
        vidas = funcion_vidas(vidas, palabra_convertida, palabra_convertida_p)
    else:
        print("Has ganado\n\n")
        vidas = -1
        
if vidas == 0:
    system("cls")
    print("Tremendo pete, has perdido\n\n")