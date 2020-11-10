import sqlite3
import time
import os

print('\nsqlite3')

file = 'example.db'
if os.path.exists(file):
    os.remove(file)
conn = sqlite3.connect(file)

c = conn.cursor()

# Create table
start = time.time()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
e = time.time() - start
print(f'Creating table {e}s')

# Insert a row of data
start = time.time()
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
e2 = time.time() - start
print(f'Inserting table {e2}s')

# Save (commit) the changes
start = time.time()
conn.commit()
e3 = time.time() - start
print(f'Saving table {e3}s')

print(f'Creating & Inserting table combined {e + e2 + e3}s')

from magiclist import Magic

magic = Magic('example')

print('\nMagiclist')

start = time.time()
magic['stock'] = {
    'date': ['2006-01-05'],
    'trans': ['BUY'],
    'symbol': ['RHAT'],
    'qty': [100],
    'price': [35.14],
}
print(f'Creating & Inserting table combined {time.time() - start}s')
