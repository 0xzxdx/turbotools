from __future__ import print_function

from turbotools import Turbotools


def main():
    """main
    """
    my_udemy = Turbotools(url='xxxx', token='xxxx')
    print(type(my_udemy))
    return my_udemy


if __name__ == '__main__':
    print(main())
