from os import system
import platform, json
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
from termcolor import colored
from collections import Counter
from tqdm import tqdm

from helpers import getTotalAmount

def parseXML(xmlFile:str):
    tree = ET.parse(xmlFile);
    root = tree.getroot();
    return root

def findIndex(id:int):
    root = parseXML('./user_data/xml/JMdict_e_examp.xml')
    count = 0
    for elem in root:
        count +=1
        if elem[0].text == str(id):
            print(count-1)
            break

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

def getKeRe(tag:Element, ke_obj:object, re_obj:object):
    elements = ['ke_pri', 'ke_inf', 're_pri', 're_inf', 're_nokanji', 're_restr']
    ke = ['ke_pri', 'ke_inf']
    re = ['re_pri', 're_inf', 're_nokanji', 're_restr']
    no_append = ['keb', 'reb']
    for elem in elements:
        if tag.tag == elem and tag.tag in ke:
            ke_obj[elem].append(tag.text)
        if tag.tag == elem and tag.tag in re:
            re_obj[elem].append(tag.text)
    
    for elem in no_append:
        if tag.tag == elem and elem == 'keb':
            ke_obj[elem] = tag.text
        if tag.tag == elem and elem == 'reb':
            re_obj[elem] = tag.text

def getSense(tag:Element):
    lang_attrib = '{http://www.w3.org/XML/1998/namespace}lang'
    def getExample(example_elem:Element):
        example = {'source':{'id':None, 'text':None}, 'text': None, 'sentence': {'jpn':None, 'eng':None}}
        for elem in example_elem:
            if elem.tag == 'ex_srce':
                example['source']['id'] = elem.text
                example['source']['text'] = elem.attrib['exsrc_type']
            if elem.tag == 'ex_text':
                example['text'] = elem.text
            if elem.tag == 'ex_sent' and elem.attrib[lang_attrib] == 'jpn':
                example['sentence']['jpn'] = elem.text
            if elem.tag == 'ex_sent' and elem.attrib[lang_attrib] == 'eng':
                example['sentence']['eng'] = elem.text
        return example
        
    sense_obj = {'pos':[], 'gloss':[], 'xref':[], 'ant':[], 'field':[], 'misc':[], 'lsource':[], 'dial':[], 'pri':[], 's_inf':[], 'example':None}
    senses = ['pos', 'gloss', 'xref', 'ant', 'field', 'misc', 'lsource', 'dial', 'pri', 's_inf']
    
    for elem in tag:
        # print(colored(f'{elem.tag}: {elem.text}', color='cyan'))
        for sense in senses:
            if elem.tag == sense:
                if elem.tag == 'lsource':
                    lsource = {'lang':elem.attrib[lang_attrib], 'text':elem.text, 'ls_wasei':True if 'ls_wasei' in elem.attrib else False}
                    sense_obj['lsource'].append(lsource)
                else:
                    sense_obj[sense].append(elem.text)
        if elem.tag == 'example':
            example_obj = getExample(elem)
            sense_obj['example'] = example_obj
    
    return sense_obj

def getWord(root:Element, index:int):
    # Total entries: 196321
    # Entries start at root[0]

    id = root[index][0].text
    data = {'id':int(id), 'k_ele':[], 'r_ele':[], 'sense':[]}
    for tag in root[index]:
        k_ele_obj = {'keb':None, 'ke_pri':[], 'ke_inf':[]}
        r_ele_obj = {'reb':None, 're_pri':[], 're_inf':[], 're_nokanji':[], 're_restr':[]}

        for tag2 in tag:
            getKeRe(tag2, k_ele_obj, r_ele_obj)
                
        if tag.tag == 'sense':
            sense_obj = getSense(tag)
            if sense_obj['pos']:
                    data['sense'].append(sense_obj)

            
        if k_ele_obj['keb']:
            data['k_ele'].append(k_ele_obj)
        if r_ele_obj['reb']:
            data['r_ele'].append(r_ele_obj)
    
    return data

def writeVocabJSON():
    vocab = []
    root = parseXML('./user_data/xml/JMdict_e_examp.xml')
    for entry in tqdm(range(getTotalAmount(root))):
        item = getWord(root, entry)
        vocab.append(item)
    
    with open('./user_data/json/vocab_dictV1.json', "w") as outfile:
        json_vocab = json.dumps(vocab, indent=4, ensure_ascii=False)
        outfile.write(json_vocab)
    
# findIndex(1014440)