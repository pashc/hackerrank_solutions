from unittest import TestCase
from . import minimum_swaps_2 as testee


class TestMinimumSwaps(TestCase):

    def test_1(self):
        n = 7
        arr = [1, 3, 5, 2, 4, 6, 7]
        result = testee.minimum_swaps(n, arr)
        self.assertEqual(result, 3)

    def test_2(self):
        n = 4
        arr = [4, 3, 1, 2]
        result = testee.minimum_swaps(n, arr)
        self.assertEqual(result, 3)

    def test_3(self):
        n = 5
        arr = [2, 3, 4, 1, 5]
        result = testee.minimum_swaps(n, arr)
        self.assertEqual(result, 3)

    def test_4(self):
        n = 7
        arr = [1, 3, 5, 2, 4, 6, 7]
        result = testee.minimum_swaps(n, arr)
        self.assertEqual(result, 3)
