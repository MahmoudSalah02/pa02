'''
test_categories runs unit and integration tests on the category module
'''

import pytest
from transactions import Transaction, to_trans_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    trans1 =  {'itemCount':1, 'amount':1, 'category':'food', 
    'date':'01-01-2011', 'description':'I bought 1 egg'}
    trans2 = {'itemCount':1, 'amount':50000, 'category':'car', 
    'date':'04-01-2011', 'description':'I bought 1 car'}
    trans3 = {'itemCount':1, 'amount':10, 'category':'fun', 
    'date':'07-07-2011', 'description':'I watched 1 movie'}
    id1=empty_db.add(trans1)
    id2=empty_db.add(trans2)
    id3=empty_db.add(trans3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        trans ={'itemCount':s,
                'amount':s,
                'category':'category'+s, 
                'date':'date'+s,
               'description':'description '+s,
                }
        rowid = small_db.add(trans)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])



@pytest.mark.simple
def test_to_trans_dict():
    ''' teting the to_trans_dict function '''
    a = to_trans_dict((7,1,1,'testcategory','testdate','testdescription'))
    assert a['rowid']==7
    assert a['itemCount']==1
    assert a['amount']==1
    assert a['category']=='testcategory'
    assert a['date']=='testdate'
    assert a['description']=='testdescription'
    assert len(a.keys())==6


@pytest.mark.add
def test_add(med_db):
    ''' add a transaction to db, the select it, then delete it'''

    trans0 = {'itemCount':1,
            'amount':1,
            'category':'test_add',
            'date':'test_add_date',
            'description':'test_add_description',
            }
    trans0 = med_db.select_all()
    rowid = med_db.add(trans0)
    trans1 = med_db.select_all()
    assert len(trans1) == len(trans0) + 1
    trans1 = med_db.select_one(rowid)
    assert trans1['itemCount']==trans0['itemCount']
    assert trans1['amount']==trans0['amount']
    assert trans1['category']==trans0['category']
    assert trans1['date']==trans0['date']
    assert trans1['description']==trans0['description']


@pytest.mark.delete
def test_delete(med_db):
    ''' add a transaction to db, delete it, and see that the size changes'''
    # first we get the initial table
    trans0 = med_db.select_all()

    # then we add this transaction to the table and get the new list of rows
    trans0 = {'itemCount':1,
            'amount':1,
            'category':'test_add',
            'date':'test_add_date',
            'description':'test_add_description',
            }
            
    rowid = med_db.add(trans0)
    trans1 = med_db.select_all()

    # now we delete the transaction and again get the new list of rows
    med_db.delete(rowid)
    trans2 = med_db.select_all()

    assert len(trans0)==len(trans2)
    assert len(trans2) == len(trans1)-1

@pytest.mark.update
def test_update(med_db):
    ''' add a transaction to db, updates it, and see that it changes'''

    # then we add this transaction to the table and get the new list of rows
    trans0 = {'itemCount':1,
            'amount':1,
            'category':'test_add',
            'date':'test_add_date',
            'description':'test_add_description',
            }
    rowid = med_db.add(cat0)

    # now we upate the transaction
    trans1 = {'itemCount':2,
            'amount':3,
            'category':'new_add',
            'date':'new_add_date',
            'description':'new_add_description',
            }
    med_db.update(rowid,trans1)

    # now we retrieve the transaction and check that it has changed
    trans2 = med_db.select_one(rowid)
    assert trans2['itemCount']==trans1['itemCount']
    assert trans2['amount']==trans1['amount']
    assert trans2['category']==trans1['category']
    assert trans2['date']==trans1['date']
    assert trans2['description']==trans1['description']
