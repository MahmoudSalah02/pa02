import sqlite3

def to_trans_dict(trans_tuple):
    ''' trans is a transaction tuple (rowid, itemCount, amount, category, date, description)'''
    trans = {'rowid':trans_tuple[0], 'itemCount':trans_tuple[1], 'amount':trans_tuple[2], 
             'category':trans_tuple[3], 'date':trans_tuple[4], 'description':trans_tuple[5],
            }
    return trans

def to_trans_dict_list(trans_tuple):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_trans_dict(trans_tuple) for cat in trans_tuple]

class Transaction():
    ''' Transaction represents a table of Transcations'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS categories
                    (name text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the categories as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from categories")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def select_one(self,rowid):
        ''' return a category with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from categories where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict(tuples[0])


    def add(self,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO categories VALUES(?,?)",(item['name'],item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,rowid,item):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE categories
                        SET name=(?), desc=(?)
                        WHERE rowid=(?);
        ''',(item['name'],item['desc'],rowid))
        con.commit()
        con.close()

    def delete(self,rowid):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM categories
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()