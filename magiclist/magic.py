"""
Magiclist is an awesome data type ! Magiclist has the ability to release
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
import random
import threading

__file__: str = 'magic.py'
__name__: str = 'magic'
__version__: str = '0.0.1'


class Magic(object):
    def __init__(self, name: str, cachename: str = None, items: iter = None):
        """Magic is the class that contains the magiclist datatype.

        Args:
            name (str): The label used for accessing/creating the state of the magiclist.
        """
        super().__init__()
        self.name: str = [name]
        self.pointer_path: str = f'{name}/pointers'
        self.memory: dict = {}
        self.cache_fileptr: open = None
        self.loaded: bool = self.load_cache(
            f'cache_{cachename}' if cachename is not None else f'cache_{name}')
        self.length: int = 0
        self.lock: bool = False
        if items is not None:
            self.append_parallel(items)

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, key: str) -> any:
        return self.get(key)

    def __add__(self, obj: object) -> object:
        copy = self
        copy.name += obj.name
        copy.name = list(set(copy.name))  # Get unique pointers only !
        return copy

    def __sub__(self, obj: object) -> object:
        copy = self
        copy.name = [item for item in obj.name if item not in copy.name]
        copy.name = list(set(copy.name))  # Get unique pointers only !
        return copy

    def __iadd__(self, obj: object) -> object:
        if not self.lock:
            self.name += obj.name
            self.name = list(set(self.name))  # Get unique pointers only !
            open(self.pointer_path, 'w').write('\n'.join(self.name))
            return self
        return None

    def __isub__(self, obj: object) -> object:
        if not self.lock:
            self.name = [item for item in obj.name if item not in self.name]
            self.name = list(set(self.name))  # Get unique pointers only !
            open(self.pointer_path, 'w').write('\n'.join(self.name))
            return self
        return None

    def load_cache(self, cachename: str) -> bool:
        """The load_cache(...) function can be used to load the previous data state from the storage device.

        Returns:
            bool: If loaded successfully or not
            cachename: The name of the in-memory cache
        """
        count = 0
        if os.path.exists(self.pointer_path):
            self.name = open(self.pointer_path).read().split('\n')
        for name in self.name:
            if not os.path.exists(name):
                if name != '':
                    os.mkdir(name)
            __cache_path: str = f'{name}/{cachename}'
            if os.path.exists(__cache_path):
                self.cache_fileptr = open(__cache_path, 'r+')
            else:
                self.cache_fileptr = open(__cache_path, 'w+')
            __cached_keys: list = self.cache_fileptr.read().split('\n')
            if len(__cached_keys) != 0 and __cached_keys != ['']:
                print(__cached_keys)
                for key in __cached_keys:
                    self.get(key)
                count += 1
        return count == len(self.name)

    def reset_cache(self) -> None:
        """The reset_cache(...) cleans the in-memory cache
        """
        self.memory.clear()

    def save_cache(self) -> None:
        """The save_cache(...) saves a references of the in-memory cache
        """
        self.cache_fileptr.write('\n'.join([key for key in self.memory]))

    def insert(self, key: str, item: any) -> None:
        """The insert(...) function can be used to insert a new element into the magic list.

        Args:
            key (str): The key used for accessing the data.
            item (any): The content to store in the magic list with that above key as reference.
        """
        if not self.lock:
            self.memory[key] = [item, 0, 0]
            self.length += 1
            threading.Thread(target=lambda: open(f'{self.name[0]}/{key}', 'w').
                             write(f'{item} 0 0')).start()
        # open(f'{self.name[0]}/{key}', 'w').write(f'{item} 0 0')

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
        _fileptr = open(f'{self.name[0]}/{key}', 'w')
        self.memory[key] = [item, access_count, trend_ratio]
        threading.Thread(target=lambda: _fileptr.write(
            f'{item} {access_count} {trend_ratio}')).start()

    def insert_parallel(self, items: dict) -> None:
        """The insert_parallel(...) function can be used to batch insert elements to the list.

        Args:
            items (dict): The dict of data to be added to the magiclist.
        """
        for key in items:
            self.insert(key, items[key])
            self.length += 1

    def random(self) -> any:
        """The random() function returns a random element from the magiclist

        Returns:
            any: returns any element
        """
        files = []
        print(self.name)
        for key in self.name:
            if key == '':
                return None
            files.extend(glob.glob(f'{key}/*'))
        # remove special elements from taking part in random like pointers, cache, etc
        files = [x for x in files if 'cache_' not in x and 'pointers' not in x]
        return self.get(random.choice(files).split('/')[1])

    def get(self, key: str) -> any:
        """The get(...) function is used to get an element from the magiclist via the key.

        Args:
            key (str): The key used for accessing the data.

        Returns:
            any: Get the element asked for via the key.
        """
        for name in self.name:
            try:
                self.memory[key][1] += 1
                self.sync(key, self.memory[key][0], self.memory[key][1],
                          self.memory[key][2])
                return self.memory[key]
            except KeyError:
                try:
                    data = open(f'{name}/{key}').read().split()
                    self.sync(key, data[0], int(data[1]), int(data[2]))
                    return self.memory[key]
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

    def __purge(self) -> None:
        try:
            low_access: int = min(
                [self.memory[key][1] for key in [i for i in self.memory]])
            for key in list(self.memory):
                if self.memory[key][1] == low_access:
                    del self.memory[key]
        except ValueError:
            # ValueError: min() arg is an empty sequence
            return

    def purge(self) -> None:
        """The purge() function will release less used elements from memory reducing the memory size of the list.
        """
        threading.Thread(target=self.__purge, args=(), daemon=True).start()
