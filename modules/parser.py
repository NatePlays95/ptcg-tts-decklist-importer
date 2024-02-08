#print("parser on")

lineRegex = "^\s*\**\s*(?P<Count>\d+)\s+(?P<Name>.+)\s+(?P<Set>[A-Za-z0-9_-]+)\s+(?P<NumberInSet>[A-Za-z0-9]+)$"

## The average line looks like this: "1 Professor's Letter BKT 146a"
## if we split on ' ' we get:
## "1", "Professor's", "Letter", "BKT", "146a"
## first index is always count
## last index is always set number, second to last is always set name
## rest should be the card's name. Let's use pop_front and pop_back to get that info.
def parseCardFromLine(line:str):
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