def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 1: "))
    print(n1 + n2)


try:
    suma()
except:
    print("Algo salio mal")
else:
    print("Todo salio bien")
finally:
    print("Eso fue todo")
