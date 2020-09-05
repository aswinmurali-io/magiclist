# sudo mkdir .magic_datas/
# sudo mount -t tmpfs -o size=512M tmpfs .magic_datas/
# python3 magic.py

import os

from magiclist._magic_handles import MAGIC_DIR
import sys

DEFAULT_SIZE: int = 128


def generate_ram_disk(size: int = DEFAULT_SIZE) -> int:
    cmd: list = [
        'mount', '-t', 'tmpfs', '-o', f'size={str(size)}M', 'tmpfs', MAGIC_DIR
    ]
    if os.system('sudo') == 0:
        cmd.append('sudo')
    if sys.platform == 'win32' and check_win32_wsl_support():
        Warning("Running in WSL mode in windows platform for ram disk")
    print(' '.join(cmd))
    return os.system(' '.join(cmd))


def check_win32_wsl_support() -> bool:
    if os.system('bash') != 0:
        Exception(
            "Bash not supported in this platform. If windows enable WSL support"
        )
        return False
    return True
