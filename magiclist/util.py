# Contains some handy functions to work with Magic data type
import glob
import shutil
from .magic import Magic


def deepcopy(src: Magic, dst: Magic):
    for name in src.name:
        print(name)
        for file in glob.glob(f'{name}/*.*'):
            print(file)
            if file != 'pointers':
                shutil.copyfile(file, f'{dst.name[0]}/{file}')
