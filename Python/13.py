# Polimorfismo
from os import system

system("cls")


class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice MUUU")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Dice BEEE")


vaca_1 = Vaca("Aurota")
oveja_1 = Oveja("Nube")

animales = [vaca_1, oveja_1]


def animal_hablar(animal):
    animal.hablar()


for animal in animales:
    animal_hablar(animal)
