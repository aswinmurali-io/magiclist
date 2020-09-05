import os.path
import glob
import threading
import multiprocessing as mp

from magiclist._magic_handles import MAGIC_DIR, MAGIC_EXT, default_maxthread, \
    magic_print, create_cache

from magiclist.ramdisk import generate_ram_disk


class MagicList(object):
    def __init__(self):
        self.undo_history: list = []
        self.tmp_memory_result: list = []
        create_cache()
        generate_ram_disk()

    def append(self, key: str, content: any) -> None:
        try:
            open(f"{MAGIC_DIR}{key}{MAGIC_EXT}", 'w').write(content)
        except FileNotFoundError:
            create_cache()

    def get(self, key: str) -> any:
        try:
            return open(f"{MAGIC_DIR}{key}{MAGIC_EXT}").read()
        except FileNotFoundError:
            return None

    def _get_thread(self, filename: str) -> any:
        try:
            print(filename)
            self.tmp_memory_result.append(open(filename).read())
        except FileNotFoundError:
            pass

    def get_all(self, maxthread: int = default_maxthread) -> list:
        tmp = glob.glob(f"{MAGIC_DIR}*.magic_data")
        with mp.Pool(maxthread) as p:
            p.map(self._get_thread, tmp)
        return self.tmp_memory_result

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
        print(f'deleted {MAGIC_DIR}{key}{MAGIC_EXT} for key {key}')
        if os.path.isfile(f'{MAGIC_DIR}{key}{MAGIC_EXT}'):
            os.remove(f'{MAGIC_DIR}{key}{MAGIC_EXT}')
        else:
            print(f"Cannot delete key {key}. Does not exist?")

    def print(self, maxthread: int = default_maxthread) -> None:
        tmp = glob.glob(f"{MAGIC_DIR}*.magic_data")
        with mp.Pool(maxthread) as p:
            p.map(magic_print, tmp)

    def print_async(self, maxthread: int = default_maxthread) -> None:
        threading.Thread(target=self.print, args=()).start()
