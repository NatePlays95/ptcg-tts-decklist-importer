import os
import json
#from modules.image_manip import getCardImage



TEST_FILEPATH = os.path.dirname(__file__) + "/../tests/json_builder/"
TEMPLATE_FILEPATH = TEST_FILEPATH + 'deck_template.json'
EXPORT_FILEPATH = os.path.dirname(__file__) + "/../exports/"

URL_BACKIMAGE = "http://cloud-3.steamusercontent.com/ugc/998016607072061655/9BE66430CD3C340060773E321DDD5FD86C1F2703/" # from jeandeaual

__USE_HIRES__ = True

__type_colors__ = {
    "Colorless": "[ffffff]", "Grass": "[4ad638]", "Fire": "[c43b12]", "Water": "[1080e3]",
    "Lightning": "[ffe30d]", "Psychic": "[9111fa]", "Fighting": "[703a10]",
    "Darkness": "[062238]", "Metal": "[a0a199]", "Dragon": "[a68803]", "Fairy": "[f72db0]"
}

__type_letters__ = {
    "Colorless": "{C}", "Grass": "{G}", "Fire": "{R}", "Water": "{W}",
    "Lightning": "{L}", "Psychic": "{P}", "Fighting": "{F}",
    "Darkness": "{D}", "Metal": "{M}", "Dragon": "{N}", "Fairy": "{Y}",

}

def makeFullJson(filename, cards_list):
    template_file = open(TEMPLATE_FILEPATH)
    deck_object = json.load(template_file)
   
    deck_state = deck_object["ObjectStates"][0]

    deck_state["DeckIDs"] = makeDeckIdsField(cards_list)
    deck_state["CustomDeck"] = makeCustomDeckField(cards_list)
    deck_state["ContainedObjects"] = makeContainedObjectsField(cards_list)

    deck_object["ObjectStates"] = [deck_state]

    save_file = open(EXPORT_FILEPATH + filename+".json", "w")
    json.dump(deck_object, save_file, indent = 2)


def makeDeckIdsField(cards_list):
    field_DeckIDs = []
    index = 1
    for card in cards_list:
        field_DeckIDs.append(index * 100)
        index += 1
    return field_DeckIDs


def makeCustomDeckField(cards_list):
    field_CustomDeck = {}
    index = 1
    for card in cards_list:
        card_object = {
            "FaceURL": card.images.large if __USE_HIRES__ else card.images.small,
            "BackURL": URL_BACKIMAGE,
            "NumWidth": 1, "NumHeight": 1,
            "BackIsHidden": True, "UniqueBack": False, "Type": 0
        }
        field_CustomDeck[str(index)] = card_object
        index += 1
    return field_CustomDeck


def makeContainedObjectsField(cards_list):
    field_ContainedObjects = []
    cardcustom_filepath = TEST_FILEPATH + "cardcustom.json"
    # print(cardcustom_filepath)
    cardcustom_template = open(cardcustom_filepath, "r")
    cardcustom_object = json.load(cardcustom_template)
    index = 1
    for card in cards_list:
        internal_CustomDeck = {
            "FaceURL": card.images.large if __USE_HIRES__ else card.images.small,
            "BackURL": URL_BACKIMAGE,
            "NumWidth": 1, "NumHeight": 1,
            "BackIsHidden": True, "UniqueBack": False, "Type": 0
        }
        card_object = cardcustom_object.copy()
        card_object["CardID"] = index * 100
        card_object["CustomDeck"] = {   
            str(index): internal_CustomDeck
        }
        card_object["Nickname"] = card.name
        card_object["Description"] = makeDescription(card)

        field_ContainedObjects.append(card_object)
        index += 1
    
    return field_ContainedObjects
        

def makeDescription(card) -> str:
    desc = ""
    desc += card.supertype + "\n"
    for subtype in card.subtypes:
        desc += subtype + " "
    desc += "\n\n"
    
    if card.supertype in ["Trainer", "Energy"]:
        if card.rules != None:
            for rule in card.rules:
                desc += rule + "\n"

    if card.supertype == "Pokémon":
        desc += card.hp + " HP\n"
        for type in card.types:
            desc += __type_colors__[type] + type + "[ffffff]"
        desc += "\n"
        if card.evolvesFrom != None:
            desc += "Evolves from " + card.evolvesFrom + "\n"
        desc += "\n"
    
        if card.ancientTrait != None:
            desc += "[00ff00][b]Ancient Trait:[ffffff]" + card.ancientTrait.name + "[/b]\n"
            desc += card.ancientTrait.text + "\n\n"
    
        if card.abilities != None:
            for ability in card.abilities:
                desc += "[ff0000][b]" + ability.type + ":[ffffff]  " + ability.name + "[/b]\n"
                desc += ability.text + "\n\n"

        if card.attacks != None:
            for attack in card.attacks:
                if attack.cost == []:
                    desc += "{FREE}   "
                else:
                    for cost in attack.cost:
                        desc += __type_colors__[cost] + __type_letters__[cost]
                    desc += "[ffffff]   "
                
                desc += f'[b]{attack.name}[/b]    {attack.damage}\n'
                desc += attack.text + "\n\n"
        
        if card.weaknesses != None:
            desc += "Weaknesses: "
            for weak in card.weaknesses:
                desc += __type_colors__[weak.type] + __type_letters__[weak.type] + "[ffffff] " + weak.value + "  "
            desc += "\n"
        if card.resistances != None:
            desc += "Resistances: "
            for res in card.resistances:
                desc += __type_colors__[res.type] + __type_letters__[res.type] + "[ffffff] " + res.value + "  "
            desc += "\n"
        
        desc += "Retreat Cost: "
        if card.convertedRetreatCost:
            desc += str(card.convertedRetreatCost)
        else:
            desc += "0"
    
    return desc
            



#makeFullJson("MyDeckObject", [])
