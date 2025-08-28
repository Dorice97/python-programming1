import unittest

from utils.subtraction import subtraction

class Test(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtraction(-3,-2),-5)

    def test_positive_numbers(self):
        self.assertEqual(subtraction(5,1),6)