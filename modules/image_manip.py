import os
from PIL import Image

TEST_FILEPATH = os.path.dirname(__file__) + "/../tests/image_manip/"

## Standard cards since Black and White are available in pokemontcg.io at the same size.
## in hi-res at 734 x 1024, in lo-res at 245 x 342.
## Cards like e-series will have different sizes.

## "Custom decks can be any aspect ratio. The game just cuts whatever image you supply into the 10x7 grid."
## Make decks as big atlas images and split them into 70 cards, 10 wide 7 tall.

def makeAtlasHires():
    atlas = Image.open(TEST_FILEPATH + "deck_hires.png")
    charizard = Image.open(TEST_FILEPATH + "charizard_hires.png")
    atlas.paste(charizard, [0,0])
    atlas.save(TEST_FILEPATH + "deck_with_charizard.png")

makeAtlasHires()