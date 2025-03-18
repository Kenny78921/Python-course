# Generador
from os import system

system("cls")


def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 2)

    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 2


print(mi_funcion())

numero = mi_generador()

print(next(numero))
print(next(numero))
print(next(numero))


def perder_vida_generator(vidas_iniciales):
    vidas = vidas_iniciales
    while vidas > 0:
        yield f"Te quedan {vidas} vidas"
        vidas -= 1
    yield "Game Over"


perder_vida = perder_vida_generator(3)

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
