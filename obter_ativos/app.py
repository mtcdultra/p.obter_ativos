import requests
from bs4 import BeautifulSoup

def retornar_acoes_existentes():

    page = requests.get("https://www.infomoney.com.br/cotacoes/empresas-b3/")
    soup = BeautifulSoup(page.content, "html.parser")
    lista_ativo = soup.find(class_="col-md-9 col-lg-8 col-xl-6 m-sm-auto m-lg-0 article-content")
    codigo_ativo = lista_ativo.find_all("td", class_="strong")

    for codigos_ativos in codigo_ativo:

        if ( codigos_ativos.text.strip()[-1:] == "F" ) or ( codigos_ativos.text.strip() == "" ) : continue

        print(codigos_ativos.text.strip())


def retornar_fiis_existentes():

    page = requests.get("https://www.fundsexplorer.com.br/funds")
    soup = BeautifulSoup(page.content, "html.parser")
    lista_ativo = soup.find(id="search-menu-select")
    codigo_ativo = lista_ativo.find_all("option")

    for codigos_ativos in codigo_ativo:

        print(codigos_ativos.text.strip()[:6])