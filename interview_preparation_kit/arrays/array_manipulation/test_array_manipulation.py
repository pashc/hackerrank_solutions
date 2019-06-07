from unittest import TestCase

from . import array_manipulation as testee


class TestArrayManipulation(TestCase):

    def test_1(self):
        n = 5
        queries = [[1, 2, 100],
                   [2, 5, 100],
                   [3, 4, 100]]

        result = testee.array_manipulation(n, queries)
        self.assertEqual(result, 200)

    def test_2(self):
        n = 10
        queries = [[1, 5, 3],
                   [4, 8, 7],
                   [6, 9, 1]]

        result = testee.array_manipulation(n, queries)
        self.assertEqual(result, 10)

    def test_3(self):
        # 1__2__3__4__5__6__7__8__9__10_11
        #
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 8, 0, 0, 0, 0, -8, 0, 0, 0, 0]
        # [0, 8, 7, 0, 0, -7, -8, 0, 0, 0, 0]
        # [1, 8, 7, 0, 0, -7, -8, 0, -1, 0, 0]
        # [1, 8, 7, 0, 15, -7, -8, 0, -1, -15, 0]
        #
        # sum(1, 8, 7, 15) = 31
        n = 10
        queries = [[2, 6, 8],
                   [3, 5, 7],
                   [1, 8, 1],
                   [5, 9, 15]]

        result = testee.array_manipulation(n, queries)
        self.assertEqual(result, 31)
