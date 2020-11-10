import os
import time
import sqlite3

file = 'example.db'
if os.path.exists(file):
    os.remove(file)
conn = sqlite3.connect(file)

c = conn.cursor()

start = time.time()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

for i in range(3000):
    c.execute(f"INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',{i},35.14)")

# conn.commit()
print(time.time() - start)
