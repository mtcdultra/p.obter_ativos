<h1>Obter ativos (ações, FIIs e BDRs) da B3</h1>

Pequeno programa para retornar todos os códigos dos ativos (ações/BDRs) da B3 e os ativos (FII) existentes utilizando os sites www.infomoney.com.br e https://www.fundsexplorer.com.br/ com a biblioteca BeautifulSoap

Por enquanto há o arquivo app.py com duas funções:

* def retornar_acoes_existentes()
  * Retornar os ativos obtidos no site da Infomoney. Retorna ações e BDRs (https://www.infomoney.com.br/cotacoes/empresas-b3/)
* def retornar_fiis_existentes()
  * Retornar os ativos obtidos no site do Funds Explorer (https://www.fundsexplorer.com.br/funds)

Falta implementar:

* Utilizar a biblioteca yfinance (https://pypi.org/project/yfinance/). Com esta biblioteca, recuperamos nome da empresa, patrimimônio líquido, dividendos, as cotações passadas entre outras informações.
* Salvar os ativos no SQLite com as respectivas informações oriundas do yfinance
* Implementar em Flask para visualizar as informações dos ativos
