import requests
from bs4 import BeautifulSoup

url_base = "https://www.baixarcursosgratis.org/"
urls_validas = []

for i in range(1, 101): # testa as 100 primeiras urls
    url = f"{url_base}/pagina-{i}"
    response = requests.get(url)
    if response.status_code == 200:
        urls_validas.append(url)

with open("urls_validas.txt", "w") as arquivo:
    for url in urls_validas:
        arquivo.write(f"{url}\n")