from unittest import TestCase

from interview_preparation_kit.stacks_and_queues import balanced_brackets as testee


class TestIsBalanced(TestCase):

    def test_1(self):
        s1 = "{[()]}"

        result = testee.is_balanced(s1)
        self.assertEqual(True, result)

    def test_2(self):
        s1 = "{[(])}"

        result = testee.is_balanced(s1)
        self.assertEqual(False, result)

    def test_3(self):
        s1 = "{{[[(())]]}}"

        result = testee.is_balanced(s1)
        self.assertEqual(True, result)
