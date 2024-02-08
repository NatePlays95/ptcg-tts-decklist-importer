from modules.parser import parseCardFromLine, filterLines
from modules.image_manip import test_makeDeckHiresCardList
# SDK
from pokemontcgsdk import Card, RestClient
from pokemontcgsdk.cardimage import CardImage
# API KEY from root/api_key.py
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

#print("Lines before filtering: ", linhas)
linhas = filterLines(linhas)
#print("Lines after filtering: ", linhas)
cards_list = []

for linha in linhas:
    cardInfo = parseCardFromLine(linha.strip())
    setName = cardInfo['setName']
    setNumber = cardInfo['setNumber']
    
    card_query = Card.where(q=f'set.ptcgoCode:{setName} number:{setNumber}')
    card = False
    
    if (card_query != []):
        card = card_query[0]

    if card:
        for i in range(cardInfo["count"]):
            cards_list.append(card)
        print("FOUND:", cardInfo["count"], "x", card.name)
    else:  
        print('ERROR:', "couldn't find", linha)

# make deck
test_makeDeckHiresCardList(cards_list)