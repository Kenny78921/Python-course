# Proyecto 3
from os import system
system("cls")

texto = input("Ingrese un texto: ")
letras = input("Ingrese 3 letras: ")

texto = texto.lower()
letras = letras.lower()

# Ver cuantas veces esta la letra en el texto
resultado_l1 = texto.count(list(letras)[0])
resultado_l2 = texto.count(list(letras)[1])
resultado_l3 = texto.count(list(letras)[2])

# Ver cuantas palabras hay en el texto
resultado_l4 = len(texto.split())

# Ver primera y ultima letra
resultado_l5 = texto[0]
resultado_l6 = texto[-1]

# Invertir texto
resultado_l7 = texto[::-1]

# Verificar la palabra python
resultado_l8 = texto.find("Python")
resultado_l8 = texto.find("python")



if resultado_l8 == -1:
    resultado_l8 = "No esta"
else:
    resultado_l8 = "Si esta"

print(resultado_l1)
print(resultado_l2)
print(resultado_l3)
print(resultado_l4)
print(resultado_l5)
print(resultado_l6)
print(resultado_l7)
print(resultado_l8)
