def getData(site):
    import requests
    from bs4 import BeautifulSoup

    cabecalho = {'user-agent': 'Mozilla/5.0'}
    retorno = requests.get(site, headers = cabecalho)
    pagina = BeautifulSoup(retorno.content, 'html.parser')

    nomeFundo = pagina.find('h3', attrs={'class': 'section-subtitle'}).text
    precoCota = pagina.find('span', attrs={'class': 'price'}).text
    lista_indic = pagina.find_all('span', attrs={'class': 'indicator-title'})
    lista_valores = pagina.find_all('span', attrs={'class': 'indicator-value'})
    try:
        variacao = pagina.find('span', attrs={'class': 'percentage positive'}).text
    except:
        variacao = pagina.find('span', attrs={'class': 'percentage negative'}).text

    print("=============================================================")

    print(nomeFundo)
    print('\nValor da cota: ' +precoCota.strip())
    print('Variação do dia: ' +variacao.strip())

    for i in range(len(lista_indic)):
        indicador = lista_indic[i].text
        valor = lista_valores[i].text
        print(indicador.strip() + ': ' + valor.strip())        

    print("=============================================================")

def menu():
    print('\n1 - Consultar fundo')
    print('2 - Encerrar programa')
    opcao = int(input('Opção: '))
    if opcao == 1:
        fund = (input('Fundo: '))
        varsite = 'https://www.fundsexplorer.com.br/funds/' + fund
        getData(varsite)
        menu()
    elif opcao == 2:
        exit()
    else:
        print('Opção inválida. Escolha novamente.')
        menu()

print('### FUNDOS IMOBILIARIOS ###')
menu()