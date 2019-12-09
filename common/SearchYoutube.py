# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup


def get_title(url):

    # check that the url is what we would expect
    if url[0:4] != "http":
        if "http" in url:
            url = 'http' + ''.join(url.split("http")[1])  
    
    # try the url but return None if bad url
    try:
        source = requests.get(url).text
    except requests.exceptions.InvalidSchema:
        print("bad url for requests")
        return None

    soup = BeautifulSoup(source, 'lxml')
    title = None
    
    for candidate in soup.find_all('span', id="eow-title"):
        print(candidate.get_text('\n'))
        title = candidate.string
        break

    if title is not None:
        return title
    else:
        return None
