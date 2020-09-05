import ray
from magiclist_ray.magic import MagicList


class MagicListParallel(MagicList):
    def __init__(self, name):
        super().__init__(name)

    @ray.remote
    def __internal_append(self, key: str, content: any):
        self.append(key, content)

    def parallel_append(self, keys: dict):
        ray.get([
            self.__internal_append.remote(ray.put(self), ray.put(i), ray.put(keys[i]))
            for i in keys
        ])
