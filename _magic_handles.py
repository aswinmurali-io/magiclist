# This problem seems to be a design feature of multiprocessing.Pool. See
# https://bugs.python.org/issue25053. For some reason Pool does not always
# work with objects not defined in an imported module. So you have to write
# your function into a different file and import the module.
# https://stackoverflow.com/questions/41385708/multiprocessing-example-giving-attributeerror

import os
import multiprocessing as mp

MAGIC_DIR: str = '.magic_datas/'
default_maxthread: int = 8


def magic_print(key_file_path: str) -> None:
    print(open(key_file_path).read())


def create_cache() -> None:
    if not os.path.isdir(MAGIC_DIR):
        os.mkdir(MAGIC_DIR)


def magic_append_all(self,
                     contents: dict,
                     maxthread: int = default_maxthread) -> None:
    with mp.Pool(maxthread) as p:
        p.starmap(self.append,
                  [(stuff, contents[stuff]) for stuff in contents])
