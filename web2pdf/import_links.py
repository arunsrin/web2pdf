'''Given a user's bookmark file (chrome format only so far), parse
the file and return a list of Link objects containing the url and the
title.

'''
from lxml import etree
from links import Link

def parse_bookmarks(bookmarks):
    '''Parse the bookmarks file and return a list of links.
    '''
    links = []
    xml = etree.parse(bookmarks, parser=etree.HTMLParser())
    xml_links = xml.findall(".//a")
    for this_link in xml_links:
        url = this_link.get('href')
        title = this_link.text
        if url:
            links.append(Link(url, title))
    return links
