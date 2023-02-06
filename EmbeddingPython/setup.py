import os, sys

from distutils.core import setup, Extension
from distutils import sysconfig

cpp_args = ['-std=c++20', '-stdlib=libc++', '-I/opt/homebrew/Cellar/pybind11/2.10.3/include']

ext_modules = [
    Extension(
        'MyPyApp',
        ['src/PyEmbeddedApp.cpp'],
        language='c++',
        extra_compile_args = cpp_args,
    ),
]

setup(
    name='MyPyApp',
    version='0.0.1',
    author='Romain Berthoule @ Throows',
    author_email='throowsdev@gmail.com',
    description='This is an example API',
    ext_modules=ext_modules,
)