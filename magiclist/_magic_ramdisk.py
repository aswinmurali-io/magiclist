# sudo mkdir .magic_datas/
# sudo mount -t tmpfs -o size=512M tmpfs .magic_datas/
# python3 magic.py

import os

from _magic_handles import MAGIC_DIR

DEFAULT_SIZE: int = 512


def generate_ram_disk(size: int = DEFAULT_SIZE) -> int:
    return os.system(''.join([
        'sudo', 'mount', '-t', 'tmpfs', '-o', f'size={str(size)}M', 'tmpfs',
        MAGIC_DIR
    ]))


def check_win32_wsl_support() -> bool:
    if os.system('bash') != 0:
        Exception(
            "Bash not supported in this platform. If windows enable WSL support"
        )
        return False
    return True
