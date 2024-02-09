from modules.parser import parseDecklistLines
from modules.image_manip import makeDeckFromCardList
# SDK
from pokemontcgsdk import Card, RestClient
from pokemontcgsdk.cardimage import CardImage
# API KEY from root/api_key.py
from api_key import API_KEY





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

# get cards
cards_list = parseDecklistLines(linhas)

# make deck
filename = "decklist_complete"
makeDeckFromCardList(filename, cards_list)