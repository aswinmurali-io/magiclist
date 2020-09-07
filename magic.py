import glob
import os.path
import threading


class Magic(object):
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name
        self.memory: dict = {}
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        self.load()

    def load(self):
        for i in glob.glob(f'{self.name}/*'):
            self.get(i[len(self.name) + 1:])
        return True

    def append(self, key: str, item: any) -> None:
        self.memory[key] = [item, 0, 0]
        threading.Thread(target=lambda: open(f'{self.name}/{key}', 'w').write(
            f'{item} 0 0')).start()

    def sync(self, key: str, item: any, access_count: int,
             trend_ratio: int) -> None:
        _fileptr = open(f'{self.name}/{key}', 'w')
        self.memory[key] = [item, access_count, trend_ratio]
        threading.Thread(target=lambda: _fileptr.write(
            f'{item} {access_count} {trend_ratio}')).start()

    def append_parallel(self, items: dict) -> None:
        for key in items:
            self.append(key, items[key])

    def get(self, key: str) -> any:
        try:
            self.memory[key][1] += 1
            self.sync(key, self.memory[key][0], self.memory[key][1],
                      self.memory[key][2])
            return self.memory[key]
        except KeyError:
            try:
                data = open(f'{self.name}/{key}').read().split()
                self.sync(key, data[0], int(data[1]), int(data[2]))
                return self.memory
            except FileNotFoundError:
                pass
        return None

    def gets(self, keys: list) -> list:
        return [self.get(key) for key in keys]

    def __purge(self):
        i = [self.memory[key][1] for key in [i for i in self.memory]]
        low_access = min(i)
        for key in list(self.memory):
            if self.memory[key][1] == low_access:
                del self.memory[key]

    def purge(self):
        threading.Thread(target=self.purge, args=(), daemon=True).start()


import time


start = time.time()
test = Magic("test")

print(time.time() - start)

for i in range(4):
    print(test.get("2"))

for i in range(6):
    print(test.purge())

print(test.memory)

test.get("1")

print(test.memory)
