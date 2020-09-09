import glob
import subprocess
import sys
from setuptools import Command, Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "magiclist",
        glob.glob("magiclist/*.py"),
        extra_compile_args=[],
        extra_link_args=[],
    ),
]

requirements = [
    'cython==0.29.1',
    'sphinx==3.2.1',
    'guzzle_sphinx_theme==0.7.11',
],


class InstallDepsCommand(Command):
    description = "Install all the deps for magiclist"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        for dep in requirements:
            x = [sys.executable, '-m', 'pip', 'install'] + dep
            subprocess.check_call(x)


setup(name='magiclist',
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
      cmdclass={
          'install_deps': InstallDepsCommand,
      })
