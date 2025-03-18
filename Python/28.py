from os import system
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4

system("cls")

#$ Opciones de Selenium
options = Options()
options.headless = True
options.add_argument("--disable-extensions")
options.add_argument("--disable-sync")
options.add_argument("--disable-logging")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")

#$ Inicio de solicitud y conversion de datos
solicitud = webdriver.Chrome(options = options)
solicitud.get("https://www.op.gg/summoners/lan/GatitaEnCelo-EVIL")
texto = solicitud.page_source
sopita = bs4.BeautifulSoup(texto, "lxml")

nombre = sopita.select(".name-container")
for x in nombre:
    nombre = x.select(".name")[0].get_text()
    nombre = nombre.split("#")[0]

resultado = sopita.select(".css-j7qwjs.ery81n90")
Sum_KDA = 0
Suma_K = 0
Suma_D = 0
Suma_A = 0
for x in resultado:
    KDA = x.select(".kda")[0].get_text()
    K,D,A = [a.strip() for a in KDA.split("/")]
    K = int(K)
    D = int(D)
    A = int(A)
    print(f"El KDA de {nombre} es: {K}/{D}/{A}")
    Suma_K = Suma_K + K
    Suma_D = Suma_D + D
    Suma_A = Suma_A + A

Suma_K = round(Suma_K / len(resultado), 3)
Suma_D = round(Suma_D / len(resultado), 3)
Suma_A = round(Suma_A / len(resultado), 3)

Sum_KDA = round(((Suma_K+Suma_A)/Suma_D), 2)


print("\n\n¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
print(f"\n\nVete a la verga {nombre}, tu KDA es de {Sum_KDA}\n\n")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")