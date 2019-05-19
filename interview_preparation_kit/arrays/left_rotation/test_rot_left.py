from unittest import TestCase

from . import left_rotation as testee


class TestRot_left(TestCase):

    def test_1(self):
        n = 5
        d = 4
        a = [1, 2, 3, 4, 5]
        result = testee.rot_left(n, d, a)
        self.assertEqual(result, [5, 1, 2, 3, 4])

    def test_2(self):
        n = 20
        d = 10
        a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
        result = testee.rot_left(n, d, a)
        self.assertEqual(result,
                         [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77])

    def test_3(self):
        n = 15
        d = 13
        a = [33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97]
        result = testee.rot_left(n, d, a)
        self.assertEqual(result,
                         [87, 97, 33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60])
