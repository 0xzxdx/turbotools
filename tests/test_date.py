import unittest
from datetime import datetime

from turbotools.date import datetime_to_str
from turbotools.date import datetime_transfer


class DateTest(unittest.TestCase):
    def setUp(self):
        self.now_time = datetime.now()
        self.range_count = 10

    def test_datetime_to_str(self):
        data = datetime_to_str({'now': self.now_time}, 'now')
        self.assertEqual(isinstance(data['now'], str), True)

    def test_datetime_transfer(self):
        data_list = [{'time': self.now_time, 'now': self.now_time} for _ in range(self.range_count)]
        data = datetime_transfer(data_list, ['time', 'now'])
        for now_time in data:
            self.assertEqual(isinstance(now_time['time'], str), True)
            self.assertEqual(isinstance(now_time['now'], str), True)
