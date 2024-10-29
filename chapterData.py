# chapterData.py
from fetchPages import get_page
import re
from tanakhVerseValidator import validate_verses

CHAPTER_MARKER = 'Chapter '

def get_chapter_title(html):
    try:
        title = {'hebrew': '', 'english': ''}
        titleWrap = html.find('h1', class_='center')
        hebWrap = titleWrap.find('span', class_='h')
        hebTitle = hebWrap.text.strip()
        engTitle = titleWrap.text.replace(hebWrap.text, '').strip()

        title['hebrew'] = hebTitle
        title['english'] = engTitle

        return title
    except Exception as error:
        print('Error in get_chapter_title:', error)
        return {'hebrew': '', 'english': ''}

def get_verse_from_html(tr):
    try:
        tds = tr.find_all('td')
        if len(tds) != 2:
            # Not a verse line
            return None

        hVerseEl, eVerseEl = tds

        # Check if the first td has class 'h'
        if 'class' in hVerseEl.attrs and 'h' in hVerseEl.attrs['class']:
            # Hebrew text
            hVerseNumberEl = hVerseEl.find('b')
            hText = ''
            if hVerseNumberEl:
                hVerseNumber = hVerseNumberEl.get_text(strip=True)
                # Get all siblings after the verse number
                hTextFragments = []
                for elem in hVerseNumberEl.next_siblings:
                    if isinstance(elem, str):
                        text = elem.strip()
                        if text:
                            hTextFragments.append(text)
                    elif elem.name == 'a':
                        # Skip <a> elements (like {פ}, {ס})
                        continue
                    else:
                        text = elem.get_text(strip=True)
                        if text:
                            hTextFragments.append(text)
                hText = ''.join(hTextFragments)
                # Remove any {...} patterns
                hText = re.sub(r'\{.*?\}', '', hText)
            else:
                hText = hVerseEl.get_text(strip=True)
                hText = re.sub(r'\{.*?\}', '', hText)

            # English text
            eVerseNumberEl = eVerseEl.find('b')
            eText = ''
            if eVerseNumberEl:
                eVerseNumber = eVerseNumberEl.get_text(strip=True)
                eTextFragments = []
                for elem in eVerseNumberEl.next_siblings:
                    if isinstance(elem, str):
                        text = elem.strip()
                        if text:
                            eTextFragments.append(text)
                    elif elem.name == 'a':
                        # Skip <a> elements (like {P}, {S})
                        continue
                    else:
                        text = elem.get_text(strip=True)
                        if text:
                            eTextFragments.append(text)
                eText = ' '.join(eTextFragments)
                # Remove any {...} patterns
                eText = re.sub(r'\{.*?\}', '', eText)
            else:
                eText = eVerseEl.get_text(strip=True)
                eText = re.sub(r'\{.*?\}', '', eText)

            verse = {'hebrew': hText.strip(), 'english': eText.strip()}
            return verse
        else:
            # Not a verse line
            return None
    except Exception as error:
        print('Error in get_verse_from_html:', error)
        return None

def get_chapter_verses(html):
    verses = {}
    versesWrapper = html.select('table[width="100%"][cellspacing="4"]')
    if not versesWrapper:
        print('Error: Verses table not found.')
        return verses

    versesWrapper = versesWrapper[0]
    tr_elements = versesWrapper.find_all('tr')
    verseNumber = 1

    for tr in tr_elements:
        verse = get_verse_from_html(tr)
        if verse:
            verse['verseNumber'] = verseNumber
            verses[verseNumber] = verse
            verseNumber += 1
        else:
            # Skip non-verse rows
            continue

    return verses

def get_chapter_number(englishTitle):
    match = re.search(r'Chapter (\d+)', englishTitle)
    if match:
        return int(match.group(1))
    else:
        return 0

def get_book_name(englishTitle):
    try:
        chapter_index = englishTitle.index('Chapter')
        book_name = englishTitle[:chapter_index].strip()
        return book_name
    except Exception as error:
        print('Error in get_book_name:', error)
        return englishTitle.strip()

def get_chapter_data_from_html(html):
    chapter_data = {}
    title = get_chapter_title(html)
    verses = get_chapter_verses(html)
    chapter_number = get_chapter_number(title['english'])
    book_name = get_book_name(title['english'])

    chapter_data['chapterNumber'] = chapter_number
    chapter_data['canonicalTitle'] = title['english']
    chapter_data['bookName'] = book_name
    chapter_data['verses'] = verses

    # Validate total verse count using bible_verse_validator
    total_verses = len(verses)
    valid = validate_verses(book_name, chapter_number=chapter_number, total_verses=total_verses)  # Adjust book_number as needed
    if not valid:
        #print(f"Warning: {book_name} Chapter {chapter_number} has an unexpected verse count ({total_verses}).")
        pass

    return chapter_data

def get_chapter_data(url):
    try:
        pageHtml = get_page(url)
        chapter_data = get_chapter_data_from_html(pageHtml)
        return chapter_data
    except Exception as error:
        print('Error in get_chapter_data:', error)
        return {}
