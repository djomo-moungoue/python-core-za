"""
EasyProblem class tests.
"""
import unittest
from problems.easyproblems import EasyProblems
# from problems.easyproblems import sum_two_numbers


class TestEasyProblems(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, i.e. the data that the tests need. This method is called before each test."""

    """
    001 Two Sum 
    """

    def test_sum_two_numbers_with_list_of_1_number(self):
        expected = []
        actual = EasyProblems.sum_two_numbers([5], 8)
        self.assertEqual(expected, actual)  # add assertion here

    def test_sum_two_numbers_with_target_found(self):
        expected = [1, 2]
        actual = EasyProblems.sum_two_numbers([7, 3, 5], 8)
        self.assertEqual(expected, actual)  # add assertion here

    def test_sum_two_numbers_with_target_not_found(self):
        expected = []
        actual = EasyProblems.sum_two_numbers([7, 3, 5], 4)
        self.assertEqual(expected, actual)  # add assertion here
    
    def test_sum_two_numbers_with_empty_list(self):
        expected = []
        actual = EasyProblems.sum_two_numbers([], 8)
        self.assertEqual(expected, actual)  # add assertion here

    """
    007 Reverse Integer
    """

    def test_reverse_1_digit_negative_integer(self):
        expected = -1
        actual = EasyProblems.reverse_integer(-1)
        self.assertEqual(expected, actual)  # add assertion here


    def test_reverse_1_digit_positive_integer(self):
        expected = 0
        actual = EasyProblems.reverse_integer(0)
        self.assertEqual(expected, actual)  # add assertion here


    def test_reverse_3_digits_negative_integer(self):
        expected = -321
        actual = EasyProblems.reverse_integer(-123)
        self.assertEqual(expected, actual)  # add assertion here


    def test_reverse_3_digits_positive_integer(self):
        expected = 321
        actual = EasyProblems.reverse_integer(123)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
