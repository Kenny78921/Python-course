# Collections
from collections import Counter
from collections import defaultdict
from collections import namedtuple

from os import system

system("cls")

numeros = [8,6,9,5,4,5,5,5,5,8,7,4]
frase = "AA BB CC AA CC"
print(Counter(numeros))
print(Counter("Astronautas"))
print(Counter(frase.split()))

mi_diccionario = {"uno": "verde", "dos": "azul", "tres": "amarillo"}
mi_diccionario = defaultdict(lambda: "No hay pana") 
print(mi_diccionario["cuatro"])

mi_tupla = namedtuple("Persona", ["Nombre", "Edad", "Altura"])
datos = mi_tupla("Aldo", 24, 1.72)
print(datos.Nombre)