import json, sqlite3, pandas
from os import path
from sqlite3 import Cursor, Error, Connection
from termcolor import colored

from XML2JSON.kanjiconvert import writeJSON
from XML2JSON.vocabconvert import writeVocabJSON
from helpers import clearConsole, select_input

def create_con(type:str):
    """ 
    make db connection
            Parameters:
                type (int): 'kanji' or 'vocab'
            
            Returns:
                sqlite connection
    """

    file = f'./user_data/sqlite/kanjiDic.sqlite' if type == 'kanji' else f'./user_data/sqlite/vocabDic.sqlite'
    conn = None
    try:
        conn = sqlite3.connect(file)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn

def checkForJSON(type:str):
    """
    Checks if JSON exists.
            Parameters:
                type (str): 'kanji' or 'vocab'
    """
    json1 = path.exists('./user_data/json/kanji_dictV1.json') if type == 'kanji' else path.exists('./user_data/json/vocab_dictV1.json')
    if (json1 == False):
        print(colored("Creating Missing JSON...\n", on_color='on_green'))
        writeJSON() if type == 'kanji' else writeVocabJSON()

def json_sql(type:str):
    """
    Converts JSON to SQL. It will also create the proper JSON file if it doesn't exist.
            Parameters:
                type (str): 'kanji' or 'vocab'
    """
    checkForJSON(type)
    
    file_loc = f'./user_data/json/kanji_dictV1.json' if type == 'kanji' else f'./user_data/json/vocab_dictV1.json'
    with open(file_loc) as json_file:
        data = json.load(json_file)
    
    frame = pandas.DataFrame(data)
    frame = frame.applymap(str)

    conn = create_con(type)
    frame.to_sql(type, conn)