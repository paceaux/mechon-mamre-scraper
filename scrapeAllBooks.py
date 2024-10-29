# scrapeAllBooks.py
import os
import sys
import json
import getopt
from bookScraper import scrapeBook

OUTPUT_DIRECTORY = 'books'

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'g:b:a', ['group=', 'book=', 'all'])
    except getopt.GetoptError:
        print('Usage: scrapeAllBooks.py -g <group> -b <book1,book2> or scrapeAllBooks.py -a')
        sys.exit(2)

    bookGroupName = None
    bookNames = None
    scrape_all = False

    for opt, arg in opts:
        if opt in ('-g', '--group'):
            bookGroupName = arg
        elif opt in ('-b', '--book'):
            bookNames = arg.split(',')
        elif opt in ('-a', '--all'):
            scrape_all = True

    try:
        with open('books/tanakhBookLinks.json', 'r', encoding='utf-8') as datafile:
            bookList = json.load(datafile)

        if scrape_all:
            # Scrape all groups and books
            for group_name, books in bookList.items():
                if group_name == "startUrl":
                    continue
                print(f"Scraping group: {group_name}")
                for book_name, url in books.items():
                    print(f"Scraping book: {book_name}")
                    scrapeBook(url)
        elif bookGroupName and bookGroupName in bookList:
            # Scrape specified group
            if bookNames:
                # Scrape specified books in the group
                for bookName in bookNames:
                    if bookName in bookList[bookGroupName]:
                        print(f"Scraping book: {bookName}")
                        scrapeBook(bookList[bookGroupName][bookName])
                    else:
                        print(f"Book '{bookName}' not found in group '{bookGroupName}'.")
            else:
                # Scrape all books in the specified group
                print(f"Scraping all books in group: {bookGroupName}")
                for book_name, url in bookList[bookGroupName].items():
                    print(f"Scraping book: {book_name}")
                    scrapeBook(url)
        else:
            print('Usage: scrapeAllBooks.py -g <group> -b <book1,book2> or scrapeAllBooks.py -a')
            sys.exit(2)

    except Exception as e:
        print('Error during scraping process')
        print(e)

if __name__ == '__main__':
    main(sys.argv[1:])
