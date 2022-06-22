import requests
from bs4 import BeautifulSoup

def getData(site):

    cabecalho =     {'user-agent': 'Mozilla/5.0'}
    retorno =       requests.get(site, headers = cabecalho)
    pagina =        BeautifulSoup(retorno.content, 'html.parser')

    nomeFundo =     pagina.find('h3', attrs={'class': 'section-subtitle'}).text
    precoCota =     pagina.find('span', attrs={'class': 'price'}).text
    lista_indic =   pagina.find_all('span', attrs={'class': 'indicator-title'})
    lista_valores = pagina.find_all('span', attrs={'class': 'indicator-value'})
    try:
        variacao =  pagina.find('span', attrs={'class': 'percentage positive'}).text
    except:
        variacao =  pagina.find('span', attrs={'class': 'percentage negative'}).text

    print("=============================================================")

    print(nomeFundo)
    print('\nValor da cota: ' +precoCota.strip())
    print('Variação do dia: ' +variacao.strip())

    for i in range(len(lista_indic)):
        indicador = lista_indic[i].text
        valor = lista_valores[i].text
        print(indicador.strip() + ': ' + valor.strip())        

    print("=============================================================")

print("### FUNDOS IMOBILIARIOS ###")
fund = (input('Fundo: '))
varsite = 'https://www.fundsexplorer.com.br/funds/' + fund
getData(varsite)