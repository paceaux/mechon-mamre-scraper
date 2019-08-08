import urllib, os, sys, getopt, json, collections
from fetchPages import simple_get
from bookScraper import scrapeBook

OUTPUT_DIRECTORY = 'books'

def main(argv):
    bookNames = None
    try:
        opts, args = getopt.getopt(argv, 'g:b:', ['g=', 'b='])
    except getopt.GetoptError:
        print('error with the arguments')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-g', '--group'):
            bookGroupName = arg
        if opt in ('-b', '--book'):
            bookNames = arg.split(',')

    try:
        with open('books/tanakhBookLinks.json') as datafile:
            bookList = json.load(datafile)
                
            # scraping a list of books
            if (bookList[bookGroupName] is not None):
                print('scraping from a list of books:' + bookGroupName)

                #list of books, and one book from that list
                if (bookNames is not None):
                    for bookName in bookNames:
                        scrapeBook(bookList[bookGroupName][bookName])

                # list of books, no specific book given
                else:
                    for book, url in bookList[bookGroupName].items():
                        print(url)
                        scrapeBook(url)

    except Exception as e:
        print('Error With outputting the file')
        print(e)


if __name__ == '__main__':
    main(sys.argv[1:])
