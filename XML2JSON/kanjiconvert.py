from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
import functions, json
from tqdm import tqdm
from termcolor import colored

from helpers import clearConsole, select_input, getTotalAmount

xmlFile = './user_data/xml/kanjidic2.xml'

def parseXML():
    tree = ET.parse(xmlFile);
    root = tree.getroot();
    return root
    # print(root[1][0].text);

def getAll(amount:int):
    root = parseXML()
    data = []
    for i in range(amount+1):
        character = root[i]
        if (i == 0):
            continue
        else:
            literal = functions.getLiteral(character)
            codepoints = functions.getCpRad(character, 'codepoint', 'cp_value', 'cp_type')
            radicals = functions.getCpRad(character, 'radical', 'rad_value', 'rad_type')
            misc = functions.getMisc(character)

            data.append({'literal': literal, 'codepoints': codepoints, 'radicals': radicals, 'misc': misc})
    if (amount == 1):
        print(data[0])
    else:
        print(data)

def getKanji(element:int, root:Element, array:bool):
    kanji = {}
    character = root[element]

    literal = functions.getLiteral(character)
    codepoints = functions.getCpRad(character, 'codepoint', 'cp_value', 'cp_type')
    radicals = functions.getCpRad(character, 'radical', 'rad_value', 'rad_type')
    misc = functions.getMisc(character)
    dictionaries = functions.getDic(character)
    query_codes = functions.getCpRad(character, 'query_code', 'q_code', 'qc_type')
    readings = functions.getReadings(character)
    names = functions.getCpRad(character, 'reading_meaning', 'nanori', None)

    if (array):
        kanji = {
            'literal': literal,
            'codepoints': codepoints,
            'radicals': radicals,
            'misc': misc,
            'dictionaries': dictionaries,
            'query_codes': query_codes,
            'readings': readings['readings'],
            'meanings': readings['meanings'],
            'names': names
        }
    else:
        kanji = {
            literal: {
                'literal': literal,
                'codepoints': codepoints,
                'radicals': radicals,
                'misc': misc,
                'dictionaries': dictionaries,
                'query_codes': query_codes,
                'readings': readings['readings'],
                'meanings': readings['meanings'],
                'names': names
            }
        }
    return kanji

# stores kanji in an array
def writeJSON():
    kanjis = []
    root = parseXML()
    for kanji in tqdm(range(getTotalAmount(root))):
        item = getKanji(kanji+1, root, True)
        kanjis.append(item)

    with open('./user_data/json/kanji_dictV1.json', "w") as outfile:
        json_kanji = json.dumps(kanjis, indent=4, ensure_ascii=False)
        outfile.write(json_kanji)

# kanji is key instead. no array
def writeJSON2():
    root = parseXML()
    json_data = {}
    def Merge(dict1, dict2):
        res = dict1 | dict2
        return res

    for kanji in tqdm(range(getTotalAmount(root)), colour='magenta'):
        item = getKanji(kanji+1, root, False)
        json_data = Merge(json_data, item)

    with open('./user_data/json/kanji_dictV2.json', "w") as outfile:
        json_kanji = json.dumps(json_data, indent=4, ensure_ascii=False)
        outfile.write(json_kanji)