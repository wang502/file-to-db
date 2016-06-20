from pg import DB
'''
db = DB(dbname='',host='',port= '',user='',passwd='')
'''
db = DB(dbname='d4pvr81kbkvo46',host='ec2-23-21-157-223.compute-1.amazonaws.com', port=5432, user='oqjvqwymcazkhw',passwd='cQb5tvoVzhfr8yZNYA6B0dSdJq')

def query_db(q):
    try:
        res = str(db.query(q))
        return res
    except Exception as e:
        print(e)
