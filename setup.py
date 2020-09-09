import glob

from Cython.Build import cythonize
from setuptools import Extension, setup

ext_modules = [
    Extension(
        "magiclist",
        glob.glob("magiclist/*.py"),
        extra_compile_args=[],
        extra_link_args=[],
    ),
]

requirements = open('requirements.txt').read().split('\n'),

setup(
    name='magiclist',
    packages=['magiclist'],
    version='0.1',
    license='Apache',
    author='Aswin Murali',
    author_email='aswinmurali.co@gmail.com',
    url='https://github.com/aswinmurali-io/magiclist',
    download_url='https://github.com/aswinmurali-io/magiclist',
    long_description=open('README.md'),
    long_description_content_type="text/markdown",
    keywords=['list', 'magic', 'algorithm'],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    ext_modules=cythonize(ext_modules, language_level='3'),
    install_requires=requirements,
)
