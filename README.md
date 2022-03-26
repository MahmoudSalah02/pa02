Script started on Fri Mar 25 09:09:37 2022
Restored session: Fri Mar 25 09:04:26 EDT 2022
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://vus-macbook-pro.dyn.brandeis.edu/Users/vu/pa02
[0m[27m[24m[J(base) vu@vus-macbook-pro pa02 % [K[?2004hppytet st test_transaction.py[?2004l

[1m============================= test session starts ==============================[0m
platform darwin -- Python 3.8.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/vu/pa02, configfile: pytest.ini
[1mcollecting ... [0m[1m
collected 4 items                                                              [0m

test_transaction.py [32m.[0m[31mF[0m[31mF[0m[32m.[0m[31m                                                 [100%][0m

=================================== FAILURES ===================================
[31m[1m___________________________________ test_add ___________________________________[0m

med_db = <transactions.Transaction object at 0x1019880a0>

    [37m@pytest[39;49;00m.mark.add
    [94mdef[39;49;00m [92mtest_add[39;49;00m(med_db):
        [33m''' add a transaction to db, the select it, then delete it'''[39;49;00m
    
        trans0 = {[33m'[39;49;00m[33mitemCount[39;49;00m[33m'[39;49;00m:[94m1[39;49;00m,
                [33m'[39;49;00m[33mamount[39;49;00m[33m'[39;49;00m:[94m1[39;49;00m,
                [33m'[39;49;00m[33mcategory[39;49;00m[33m'[39;49;00m:[33m'[39;49;00m[33mtest_add[39;49;00m[33m'[39;49;00m,
                [33m'[39;49;00m[33mdate[39;49;00m[33m'[39;49;00m:[33m'[39;49;00m[33mtest_add_date[39;49;00m[33m'[39;49;00m,
                [33m'[39;49;00m[33mdescription[39;49;00m[33m'[39;49;00m:[33m'[39;49;00m[33mtest_add_description[39;49;00m[33m'[39;49;00m,
                }
        trans0 = med_db.select_all()
>       rowid = med_db.add(trans0)

[1m[31mtest_transaction.py[0m:85: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <transactions.Transaction object at 0x1019880a0>
item = [{'amount': 1, 'category': 'food', 'date': '-2011', 'description': 'I bought 1 egg', ...}, {'amount': 50000, 'category...escription 1', ...}, {'amount': 2, 'category': 'category2', 'date': 'date2', 'description': 'description 2', ...}, ...]

    [94mdef[39;49;00m [92madd[39;49;00m([96mself[39;49;00m,item):
        [33m''' add a transaction to the transactions table.[39;49;00m
    [33m        this returns the rowid of the inserted element[39;49;00m
    [33m    '''[39;49;00m
        con= sqlite3.connect([96mself[39;49;00m.dbfile)
        cur = con.cursor()
        cur.execute([33m"[39;49;00m[33mINSERT INTO transactions VALUES(?,?,?,?,?)[39;49;00m[33m"[39;49;00m,
>       (item[[33m'[39;49;00m[33mitemCount[39;49;00m[33m'[39;49;00m],item[[33m'[39;49;00m[33mamount[39;49;00m[33m'[39;49;00m],item[[33m'[39;49;00m[33mcategory[39;49;00m[33m'[39;49;00m],item[[33m'[39;49;00m[33mdate[39;49;00m[33m'[39;49;00m], item[[33m'[39;49;00m[33mdescription[39;49;00m[33m'[39;49;00m]))
[1m[31mE       TypeError: list indices must be integers or slices, not str[0m

[1m[31mtransactions.py[0m:53: TypeError
[31m[1m_________________________________ test_delete __________________________________[0m

med_db = <transactions.Transaction object at 0x101a2d9a0>

    [37m@pytest[39;49;00m.mark.delete
    [94mdef[39;49;00m [92mtest_delete[39;49;00m(med_db):
        [33m''' add a transaction to db, delete it, and see that the size changes'''[39;49;00m
        [90m# first we get the initial table[39;49;00m
        trans0 = med_db.select_all()
    
        [90m# then we add this transaction to the table and get the new list of rows[39;49;00m
        trans0 = {[33m'[39;49;00m[33mitemCount[39;49;00m[33m'[39;49;00m:[94m1[39;49;00m,
                [33m'[39;49;00m[33mamount[39;49;00m[33m'[39;49;00m:[94m1[39;49;00m,
                [33m'[39;49;00m[33mcategory[39;49;00m[33m'[39;49;00m:[33m'[39;49;00m[33mtest_add[39;49;00m[33m'[39;49;00m,
                [33m'[39;49;00m[33mdate[39;49;00m[33m'[39;49;00m:[33m'[39;49;00m[33mtest_add_date[39;49;00m[33m'[39;49;00m,
                [33m'[39;49;00m[33mdescription[39;49;00m[33m'[39;49;00m:[33m'[39;49;00m[33mtest_add_description[39;49;00m[33m'[39;49;00m,
                }
    
        rowid = med_db.add(trans0)
        trans1 = med_db.select_all()
    
        [90m# now we delete the transaction and again get the new list of rows[39;49;00m
        med_db.delete(rowid)
        trans2 = med_db.select_all()
    
>       [94massert[39;49;00m [96mlen[39;49;00m(trans0)==[96mlen[39;49;00m(trans2)
[1m[31mE       AssertionError: assert 5 == 13[0m
[1m[31mE        +  where 5 = len({'amount': 1, 'category': 'test_add', 'date': 'test_add_date', 'description': 'test_add_description', ...})[0m
[1m[31mE        +  and   13 = len([{'amount': 1, 'category': 'food', 'date': '-2011', 'description': 'I bought 1 egg', ...}, {'amount': 50000, 'category...escription 1', ...}, {'amount': 2, 'category': 'category2', 'date': 'date2', 'description': 'description 2', ...}, ...])[0m

[1m[31mtest_transaction.py[0m:117: AssertionError
=========================== short test summary info ============================
FAILED test_transaction.py::test_add - TypeError: list indices must be intege...
FAILED test_transaction.py::test_delete - AssertionError: assert 5 == 13
[31m========================= [31m[1m2 failed[0m, [32m2 passed[0m[31m in 0.10s[0m[31m ==========================[0m
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://vus-macbook-pro.dyn.brandeis.edu/Users/vu/pa02
[0m[27m[24m[J(base) vu@vus-macbook-pro pa02 % [K[?2004hppylint transaction.py[?2004l

************* Module transaction.py
transaction.py:1:0: F0001: No module named transaction.py (fatal)
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://vus-macbook-pro.dyn.brandeis.edu/Users/vu/pa02
[0m[27m[24m[J(base) vu@vus-macbook-pro pa02 % [K[?2004hppylint transactions.py[?2004l

************* Module transactions
transactions.py:5:116: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:5:0: C0301: Line too long (116/100) (line-too-long)
transactions.py:74:0: C0301: Line too long (105/100) (line-too-long)
transactions.py:93:0: C0301: Line too long (102/100) (line-too-long)
transactions.py:98:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:103:0: C0301: Line too long (102/100) (line-too-long)
transactions.py:117:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:126:0: C0303: Trailing whitespace (trailing-whitespace)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transactions.py:90:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:100:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:109:4: C0116: Missing function or method docstring (missing-function-docstring)
transactions.py:118:4: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.45/10 (previous run: 8.45/10, +0.00)

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://vus-macbook-pro.dyn.brandeis.edu/Users/vu/pa02
[0m[27m[24m[J(base) vu@vus-macbook-pro pa02 % [K[?2004hppylint.tracker.p           tracker.py[?2004l

************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:92:34: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:102:0: C0301: Line too long (125/100) (line-too-long)
tracker.py:131:0: W0311: Bad indentation. Found 9 spaces, expected 8 (bad-indentation)
tracker.py:136:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:164:0: C0301: Line too long (154/100) (line-too-long)
tracker.py:167:0: C0301: Line too long (105/100) (line-too-long)
tracker.py:178:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:46:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:112:8: W0622: Redefining built-in 'id' (redefined-builtin)
tracker.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:61:0: R0914: Too many local variables (19/15) (too-many-locals)
tracker.py:63:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:84:8: C0103: Variable name "itemCount" doesn't conform to snake_case naming style (invalid-name)
tracker.py:88:8: C0103: Variable name "itemCategory" doesn't conform to snake_case naming style (invalid-name)
tracker.py:92:8: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
tracker.py:93:12: R1723: Unnecessary "else" after "break" (no-else-break)
tracker.py:112:8: C0103: Variable name "id" doesn't conform to snake_case naming style (invalid-name)
tracker.py:61:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:61:0: R0912: Too many branches (18/12) (too-many-branches)
tracker.py:61:0: R0915: Too many statements (64/50) (too-many-statements)
tracker.py:142:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:154:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:155:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:158:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:163:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:164:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:166:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:167:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:33:0: W0611: Unused import sys (unused-import)

------------------------------------------------------------------
Your code has been rated at 6.63/10 (previous run: 6.63/10, +0.00)

[1m[7m%[27m[1m[0m                                                                               
 
]7;file://vus-macbook-pro.dyn.brandeis.edu/Users/vu/pa02
[0m[27m[24m[J(base) vu@vus-macbook-pro pa02 % [K[?2004httracker.py[?2004l

zsh: command not found: tracker.py
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://vus-macbook-pro.dyn.brandeis.edu/Users/vu/pa02
[0m[27m[24m[J(base) vu@vus-macbook-pro pa02 % [K[?2004hppython tracker, .py[?2004l


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

> 11

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

> 1
id  name       description                   
---------------------------------------------
1   ee         ee                            
> 2
category name: Me
category description: Simpol  le 
> 3
modifying category
rowid: 1
new category name: not ee
new category description: Not   nn o longer ee
> 4
rowid item       amount     category   date                 description                   
---------------------------------------------------------------------------
1     1          1          1          1                    1                             
2     2          3          s                                                             
3     1          1          1          1                    1                             
4     3          3          3          3                    3                             
5     1          1          5          1                    1                             
6     1          1          2          1                    1                             
7     1          1          2          5                    5                             
8     13         1332       ee         12-21-2002           lmao                          
> 5
adding transaction
itemCount: 12345
amount: 12
id  name       description                   
---------------------------------------------
1   not ee     no longer ee                  
2   Me         Simple                        
select the category's name: Me
date: 12-21-2002
the item description: Just a test
> 4
rowid item       amount     category   date                 description                   
---------------------------------------------------------------------------
1     1          1          1          1                    1                             
2     2          3          s                                                             
3     1          1          1          1                    1                             
4     3          3          3          3                    3                             
5     1          1          5          1                    1                             
6     1          1          2          1                    1                             
7     1          1          2          5                    5                             
8     13         1332       ee         12-21-2002           lmao                          
9     12345      12         Me         12-21-2002           Just a test                   
> 6
Input the row ID to be deleted1
> 4
rowid item       amount     category   date                 description                   
---------------------------------------------------------------------------
2     2          3          s                                                             
3     1          1          1          1                    1                             
4     3          3          3          3                    3                             
5     1          1          5          1                    1                             
6     1          1          2          1                    1                             
7     1          1          2          5                    5                             
8     13         1332       ee         12-21-2002           lmao                          
9     12345      12         Me         12-21-2002           Just a test                   
> 7
Input the date (MM-DD-YYYY): 12-21-2002
rowid item       amount     category   date                 description                   
---------------------------------------------------------------------------
8     13         1332       ee         12-21-2002           lmao                          
9     12345      12         Me         12-21-2002           Just a test                   
> 8
Input the month (Just the month): 21  12
rowid item       amount     category   date                 description                   
---------------------------------------------------------------------------
8     13         1332       ee         12-21-2002           lmao                          
9     12345      12         Me         12-21-2002           Just a test                   
> 9
Input the year (Just the year): 2002
rowid item       amount     category   date                 description                   
---------------------------------------------------------------------------
8     13         1332       ee         12-21-2002           lmao                          
9     12345      12         Me         12-21-2002           Just a test                   
> 10
Input the category: ee
rowid item       amount     category   date                 description                   
---------------------------------------------------------------------------
8     13         1332       ee         12-21-2002           lmao                          
> 0
bye
[1m[7m%[27m[1m[0m                                                                               
 
]7;file://vus-macbook-pro.dyn.brandeis.edu/Users/vu/pa02
[0m[27m[24m[J(base) vu@vus-macbook-pro pa02 % [K[?2004heexit[?2004l

Saving session...
...saving history...truncating history files...
...completed.

Script done on Fri Mar 25 09:14:31 2022
