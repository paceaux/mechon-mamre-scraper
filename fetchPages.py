from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return ((resp.status_code == 200) 
        and content_type is not None 
        and content_type.find('html') > -1)

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except Exception as err:
        print(err)

def get_page(url):
    try:
        raw_html = simple_get(url);
        html = BeautifulSoup(raw_html, 'html.parser')
        return html
    except Exception as err:
        print(err)