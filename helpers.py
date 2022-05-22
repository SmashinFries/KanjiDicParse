import platform
from os import path, system, mkdir
from pyfiglet import Figlet
from termcolor import colored
import xml.etree.ElementTree as ET
from xml.dom.minidom import Element

def parseXML(xmlFile:str):
    tree = ET.parse(xmlFile);
    root = tree.getroot();
    return root

def clearConsole():
    system('clear' if platform.system() == 'Linux' else 'cls')

def menu_title(title:str, color:str):
    message = Figlet()
    return colored(message.renderText(title), color)

def select_input():
    return input(colored("\n>> ", color='yellow'))

def locate_dictionaries():
    availability = {'kanji':False, 'vocab':False}
    user_data = path.exists('./user_data/')
    xml_folder = path.exists('./user_data/xml/')
    kanji_dic = path.exists('./user_data/xml/kanjidic2.xml')
    vocab_dic = path.exists('./user_data/xml/JMdict_e_examp.xml')
    json_folder = path.exists('./user_data/json/')
    sql_folder = path.exists('./user_data/sqlite/')

    # Check/Create user_data folder
    if (kanji_dic):
        availability['kanji'] = True
    if (vocab_dic):
        availability['vocab'] = True

    mkdir('./user_data/') if not user_data else None
    mkdir('./user_data/xml/') if not xml_folder else None
    mkdir('./user_data/json/') if not json_folder else None
    mkdir('./user_data/sqlite/') if not sql_folder else None

    return availability

def getTotalAmount(root:Element):
    return len(root)-1