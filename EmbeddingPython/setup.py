import os, sys

from distutils.core import setup, Extension
from distutils import sysconfig

cpp_args = ['-std=c++11', '-stdlib=libc++']

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
    version='0.0.2',
    author='Romain Berthoule @ Throows',
    author_email='throowsdev@gmail.com',
    description='This is an example API',
    ext_modules=ext_modules,
)