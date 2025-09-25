# Pour chaque livre, je veux que tu récupères le titre, le nombre d’étoiles et le prix.
# Vous devez écrire toutes ces informations dans un nouveau fichier au format CSV.

from bs4 import BeautifulSoup
import requests
from pathlib import Path

Path = Path.cwd() / "livres.txt"
liste = []


def get_data(page):
    data = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html").content
    soup = BeautifulSoup(data, "html.parser")
    price = soup.select(".price_color")
    title = soup.select(".product_pod h3 a")
    book = zip(title, price)
    for i, j in book:
        tup = (i['title'], j.string)
        liste.append(tup)
    return True

def save_csv():
    with open (Path, "a") as f:
        for i in liste:
            titre, prix = i
            texte = f"{titre} au prix de {prix}."
            f.write(f"{texte}\n")




for _ in range(50):
    get_data(_)

save_csv()


