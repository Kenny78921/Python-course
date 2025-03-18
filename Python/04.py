# Listas

lista_1 = [1, 2, 4, 5, 6, 7]
lista_2 = ["a", "b", "c"]
lista_3 = [8, 5, 6]

# Indexado
print(lista_1[1:3])
# [2, 4]

# Cantidad de elementos
print(len(lista_1))
# 6

# Concatenación
print(lista_1 + lista_2)
# [1, 2, 4, 5, 6, 7, a. b. c]"

# Append
"lista_1.append('X')"
print(lista_1)
# [1, 2, 4, 5, 6, 7, X]"

# Pop
print(lista_1.pop(5))
# 7

# Sort
lista_3.sort()
print(lista_3)
# [5, 6, 8]

# Reverse
lista_1.reverse()
print(lista_1)
# [6, 5, 4, 2, 1]

# Insert
lista_2.insert(4, "naranja") 
print(lista_2)
# lista_2 = ["a", "b", "c", "naranja"]