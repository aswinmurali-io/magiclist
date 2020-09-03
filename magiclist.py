import numpy as np
from numba import jit

__version__: str = "0.0.1"


class MagicList(object):
    """
    Magic List main class containing the high level API implementation of the
    next generation list with lot of features for modern problems
    """
    def __init__(self):
        self.__internal_memory = np.array([], dtype=object)
        self.undo_history: list = []
        self.undo_history_size: int = 30
        self.memory_size: int = 20  # 6 * (1024 ^ 2)

    def append(self, obj):
        print(self.__internal_memory.nbytes)
        if self.memory_size < self.__internal_memory.nbytes:
            self.__internal_memory = np.append(self.__internal_memory, obj)
        else:
            MemoryError("Out of memory for magic list " + self)

    def traverse(self):
        for i in self.__internal_memory:
            print(i)


t = MagicList()
t.append("Hi")
t.append("Hi2")
t.append("Hi3")
t.traverse()
