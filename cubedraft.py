## Cube Draft support is simple, but it will have to wait
## for either PokemonCard or CubeKoga to finish their cubelist exporters.
## Otherwise there's no universal format to support.
## You can still try making decks larger than 60 cards and exporting as JSON, however.

from modules.cube_parser import parseCubedraftLines
from modules.image_manip import makeDeckFromCardList
from modules.json_builder import makeFullJson
# SDK
from pokemontcgsdk import Card, RestClient
from pokemontcgsdk.cardimage import CardImage
# API KEY from root/api_key.py
from api_key import API_KEY





key = API_KEY
RestClient.configure(key)

INPUT_FILE = 'tests/cube_parser/Cube Draft.txt'
lines = []
try:
    with open(INPUT_FILE, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f'File \"{INPUT_FILE}\" was not found')
except Exception as e:
    print(f'ERROR:: {e}')

# get cards
cards_list = parseCubedraftLines(lines)

# make deck
filename = "cubedraft_complete"
#makeDeckFromCardList(filename, cards_list)
makeFullJson(filename, cards_list)
