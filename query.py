"""
file-to-db
query.py

generate db query statements for db

@By Seth (Xiaohui) Wang
@email: sethwang199418@gmail.com
"""

from db import db

class query:
    def __init__(self, name, pk, col_names, data, types):
        self.table_name = name
        self.primary_key = pk
        self.col_names = col_names
        self.data = data
        self.types = types

    def create_table(self):
        return create_table(self.table_name, self.primary_key, self.col_names, self.types)

    def insert_one_row(self):
        return insert_one_row(self.table_name, self.col_names, self.data[0], self.types)

    def insert_n_rows(self):
        return insert_n_rows(self.table_name, self.col_names, self.data, self.types)

    def __str__(self):
        strs = "table name: " + self.table_name + "\n"
        for col in self.col_names:
            strs += str(col) + "             "
        strs += "\n"
        for row in self.data:
            for cell in row:
                strs += str(cell) + "             "
            strs += "\n"
        return strs

# postgresql create table statement
def create_table(table_name, primary_key, col_names, types):
    query = "create table " + table_name + " ("
    for i in range(len(col_names)):
        query += col_names[i] + " " + types[col_names[i]] + (" unique" if col_names[i]==primary_key else "") + ("" if i==len(col_names)-1 else ",")
    query += ")"
    return query

# postgresql insert data statement for one inserting one row
def insert_one_row(table_name, col_names, row_data, types):
    query = "insert into " + table_name + "("
    for i in range(len(col_names)):
        query += col_names[i] + ("" if i == len(col_names)-1 else ",")
    query += ") values ("
    for j in range(len(row_data)):
        name = col_names[j]
        d_type = types[name]
        query += "'" if d_type == "text" else ""
        query += row_data[j]
        query += "'" if d_type == "text" else ""
        query += ("" if j == len(row_data)-1 else ",")
    query += ")"
    return query

# postgresql insert multiple rows
def insert_n_rows(table_name, col_names, data, types):
    print(types)
    query = "insert into " + table_name + "("
    for i in range(len(col_names)):
        query += col_names[i] + ("" if i == len(col_names)-1 else ",")
    query += ") values "
    for row in data:
        query += "("
        for j in range(len(row)):
            name = col_names[j]
            d_type = types[name]
            query += "'" if d_type == "text" else ""
            query += row[j]
            query += "'" if d_type == "text" else ""
            query += ("" if j == len(row)-1 else ",")
        query += ")"
        if data.index(row) == len(data)-1:
            query += ""
        else:
            query += ","
    query += ";"
    return query
