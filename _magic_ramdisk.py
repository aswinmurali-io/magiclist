# sudo mkdir .magic_datas/
# sudo mount -t tmpfs -o size=512M tmpfs .magic_datas/
# python3 magic.py

size = 512
linux_ram = f"sudo mount -t tmpfs -o size={size}M tmpfs {MAGIC_DIR}"
