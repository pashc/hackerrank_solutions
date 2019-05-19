from unittest import TestCase

from . import counting_valleys as testee


class TestCountingValleys(TestCase):

    def test_1(self):
        n = 8
        s = 'UDDDUDUU'
        valleys = testee.counting_valleys(n, s)

        self.assertEqual(valleys, 1)

    def test_2(self):
        n = 12
        s = 'DDUUDDUDUUUD'
        valleys = testee.counting_valleys(n, s)

        self.assertEqual(valleys, 2)
