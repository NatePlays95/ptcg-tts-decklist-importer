from ratelimit import limits, sleep_and_retry
from datetime import timedelta
# SDK
from pokemontcgsdk import Card

lineRegex = "^\s*\**\s*(?P<Count>\d+)\s+(?P<Name>.+)\s+(?P<Set>[A-Za-z0-9_-]+)\s+(?P<NumberInSet>[A-Za-z0-9]+)$"
__digits_list__ = ['0','1','2','3','4','5','6','7','8','9']
__types_list__ = ["Grass", "Fire", "Water", "Lightning", "Psychic", "Fighting", "Darkness", "Metal", "Fairy"]
__basic_energy_setname__ = "SUM" # Sun and Moon, as it still had fairy energy.
__basic_energy_set_offset__ = 163 # energies start at 164 for energy 1




def parseDecklistLines(lines:[str]):
    cards_list = []
    lines = filterLines(lines)
    
    for line in lines:
        card_info = parseCardFromLine(line)
        print("ATTEMPT:", card_info["name"])
        card = queryCard(card_info)
        
        if card == False: # if query failed, # try energy fallback.
            card_info = parseFallbackEnergy(line)
            card = queryCard(card_info)
            if card != False:
                print("Found energy card via fallback")
        
        if card != False:
            print("FOUND:", line)
            for i in range(card_info["count"]):
                cards_list.append(card)
            continue

        print('ERROR:', "couldn't find", line)
    
    return cards_list

# TODO: make way to detect lack of api key to throttle calls
@sleep_and_retry
@limits(calls=1, period=timedelta(seconds=2).total_seconds())
def queryCard(card_info):
    card_query = Card.where(q=f'set.ptcgoCode:{card_info["setName"]} number:{card_info["setNumber"]}')

    if card_query == []: # if query failed,
        # try query by name, fallback for SV cards. TODO: remove this fallback when SV set codes are fixed.
        query_fstring = f'name:\"{card_info["name"]}\" number:{card_info["setNumber"]}'
        print("trying name fallback on", query_fstring)
        card_query = Card.where(q=query_fstring)
        if card_query != []: 
            print("Found SV card via name fallback.")
    
    if len(card_query) > 0:
        if len(card_query) > 1: print("Multiple results??", card_query) # shouldn't happen?
        return card_query[0] # type 'Card'

    return False


## Returns a new array with empty lines removed
## and divider lines "Pokémon, Trainer, Items" removed.
def filterLines(lines_array:list) -> list:
    new_array = []
    for line in lines_array:
        line : str = line.strip()
        if line == "": continue # if line is empty, skip
        if line[0] not in __digits_list__: continue # if line doesn't have card count, it's invalid
        new_array.append(line)
    return new_array

## The average line looks like this: "1 Professor's Letter BKT 146a"
## if we split on ' ' we get:
## "1", "Professor's", "Letter", "BKT", "146a"
## first index is always count
## last index is always set number, second to last is always set name
## rest should be the card's name. Let's use pop_front and pop_back to get that info.
def parseCardFromLine(line:str) -> dict:
    line = line.strip()

    cardInfo = {
        "name": "",
        "count": 0,
        "setName": "",
        "setNumber": "",
    }
    
    splitLine = line.split(' ')
    cardInfo["count"] = int(splitLine.pop(0))
    cardInfo["setNumber"] = splitLine.pop(-1)

    # for LigaPokemon decklists, remove starting zeroes.
    cardInfo["setNumber"] = cardInfo["setNumber"].lstrip("0")

    # if last name is exactly "Energy", set name is missing, this is basic energy.
    if splitLine[-1] == "Energy":
        cardInfo["setName"] = __basic_energy_setname__
        # change specific to SUM energy, energy starts at index 164.
        cardInfo["setNumber"] = str(int(cardInfo["setNumber"]) + __basic_energy_set_offset__)
    else:
        cardInfo["setName"] = splitLine.pop(-1)
    
    cardInfo["name"] = ' '.join(splitLine)

    return cardInfo

## Use this if the card is a promo energy from a set that's not recognized by the API.
def parseFallbackEnergy(line:str) -> dict:
    line = line.strip()
    
    if not ("Energy" in line): return {}
    
    cardInfo = {"name": "","count": 0,"setName": "","setNumber": "",}
    splitLine = line.split(' ')

    for i in range(len(__types_list__)):
        energy_type_index = i + 1
        energy_name = __types_list__[i] + " Energy"
        if energy_name in line:
            cardInfo["count"] = int(splitLine.pop(0))
            cardInfo["setName"] = __basic_energy_setname__
            cardInfo["setNumber"] = energy_type_index + __basic_energy_set_offset__
            cardInfo["name"] = energy_name
            break

    if cardInfo["count"] == 0: return {}
   
    return cardInfo