from modules.parser import parseCardFromLine, filterLines, checkFallbackEnergy
from modules.image_manip import makeDeckFromCardList
# SDK
from pokemontcgsdk import Card, RestClient
from pokemontcgsdk.cardimage import CardImage
# API KEY from root/api_key.py
from api_key import API_KEY

input = "1 Professor's Letter BKT 146a"
cardInfo = parseCardFromLine(input)

key = API_KEY
RestClient.configure(key)

nome_arquivo = 'tests/parser/decklist_ligapokemon.txt'
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
    cardInfo = parseCardFromLine(linha)
    
    card_query = Card.where(q=f'set.ptcgoCode:{cardInfo["setName"]} number:{cardInfo["setNumber"]}')
    card = False
    
    if (card_query != []):
        card = card_query[0]

    if card:
        for i in range(cardInfo["count"]):
            cards_list.append(card)
        print("FOUND:", cardInfo["count"], "x", card.name)
        continue

    # try energy fallback.
    fallback = checkFallbackEnergy(linha)

    if fallback == {}:
        print('ERROR:', "couldn't find", linha)
        continue
    
    card_query = Card.where(q=f'set.ptcgoCode:{fallback["setName"]} number:{fallback["setNumber"]}')
    if (card_query != []):
        card = card_query[0]
        
    if card:
        for i in range(fallback["count"]):
            cards_list.append(card)
        print("FOUND by energy fallback:", fallback["count"], "x", card.name)
        continue
    
    else:
        print('ERROR:', "couldn't find", linha, "by fallback.")


# make deck
filename = "decklist_complete"
makeDeckFromCardList(filename, cards_list)