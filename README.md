
# Mechon-Mamre HTML to JSON Converter

A utility to convert [Mechon-Mamre](https://www.mechon-mamre.org/p/pt/pt0.htm) content from HTML to JSON, useful for building an API. **This project is not endorsed by Mechon-Mamre**.

## Prerequisites

- **Python 3.x**
- **Beautiful Soup** - for parsing HTML content. Install via `pip`:

  ```bash
  pip install beautifulsoup4 requests
  ```

## Command Line Usage

### 1. Convert a Single Book to JSON

To create a JSON file for a single book:

```bash
python bookScraper.py -u https://mechon-mamre.org/p/pt/pt0101.htm
```

This command finds all chapters in the specified book and generates a single JSON file containing the book's content.

### 2. Generate a JSON List of All Books

To create a JSON file that lists all books in the Tanakh:

```bash
python tanakScraper.py -u https://www.mechon-mamre.org/p/pt/pt0.htm
```

### 3. Generate JSON Files for Selected or All Books from the Book List

To scrape books from the Tanakh JSON list and create individual JSON files:

- Use `-g` to specify the group (`torah`, `prophets`, or `writings`).
- Use `-b` to specify specific books (comma-separated).
- Use `-a` to scrape *all* books.

#### Scrape Specific Books

```bash
python scrapeAllBooks.py -g prophets -b Zephaniah,Haggai
```

This example scrapes and saves JSON files for *Zephaniah* and *Haggai* from the *prophets* group.

#### Scrape All Books

```bash
python scrapeAllBooks.py -g writings -a
```

This command scrapes and saves JSON files for *all books* in the *writings* group.

## File Structure

The script saves HTML files to a `data/html` directory to prevent re-downloading content on repeated runs. This caching speeds up the process and reduces unnecessary server requests.

## Important Notes

- **Copyright**: Mechon-Mamre states that their content is copyrighted with all rights reserved. This project aims to respect these rights, and permission has been sought to perform this scraping; however, no response has been received.

- **Use Responsibly**: This tool is intended for educational and non-commercial use. Please ensure your usage aligns with Mechon-Mamre’s terms.

---

**Disclaimer**: This utility is independently created and is not affiliated with or endorsed by Mechon-Mamre.
