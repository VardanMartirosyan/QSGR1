import math
import unittest

class TestClass(unittest.TestCase):
    def setUp(self):
        self.num = math.pow(3, 4)

    def test_pow(self):
        assert self.num == 81

    def tearDown(self):
        del self.num
