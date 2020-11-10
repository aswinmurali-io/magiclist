import time
from magiclist import Magic

magic = Magic('example')

print('\nMagiclist')

start = time.time()
for i in range(3000):
    magic[f'stock{i}'] = {
        'date': '2006-01-05',
        'trans': 'BUY',
        'symbol': 'RHAT',
        'qty': i,
        'price': 35.14,
    }

print(time.time() - start)
