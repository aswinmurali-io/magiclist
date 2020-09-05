from magiclist_ray import MagicList
from magiclist_ray.contants import MAX_THREADS
from magiclist_ray.magic_parallel import MagicListParallel
import ray

ray.init(num_cpus=MAX_THREADS)


def main():
    # t = MagicList("test")
    # t.append('t', '2')
    # t.delete(0)
    # t.get(1)
    # print(list(t.get_keys()))

    e = MagicListParallel("test")
    e.parallel_append({str(i): "hi" for i in range(30)})
    print(e.get("1"))
    print(list(e.get_keys()))
    print(e.parallel_get(["1", "2"]))


if __name__ == "__main__":
    main()
