import glob
import threading
import multiprocessing as mp

from _magic_handles import MAGIC_DIR, default_maxthread, magic_print, \
    create_cache


class MagicList(object):
    def __init__(self):
        self.undo_history: list = []
        create_cache()

    def append(self, key: str, content: any) -> None:
        try:
            open(f"{MAGIC_DIR}{key}.magic_data", 'w').write(content)
        except FileNotFoundError:
            create_cache()

    def append_all(self,
                   contents: dict,
                   maxthread: int = default_maxthread) -> None:
        with mp.Pool(maxthread) as p:
            p.starmap(self.append,
                      [(stuff, contents[stuff]) for stuff in contents])

    def cache(self) -> None:
        pass

    def undo(self) -> None:
        pass

    def export(self) -> dict:
        # This function will be slow
        pass

    def set_undosize(self, size: int) -> None:
        pass

    def set_memsize(self, bytes: int) -> None:
        pass

    def search(self, key: str, maxthread: int = 1):
        pass

    def map(self, func) -> None:
        pass

    def insert_front(self, key: str, content: any) -> None:
        pass

    def insert_back(self, key: str, content: any) -> None:
        pass

    def insert_front_all(self,
                         contents: dict,
                         maxthread: int = default_maxthread) -> None:
        pass

    def insert_back_all(self,
                        contents: dict,
                        maxthread: int = default_maxthread) -> None:
        pass

    def pop_front(self) -> any:
        pass

    def pop_back(self) -> any:
        pass

    def sort(self, maxthread: int = default_maxthread) -> None:
        # This function will be slow
        pass

    def delete(self, key: str) -> None:
        pass

    def print(self, maxthread: int = default_maxthread) -> None:
        tmp = glob.glob(f"{MAGIC_DIR}*.magic_data")
        with mp.Pool(maxthread) as p:
            p.map(magic_print, tmp)

    def print_async(self, maxthread: int = default_maxthread) -> None:
        threading.Thread(target=self.print, args=()).start()


if __name__ == "__main__":
    t = MagicList()
    t.append_all({str(i): "test" for i in range(2000)})
    t.print()
