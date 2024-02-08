#print("parser on")

lineRegex = "^\s*\**\s*(?P<Count>\d+)\s+(?P<Name>.+)\s+(?P<Set>[A-Za-z0-9_-]+)\s+(?P<NumberInSet>[A-Za-z0-9]+)$"
_digitsList = ['0','1','2','3','4','5','6','7','8','9']

## Returns a new array with empty lines removed
## and divider lines "Pokémon, Trainer, Items" removed.
def filterLines(lines_array:list) -> list:
    new_array = []
    for line in lines_array:
        line : str = line.strip()
        if line == "": continue # if line is empty, skip
        if line[0] not in _digitsList: continue # if line doesn't have card count, it's invalid
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
        "count": "",
        "setName": "",
        "setNumber": "",
    }
    
    splitLine = line.split(' ')
    cardInfo["count"] = int(splitLine.pop(0))
    cardInfo["setNumber"] = splitLine.pop(-1)
    cardInfo["setName"] = splitLine.pop(-1)
    cardInfo["name"] = ' '.join(splitLine)

    return cardInfo

