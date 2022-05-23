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

    """
    009 Palindrome Number
    """

    def test_1_character_palindrome(self):
        expected = True
        actual = EasyProblems.is_palindrome(1)
        self.assertEqual(expected, actual)  # add assertion here

    def test_odd_character_len_palindrome(self):
        expected = True
        actual = EasyProblems.is_palindrome(14341)
        self.assertEqual(expected, actual)  # add assertion here

    def test_even_character_len_palindrome(self):
        expected = True
        actual = EasyProblems.is_palindrome(1441)
        self.assertEqual(expected, actual)  # add assertion here

    def test_non_palindrome(self):
        expected = False
        actual = EasyProblems.is_palindrome(1471)
        self.assertEqual(expected, actual)  # add assertion here

if __name__ == '__main__':
    unittest.main()
