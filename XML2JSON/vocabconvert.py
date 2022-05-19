from os import system
import platform
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
from termcolor import colored
from collections import Counter

def parseXML(xmlFile:str):
    tree = ET.parse(xmlFile);
    root = tree.getroot();
    return root

def viewTree(root:Element, index:int):
    for tag in root[index]:
        print(colored(f' {tag.tag}: {tag.text} ', on_color='on_red'))
        for tag2 in tag:
            print(colored(f'{tag2.tag}: {tag2.text}', color='green'))

def checkKeys(tag:Element, obj:object):
    for key in obj.keys():
        if tag.tag == key:
                obj[key] = tag.text
    
    return obj

def getWord(root:Element, index:int):
    # Total entries: 196321
    # Entries start at root[0]

    id = root[index][0].text
    data = {'id':id, 'k_ele':[], 'r_ele':[]}
    for tag in root[index]:
        k_ele_obj = {'keb':None, 'ke_pri':[], 'ke_inf':[]}
        r_ele_obj = {'reb':None, 're_pri':[], 're_inf':[], 're_nokanji':[], 're_restr':[]}
        for tag2 in tag:
            # k_ele
            if tag2.tag == 'keb':
                k_ele_obj['keb'] = tag2.text
            if tag2.tag == 'ke_pri':
                k_ele_obj['ke_pri'].append(tag2.text)
            if tag2.tag == 'ke_inf':
                k_ele_obj['ke_inf'].append(tag2.text)

            # r_ele
            if tag2.tag == 'reb':
                r_ele_obj['reb'] = tag2.text
            if tag2.tag == 're_pri':
                r_ele_obj['re_pri'].append(tag2.text)
            if tag2.tag == 're_inf':
                r_ele_obj['re_inf'].append(tag2.text)
            if tag2.tag == 're_nokanji':
                r_ele_obj['re_nokanji'].append(tag2.text)
            if tag2.tag == 're_restr':
                r_ele_obj['re_restr'].append(tag2.text)
            
        if k_ele_obj['keb']:
            data['k_ele'].append(k_ele_obj)
        if r_ele_obj['reb']:
            data['r_ele'].append(r_ele_obj)
    
    print(colored(f'\n{data}', color='blue'))

def vocab2JSON():
    system('clear' if platform.system() == 'Linux' else 'cls')
    root = parseXML('./user_data/xml/JMdict_e.xml')
    getWord(root, 56171)

# vocab2JSON()
checkKeys(None)