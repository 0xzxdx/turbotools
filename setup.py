import codecs
import os

from turbotools import __title__
from turbotools import __version__
from turbotools import __author__
from turbotools import __email__

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description='Toolset. ',
    long_description=long_description,
    url='https://github.com/anshengme/turbotools',
    license='LICENSE.txt',
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ]
)
