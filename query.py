"""
file-to-db
query.py

generate db query statements for db

@By Seth (Xiaohui) Wang
@email: sethwang199418@gmail.com
"""

from db import db

# postgresql create table statement
def create_table(table_name, primary_key, col_names, types):
    query = "create table " + table_name + " ("
    for i in range(len(col_names)):
        query += col_names[i] + " " + types[col_names[i]] + (" unique" if col_names[i]==primary_key else "") + ("" if i==len(col_names)-1 else ",")
    query += ")"
    return query

# postgresql insert data statement for one inserting one row
def insert_one_row(table_name, col_names, row_data):
    query = "insert into " + table_name + "("
    for i in range(len(col_names)):
        query += col_names[i] + ("" if i == len(col_names)-1 else ",")
    query += ") values ("
    for j in range(len(row_data)):
        query += row_data[j] + ("" if j == len(row_data)-1 else ",")
    query += ")"
    return query

# postgresql insert multiple rows
def insert_rows(table_name, col_names, data):
    query = "insert into " + table_name + "("
    for i in range(len(col_names)):
        query += col_names[i] + ("" if i == len(col_names)-1 else ",")
    query += ") values "
    for row in data:
        query += "("
        for j in range(len(row)):
            query += row[j] + ("" if j == len(row)-1 else ",")
        query += ")"
        if data.index(row) == len(data)-1:
            query += ""
        else:
            query += ","
    return query
