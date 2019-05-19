from unittest import TestCase

from . import new_year_chaos as testee


class TestMinimumBribes(TestCase):

    def test_1(self):
        n = 5
        q = [2, 1, 5, 3, 4]
        result = testee.minimum_bribes(n, q)
        self.assertEqual(result, 3)

    def test_2(self):
        n = 5
        q = [2, 5, 1, 3, 4]
        result = testee.minimum_bribes(n, q)
        self.assertEqual(result, 'Too chaotic')

    def test_3(self):
        n = 8
        q = [1, 2, 5, 3, 4, 7, 8, 6]
        result = testee.minimum_bribes(n, q)
        self.assertEqual(result, 4)
