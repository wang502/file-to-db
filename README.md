# file-to-db
Read csv data file and store them into relational database

### Set up
- clone the repo
- ```pip install -r requirements.txt```
- config postgresql
```
pico -w ~/.bash_profile
```
A the following lines to ~/.bash_profile
```
export PG_NAME = ''
export PG_HOST = ''
export PG_PORT =
export PG_USER = ''
export PG_PASSWORD = ''
```
### Usage
```
import parseFile as pf
file = './example.csv'
table = 'example'
primary_key = None
pf.parseFile(file, table, primary_key)
```
