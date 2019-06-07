from unittest import TestCase

from . import check_magazine as testee


class TestCheckMagazine(TestCase):

    def test_1(self):
        magazine = "give me one grand today night".split()
        note = "give one grand today".split()
        result = testee.check_magazine(magazine, note)
        self.assertEqual(result, "Yes")

    def test_2(self):
        magazine = "two times three is not four".split()
        note = "two times two is four".split()
        result = testee.check_magazine(magazine, note)
        self.assertEqual(result, "No")

    def test_3(self):
        magazine = "give me one grand today night".split()
        note = "give one grand today".split()
        result = testee.check_magazine(magazine, note)
        self.assertEqual(result, "Yes")
