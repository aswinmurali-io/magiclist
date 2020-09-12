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

import os.path
import _thread
import threading
import warnings

from magiclist.exceptions import MagicListLocked, MagicListKeyNotFound

__file__: str = 'magic.py'

warnings.simplefilter('always')
# warnings.simplefilter('ignore')


class Magic(object):
    def __init__(self, name: str, items: iter = None):
        """Magic is the class that contains the magiclist datatype.

        Args:
            name (str): The label used for accessing/creating the state of the magiclist.
        """
        super().__init__()
        self.memory: dict = {}
        self.lock: bool = False
        self.name: list = [name]
        self.LENGTH_FILE: str = f'{name}/length'
        self.POINTER_PATH: str = f'{name}/pointers'
        self.new: bool = self.load()

        if items is not None:
            self.append_parallel(items)

    def __len__(self) -> int:
        # TODO: add proper len listener
        count = 0
        for name in self.name:
            count += len(os.listdir(name))
        return count

    def __getitem__(self, key: str) -> any:
        return self.get(key)

    def __add__(self, obj: object) -> object:
        copy = Magic('temp')
        copy.name = self.name.copy()
        copy.name += [name for name in obj.name if name not in copy.name]
        return copy

    def __sub__(self, obj: object) -> object:
        copy = Magic('temp')
        copy.name = self.name.copy()
        copy.name = [name for name in obj.name if name not in copy.name]
        return copy

    def __iadd__(self, obj: object) -> object:
        if not self.lock:
            self.name += [name for name in obj.name if name not in self.name]
            with open(self.POINTER_PATH, 'w') as file:
                file.write(' '.join(self.name))
            return self
        return None

    def __isub__(self, obj: object) -> object:
        if not self.lock:
            self.name = list(set([item for item in obj.name if item not in self.name]))  # Get unique pointers only !
            with open(self.POINTER_PATH, 'w') as file:
                file.write(' '.join(self.name))
            return self
        return None

    def get_keys(self) -> list:
        """The get_keys() function will return all the keys in that current list.

        Returns:
            list: Returns a list of all the keys in a python list.
        """
        keys = []
        for name in self.name:
            keys.extend([key for key in os.listdir(name)])
        return keys

    def load(self) -> bool:
        """The load() function can be used to load the previous data state from the storage device.

        Returns:
            bool: If loaded successfully or not (new list will not be able to load because it's new)
        """
        present = False
        for name in self.name:
            if not os.path.exists(name):
                os.mkdir(name)
                present = True
        if os.path.exists(self.POINTER_PATH):
            with open(self.POINTER_PATH) as file:
                self.name = file.read().split(' ')
        if not present:
            return False
        return True

    def reset_cache(self) -> None:
        """The reset_cache() cleans the in-memory cache
        """
        self.memory.clear()

    def insert(self, key: str, item: any) -> None:
        """The insert(...) function can be used to insert a new element into the magic list.

        Args:
            key (str): The key used for accessing the data.
            item (any): The content to store in the magic list with that above key as reference.
        """
        if not self.lock:
            return self.sync(key, item, 0, 0)
        warnings.warn(f"Magiclist {self.name[0]} is currently in locked state. Cannot modify values, please unlock the list", MagicListLocked)

    @staticmethod
    def __sync_thread(name, key, item, access_count, trend_ratio):
        with open(f'{name}/{key}', 'w') as file:
            file.write(f'{item} {access_count} {trend_ratio}')

    def sync(self, key: str, item: any, access_count: int, trend_ratio: int) -> None:
        """The sync function can be used to sync the data changes given in the function args to the in-memory magic
        list and to the storge-based (async) magiclist.

        Args:
            key (str): The key used for accessing the data.
            item (any): The content to store in the magic list with that above key as reference.
            access_count (int): The number of times the elements is been accessed.
            trend_ratio (int): The access_count w.r.t to a specific time interval.
        """
        self.memory[key] = [item, access_count, trend_ratio]
        _thread.start_new_thread(self.__sync_thread, (self.name[0], key, item, access_count, trend_ratio))

    def inserts(self, items: dict) -> None:
        """The inserts(...) function can be used to batch insert elements to the list.

        Args:
            items (dict): The dict of data to be added to the magiclist.
        """
        for key in items:
            self.insert(key, items[key])

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
                self.sync(key, self.memory[key][0], self.memory[key][1], self.memory[key][2])
                return self.memory[key]
            except KeyError:
                try:
                    with open(f'{name}/{key}') as data:
                        data = data.read().split()
                        self.sync(key, data[0], int(data[1]) + 1, int(data[2]))
                    return self.memory[key]
                except FileNotFoundError:
                    pass
        warnings.warn(f'Unable to find the key "{key}" in magiclist "{self.name[0]}"', MagicListKeyNotFound)
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
            low_access: int = min([self.memory[key][1] for key in [i for i in self.memory]])
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
