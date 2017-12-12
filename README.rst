===============
Turbotools
===============

.. image:: https://travis-ci.org/anshengme/turbotools.svg?branch=master
   :target: https://travis-ci.org/anshengme/turbotools

.. image:: https://coveralls.io/repos/github/anshengme/turbotools/badge.svg?branch=master
   :target: https://coveralls.io/github/anshengme/turbotools?branch=master

.. image:: https://img.shields.io/pypi/v/turbotools.svg?
   :target: http://badge.fury.io/py/turbotools

.. image:: https://img.shields.io/pypi/pyversions/turbotools.svg
   :target: https://github.com/anshengme/turbotools

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
   :target: https://github.com/anshengme/turbotools/blob/master/LICENSE

常用的小工具合集，`Documentation on Readthedocs <https://turbotools.readthedocs.io/>`_。

安装
===============
使用pip安装

.. code-block:: bash

    $ pip install turbotools


或者从源码包安装

.. code-block:: bash

    $ git clone https://github.com/anshengme/turbotools
    $ cd turbotools
    $ python setup.py install

示例
===============

- 获取随机字符串

.. code-block:: pycon

    >>> from turbotools.utils import get_random_str
    >>> get_random_str()
    's8pqVnVfykU8QxGIMD3z2id4DkQGdOc2'

    >>> get_random_str(length=4)
    'Muea'

    >>> get_random_str(length=4, chars='123456')
    '2231'

发布PyPi
===============

.. code-block:: bash

    $ python setup.py sdist
    $ twine upload dist/*
