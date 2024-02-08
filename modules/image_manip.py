import os
from io import BytesIO
from PIL import Image, ImageOps
from urllib.request import urlopen
import requests
# SDK
from pokemontcgsdk.cardimage import CardImage
from pokemontcgsdk import Card
# KEY
from api_key import API_KEY




TEST_FILEPATH = os.path.dirname(__file__) + "/../tests/image_manip/"

TEST_URL_PALAFIN_HIRES = "https://images.pokemontcg.io/sv4pt5/225_hires.png"

TEST_API_KEY = ""

## Standard cards since Black and White are available in pokemontcg.io at the same size.
## in hi-res at 734 x 1024, in lo-res at 245 x 342.
## Cards like e-series will have different sizes.

## "Custom decks can be any aspect ratio. The game just cuts whatever image you supply into the 10x7 grid."
## Make decks as big atlas images and split them into 70 cards, 10 wide 7 tall.




#### HIGH RESOLUTION ####

## TODO: change to blank file or something
def getHiresAtlas():
    return Image.open(TEST_FILEPATH + "deck_hires.png")

## 1 indexed.
def getHiresPositionAtIndex(index:int):
    index -= 1
    x = (index % 10) * 734
    y = (index // 10) * 1024
    return [x, y]

def getHiresBackImage(is_japanese=False):
    
    url = "https://images.pokemontcg.io/"
    response = requests.get(url, headers = {"X-Api-Key": API_KEY})
    img = Image.open(BytesIO(response.content))
    img = ImageOps.fit(img, (734, 1024))
    return img
    #return Image.open(TEST_FILEPATH + "charizard_hires.png")

def getHiresCardImage(card_image:CardImage):
    url = card_image.large
    response = requests.get(url, headers = {"X-Api-Key": API_KEY})
    img = Image.open(BytesIO(response.content))
    img = ImageOps.fit(img, (734, 1024))
    return img

#### LOW RESOLUTION ####

# def getHiresPositionAtIndex(index:int):
#     i = index - 1
#     x = (i % 10) * 734
#     y = (i // 10) * 1024
#     return [x, y]

def getLowresCardImage(card_image:CardImage):
    url = card_image.small
    response = requests.get(url, headers = {"X-Api-Key": API_KEY})
    img = Image.open(BytesIO(response.content))
    img = ImageOps.fit(img, (734, 1024)) # TODO: change to actual lowres size
    return img


#### DEBUG TESTS

def test_getHiresPalafin():
    response = requests.get(TEST_URL_PALAFIN_HIRES, headers = {"X-Api-Key": API_KEY})
    img = Image.open(BytesIO(response.content))
    return img

def test_makeDeckHiresCharizard():
    atlas = getHiresAtlas()
    
    # 57 charizards
    for i in range(1, 58):
        charizard = Image.open(TEST_FILEPATH + "charizard_hires.png")
        atlas.paste(charizard, getHiresPositionAtIndex(i))
    
    # palafin at n° 1
    atlas.paste(test_getHiresPalafin(), getHiresPositionAtIndex(1))
    
    # back image at n° 70
    atlas.paste(getHiresBackImage(), getHiresPositionAtIndex(70))
    
    atlas.save(TEST_FILEPATH + "deck_with_charizard.png")

def test_makeDeckHiresCardList(cards_list:list[Card]):
    atlas = getHiresAtlas()
    print("Atlas created.")
    index = 1
    for card in cards_list:
        card_image = card.images
        img = getLowresCardImage(card_image) # TODO: change to hi res after low res is sorted.
        position = getHiresPositionAtIndex(index)
        atlas.paste(img, position) # position goes from x,y to x,y,w,h.
        print("pasted", card.name, "onto atlas, index", index, "and position", position)
        
        index += 1
    # back image at n° 70
    atlas.paste(getHiresBackImage(), getHiresPositionAtIndex(70))
    atlas.save(TEST_FILEPATH + "deck_from_decklist.png")

    print("Atlas saved.")
