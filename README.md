# Pokémon TCG to Tabletop Simulator Decklist Importer

Generates decks for Tabletop Simulator from Pokémon TCG decklists using [PokemonTCG.io API v2](https://pokemontcg.io/)

Inspired by [TTS Deck Converter](https://github.com/jeandeaual/tts-deckconverter) and [Frogtown](https://www.frogtown.me/)

<img src="https://github.com/NatePlays95/ptcg-tts-decklist-importer/blob/main/readme_image_3.png?raw=true" height="400">


## Features
- Supports cards from Black and White onwards, including cards after Scarlet and Violet
- Compatible with decklists from: [pokemoncard.io](https://pokemoncard.io) | [limitlesstcg.com](https://limitlesstcg.com) | [ligapokemon.com.br](https://ligapokemon.com.br) 

GUI:
- Exports json files to be opened as TTS saved objects
- Cards from the json have a transcript of the original card in their description
- Supports custom card backs to emulate card sleeves

Python Script:
- Also exports images to be used in TTS custom decks
- Can be set up with an API KEY from PokemonTCG.io to make decks faster.

<img src="https://github.com/NatePlays95/ptcg-tts-decklist-importer/blob/main/readme_image_1.jpeg?raw=true" height="300"><img src="https://github.com/NatePlays95/ptcg-tts-decklist-importer/blob/main/readme_image_2.jpeg?raw=true" height="300">

## How to use the GUI executable

1. Open the executable ``decklist-importer-gui`` in Releases
2. Paste your decklist into the textbox
3. Select a name for your deck (it's the name for the json file too)
4. Choose a image for the back of the cards
5. Click "Generate JSON" and wait. The top bar will be fully blue when finished.

## How to use the Python scripts
1. Download the source code in this repo
2. Install Python 3.10 or newer and dependencies:
    ```sh
    pip install pillow
    pip install ratelimit
    pip install requests
    pip install pokemontcgsdk
    ```
3. Place your decklist inside the source code folder as a .txt file
4. Inside "main.py", change ``INPUT_FILE`` to your decklist's file name, and ``EXPORT_FILENAME`` to the name of the exported files.
5. Run "main.py" with Python from your terminal or IDE of choice. Resulting image will be found in the "exports" folder.
    ```sh
    python main.py
    ```
6. Optionally, to add an API key, make a file named ``api_key.py`` in the repo's source folder and type this inside it:
    ```txt
    API_KEY = "YOUR_API_KEY_HERE_AS_STRING"
    ```

# How to import the resulting files into TTS
### JSON file
1. Open your TTS vault of saved objects. By default it's in ``Documents/My Games/Tabletop Simulator/Saves/Saved Objects``
2. Paste your JSON file inside the Saved Objects folder or one of its subfolders.
3. Open TTS and enter a session, go to Objects > Saved Objects and your deck will be there with a question mark symbol.
### Image Atlas (will not feature descriptions!)
1. Open TTS, go to Objects > Components > Custom and select the Deck. A popup for Custom Deck should appear.
2. For the "Face" field, click the folder icon and select your image atlas. Select the "Cloud" option in the next screen if you want to play with other players.
3. For the "Back" field, you can select any image, custom images will look like card sleeves. Here's a link for the standard card back:
    
    ``http://cloud-3.steamusercontent.com/ugc9980166070720616559BE66430CD3C340060773E321DDD5FD86C1F2703/``
4. Leave the width and height options as they are, and choose the amount of cards your deck has (60 usually), then click Import.

## Build instructions
To build the GUI app, run:
```sh
pyinstaller decklist-importer-gui.py --onefile --add-data "assets:assets"
```

## Future plans
- Automatically find TTS's vault/chest/saves folder
- Support for importing cube draft lists from PokemonCard
- Support for cards from HGSS and older
