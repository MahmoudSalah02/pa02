#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''
import sys


from category import Category
from transactions import Transaction


transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''

def process_choice(choice):

    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
<<<<<<< HEAD

    #5.add transaction feature by Ni Jian
    elif choice=='5':
        print("adding transaction")
        itemCount = int(input("itemCount: "))
        amount = int(input("amount: "))
        cats = category.select_all()
        print_categories(cats)
        itemCategory = input("select the category's name: ")
        #print(category['name'])

        found = False
        for i in range(len(cats)):            
            if itemCategory == cats[i]['name']:
                found = True
                break
            else:
                continue

        if found:
            date = input("date: ")
            description = input("the item description: ")
            trans = {'itemCount':itemCount, 'amount':amount, 'category':itemCategory, 'date':date, 'description':description}
            transactions.add(item)
        else:
            print('category name not found')

=======
    elif choice=='4':
        transac= transactions.select_all()
        print_transactions(transac)
    elif choice=='5':
        itemcount = input("Item #: ")
        amount = input("Amount: ")
        category_ = input("Category: ")
        date = input("Date (MM-DD-YYYY): ")
        description = input("Description: ")
        trans = {'itemCount':itemcount, 'amount':amount, 'category':category_, 'date': date, 'description':description}
        transactions.add(trans)
    elif choice=='6':
        id = input('Input the row ID to be deleted')
        transactions.delete(id)
    elif choice=='7':
        date = input('Input the date (MM-DD-YYYY): ')
        trans = transactions.sort_by_date(date)
        print_transactions(trans)
    elif choice=='8':
        month = input('Input the month (Just the month): ')
        trans = transactions.sort_by_month(month)
        print_transactions(trans)
    elif choice=='9':
        year = input('Input the year (Just the year): ')
        trans = transactions.sort_by_year(year)
        print_transactions(trans)
    elif choice=='10':
        category_ = input('Input the category: ')
        trans = transactions.sort_by_category(category_)
        print_transactions(trans)
    elif choice=='11':
         print(menu)
>>>>>>> da0c1cbd83f2e6444a13c36218abc81d9c9ad52f
    else:
        print("choice",choice,"not yet implemented")

    choice = input("> ")
    return(choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#


def print_category(cat):
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)

def print_transaction(trans):
    print("%-5d %-10s %-10s %-10s %-20s %-30s"%(trans['rowid'], trans['itemCount'],trans['amount'],trans['category'],trans['date'], trans['description']))

def print_transactions(trans):
    print("%-5s %-10s %-10s %-10s %-20s %-30s"%('rowid','item','amount','category','date','description'))
    print('-'*75)
    for tran in trans:
        print_transaction(tran)

# here is the main call!

toplevel()




