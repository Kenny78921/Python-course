# POO
from os import system
system("cls")

class Pajaro:

    alas = True
    
    def __init__(self, raza, color, altura):
        self.raza = raza
        self.color =  color
        self.altura = altura

    def piar(self):
        print("Pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

    #$ Metodo de instancia
    def pintar_pajaro(self):
        self.color = "Negro"
        print("Ahora el color del pajaro es negro")

    #$ @Classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

    #$ @Staticmethod
    def mirar():
        print("El pajaron mira")

mi_pajaro = Pajaro("Canario","Amarillo", "19")
mi_pajaro.piar()
mi_pajaro.volar(50)
mi_pajaro.pintar_pajaro()
mi_pajaro.poner_huevos(2)
mi_pajaro.mirar()

print(mi_pajaro.color)
print(mi_pajaro.altura) 
