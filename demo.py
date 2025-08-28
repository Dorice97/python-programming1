import unittest

from utils.addition import addition

# build a testcase
class TestAddition(unittest.TestCase) :
    def test_add_positive(self) :

        self.assertEqual(addition(2,3),5)
