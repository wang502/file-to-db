from pg import DB
'''
db = DB(dbname='',host='',port= '',user='',passwd='')
'''

def query_db(q):
    try:
        res = str(db.query(q))
        return res
    except Exception as e:
        print(e)
