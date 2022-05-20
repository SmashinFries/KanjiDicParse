from helpers import clearConsole, locate_dictionaries, menu_title, select_input
from XML2JSON import xml2json
from termcolor import colored
from os import path, mkdir
from edrdgDownload import download_menu

def convertType_menu(available):
    while True:
        clearConsole()
        print(colored("Choose output type:", on_color='on_green'))
        print(f"""
        {colored('1', color='magenta')} : JSON
        {colored('2', color='blue')} : SQLite
        {colored('0', color='red')} : Go Back"""
        )
        # {colored('2', color='green')} : Navigate Dictionary

        choice = select_input()
        if choice == '1':
            xml2json.xml2json(available)
        elif choice == '2':
            return
        elif choice == '0':
            return

def main_menu():
    while True:
        clearConsole()
        available = locate_dictionaries()

        print(menu_title('JD-CLI', 'cyan'))
        print("Dictionaries Found:")
        print(f"kanjidic2: {colored(available['kanji'], color='green' if available['kanji'] else 'red')}")
        print(f"JMdict_e_examp: {colored(available['vocab'], color='green' if available['vocab'] else 'red')}\n")
        
        print(colored("Select an option:", on_color='on_white'))
        print(f"""
        {colored('1', color='magenta')} : Convert XML
        {colored('2', color='blue')} : Download XML Dictionaries
        {colored('0', color='red')} : Exit"""
        )
        # {colored('2', color='green')} : Navigate Dictionary

        choice = select_input()
        if choice == '1':
            convertType_menu(available)
        # elif choice == '2':
        #     print("Chose 2")
        elif choice == '2':
            clearConsole()
            download_menu()
        elif choice == '0':
            clearConsole()
            exit()

if __name__ == "__main__":
    main_menu()