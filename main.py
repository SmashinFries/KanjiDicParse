from helpers import clearConsole, locate_dictionaries, menu_title, select_input
from XML2JSON import xml2json
from termcolor import colored
from os import path, mkdir
from edrdgDownload import download_menu

def main_menu():
    while True:
        clearConsole()
        available = locate_dictionaries()

        print(menu_title('jpn-dictionaries-cli', 'cyan'))
        print("Dictionaries Found:")
        print(f"kanjidic2: {colored(available['kanji'], color='green' if available['kanji'] else 'red')}")
        print(f"JMdict_e: {colored(available['vocab'], color='green' if available['vocab'] else 'red')}\n")
        
        print(colored("Select an option:", on_color='on_white'))
        print(f"""
        {colored('1', color='magenta')} : Convert XML to JSON
        {colored('2', color='green')} : Navigate Dictionary
        {colored('3', color='blue')} : Download XML Dictionaries
        {colored('0', color='red')} : Exit"""
        )

        choice = select_input()
        if choice == '1':
            xml2json.xml2json(available)
        elif choice == '2':
            print("Chose 2")
        elif choice == '3':
            clearConsole()
            download_menu()
        elif choice == '0':
            clearConsole()
            exit()

if __name__ == "__main__":
    main_menu()