import importlib
from modules.parser import parseDecklistLines
from modules.image_manip import makeDeckFromCardList
from modules.json_builder import makeFullJson
# SDK
from pokemontcgsdk import Card, RestClient
from pokemontcgsdk.cardimage import CardImage


# API KEY from root/api_key.py
api_key_exists = not (importlib.util.find_spec("api_key") == None)
if api_key_exists:
    from api_key import API_KEY
    RestClient.configure(API_KEY)


INPUT_FILE = 'tests/parser/decklist_accent_marks.txt'
lines = []
try:
    with open(INPUT_FILE, 'r', encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f'File \"{INPUT_FILE}\" was not found')
except Exception as e:
    print(f'ERROR:: {str(e)}')

# get cards
cards_list = parseDecklistLines(lines)

# make deck
filename = "decklist_complete"
makeDeckFromCardList(filename, cards_list)
#makeFullJson(filename, cards_list)