from unittest import TestCase

from . import two_d_array_ds as testee


class TestTwoDArrayDs(TestCase):

    def test_1(self):
        arr = [[1, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0],
               [1, 1, 1, 0, 0, 0],
               [0, 0, 2, 4, 4, 0],
               [0, 0, 0, 2, 0, 0],
               [0, 0, 1, 2, 4, 0]]

        result = testee.hourglass_sum(arr)
        self.assertEqual(result, 19)

    def test_2(self):
        arr = [[1, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0],
               [1, 1, 1, 0, 0, 0],
               [0, 9, 2, -4, -4, 0],
               [0, 0, 0, -2, 0, 0],
               [0, 0, -1, -2, -4, 0]]

        result = testee.hourglass_sum(arr)
        self.assertEqual(result, 13)
