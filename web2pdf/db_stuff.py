'''
Main class to connect to the sqlite db and insert/update records.
'''
import sqlite3
import sys
import logging

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler(sys.stdout))
LOG.setLevel(logging.INFO)


class LinkDB(object):
    '''Connects to sqlite DB and imports links, and updates them to saved
    status once the pdf has been downloaded.
    Table schema:
    Col1: url (primary key)
    Col2: title (text)
    Col3: saved (integer) 0 for not-saved, 1 for saved, 2 for error
    Col4: error (text) error text string/exception if any
    '''

    def __init__(self, DB):
        '''Connect to DB and create the table if it doesn't exist.
        '''
        self.table_name = 'links'
        self.conn = sqlite3.connect(DB)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS {} (
        url text not null primary key,
        title text not null,
        saved integer DEFAULT 0,
        error text)'''.format(self.table_name))
        self.conn.commit()

    def insert_into_db(self, links):
        '''Iterate through the list of Link objects given and insert them into
        the table.
        '''
        for link in links:
            LOG.debug('inserting %s | %s into table',
                      link.url, link.title)
            query = 'INSERT INTO {} (url, title) VALUES (?,?)'.format(
                self.table_name)
            try:
                self.cur.execute(query,
                                 (link.url.decode('utf-8'),
                                  link.title.decode('utf-8')))
            except sqlite3.IntegrityError:
                LOG.debug('ignoring pre-existing row')
        self.conn.commit()

    def update_save_status(self, link, saved, error=None):
        '''Update a row and set the saved flag to 1 or 2 depending on whether
        an success or failure.
        '''
        self.cur.execute('UPDATE {} SET saved={}, error={} WHERE url={}'.format(
            self.table_name, saved, error, link))

    def db_status(self):
        '''Print a summary report of all links, and downloaded vs pending
        count.
        '''
        query = 'SELECT Count(*) FROM {}'.format(self.table_name)
        result = self.cur.execute(query).fetchone()[0]
        LOG.info('Found %s rows in the bookmark db', result)
        query2 = 'SELECT Count(*) FROM {} WHERE saved=1'.format(
            self.table_name)
        result = self.cur.execute(query2).fetchone()[0]
        LOG.info('..of which %s links are already saved', result)
        query3 = 'SELECT Count(*) FROM {} WHERE saved=0'.format(
            self.table_name)
        result = self.cur.execute(query3).fetchone()[0]
        LOG.info('..and %s are pending', result)

    def get_unsaved_links(self):
        '''Return a list of Link elements that have not been saved yet.
        '''
        query = 'SELECT url,title FROM {} WHERE saved=0'.format(
            self.table_name)
        return self.cur.execute(query).fetchall()

    def update_record(self, url, status, error=None):
        '''saved should be 1 if True and 2 if False.
        Update the row for that url accordingly.'''
        saved = 1 if status else 2
        LOG.info('Updating row %s with saved as %s and error as %s',
                 url, saved, error)
        query = 'UPDATE {} SET saved=?, error=? WHERE url=?'.format(
            self.table_name)
        self.cur.execute(query, (saved, error, url))
        self.conn.commit()
