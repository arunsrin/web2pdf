'''Class to represent a link. Contains a normalized url and title for
now.
'''
import urltools
from slugify import slugify

class Link(object):
    '''Contains the url, title and whether saved or not.
    '''

    def __init__(self, url, title):
        normalized_url = urltools.normalize(url)
        self.url = normalized_url.encode('utf-8')
        self.title = self.sanitize_title(title).encode('utf-8') if title else 'UNTITLED'

    def __repr__(self):
        return '{} | {} '.format(
            self.url, self.title.encode(
                'utf-8'))

    def sanitize_title(self, title):
        '''For now, use python-slugify to return a neat string that can be
        used as a filename.
        '''
        return slugify(title)
