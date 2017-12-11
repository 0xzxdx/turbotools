import unittest

from turbotools.utils import get_random_str


class UtilsTest(unittest.TestCase):
    def test_get_random_str(self):
        random_str = get_random_str(length=4, chars='0123456789')
        self.assertEqual(isinstance(int(random_str), int), True)
        self.assertEqual(len(random_str), 4)
