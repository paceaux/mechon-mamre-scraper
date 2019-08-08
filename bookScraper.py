import urllib, os, sys, getopt, json, collections
from fetchPages import simple_get
from chapterData import get_chapter_data
from bookData import get_book_data

OUTPUT_DIRECTORY = 'books'

def scrapeBook(url):
    book_data = get_book_data(url)
    sanitized_book_name = book_data['canonicalBookName'].replace(' ', '_').replace('/','+')
    book_file_name = OUTPUT_DIRECTORY + '/' + sanitized_book_name + '.json'

    for chapter_num, chapter_link in book_data['chapters'].items():
        chapter_data = get_chapter_data(chapter_link)
        chapter_data['link'] = chapter_link
        book_data['chapters'][chapter_num] = chapter_data

    with open(book_file_name, 'w') as outfile:
        json.dump(book_data, outfile, indent=4)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'u:', ['url='])
    except getopt.GetoptError:
        print('error with the arguments')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-u', '--url'):
            url = arg

    try:
        scrapeBook(url)

    except Exception as e:
        print('Error With outputting the file')
        print(e)


if __name__ == '__main__':
    main(sys.argv[1:])
