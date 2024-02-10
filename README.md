# Pokémon TCG to Tabletop Simulator Decklist Importer

Generates decks for Tabletop Simulator from Pokémon TCG decklists using [PokemonTCG.io API v2](https://pokemontcg.io/)

Inspired by [TTS Deck Converter](https://github.com/jeandeaual/tts-deckconverter) and [Frogtown](https://www.frogtown.me/)

## Features
- Exports json files to be opened as TTS saved objects
- Exports images to be used in TTS custom decks
- Script opens decklists from .txt files
- Has a GUI executable to help with usability
- Supports cards from Black and White onwards, including cards after Scarlet and Violet

<img src="https://github.com/NatePlays95/ptcg-tts-decklist-importer/blob/main/readme_image_1.jpeg?raw=true" height="400"><img src="https://github.com/NatePlays95/ptcg-tts-decklist-importer/blob/main/readme_image_2.jpeg?raw=true" height="400">

## Compatible decklist websites
- [pokemoncard.io](https://pokemoncard.io)
- [limitlesstcg.com](https://limitlesstcg.com)
- [ligapokemon.com.br](https://ligapokemon.com.br)

## How to use the GUI executable
?

## How to use the Python scripts
1. ~~Get a [PokémonTCG.io API key](https://dev.pokemontcg.io/)~~ Works entirely without API keys, but feel free to add those yourself to make the queries faster.
2. Download the source code in this repo
3. Install Python 3.10 or newer and dependencies:
```sh
pip install pillow
pip install ratelimit
pip install requests
pip install pokemontcgsdk
```
5. Change ``INPUT_FILE`` in "main.py" to your decklist's file name.
6. Run "main.py" with Python from your terminal or IDE of choice. Resulting image will be found in the "exports" folder.
```sh
python main.py
```

## Build instructions
To build the GUI app, run:
```sh
pyinstaller decklist-importer-gui.py --onefile --add-data "assets:assets"
```

## Future plans
- Automatically find TTS's vault/chest/saves folder
- Support for importing cube draft lists from PokemonCard
- Support for cards from HGSS and older
