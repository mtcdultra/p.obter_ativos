import requests
from bs4 import BeautifulSoup
import yfinance as yf

def retornar_acoes_existentes():

    page = requests.get("https://www.infomoney.com.br/cotacoes/empresas-b3/")
    soup = BeautifulSoup(page.content, "html.parser")
    lista_ativo = soup.find(class_="col-md-9 col-lg-8 col-xl-6 m-sm-auto m-lg-0 article-content")
    codigo_ativo = lista_ativo.find_all("td", class_="strong")

    resultados = []

    for codigos_ativos in codigo_ativo:

        if ( codigos_ativos.text.strip()[-1:] == "F" ) or ( codigos_ativos.text.strip() == "" ) : continue

        resultados.append(codigos_ativos.text.strip()+".SA")

    return resultados


def retornar_fiis_existentes():

    page = requests.get("https://www.fundsexplorer.com.br/funds")
    soup = BeautifulSoup(page.content, "html.parser")
    lista_ativo = soup.find(id="search-menu-select")
    codigo_ativo = lista_ativo.find_all("option")

    resultados = []

    for codigos_ativos in codigo_ativo:

        resultados.append(codigos_ativos.text.strip()[:6]+".SA")
    
    return resultados


def retornar_detalhes_ativo_antigo(ativo):

    nome_empresa, setor, website = "", "", ""
    
    ativo_ = yf.Ticker(ativo)

    try:
        ativo_.info["longName"]
    except KeyError:
        codigo_ativo = ativo
    else:
        codigo_ativo = ativo
        nome_empresa = ativo_.info["longName"]
        setor = ativo_.info["sector"]
        website = ativo_.info["website"]        

    return codigo_ativo, nome_empresa, setor, website



def retornar_todos_ativos():

    ...

    return retornar_acoes_existentes(), retornar_fiis_existentes()

def retornar_detalhes_ativo(ativo):

    nome_empresa_longo, nome_empresa_curto, setor, website, tipo_ativo = "", "", "", "", ""
    
    ativo_ = yf.Ticker(ativo)

    try:
        ativo_.info["longName"]
    except KeyError:
        codigo_ativo = ativo
        ativo_existente = 0
    else:
        codigo_ativo = ativo
        nome_empresa_longo = ativo_.info["shortName"]
        nome_empresa_curto = ativo_.info["longName"]
        
        setor = ativo_.info["sector"]
        ativo_existente = 1
        website = ativo_.info["website"]
        tipo_ativo = "acao"
        if nome_empresa_longo.find("Fundo") > -1: tipo_ativo = "fii"

    return codigo_ativo, nome_empresa_longo, nome_empresa_curto, setor, website, tipo_ativo, ativo_existente





#teste = retornar_acoes_existentes()




#for i in teste:
    
    #print(retornar_detalhes_ativo(i))