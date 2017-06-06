'''Use pdfkit -> wkhtmltopdf to download a pdf version of a link. Save
to OUTPUT_DIR. Caller updates the DB accordingly on pass/failure.

'''
import os
import sys
import logging
import pdfkit
from conf import OUTPUT_DIR

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler(sys.stdout))
LOG.setLevel(logging.INFO)

def download_pdf(link, title):
    '''For an input 'link', fetch the URL and save it as a pdf to
    OUTPUT_DIR.  Returns a tuple of (True, None) or (False,
    exception-string) based on success/failure.

    '''
    output_file = os.path.join(OUTPUT_DIR, title + '.pdf')
    LOG.info('Downloading %s | %s', link, title)
    try:
        pdfkit.from_url(link, output_file)
    except OSError as exc:
        LOG.info('Failed to download %s with error %s',
                 link, str(exc))
        return (False, str(exc))
    return (True, None)
