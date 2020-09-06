from magiclist_ray import MagicList
from magiclist_ray.contants import DIR
from magiclist_ray.magic_parallel import MagicListParallel

import time
import shutil
import os


def main():
    try:
        shutil.rmtree(DIR)
    except:
        pass
    os.mkdir(DIR)
    start = time.time()
    t = MagicList("test")
    [t.append(str(i), 'hi') for i in range(50)]
    [t.get(i) for i in range(50)]
    print(time.time() - start)

    # shutil.rmtree(DIR)
    # os.mkdir(DIR)

    start = time.time()
    e = MagicListParallel("test")
    e.parallel_append({str(i): 'hi' for i in range(50)})
    e.parallel_get([str(i) for i in range(50)])
    print(time.time() - start)


if __name__ == "__main__":
    main()
