"""
file-to-db
readfile.py

read in data file and generate data object for further db queries

@By Seth (Xiaohui) Wang
@email: sethwang199418@gmail.com
"""
import csv
import sys
from query import *
from db import *

formats = ['csv', 'txt', 'json']
supported_types = ['text', 'integer']

def check_format(filename):
    tokens = filename.split('.')
    return tokens[-1]

def parse_file(filename, table_name, primary_key = None):
    f_format = check_format(filename)
    if f_format in formats:
        if f_format == 'csv':
            parse_csv(filename, table_name, primary_key)

def parse_csv(filename, table_name, primary_key=None):
    f = open(filename)
    data = []
    types = {}
    col_names = []
    try:
        i = 0
        col_names = []
        reader = csv.reader(f)
        for row in reader:
            if i == 0:
                col_names = row
                i+=1
            elif i == 1:
                try:
                    for j in range(len(row)):
                        if row[j].isdigit():
                            types[col_names[j]] = 'integer'
                        else:
                            types[col_names[i]] = 'text'
                            j += 1
                    data.append(row)
                    assert(len(row) == len(col_names))
                except:
                    print "Data does not have equal number of column as column names"
                i += 1
            else:
                data.append(row)
    except Exception as e:
        print e
    f.close()
    q = query(table_name, primary_key, col_names, data, types)
    return q

if __name__ == "__main__":
    filename = "./example.csv"
    q = parse_csv(filename, "portfolio", "id")
    status = query_db(q.insert_n_rows())
    print(status)
