import csv
import sys

formats = ['csv', 'txt', 'json']
supported_types = ['text', 'int']

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
                            types[col_names[j]] = 'int'
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
    primary_index = col_names.index(primary_key)
    print data
    print types
    print primary_index

if __name__ == "__main__":
    filename = "./Book1.csv"
    parse_csv(filename, "portfolio", "id")
