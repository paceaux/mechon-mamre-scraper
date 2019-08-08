# A utility to convert [mechon-mamre](https://www.mechon-mamre.org/p/pt/pt0.htm) content from HTML to JSON

Useful for building an API

Not endorsed by Mechon-mamre in any way.

## prerequisites:
Beautiful Soup

## Command Line
### Create JSON file for a single book
```python bookScraper.py -u https://mechon-mamre.org/p/pt/pt0101.htm```

This will find all chapters in the book and generate a single JSON file. 

### Create JSON file that lists all of the books
```python tanakScraper.py -u https://www.mechon-mamre.org/p/pt/pt0.htm```

### Create JSON files for books _from_ the JSON file that lists them

* `-g` name of group. Required. torah || prophets || writings
* `-b` name of book(s). Optional. comma separated names of books
```scrapeAllBooks.py -g prophets -b Zephaniah,Haggai```

# Note
Mechon-mamre states that their content is copyrighted with all rights reserved. I have asked their permission to do this, they have not responded. 