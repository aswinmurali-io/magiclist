from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "magic",
        ["magic.py"],
        extra_compile_args=[],
        extra_link_args=[],
    )
]

setup(
    name='magiclist',
    ext_modules=cythonize(ext_modules),
)
