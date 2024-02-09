# [WIP] Pokémon TCG to Tabletop Simulator Decklist Importer

Generates decks for Tabletop Simulator from Pokémon TCG decklists using [PokemonTCG.io API v2](https://pokemontcg.io/)

Inspired by [TTS Deck Converter](https://github.com/jeandeaual/tts-deckconverter) and [Frogtown](https://www.frogtown.me/)


## Features
- Opens decklists from .txt files
- Exports images to be used in TTS custom decks
- Exports json files to be opened as TTS saved objects
- Supports cards from Black and White onwards, including cards after Scarlet and Violet

<img src="https://github.com/NatePlays95/ptcg-tts-decklist-importer/blob/main/readme_image_1.jpeg?raw=true" height="400"><img src="https://github.com/NatePlays95/ptcg-tts-decklist-importer/blob/main/readme_image_2.jpeg?raw=true" height="400">

## Compatible decklist websites
- [pokemoncard.io](https://pokemoncard.io)
- [limitlesstcg.com](https://limitlesstcg.com)
- [ligapokemon.com.br](https://ligapokemon.com.br)


## How to use:
1. Get a [PokémonTCG.io API key](https://dev.pokemontcg.io/)
2. Download the source code in this repo
3. Install Python 3.10 or newer and dependencies:
```sh
pip install pillow
pip install pokemontcgsdk
pip install ratelimit
```
4. Create a file named "api_key.py" in the project's root folder. Include the following code inside it:
```text
API_KEY = "your_api_key_as_string"
```
5. [WIP] Change ``INPUT_FILE`` in "main.py" to your decklist's file name.
6. Run "main.py" with Python. Resulting image will be found in the "exports" folder.
```sh
python main.py
```
   
