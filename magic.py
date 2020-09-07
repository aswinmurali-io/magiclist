import os.path
import threading


class Magic(object):
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name
        self.memory: dict = {}
        if not os.path.exists(self.name):
            os.mkdir(self.name)

    def append(self, key: str, item: any) -> None:
        self.memory[key] = [item, 0, 0]
        threading.Thread(target=lambda: open(f'{self.name}/{key}', 'w').write(
            f'{item} 0 0')).start()

    def sync(self, key: str, item: any, access_count: int,
             trend_ratio: int) -> None:
        self.memory[key] = [item, access_count, trend_ratio]
        threading.Thread(target=lambda: open(f'{self.name}/{key}', 'w').write(
            f'{item} {access_count} {trend_ratio}')).start()

    def append_parallel(self, items: dict) -> None:
        for key in items:
            self.append(key, items[key])

    def get(self, key: str) -> any:
        try:
            self.memory[key][1] += 1
            self.sync(key, self.memory[key][0], self.memory[key][1], self.memory[key][2])
            print(self.memory)
            return self.memory[key][0]
        except KeyError:
            try:
                data = open(f'{self.name}/{key}').read().split()
                self.memory[key] = [
                    self.memory[key][0],
                    int(data[1]) + 1,
                    int(data[2])
                ]
                self.append(key, self.memory[key][0])
                return self.memory[key]
            except FileNotFoundError:
                pass
        return None

    def gets(self, keys: list) -> list:
        return [self.get(key) for key in keys]


import time

start = time.time()
test = Magic("test")
[test.append(f'{i}', i) for i in range(5)]
print(time.time() - start)

for i in range(4):
    print(test.get("2"))
