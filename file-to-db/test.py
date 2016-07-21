from parseFile import *

local_csv = "./files/example.csv"
remote_csv = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
remote_csv2 = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'
q = parse_csv(remote_csv, "transactions", None)
print(q)
c_status = query_db(q.create_table())
print(c_status)
status = query_db(q.insert_n_rows())
print(status)

'''
local_xl= "./files/example.xlsx"
#remote_xl = 'http://www.exinfm.com/excel%20files/capbudg.xls'
remote_xl = 'spreadsheetpage.com/downloads/xl/worksheet%20functions.xlsx'
qs = parse_xl(remote_xl, "startups", "name")
for q in qs:
    print(q)
'''
