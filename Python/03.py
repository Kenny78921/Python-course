# Metodos de Strings
palabra = "Hola mundo"

# count()
print(palabra.count("Hola"))
# 1

# find() e index()
print(palabra.find("wolrd"))
# -1

# rfind() e rindex()
print(palabra.rfind("mundo"))
# 5

# startswith() e endswith()
print(palabra.startswith("mundo"))
# false

# isdigit()
print(palabra.isdigit())
# false

# isdecimal()
print(palabra.isdecimal())
# false

# isalnum()
print(palabra.isalnum())
# false

# isalpha()
print(palabra.isalpha())
# false




palabra = "hola mundo"

# capitalize()
print(palabra.capitalize())
# Hola mundo

# replace()
print(palabra.replace("mundo", "world"))
# Hola world

# lower()
print(palabra.lower())
# hola mundo

# upper()
print(palabra.upper())
# HOLA MUNDO

# swapcase()
print(palabra.swapcase())
# HOLA MUNDO

# strip()
print(palabra.strip())
# hola mundo

n, m, p = map(int, input().split())
print(n,m,p)