# Herencia
from os import system

system("cls")


# $ Clases padres
class Padre:
    def hablar(self):
        print("Hola")


class Madre:
    def reir(self):
        print("jajaja")


# $ Clase hijo
class Hijo(Padre, Madre):
    pass


# $ Clase nieto
class Nieto(Hijo):
    pass


nieto = Nieto()
nieto.hablar()
