from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "magic",
        ["magic.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
    name='magiclist',
    ext_modules=cythonize(ext_modules),
)
