from fetchPages import get_page
from chapterData import get_chapter_title

BOOK_INFO_SELECTOR= 'table[width="100%"][cellspacing="10"] font'

def get_chapter_links(html):
    chapter_link_wrapper = html.select(BOOK_INFO_SELECTOR)[0]
    chapter_link_els = chapter_link_wrapper.select('a:first-child ~ a[href*="pt"]')
    chapter_links = {}

    for chapter_link_el in chapter_link_els:
        chapter_links[chapter_link_el.text] = chapter_link_el['href']

    return chapter_links

def get_canonical_name(html):
    book_name_wrapper = html.select(BOOK_INFO_SELECTOR)[0]
    book_name_node = book_name_wrapper.select('a:first-child')[0].next_sibling
    book_name = book_name_node.replace('-', '').replace('\n','').strip()

    return book_name

def get_book_data_from_html(html):
    book_data = {}
    canonicalBookName = get_canonical_name(html)
    chapter_links = get_chapter_links(html)

    book_data['canonicalBookName'] = canonicalBookName
    book_data['chapters'] = chapter_links

    return book_data

def get_first_chapter_link(url):
    url_parts = url.split('/')
    url_parts_len = len(url_parts)
    chapter_one_url = url_parts[url_parts_len - 1]

    return chapter_one_url

def get_book_data(url):
    try:
        pageHtml = get_page(url)
        book_data = get_book_data_from_html(pageHtml)
        book_title = get_chapter_title(pageHtml)
        first_chapter_link =  get_first_chapter_link(url)
        full_url_path = url.replace(first_chapter_link, '')

        book_data['bookName'] = book_title
        book_data['chapters']['1'] = first_chapter_link

        for chapterLinkK, chapterLinkV in book_data['chapters'].items():
            book_data['chapters'][chapterLinkK] = full_url_path + chapterLinkV

        return book_data
    
    except Exception as error:
        print(error)