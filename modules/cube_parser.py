
from pokemontcgsdk import Card


def parseCubedraftLines(lines:[str]):
    cards_list = []
    lines = filterLines(lines)
    
    for line in lines:
        card_info = parseCardFromLine(line)
        card = queryCard(card_info)
        
        if card != False:
            print("FOUND:", line, " --- ", card.name)
            cards_list.append(card)
            continue

        print('ERROR:', "couldn't find", line)
    
    return cards_list


def queryCard(card_info):
    card_query = Card.where(q=f'set.id:{card_info["setID"]} number:{card_info["setNumber"]}')
    
    if len(card_query) > 0:
        if len(card_query) > 1: print("Multiple results??", card_query) # shouldn't happen?
        return card_query[0] # type 'Card'

    return None


def filterLines(lines_array:list) -> list:
    new_array = []
    for line in lines_array:
        line : str = line.strip()
        if line == "": continue # if line is empty, skip
        if line[0] == '#': continue # if line doesn't have card count, it's invalid
        if "Cube" in line: continue # header
        new_array.append(line)
    return new_array


## The average line looks like this: "swsh11-68".
## Split on "-" and we have the set id and set number.
def parseCardFromLine(line:str) -> dict:
    print("Looking at:",line)
    line = line.strip()
    splitLine = line.split('-')
    cardInfo = {
        "setID": splitLine[0],
        "setNumber": splitLine[1],
    }
    return cardInfo