# Herencia
from os import system

class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("He nacido")

class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self,metros):
        print(f"El pajaro volo {metros} metros")

system("cls")

piolin = Pajaro(2, "Blanco")

print(piolin.color)