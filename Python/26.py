from os import system
import bs4
import requests
system("cls")

solicitud = requests.get("https://www.escueladirecta.com/courses")

sopa = bs4.BeautifulSoup(solicitud.text, "lxml")

imagenes = sopa.select(".course-box-image")[0]["src"]

imagen_curso = requests.get(imagenes)

f = open("mi_imagen.jpg", "wb")
f.write(imagen_curso.content)
f.close()