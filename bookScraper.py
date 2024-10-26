# bookScraper.py -u <url>
import os
import sys
import getopt
import json
from chapterData import get_chapter_data
from bookData import get_book_data

OUTPUT_DIRECTORY = 'books'

def scrapeBook(url):
    book_data = get_book_data(url)
    sanitized_book_name = book_data['canonicalBookName'].replace(' ', '_').replace('/','+')
    book_file_name = os.path.join(OUTPUT_DIRECTORY, f"{sanitized_book_name}.json")

    for chapter_num, chapter_link in book_data['chapters'].items():
        print(f"Processing Chapter {chapter_num}")
        chapter_data = get_chapter_data(chapter_link)
        chapter_data['link'] = chapter_link
        book_data['chapters'][chapter_num] = chapter_data

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    with open(book_file_name, 'w', encoding='utf-8') as outfile:
        json.dump(book_data, outfile, ensure_ascii=False, indent=4)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'u:', ['url='])
    except getopt.GetoptError:
        print('Usage: bookScraper.py -u <url>')
        sys.exit(2)

    url = None
    for opt, arg in opts:
        if opt in ('-u', '--url'):
            url = arg

    if not url:
        print('Usage: bookScraper.py -u <url>')
        sys.exit(2)

    try:
        scrapeBook(url)
    except Exception as e:
        print('Error with outputting the file')
        print(e)

if __name__ == '__main__':
    main(sys.argv[1:])
