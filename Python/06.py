# Rango

for valor in range(1, 5, 1):
    print(valor)

variable_1 = list(range(0, 5, 1))
print(variable_1)


# Enumerate
for indice, numero in enumerate(["a", "b", "c"]):
    print(indice, numero)


variable_1 = list(enumerate("Holi"))
print(variable_1)
# [(0, 'H'), (1, 'o'), (2, 'l'), (3, 'i')]


# Zip
lista_1 = ["a", "b", "c", "d"]
lista_2 = ["10", "100", "1000"]

for a, b in zip(lista_1, lista_2):
    print(f"Lista 1: {a} y Lista 2: {b}")
# Lista 1: a y Lista 2: 10
# Lista 1: b y Lista 2: 100
# Lista 1: c y Lista 2: 1000


# Min y Max
lista_1 = [10, 2000, 100, 1000, 50]
lista_2 = ["z", "b", "a", "f", "h"]

print(max(lista_1))
# 2000

print(min(lista_2))
# a


# Random
from random import *

valor_1 = randint(1, 10)
print(valor_1)
# 5

valor_2 = random()
print(valor_2)
# 0.91

valor_3 = choice(lista_2)
print(valor_3)
# b

shuffle(lista_2)
print(lista_2)
# ['h', 'b', 'a', 'f', 'z']


# Random
lista_4 = [n if n * 2 > 10 else "no" for n in range(0, 10, 2)]
print(lista_4)
# ['no', 'no', 'no', 6, 8]
