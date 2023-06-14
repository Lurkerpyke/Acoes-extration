import requests
import json

# Adicionar a chave API do site que vai receber a raspagem
API_KEY = 'sua chave API' #digite sua chave api que recebeu do site que esta na url

# Listar as ações que vão ser analisadas(Código da B3)
symbols = ['PETR4.SAO', 'ITSA4.SAO', 'VALE3.SAO']#Escolha as acoes que deseja analisar

for symbol in symbols:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    
    # Extrai os dados relevantes do JSON retornado pela API
    symbol = data['Global Quote']['01. symbol']
    price = data['Global Quote']['05. price']
    change = data['Global Quote']['09. change']
    percent_change = data['Global Quote']['10. change percent']
    
    # Imprime os dados formatados para cada ação
    print(f'Símbolo: {symbol}')
    print(f'Preço: {price}')
    print(f'Variação: {change}')
    print(f'Variação percentual: {percent_change}%')
