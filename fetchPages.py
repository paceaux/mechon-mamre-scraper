# fetchPages.py
import os
import hashlib
from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def is_good_response(resp):
    content_type = resp.headers.get('Content-Type', '').lower()
    return ((resp.status_code == 200)
            and content_type is not None
            and 'html' in content_type)

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                print(f"Error: Bad response from {url}")
                return None
    except Exception as err:
        print(f"Exception during GET request to {url}: {err}")
        return None

def get_filename_from_url(url):
    # Use MD5 hash of the URL to generate a unique filename
    url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    filename = f"{url_hash}.html"
    return filename

def get_page(url):
    try:
        # Define the directory to store cached HTML files
        data_dir = os.path.join('data', 'html')
        os.makedirs(data_dir, exist_ok=True)

        filename = get_filename_from_url(url)
        filepath = os.path.join(data_dir, filename)

        if os.path.exists(filepath):
            # Read from the cached file
            with open(filepath, 'rb') as f:
                raw_html = f.read()
            # print(f"Loaded cached page for {url}")
        else:
            # Download the page
            raw_html = simple_get(url)
            if raw_html is None:
                return None
            # Save to cache
            with open(filepath, 'wb') as f:
                f.write(raw_html)
            # print(f"Downloaded and cached page for {url}")

        html = BeautifulSoup(raw_html, 'html.parser')
        return html
    except Exception as err:
        print(f"Error in get_page for {url}: {err}")
        return None
