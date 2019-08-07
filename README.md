# A utility to convert [mechon-mamre](https://www.mechon-mamre.org/p/pt/pt0.htm) content from HTML to JSON

Useful for building an API

Not endorsed by Mechon-mamre in any way.

## prerequisites:
Beautiful Soup

## Command Line
### Get JSON for a book
```python bookScraper.py -u https://mechon-mamre.org/p/pt/pt0101.htm```

This will find all chapters in the book and generate a single JSON file. 

Note, you would need to run this for each book in the Torah. 

### get JSON that lists all books:
```python tanakScraper.py -u https://www.mechon-mamre.org/p/pt/pt0.htm```
