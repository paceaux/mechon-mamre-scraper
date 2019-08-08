import urllib, os, sys, getopt, json, collections
from fetchPages import simple_get
from bookScraper import scrapeBook

OUTPUT_DIRECTORY = 'books'

def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'g:b:', ['g=', 'b='])
    except getopt.GetoptError:
        print('error with the arguments')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-g', '--group'):
            bookGroupName = arg
        if opt in ('-b', '--book'):
            bookName = arg

    try:
        with open('books/tanakhBookLinks.json') as datafile:
            bookList = json.load(datafile)

            if (bookList[bookGroupName] is not None):
                print('getting list of books:' + bookGroupName)
                for book, url in bookList[bookGroupName].items():
                    print(url)
                    scrapeBook(url)

    except Exception as e:
        print('Error With outputting the file')
        print(e)


if __name__ == '__main__':
    main(sys.argv[1:])
