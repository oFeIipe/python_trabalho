#Instalar selenium e pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

lista_precos = []
lista_titulos = []

dataFrame = {
    "titulo": [],
    "preco": [],
    "link": []
}
service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

#coloquei outro item para busca porque o carrefour só tinha 1 piano
driver.get("https://www.carrefour.com.br/busca/tv")

titulos = driver.find_elements('xpath', '//*[@id="root"]/div/div[2]/div/div[2]/a/div[2]/h2')
precos = driver.find_elements('xpath', '//*[@id="root"]/div/div[2]/div/div[2]/a/div[2]/div/div[1]/span')
links = driver.find_elements('xpath', '//*[@id="root"]/div/div[2]/div/div[2]/a')

for preco in precos:
    preco_format = float(preco.text.replace("R$ ", "").replace(".", "").replace(",", "."))
    lista_precos.append(preco_format)

lista_links = [l.get_attribute("href") for l in links]
lista_titulos = [titulo.text for titulo in titulos]
dataFrame['preco'] = lista_precos
dataFrame['link'] = lista_links
dataFrame['titulo'] = lista_titulos

df = pd.DataFrame(dataFrame)

idx_min = df['preco'].idxmin()

menor_valor = df.loc[idx_min]

print(f"Nome: {menor_valor.titulo}")
print(f"Preço: R$:{menor_valor.preco}")
print(f"Link: {menor_valor.link}")