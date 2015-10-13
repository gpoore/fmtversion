# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Geoffrey M. Poore
# All rights reserved.
#
# Licensed under the BSD 3-Clause License:
# http://opensource.org/licenses/BSD-3-Clause
#


import sys
import os
# Get a version of open() that can handle encoding
if sys.version_info.major == 2:
    from io import open
import collections


try:
    from setuptools import setup
    setup_package_dependent_keywords = dict()
except ImportError:
    from distutils.core import setup
    setup_package_dependent_keywords = dict()


# Extract the version from pkgversion.py
fname = os.path.join(os.path.dirname(__file__), 'pkgversion.py')
with open(fname, 'rb') as f:
    c = compile(f.read(), 'pkgversion.py', 'exec')
    exec(c)
    version = __version__

fname = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(fname, encoding='utf8') as f:
    long_description = f.read()


setup(
    name = 'pkgversion',
    version = version,
    py_modules = ['pkgversion'],
    packages = [],
    description = 'Simple version variables for Python packages',
    long_description = long_description,
    author = 'Geoffrey M. Poore',
    author_email = 'gpoore@gmail.com',
    url = 'http://github.com/gpoore/pkgversion',
    license = 'BSD',
    keywords = ['packaging', 'versioning'],
    # https://pypi.python.org/pypi?:action=list_classifiers
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    **setup_package_dependent_keywords
)
