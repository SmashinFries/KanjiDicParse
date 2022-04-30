from xml.etree.ElementTree import Element

def checkElement(element:Element):
    if element == None:
        return None
    else:
        return element.text

def getLiteral(character:Element):
    return character.find('literal').text

# Simplified function of getCodePoints and getRadicals
# Can extract parent tag children attrib and text
def getCpRad(character:Element, parent:str, tag:str, attrib:str):
    data = []
    
    parent = character.find(parent)
    child = parent.findall(tag)
    for value in child:
        data.append({'type':value.attrib[attrib], 'value':value.text})

    return data

# Individual functions to get codepoints and radicals
def getCodePoints(character:Element):
    codepoints = []
    
    codepoint = character.find('codepoint')
    cp_value = codepoint.findall('cp_value')
    for codepoint in cp_value:
        codepoints.append({'type':codepoint.attrib['cp_type'], 'value':codepoint.text})

    return codepoints

def getRadicals(character:Element):
    radicals = []

    radical = character.find('radical')
    rad_value = radical.findall('rad_value')
    for radical in rad_value:
        radicals.append({'type':radical.attrib['rad_type'], 'value':radical.text})
    
    return radicals

def getMisc(character:Element):
    misc = character.find('misc')
    if misc != None:
        grade = checkElement(misc.find('grade'))
        stroke_count = checkElement(misc.find('stroke_count'))
        freq = checkElement(misc.find('freq'))
        rad_name = checkElement(misc.find('rad_name'))
        jlpt = checkElement(misc.find('jlpt'))

        variant_data = misc.find('variant')
        variant = {'type':variant_data.attrib['var_type'], 'value':variant_data.text} if variant_data else None

        misc_data = {'grade':grade, 'stroke_count':stroke_count, 'freq':freq, 'rad_name':rad_name, 'jlpt':jlpt, 'variant':variant}
    else:
        misc_data = None
    return misc_data