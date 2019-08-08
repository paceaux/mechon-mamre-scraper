import urllib, os, sys, getopt, json, collections
from fetchPages import simple_get
from tanakhData import get_tanakh_data

OUTPUT_DIRECTORY = 'books'


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
        tanakh_data = get_tanakh_data(url)
        file_name = OUTPUT_DIRECTORY + '/' + 'tanakhBookLinks.json'

        with open(file_name, 'w') as outfile:
            json.dump(tanakh_data, outfile, indent=4)

    except Exception as e:
        print('Error With outputting the file')
        print(e)


if __name__ == '__main__':
    main(sys.argv[1:])
