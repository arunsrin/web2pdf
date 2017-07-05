#!/usr/bin/env python
'''Main application. Read a bookmark.html file as input, and fetch
each link in it.  Convert to pdf and store in output directory.
Edit conf.py to tweak these settings.
'''
import sys
import logging
from conf import INPUT, DB
from db_stuff import LinkDB
from import_links import parse_bookmarks
from downloader import download_pdf

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler(sys.stdout))
LOG.setLevel(logging.INFO)


def main():
    '''main function. Import bookmarks, iterate through them and download
    PDF versions.
    '''
    with open(INPUT) as bookmarks:
        links = parse_bookmarks(bookmarks)
    LOG.info('Found %s links in the bookmark file', len(links))
    link_db = LinkDB(DB)
    link_db.insert_into_db(links)
    link_db.db_status()
    input('Hit enter to start downloading pending PDFs')
    unsaved_links = link_db.get_unsaved_links()
    for link in unsaved_links:
        result, errstring = download_pdf(link_db, link[0], link[1])
        if not result:
            print('Something went wrong with this one: {}'.format(
                errstring))

if __name__ == '__main__':
    main()
