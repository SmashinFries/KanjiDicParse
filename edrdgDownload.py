import requests, gzip, shutil, os
from termcolor import colored
from helpers import clearConsole, locate_dictionaries, select_input
from tqdm import tqdm

def downloadZIP(url:str, filename:str):
    with requests.get(url, stream=True) as r:
        total_length = int(r.headers.get('content-length'))

        with tqdm.wrapattr(r.raw, "read", total=total_length) as raw:
            with open(f'./user_data/xml/{filename}', 'wb') as zip_out:
                shutil.copyfileobj(raw, zip_out)

def extractZIP(filename:str):
    extracted_name = filename[:len(filename)-2] if '.xml' in filename else filename[:len(filename)-2] + 'xml'
    with gzip.open(f'./user_data/xml/{filename}', 'rb') as f_in:
        with open(f'./user_data/xml/{extracted_name}', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def download_xml(url:list):
    for link in url:
        filename = link.rsplit('/', 1)[1]
        print(colored(f" Downloading {filename[:len(filename)-2]}... \n", on_color='on_green'))
        downloadZIP(link, filename)
        print(colored("\n Extracting... ", on_color='on_blue'))
        extractZIP(filename)
        os.remove(f'./user_data/xml/{filename}')
        clearConsole()

    print(colored(" Successful! ", on_color='on_green'))

def download_menu():
    vocabUrl = 'http://ftp.edrdg.org/pub/Nihongo/JMdict_e_examp.gz'
    kanjiUrl = 'http://www.edrdg.org/kanjidic/kanjidic2.xml.gz'

    def isDownloaded(num:str, color:str, truthy:bool, message:str):
        if truthy:
            return colored(num+message, on_color=f'on_{color}')
        else:
            return colored(num, color=color) + message

    while True:
        downloaded = locate_dictionaries()
        print(colored(' Select Download ', on_color='on_cyan'))
        print("*Highlighted items already exist.*")
        print(f"""
        {isDownloaded('1', 'magenta', True if downloaded['kanji'] and downloaded['vocab'] else False, ' : All')}
        {isDownloaded('2', 'green', downloaded['kanji'], ' : Kanji Dictionary')}
        {isDownloaded('3', 'blue', downloaded['vocab'], ' : Vocabulary Dictionary')}
        {colored('4', color='white')} : Remove Downloaded XML
        {colored('0', color='red')} : Go Back"""
        )
        choice = select_input()

        if choice == '1':
            download_xml([kanjiUrl, vocabUrl])
        elif choice == '2':
            download_xml([kanjiUrl])
        elif choice == '3':
            download_xml([vocabUrl])
        elif choice == '4':
            if os.path.exists('./user_data/xml/kanjidic2.xml'):
                os.remove('./user_data/xml/kanjidic2.xml')
            if os.path.exists('./user_data/xml/JMdict_e_examp.xml'):
                os.remove('./user_data/xml/JMdict_e_examp.xml')
            clearConsole()
            print(colored(" Removed! ", on_color='on_green'))
        elif choice == '0':
            clearConsole()
            return
