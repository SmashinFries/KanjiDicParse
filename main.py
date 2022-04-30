import xml.etree.ElementTree as ET
import functions

xmlFile = 'kanjidic2.xml'

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

def getKanji(element:int):
    root = parseXML()
    character = root[element]

    literal = functions.getLiteral(character)
    codepoints = functions.getCpRad(character, 'codepoint', 'cp_value', 'cp_type')
    radicals = functions.getCpRad(character, 'radical', 'rad_value', 'rad_type')
    misc = functions.getMisc(character)

    print({'literal': literal, 'codepoints': codepoints, 'radicals': radicals, 'misc': misc})

getKanji(6)