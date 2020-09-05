import os
import glob
import warnings

from magiclist_ray import ramdisk
from magiclist_ray.contants import DIR, EXT
from magiclist_ray.exceptions import MagicKeyAlreadyExists, \
    MagicIOError, MagicKeyNotFound


def get_slot(key: str) -> str:
    return f"{DIR}{key}{EXT}"


class MagicList(object):
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name
        ramdisk.make_disk(name)

    def append(self, key: str, content: any) -> None:
        try:
            if os.path.isfile(get_slot(key)):
                open(get_slot(key), 'w').write(content)
                warnings.warn(f"Found existing key {key}, overriding value",
                              MagicKeyAlreadyExists)
            open(get_slot(key), 'w').write(content)
        except FileNotFoundError:
            if ramdisk.make_disk(self.name):
                warnings.warn("Failed to append data because of IO issues",
                              MagicIOError)

    def get(self, key: str) -> any:
        try:
            if not os.path.isfile(get_slot(key)):
                warnings.warn(f"Cannot find {key}", MagicKeyNotFound)
                return None
            return open(get_slot(key)).read()
        except (FileNotFoundError, PermissionError):
            warnings.warn("Cannot get data because of IO issues", MagicIOError)
        return None

    def delete(self, key: str):
        if os.path.isfile(get_slot(key)):
            try:
                os.remove(get_slot(key))
            except PermissionError as e:
                warnings.warn(f"Cannot delete key {key}, {e.args}",
                              MagicIOError)
        else:
            warnings.warn(f"Cannot delete key {key}. Does not exist?",
                          MagicKeyNotFound)

    def get_keys(self) -> map:
        i = glob.glob(f"{DIR}*{EXT}")
        return map(lambda i: i[i.find('/') + 1:-len(EXT)], i)
