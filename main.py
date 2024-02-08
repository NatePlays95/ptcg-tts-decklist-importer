from modules.parser import parseCardFromLine

# SDK
from pokemontcgsdk import Card, RestClient

# CHAVE DA API (fora do repositorio)
from api_key import API_KEY

input = "1 Professor's Letter BKT 146a"
cardInfo = parseCardFromLine(input)

key = API_KEY
RestClient.configure(key)

nome_arquivo = 'tests/parser/decklist_after_sv.txt'
linhas = []
try:
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    print(f'O arquivo {nome_arquivo} não foi encontrado.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

for linha in linhas:
    cardInfo = parseCardFromLine(linha.strip())
    setName = cardInfo['setName']
    setNumber = cardInfo['setNumber']
    card = Card.where(q=f'set.ptcgoCode:{setName} number:{setNumber}')
    if (card != []):
        print(card[0].name)
    else:  
        print('nada')



#cards = Card.where(q='set.ptcgoCode:CRE number:22')
#print(cards)

