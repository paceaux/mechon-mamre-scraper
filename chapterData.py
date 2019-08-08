from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import urllib, os, sys, getopt, json, collections
from fetchPages import get_page

CHAPTER_MARKER = 'Chapter '

def get_chapter_title(html):
    try:
        title = {'hebrew': '', 'english': ''}
        titleWrap = html.find('h1', attrs={'align':'CENTER'})
        hebWrap = titleWrap.find('span', attrs={'class':'h'})
        hebTitle = hebWrap.text
        fullTitle = titleWrap.text
        engTitle = fullTitle.replace(hebTitle, '')

        title['hebrew'] = hebTitle.strip()
        title['english'] = engTitle.strip()

        return title
    except Exception as error:
        print(error)

def get_verse_from_html(tr):
    try: 
        hVerseEl = tr.select('td.h')[0]
        hVerseTextEls = hVerseEl.find('b').next_siblings
        eVerseTextEls = hVerseEl.next_sibling.find('b').next_siblings

        hVerseText = ''
        eVerseText = ''

        for hVerseTextEl in hVerseTextEls:
            if (hasattr(hVerseTextEl, 'string') and hVerseTextEl.string is not None):
                hVerseText =  hVerseText + hVerseTextEl.string 

        for eVerseTextEl in eVerseTextEls:
                if (hasattr(eVerseTextEl, 'string') and eVerseTextEl.string is not None):
                    eVerseText = eVerseText + eVerseTextEl.string

        verse = {'hebrew': hVerseText.strip(), 'english': eVerseText.strip() }

        return verse
    except Exception as error:
        print(error)
        print(hVerseTextEls)
        print('hebrew verse', hVerseText)
        print('english verse', eVerseText)

def get_chapter_verses(html):
    verses = {}
    versesWrapper = html.select('table[width="100%"][cellspacing="4"]')[0]
    versesElements = versesWrapper.select('tr')
    verseNumber = 1
    
    for verseElement in versesElements:
        verse = get_verse_from_html(verseElement)
        verse['verseNumber'] = verseNumber
        verses[verseNumber] = verse
        verseNumber += 1

    return verses

def get_chapter_number(englishTitle):
    try:
        chapter_marker_len = len(CHAPTER_MARKER)
        chapter_number_index = englishTitle.index(CHAPTER_MARKER) + chapter_marker_len
        chapter_number = englishTitle[chapter_number_index:]
    except Exception as error:
        print(error)

    return chapter_number

def get_book_name(englishTitle):
    try:
        chapter_number_index = englishTitle.index(CHAPTER_MARKER)
        book_name = englishTitle[:chapter_number_index]

        return book_name
    except Exception as error:
        print(error)

def get_chapter_data_from_html(html):
        chapter_data = {}
        title = get_chapter_title(html)
        verses = get_chapter_verses(html)
        chapter_number = int(get_chapter_number(title['english']))

        chapter_data['chapterNumber'] = chapter_number
        chapter_data['canonicalTitle'] = title['english']
        chapter_data['verses'] = verses

        return chapter_data

def get_chapter_data(url):
    try:
        pageHtml = get_page(url)
        chapter_data = get_chapter_data_from_html(pageHtml)

        return chapter_data

    except Exception as error:
        print(error)



