import unittest
from Functions import Functions


class Base():
    def __init__(self):
        self.functions = Functions()


class TestBase(unittest.TestCase, Base):

    def setUp(self):
        Base.__init__(self)

    def test_sum_function(self):
        assert self.functions.sum(1,3) == 4

    def test_divide_function(self):
        print "====",self.functions.difference(10,4)

