from helpers import clearConsole, select_input
from termcolor import colored
from JSON2SQL import sqlconvert

def sql_menu():
    while True:
        clearConsole()
        print(colored("Choose output type:", on_color='on_green'))
        print(f"""
        {colored('1', color='magenta')} : Kanji
        {colored('2', color='blue')} : Vocabulary
        {colored('0', color='red')} : Go Back"""
        )

        choice = select_input()
        if choice == '1':
            sqlconvert.json_sql('kanji')
        elif choice == '2':
            sqlconvert.json_sql('vocab')
        elif choice == '0':
            return
