from modules.parser import parseDecklistLines
from modules.image_manip import makeDeckFromCardList
# SDK
from pokemontcgsdk import Card, RestClient
from pokemontcgsdk.cardimage import CardImage
# API KEY from root/api_key.py
from api_key import API_KEY





key = API_KEY
RestClient.configure(key)

INPUT_FILE = 'tests/parser/decklist_ligapokemon.txt'
lines = []
try:
    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f'File \"{INPUT_FILE}\" was not found')
except Exception as e:
    print(f'ERROR:: {e}')

# get cards
cards_list = parseDecklistLines(lines)

# make deck
filename = "decklist_complete"
makeDeckFromCardList(filename, cards_list)