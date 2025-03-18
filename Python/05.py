# Repaso

numero_1 = 10
numero_2 = 100

afirmacion_1 = True
afirmacion_2 = False

resultado_1 = numero_1 == numero_2
print(resultado_1)
# False

resultado_1 = numero_1 <= numero_2
print(resultado_1)
# True

resultado_1 = numero_1 <= numero_2 and afirmacion_1 == True
print(resultado_1)
# True

resultado_1 = numero_1 == numero_2 or afirmacion_1 == True
print(resultado_1)
# True

resultado_1 = not numero_1 == numero_2
print(resultado_1)
# True

if numero_1 == numero_2:
    print("Opción A")
elif afirmacion_1 == True:
    print("Opción B")
else:
    print("Opción C")

lista_1 = ["1","2","3","4","5"]
lista_2 = ["nabetse","perry","ryuk","perro","nancy"]
lista_3 = [1,2,3,4,5]

for letras in lista_1:
    print("Letra: " + letras)
# Letra: 1
# Letra: 2
# Letra: 3
# Letra: 4
# Letra: 5

for palabras in lista_2:
    if palabras.startswith("n"):
        print(f"El nombre {palabras} empieza con: n" )
# El nombre nabetse empieza con: n
# El nombre nancy empieza con: n

resultado_suma = 0
for numeros in lista_3:
    resultado_suma = resultado_suma + numeros
    print(resultado_suma)

numero_w = 10

while numero_w > -1:
    print(numero_w)
    numero_w=numero_w-1
else:
    print("Acabo")
