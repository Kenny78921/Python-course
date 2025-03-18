from os import system
import bs4
import requests
system("cls")

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

solicitud = requests.get("https://www.op.gg/summoners/lan/GatitaEnCelo-EVIL", headers = headers)

print(solicitud.status_code)

sopita = bs4.BeautifulSoup(solicitud.text, "lxml")

resultado = sopita.select(".css-j7qwjs.ery81n90")

for x in resultado:
    print(x.text)