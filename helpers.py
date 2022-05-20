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

    # Check/Create user_data folder
    if (path.exists('./user_data/')):
        if (path.exists('./user_data/xml/')):
            if (path.exists('./user_data/xml/kanjidic2.xml')):
                availability['kanji'] = True
            if (path.exists('./user_data/xml/JMdict_e_examp.xml')):
                availability['vocab'] = True
        else:
            mkdir('./user_data/xml/')
    else:
        mkdir('./user_data/')
        mkdir('./user_data/xml/')
        mkdir('./user_data/json/')

    return availability

def getTotalAmount(root:Element):
    return len(root)-1