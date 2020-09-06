import _thread
from threading import Thread

from magiclist_ray.magic import MagicList


class MagicListParallel(MagicList):
    def __init__(self, name):
        super().__init__(name)

    def parallel_append(self, keys: dict):
        [_thread.start_new_thread(self.append, (i, keys[i])) for i in keys]

    def parallel_get(self, keys: list) -> list:
        roo = [Thread(target=self.get, args=(i, )) for i in keys]
        [i.start() for i in roo]
        return [i.join() for i in roo]
