from XML2JSON.kanjiconvert import writeJSON, writeJSON2
from XML2JSON.vocabconvert import writeVocabJSON
from helpers import clearConsole, select_input
from termcolor import colored

def version_menu(dic:str):
    clearConsole()
    print(colored("Select Type of JSON", on_color='on_green'))
    print(colored("\nDictionary: " + dic, color="cyan"))
    if dic == 'Kanji':
        print(f"""
        {colored('1', color='magenta')} : Objects stored in a big list
        {colored('2', color='green')} : No list, each object is keyed by kanji literal
        {colored('0', color='red')} : Go Back"""
        )
        choice = select_input()
        if choice == '1':
            print(colored("Parsing XML!\n", on_color='on_green'))
            writeJSON()
            print(colored("\nSaved at: ./json/", on_color="on_cyan"))
            print(colored("またね！", on_color="on_red"))
        elif choice == '2':
            print(colored("Parsing XML!\n", on_color='on_green'))
            writeJSON2()
            print(colored("\nSaved at: ./json/", on_color="on_cyan"))
            print(colored("またね！", on_color="on_red"))
        elif choice == '0':
            exit()
    
    elif dic == 'Vocab':
        print(f"""
        {colored('1', color='magenta')} : Objects stored in a big list
        {colored('0', color='red')} : Go Back"""
        )
        choice = select_input()
        if choice == '1':
            print(colored("Parsing XML!\n", on_color='on_green'))
            writeVocabJSON()
            print(colored("\nSaved at: ./user_data/json/", on_color="on_cyan"))
            print(colored("またね！", on_color="on_red"))
        elif choice == '0':
            exit()

def xml2json(avaiable):
    option1 = f"{colored('1', color='magenta')} : Kanji Dictionary"
    option2 = f"{colored('2', color='green')} : Vocabulary Dictionary"
    
    clearConsole()
    while True:
        print(colored("Use Kanji or Vocab Dictionary?", on_color='on_green'))
        print(f"""
        {option1 if avaiable['kanji'] else 'Please add kanjidic2.xml to /user_data/xml/ folder'}
        {option2 if avaiable['vocab'] else 'Please add JMdict_e.xml to /user_data/xml/ folder'}
        {colored('0', color='red')} : Go back"""
        )

        selectedDictionary = select_input()
        if selectedDictionary == '1':
            version_menu(dic='Kanji')
        elif selectedDictionary == '2':
            version_menu(dic='Vocab')
        elif selectedDictionary == '0':
            clearConsole()
            return