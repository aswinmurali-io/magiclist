import ray
from magiclist_ray.magic import MagicList


class MagicListParallel(MagicList):
    def __init__(self, name):
        super().__init__(name)

    @ray.remote
    def __internal_append(self, key: str, content: any):
        self.append(key, content)

    @ray.remote
    def __internal_get(self, key: str) -> None:
        return self.get(key)

    def parallel_append(self, keys: dict):
        ray.get([
            self.__internal_append.remote(ray.put(self), ray.put(i),
                                          ray.put(keys[i])) for i in keys
        ])

    def parallel_get(self, keys: list) -> list:
        return ray.get([
            self.__internal_get.remote(ray.put(self), ray.put(i))
            for i in keys
        ])
