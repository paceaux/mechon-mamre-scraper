from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import urllib, os, sys, getopt, json, collections, re
from fetchPages import get_page

def get_links_from_start(startPoint, prepended_path = ''):
    linkList = {}
    for element in startPoint.next_siblings:
        if (element.name == 'br'):
            break
        if (element.name == 'a'):
            linkList[element.text] = prepended_path + element['href']
    return linkList

def get_tanakh_data_from_html(pageHtml, url):
    full_path = get_path_for_urls(url)
    torahListStart = pageHtml.find('strong', text=re.compile('Torah'))
    neviimListStart = pageHtml.find('strong', text=re.compile('Prophets'))
    kethuvimListStart = pageHtml.find('strong', text=re.compile('Writings'))

    torahList = get_links_from_start(torahListStart, prepended_path = full_path)
    neviimList = get_links_from_start(neviimListStart, prepended_path = full_path)
    kethuvimList = get_links_from_start(kethuvimListStart, prepended_path = full_path)

    return {'torah': torahList, 'prophets': neviimList, 'writings': kethuvimList }

def get_current_page(url):
    url_parts = url.split('/')
    url_parts_len = len(url_parts)

    return url_parts[url_parts_len - 1]

def get_path_for_urls(url):
    current_page = get_current_page(url)
    path_for_urls = url.replace(current_page, '')

    return path_for_urls

def get_tanakh_data(url):
    print(url)
    try:
        pageHtml = get_page(url)
        tanakh_data = get_tanakh_data_from_html(pageHtml, url)
        tanakh_data['startUrl'] = url

        return tanakh_data

    except Exception as error:
        print(error)

