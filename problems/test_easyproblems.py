"""
EasyProblem class tests.
"""
import unittest
from problems.easyproblems import EasyProblems
# from problems.easyproblems import sum_two_numbers


class TestEasyProblems(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, i.e. the data that the tests need. This method is called before each test."""

    def test_sum_two_numbers_with_list_of_1_number(self):
        expected = []
        actual = EasyProblems.sum_two_numbers(self, [5], 8)
        self.assertEqual(expected, actual)  # add assertion here

    def test_sum_two_numbers_with_target_found(self):
        expected = [1, 2]
        actual = EasyProblems.sum_two_numbers(self, [7, 3, 5], 8)
        self.assertEqual(expected, actual)  # add assertion here

    def test_sum_two_numbers_with_target_not_found(self):
        expected = []
        actual = EasyProblems.sum_two_numbers(self, [7, 3, 5], 4)
        self.assertEqual(expected, actual)  # add assertion here
    
    def test_sum_two_numbers_with_empty_list(self):
        expected = []
        actual = EasyProblems.sum_two_numbers(self, [], 8)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
