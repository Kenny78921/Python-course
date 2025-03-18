# Proyecto 6
# * Importar librerias
from os import system
from pathlib import Path
import time

system("cls")
numero_recetas = 0
salir_while = 0
numero_de_receta = 0
valor_while_2 = 0

# * Variables globales "**/*.txt"
ruta = Path(Path.home(), "Recetas")
for x in Path(ruta).glob("**/*.txt"):
    numero_recetas += 1

print(
    f"Hola usuario, la ruta de la carpeta de las recetas es: {ruta}\n\nEl número de recetas disponibles son: {numero_recetas}\n"
)
numero_recetas = 0
while salir_while == 0:
    valor_while = input(
        f"Bienvenido al menú principal, elija una opción para continuar: \n1. Carnes\n2. Ensaladas\n3. Pastas\n4. Postres\n5. Crear carpeta\n6. Crear archivo en Carnes\n#. Finalizar\n\n"
    )
    system("cls prev_line")

    # $ Condicional del menu
    # ° Menu de Carnes
    if valor_while == "1":
        print(f"Las recetas disponibles son: \n")
        ruta_a = Path(Path.home(), "Recetas", "Carnes")

        for x in Path(ruta_a).glob("**/*.txt"):
            print(x)

        valor_ruta = input(f"\nElige que receta quieres leer (Escriba el nombre):\n")
        ruta_b = Path(Path.home(), "Recetas", "Carnes", valor_ruta)
        archivo = open(ruta_b, "r")
        system("cls")
        print(archivo.readline())

        print("\nSe volver al menu anterior")
        time.sleep(2)
        system("cls")

    # ° Menu de Ensaladas
    elif valor_while == "2":
        print(f"Las recetas disponibles son: \n")
        ruta_a = Path(Path.home(), "Recetas", "Ensaladas")

        for x in Path(ruta_a).glob("**/*.txt"):
            print(x)

        valor_ruta = input(f"\nElige que receta quieres leer (Escriba el nombre):\n")
        ruta_b = Path(Path.home(), "Recetas", "Ensaladas", valor_ruta)
        archivo = open(ruta_b, "r")
        system("cls")
        print(archivo.readline())

        print("\nSe volver al menu anterior")
        time.sleep(2)
        system("cls")

    # ° Menu de Pastas
    elif valor_while == "3":
        print(f"Las recetas disponibles son: \n")
        ruta_a = Path(Path.home(), "Recetas", "Pastas")

        for x in Path(ruta_a).glob("**/*.txt"):
            print(x)

        valor_ruta = input(f"\nElige que receta quieres leer (Escriba el nombre):\n")
        ruta_b = Path(Path.home(), "Recetas", "Pastas", valor_ruta)
        archivo = open(ruta_b, "r")
        system("cls")
        print(archivo.readline())

        print("\nSe volver al menu anterior")
        time.sleep(2)
        system("cls")

    # ° Menu de Postres
    elif valor_while == "4":
        print(f"Las recetas disponibles son: \n")
        ruta_a = Path(Path.home(), "Recetas", "Postres")

        for x in Path(ruta_a).glob("**/*.txt"):
            print(x)

        valor_ruta = input(f"\nElige que receta quieres leer (Escriba el nombre):\n")
        ruta_b = Path(Path.home(), "Recetas", "Postres", valor_ruta)
        archivo = open(ruta_b, "r")
        system("cls")
        print(archivo.readline())

        print("\nSe volver al menu anterior")
        time.sleep(2)
        system("cls")

    # ° Menu de crear carpeta
    elif valor_while == "5":
        variable_crear = input("¿Quieres crear una carpeta?\n1.Si\n2.No\n\n")
        if variable_crear == "1":
            nombre_carpeta_creada = input(
                "\n¿Que nombre quieres ponerle a la carpeta?\n\n"
            )
            ruta_a = Path(Path.home(), "Recetas", nombre_carpeta_creada)
            if ruta_a.exists():
                print(f"Ya existe la carpeta: {nombre_carpeta_creada}\n")
                print("\nSe volvera al menu anterior")
                time.sleep(2)
                system("cls")
            else:
                ruta_a.mkdir()
                print(
                    f"Carpeta con el nombre: {nombre_carpeta_creada} fue creada con éxito\n"
                )
                print("\nSe volvera al menu anterior")
                time.sleep(2)
                system("cls")
        else:
            print("\nSe volvera al menu anterior")
            time.sleep(2)
            system("cls")
    # ° Menu de crear archivo en carnes
    elif valor_while == "6":
        variable_crear = input("¿Quieres crear un archivo?\n1.Si\n2.No\n\n")
        if variable_crear == "1":
            nombre_archivo_creado = input(
                "\n¿Que nombre quieres ponerle al archivo?\n\n"
            )
            ruta_a = Path(Path.home(), "Recetas", "Carnes", nombre_archivo_creado)
            if ruta_a.exists():
                print(f"Ya existe el archivo: {nombre_archivo_creado}\n")
                print("\nSe volvera al menu anterior")
                time.sleep(2)
                system("cls")
            else:
                ruta_a.touch()
                print(
                    f"El archivo con el nombre: {nombre_archivo_creado} fue creado con éxito\n"
                )
                print("\nSe volvera al menu anterior")
                time.sleep(2)
                system("cls")
        else:
            print("\nSe volvera al menu anterior")
            time.sleep(2)
            system("cls")

    # ° Finalizar
    elif valor_while == "#":
        salir_while = 1
        print("Hasta luego, gracias por usar el recetario")

    else:
        print("Favor de ingresar un valor correcto \n")
