from os import system
import re
system("cls")

texto = "Hola a todos los que estan leyendo esto, mi numero es 55-2562-8308"

#search()
#findall()
patron = r"\d\d\D\d\d\d\d\D\d\d\d\d"

resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())

#$ Combinacion para separar los numeros
numero = [int(digit) for digit in resultado.group() if digit.isdigit()]
print(numero)

buscar = re.search("todos", texto)
print(buscar.span())

resultado_2 = re.findall(r"\d", texto)
print(resultado_2)
