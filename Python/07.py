# Funciones
def saludar():
    print("Holiwis")

saludar()
# Holiwis

def sumar(a,b,c):
    print(a+b+c)

sumar(1,2,3)
# 6


# Ejemplo de funciones
def todos_positivos(lista_numeros):
    if all (todos_positivos > 0 for todos_positivos in lista_numeros):
        print("Todos lo son")
    else:
        print("No lo son")
  
lista_numeros = [1, 2, 3, 782]
todos_positivos(lista_numeros)

# *args
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return  total

print(suma(1,2,3,4,5,6,7,8,9,10))
# 55

def sumayletras(argsl, *argsn):
    nombre = argsl
    total = 0
    for arg in argsn:
        total += arg
    print(f"Tu nombre {nombre}, combina con tu num que es: {total}")
    return
    
sumayletras("Aldo",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# 55