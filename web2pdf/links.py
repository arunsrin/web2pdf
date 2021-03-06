'''Class to represent a link. Contains a normalized url and title for
now.
'''
import random
import string
import urltools
from slugify import slugify

class Link(object):
    '''Contains the url, title and whether saved or not.
    '''

    def __init__(self, url, title):
        normalized_url = urltools.normalize(url)
        self.url = normalized_url.encode('utf-8')
        self.title = self.get_title(title).encode('utf-8')

    def __repr__(self):
        return '{} | {} '.format(
            self.url, self.title.encode(
                'utf-8'))

    def get_title(self, title):
        '''For now, use python-slugify to return a neat string that can be
        used as a filename.
        '''
        if title is not None:
            return slugify(title)
        else:
            rand_name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            return 'UNTITLED-' + rand_name
