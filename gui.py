import eel
from modules.parser import parseDecklistLines
from modules.image_manip import makeDeckFromCardListWeb


@eel.expose
def handle_deck_list(text:str):
    print("gerando deck...")
    cards_list = text.split('\n')
    cards_list = parseDecklistLines(cards_list)
    makeDeckFromCardListWeb("deck_list", cards_list)
    print("deck pronto.")
    eel.on_deck_finished()

@eel.expose # Expose this function to Javascript
def say_hello_py(x):
    print('content:\n%s' % x)

eel.init('static_web_folder')
eel.start('index.html',mode='default') # mode default to open on user's default browser, not just chome
