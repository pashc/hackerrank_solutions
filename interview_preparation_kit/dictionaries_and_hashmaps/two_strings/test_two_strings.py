from unittest import TestCase

from . import two_strings as testee


class TestTwoStrings(TestCase):

    def test_1(self):
        s1 = "hello"
        s2 = "world"

        result = testee.two_strings(s1, s2)
        self.assertEqual(result, "YES")

    def test_2(self):
        s1 = "hi"
        s2 = "world"

        result = testee.two_strings(s1, s2)
        self.assertEqual(result, "NO")
