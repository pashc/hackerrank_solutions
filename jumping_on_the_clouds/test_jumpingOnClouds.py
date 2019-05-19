from unittest import TestCase

from . import jumping_on_the_clouds as testee


class TestJumpingOnClouds(TestCase):

    def test_1(self):
        n = 6
        c = [0, 0, 0, 0, 1, 0]
        min_jumps = testee.jumping_on_clouds(n, c)
        self.assertEqual(min_jumps, 3)

    def test_2(self):
        n = 6
        c = [0, 0, 0, 1, 0, 0]
        min_jumps = testee.jumping_on_clouds(n, c)
        self.assertEqual(min_jumps, 3)

    def test_3(self):
        n = 7
        c = [0, 0, 1, 0, 0, 1, 0]
        min_jumps = testee.jumping_on_clouds(n, c)
        self.assertEqual(min_jumps, 4)
