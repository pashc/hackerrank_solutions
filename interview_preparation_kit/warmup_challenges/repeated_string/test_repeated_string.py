from unittest import TestCase

from . import repeated_string as testee


class TestRepeatedString(TestCase):

    def test_1(self):
        s = 'aba'
        n = 10
        result = testee.repeated_string(s, n)
        self.assertEqual(result, 7)

    def test_2(self):
        s = 'a'
        n = 1000000
        result = testee.repeated_string(s, n)
        self.assertEqual(result, n)
