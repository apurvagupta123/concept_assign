from django.test import TestCase

# Create your tests here.
from fib_calculator import utils


class TestFibCalculator(TestCase):
    def test_cal_fib_num(self):
        fib_num = utils.cal_fib_num(1)
        self.assertEqual(fib_num, 1)
        fib_num = utils.cal_fib_num(2)
        self.assertEqual(fib_num, 1)
        fib_num = utils.cal_fib_num(6)
        self.assertEqual(fib_num, 8)
