# Proyecto 7
from os import system
import time
system("cls")

#! Definir variables globales
variable_while = 0

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
        
    def __init__(self, nombre, apellido, numero_c, balance):
        super().__init__(nombre, apellido)
        self.numero_c = numero_c
        self.balance = balance

    def __str__(self):
        return f"Bienvenido: {self.nombre} {self.apellido} con número de cuenta {self.numero_c}. \nSu saldo actual es: ${self.balance}"
    
    def depositar(self, deposito):
        self.balance += deposito
        print(f"Tu saldo actual es de: {self.balance}")

    def retirar(self, retiro):
        if self.balance - retiro < 0:
            print("No dispones de los fondos suficientes")
        else:
            self.balance -= retiro
            print(f"Tu saldo actual es de: {self.balance}")
    
    def consultar(self):
        print(f"Tu saldo actual es de: {self.balance}")

cliente_1 = Cliente("Aldo", "Solares", 78921, 250000)

while variable_while == 0:
    system("cls")
    variable_if = input(f"¿Que deseas hacer?\n1. Depositar\n2. Retirar\n3. Consultar saldo\n#. Finalizar\n\n")

    if variable_if == "1":
        system("cls")
        deposito = int(input(f"Ingresa la cantidad a depositar: "))
        cliente_1.depositar(deposito)
        print("\nRegresando al menu...")
        time.sleep(3)

    elif variable_if == "2":
        system("cls")
        retiro = int(input(f"Ingresa la cantidad a retirar: "))
        cliente_1.retirar(retiro)
        print("\nRegresando al menu..")
        time.sleep(3)

    elif variable_if == "3":
        system("cls")
        cliente_1.consultar()
        print("\nRegresando al menu..")
        time.sleep(3)

    elif variable_if == "#":
        system("cls")
        print("Hasta la proxima")
        variable_while = 1

    else:
        print("Introduzca una opción valida")

