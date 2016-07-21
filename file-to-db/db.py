from pg import DB
import os

name= os.environ.get('PG_NAME')
host= os.environ.get('PG_HOST')
port = int(os.environ.get('PG_PORT'))
user = os.environ.get('PG_USER')
password = os.environ.get('PG_PASSWORD')

db = DB(dbname=name, host=host, port=port, user=user, passwd=password)
def query_db(q):
    try:
        res = str(db.query(q))
        return res
    except Exception as e:
        print(e)

if __name__ == "__main__":
    q = "select * from portfolio"
    print(query_db(q))
