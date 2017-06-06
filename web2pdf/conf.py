'''Main config file. Apart from the INPUT and OUTPUT_DIR variables,
most of the others are internally used and need not be modified much.
'''
import os

# Path to static directory. contains our sqlite db, the test bookmark
# file, and the public_suffix_list.dat file used by urltools to
# normalize the url (and avoid making network connections each time).
STATIC_DIR = '../static'

# Your bookmarks.html file. currently tested with chrome's format
INPUT = os.path.join(STATIC_DIR, 'bookmarks.html')

# Where to store the output PDFs
OUTPUT_DIR = os.path.join(STATIC_DIR, 'output')

# The temp db we use to mark which ones are downloaded etc.
DB = os.path.join(STATIC_DIR, 'web2pdf.db')

# Path to public suffix list (see https://publicsuffix.org)
SUFFIX_LIST = os.path.join(STATIC_DIR, 'public_suffix_list.dat')

# urltools needs this
os.environ['PUBLIC_SUFFIX_LIST'] = SUFFIX_LIST
