import requests
import time
from lxml import etree

list_of_words = [''' list,
                     of,
                     words,
                     to,
                     get,
                     definition''']


for wrd in list_of_words[0].split(',')[1:-1]:

    try:
        word = wrd.replace(" ",'').lower()
        

        url = 'http://www.dictionary.com/browse/{}?s=t'.format(word)
        

        page = requests.get(url)
        soup = page.text
        page.close()

        doc = etree.HTML(soup)

        definition = doc.xpath('//span[@class="css-4x41l7 e10vl5dg6"]')[0]
        print(word)
        print(definition.text)
    except:
        word = wrd.replace(" ",'').lower()
        print(word)

        url = 'http://www.dictionary.com/misspelling?term={}&s=t'.format(word)
        

        page = requests.get(url)
        soup = page.text
        page.close()

        doc = etree.HTML(soup)

        new_word = doc.xpath('//a[@data-linkid="rtxtk5"]')
        new_word = new_word[0].text
        
        url = 'http://www.dictionary.com/browse/{}?s=t'.format(new_word)
        

        page = requests.get(url)
        soup = page.text
        page.close()

        doc = etree.HTML(soup)

        definition = doc.xpath('//span[@class="css-4x41l7 e10vl5dg6"]')[0]
        print('{} ({})'.format(word, new_word))
        print(definition.text)
        


