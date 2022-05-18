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
def getCpRad(character:Element, parent:str, tag:str, attrib:str|None):
    data = []
    
    parent = character.find(parent)
    if parent != None:
        child = parent.findall(tag)
        if attrib == None and child != None:
            for item in child:
                data.append(item.text)
        else:
            if child != None:
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

def getDic(character:Element):
    dictions = []

    dic_number = character.find('dic_number')
    if dic_number != None:
        dic_ref = dic_number.findall('dic_ref')
        if dic_ref:
            for dic in dic_ref:
                if (dic.attrib['dr_type'] == 'moro'):
                    volume = dic.attrib.get('m_vol')
                    page = dic.attrib.get('m_page')
                    dictions.append({'type':dic.attrib['dr_type'], 'volume':volume, 'page':page, 'value':dic.text})
                else:
                    dictions.append({'type':dic.attrib['dr_type'], 'value':dic.text})

    return dictions

def getMeanings(rmgroup:Element):
    meaning_elements = rmgroup.findall(".//meaning")
    english_meanings = []
    fr_meanings = []
    es_meanings = []
    pt_meanings = []
    for meaning in meaning_elements:
        if meaning.attrib:
            if meaning.attrib['m_lang'] == 'fr':
                fr_meanings.append(meaning.text)
            elif meaning.attrib['m_lang'] == 'es':
                es_meanings.append(meaning.text)
            elif meaning.attrib['m_lang'] == 'pt':
                pt_meanings.append(meaning.text)
        else:
            english_meanings.append(meaning.text)

    meanings = {
        'english': english_meanings,
        'fr': fr_meanings,
        'es': es_meanings,
        'pt': pt_meanings
    }

    return meanings

def getReadings(character:Element):
    def getAllValues(elements:list[Element]):
        values = []
        for value in elements:
            values.append(value.text)
        return values
    
    # initialize variables
    f_readings = None
    meanings = None

    reading_meaning = character.find('reading_meaning')
    if reading_meaning != None:
        rmgroup = reading_meaning.find('rmgroup')
        
        # foreign readings
        pinyins = rmgroup.findall(".//reading/[@r_type='pinyin']")
        korean_rs = rmgroup.findall(".//reading/[@r_type='korean_r']")
        korean_hs = rmgroup.findall(".//reading/[@r_type='korean_h']")
        vietnams = rmgroup.findall(".//reading/[@r_type='vietnam']")
        ja_on = rmgroup.findall(".//reading/[@r_type='ja_on']")
        ja_kun = rmgroup.findall(".//reading/[@r_type='ja_kun']")

        # meanings
        meanings = getMeanings(rmgroup)
        
        f_readings = {
            'pinyin': getAllValues(pinyins),
            'korean_r': getAllValues(korean_rs),
            'korean_h': getAllValues(korean_hs),
            'vietnam': getAllValues(vietnams),
            'ja_on': getAllValues(ja_on),
            'ja_kun': getAllValues(ja_kun)
        }
        
    return {'readings':f_readings, 'meanings':meanings}