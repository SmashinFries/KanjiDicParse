from XML2JSON.kanjiconvert import version_menu
from helpers import clearConsole, menu_title, select_input
from termcolor import colored

def xml2json(avaiable):
    option1 = f"{colored('1', color='magenta')} : Kanji Dictionary"
    option2 = f"{colored('2', color='green')} : Vocabulary Dictionary"

    while True:
        clearConsole()
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
            exit()
        elif selectedDictionary == '0':
            clearConsole()
            return