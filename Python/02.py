# Strings y substrings

Variable_texto = "Mi texto en python en VS"
resultado = Variable_texto[3]
resultado_2 = Variable_texto.index("M")
resultado_3 = Variable_texto.index("e", 5)
resultado_4 = Variable_texto.rindex("e")

print(resultado)
print(resultado_2)
print(resultado_3)
print(resultado_4)

Variable_texto = "1234567890"
resultado_5 = Variable_texto[0:8]
resultado_6 = Variable_texto[0:8:2]
resultado_7 = Variable_texto[::-1]

print(resultado_5)
print(resultado_6)
print(resultado_7)
