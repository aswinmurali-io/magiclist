"""Magiclist is an awesome data type ! Magiclist has the ability to release
memory on a per element basis rather than the object itself! This way magiclist
can store a large amount of data inside it without running out of memory. When
magiclist runs out of memory, then purge() function can be called and all the
inactive elements are suspended from the memory and later on returned when needed.
It is capable for storing persistent data. Magiclist can be used for handling
BIG data, perfect for data science! Multiple programs can share the same magiclist
data with their own in-memory cache!
"""

import glob
import os.path
import threading

__file__: str = 'magic.py'
__name__: str = 'magic'
__version__: str = '0.0.1'


class Magic(object):
    def __init__(self, name: str):
        """Magic is the class that contains the magiclist datatype.

        Args:
            name (str): The label used for accessing/creating the state of the magiclist.
        """
        super().__init__()
        self.name: str = name
        self.memory: dict = {}
        self.loaded: bool = self.load()

    def load(self) -> bool:
        """The load() function can be used to load the previous data state from the storage device.

        Returns:
            bool: If loaded successfully or not
        """
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        items = glob.glob(f'{self.name}/*')
        if len(items) < 1:
            return False
        else:
            for i in items:
                self.get(i[len(self.name) + 1:])
            return True

    def append(self, key: str, item: any) -> None:
        """The append(...) function can be used to append a new element into the magic list.

        Args:
            key (str): The key used for accessing the data.
            item (any): The content to store in the magic list with that above key as reference.
        """
        self.memory[key] = [item, 0, 0]
        threading.Thread(target=lambda: open(f'{self.name}/{key}', 'w').write(
            f'{item} 0 0')).start()

    def sync(self, key: str, item: any, access_count: int,
             trend_ratio: int) -> None:
        """The sync function can be used to sync the data changes given in the function args to the in-memory magic
        list and to the storge-based (async) magiclist.

        Args:
            key (str): The key used for accessing the data.
            item (any): The content to store in the magic list with that above key as reference.
            access_count (int): The number of times the elements is been accessed.
            trend_ratio (int): The access_count w.r.t. to a specific time interval.
        """
        _fileptr = open(f'{self.name}/{key}', 'w')
        self.memory[key] = [item, access_count, trend_ratio]
        threading.Thread(target=lambda: _fileptr.write(
            f'{item} {access_count} {trend_ratio}')).start()

    def append_parallel(self, items: dict) -> None:
        """The append_parallel(...) function can be used to batch append elements to the list.

        Args:
            items (dict): The dict of data to be added to the magiclist.
        """
        for key in items:
            self.append(key, items[key])

    def get(self, key: str) -> any:
        """The get(...) function is used to get an element from the magiclist via the key.

        Args:
            key (str): The key used for accessing the data.

        Returns:
            any: Get the element asked for via the key.
        """
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

    def gets(self, keys: iter) -> list:
        """The gets(...) function is used to batch get elements w.r.t to all the keys specified

        Args:
            keys (iter): The keys used for accessing the datas.

        Returns:
            list: Get all the elements asked for via the keys.
        """
        return [self.get(key) for key in keys]

    def __purge(self):
        low_access: int = min([self.memory[key][1] for key in [i for i in self.memory]])
        for key in list(self.memory):
            if self.memory[key][1] == low_access:
                del self.memory[key]

    def purge(self):
        """The purge() function will release less used elements from memory reducing the memory size of the list.
        """
        threading.Thread(target=self.__purge, args=(), daemon=True).start()
