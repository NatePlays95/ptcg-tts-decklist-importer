from functools import partial
import threading
import traceback
from customtkinter import *
import modules.utils as utils
import modules.parser as parser
import modules.json_builder as json_builder

# pieces
global PROGRESS_BAR
global TABS
global TEXTBOX_DECKLIST
global ENTRY_DECKNAME
global CTKVAR_COMBOBOXBACK
global ENTRY_CUSTOMCARDBACK
global BTN_GENERATE_JSON

CHOSEN_CARDBACK = "Standard"









def setupApp():
    app = CTk()
    app.geometry("860x640")
    return app

def createElements(app):
    global PROGRESS_BAR
    PROGRESS_BAR = CTkProgressBar(app, orientation="horizontal", mode="determinate", determinate_speed=1, width=2000, height=20, corner_radius=0)
    PROGRESS_BAR.pack(anchor="n")
    PROGRESS_BAR.set(0)
    utils.addProgressCallback(onProgressIncreased)
    utils.resetProgress()

    global TABS
    TABS = CTkTabview(master=app, width=800, height=600)
    TABS.pack(expand=True, padx=20, pady=20, anchor="center")
    TABS.add("Export as JSON Object")  # add tab at the end
    #TABS.add("Export as Card Sheet")  # add tab at the end

    createTabJsonElements(TABS.tab("Export as JSON Object"))


def createTabJsonElements(tab):
    label_decklist = CTkLabel(master=tab, width=400, text="Decklist:", font=("Rubik", 20))
    label_decklist.pack(padx=20,pady=10)

    global TEXTBOX_DECKLIST
    TEXTBOX_DECKLIST = CTkTextbox(master=tab, width=400, height=200, wrap="none")
    TEXTBOX_DECKLIST.pack()
    TEXTBOX_DECKLIST.insert("0.0", "Paste your decklist here.")

    label_deckname = CTkLabel(master=tab, width=400, text="Deck name:", font=("Rubik", 20))
    label_deckname.pack(padx=20, pady=10)

    global ENTRY_DECKNAME
    ENTRY_DECKNAME = CTkEntry(master=tab, width=400, placeholder_text="My Custom Deck 1")
    ENTRY_DECKNAME.pack()

    frame_back = CTkFrame(tab, width=400)
    frame_back.pack(padx=20, pady=10)
    label_back = CTkLabel(master=frame_back, text="Card back texture:", font=("Rubik", 20))
    label_back.grid(row=0, column=0, padx=20, pady=10)
    global CTKVAR_COMBOBOXBACK
    CTKVAR_COMBOBOXBACK = StringVar(value="Standard") 
    combobox_back = CTkComboBox(master=frame_back, state="readonly", values=["Standard", "Japanese", "Custom"], variable=CTKVAR_COMBOBOXBACK, command=onComboboxBackClicked)
    #combobox_back.bind('<<ComboboxSelected>>',onComboboxBackClicked)
    combobox_back.grid(row=0, column=1, padx=20, pady=10)
    
    global ENTRY_CUSTOMCARDBACK
    ENTRY_CUSTOMCARDBACK = CTkEntry(master=frame_back, width=400, height=30, placeholder_text="https://forum.tcgone.net/uploads/default/original/2X/7/77fe3f5ed22d5ffb44fa2ccff4a441ee2983b3ec.png")

    global BTN_GENERATE_JSON
    BTN_GENERATE_JSON = CTkButton(tab, text="Generate JSON", font=("Rubik bold", 20), width=230, command=onBtnGenerateJsonClicked)
    BTN_GENERATE_JSON.pack(padx=20, pady=20, ipady=10)


def onProgressIncreased(current_progress):
    PROGRESS_BAR.step()


def onComboboxBackClicked(choice):
   # choice = CTKVAR_COMBOBOXBACK
    global CHOSEN_CARDBACK
    CHOSEN_CARDBACK = choice
    #print(choice)
    global ENTRY_CUSTOMCARDBACK
    if choice == "Custom":
        ENTRY_CUSTOMCARDBACK.grid(row=1, columnspan=2)
    else:
        ENTRY_CUSTOMCARDBACK.grid_forget()


def onBtnGenerateJsonClicked():
    BTN_GENERATE_JSON.configure(state="disabled", text="Generating...")
    TABS.configure(state="disabled")
    PROGRESS_BAR.set(0)

    thread = threading.Thread(target=generateJson)
    thread.start()
    return


def generateJson():
    try:
        input = TEXTBOX_DECKLIST.get("0.0", "end")
        filename = ENTRY_DECKNAME.get()
        PROGRESS_BAR.step()
        cards_list = parser.parseDecklistLines(input.splitlines())
        PROGRESS_BAR.step()
        PROGRESS_BAR.step()
        PROGRESS_BAR.step()
        json_builder.makeFullJson(filename, cards_list, CHOSEN_CARDBACK)
        PROGRESS_BAR.set(1)
    except Exception as e:
        print(f'ERROR: {e}, {traceback.format_exc()}')
        PROGRESS_BAR.set(0)
    
    utils.resetProgress()
    BTN_GENERATE_JSON.configure(state="normal", text="Generate JSON")
    TABS.configure(state="normal")


app = setupApp()
createElements(app)

app.mainloop()