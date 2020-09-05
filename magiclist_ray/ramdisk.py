# sudo mkdir .magic_datas/
# sudo mount -t tmpfs -o size=512M tmpfs .magic_datas/
# python3 magic.py

import os
import sys
import warnings

from magiclist_ray.contants import DIR
from magiclist_ray.exceptions import MagicWSLNotFoundError

DEFAULT_SIZE: int = 128


def make_disk(volname: str) -> bool:
    if os.path.exists(volname):
        return True
    else:
        try:
            os.mkdir(volname)
            return True
        except PermissionError:
            raise Exception("Cannot make a disk slot for magic list")
    return False


def generate_ram_disk(size: int = DEFAULT_SIZE) -> int:
    cmd: list = [
        'mount',
        '-t',
        'tmpfs',
        '-o',
        f'size={str(size)}M',
        'tmpfs',
        DIR,
    ]
    if os.system('sudo') == 0:
        cmd.insert(0, 'sudo')
    if sys.platform == 'win32' and check_win32_wsl_support():
        warnings.warn("Running in WSL mode in windows platform for ram disk",
                      Warning)
    print(' '.join(cmd))
    return os.system(' '.join(cmd))


def check_win32_wsl_support() -> bool:
    if os.system('bash') != 0:
        warnings.warn(
            "Bash not supported in this platform. If windows enable WSL support",
            MagicWSLNotFoundError)
        return False
    return True
