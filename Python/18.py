# Decoradores
from os import system
import time
system("cls")

def calcular_tiempo(funcion):

    def funcion_decoradora(x):

        inicio = time.time()
        funcion(x)
        fin = time.time()
        print(f"La función tomó {fin - inicio} segundos.")

    return funcion_decoradora

@calcular_tiempo
def imprimir_numeros(n):
    for x in range(n):
        print(x)

imprimir_numeros(100000)