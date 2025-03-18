from os import system
import bs4
import requests
system("cls")

for x in range(1,50):
    solicitud = requests.get(f"https://books.toscrape.com/catalogue/page-{x}.html")
    sopita = bs4.BeautifulSoup(solicitud.text, "lxml")
    libros = sopita.select(".product_pod")
    print(f"Pagina: {x}")
    for libro in libros:
        if len(libro.select(".star-rating.Five")) != 0:
            titulos = libro.select("a")[1]["title"]
            print(titulos)
    print("\n")
