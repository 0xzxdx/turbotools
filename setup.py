#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from turbotools import __title__
from turbotools import __version__
from turbotools import __author__
from turbotools import __email__

# from distutils.core import setup
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
  name=__title__,
  version=__version__,
  author=__author__,
  author_email=__email__,
  description='My short description for my project. ',
  long_description=long_description,
  url='https://github.com/anshengme/turbotools',
  packages=find_packages(exclude=('tests',)),
  install_requires=['requests'],
  entry_points='''
    [console_scripts]
    turbotools-cli=turbotools.cli:main
  ''',
  classifiers=[
    # Trove classifiers
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    # 'License :: OSI Approved :: ISC License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy']
)
