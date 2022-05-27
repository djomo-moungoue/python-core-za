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

    """
    013 Roman to Integer
    Exemple 1: I renvoie 1 <br/>
    Exemple 2: V renvoie 5 <br/>
    Exemple 3: X renvoie 10 <br/>
    Exemple 4: L renvoie 50 <br/>
    Exemple 5: C renvoie 100 <br/>
    Exemple 6: D renvoie 500 <br/>
    Exemple 7: M renvoie 1000 <br/>
    Exemple 8: III renvoie 3 <br/>
    Exemple 9: IV renvoie 4 <br/>
    Exemple 10: MCMLXXXVIII renvoie 1988 <br/>
    Exemple 11: MMXXII renvoie 2022 <br/>
    Exemple 12: MMMCMXCIX renvoie 3999 <br/>
    """

    def test_roman_I_to_integer_1(self):
        expected = 1
        actual = EasyProblems.convert_roman_to_integer('I')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_III_to_integer_3(self):
        expected = 3
        actual = EasyProblems.convert_roman_to_integer('III')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_IV_to_integer_4(self):
        expected = 4
        actual = EasyProblems.convert_roman_to_integer('IV')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_MMMMCMXCIX_to_integer_1988(self):
        expected = 1988
        actual = EasyProblems.convert_roman_to_integer('MCMLXXXVIII')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_MMXXII_to_integer_2022(self):
        expected = 2022
        actual = EasyProblems.convert_roman_to_integer('MMXXII')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_MMMCMXCIX_to_integer_3999(self):
        expected = 3999
        actual = EasyProblems.convert_roman_to_integer('MMMCMXCIX')
        self.assertEqual(expected, actual)  # add assertion here

    """
    013 Roman to Integer - Optimal Solution
    Exemple 1: I renvoie 1 <br/>
    Exemple 2: V renvoie 5 <br/>
    Exemple 3: X renvoie 10 <br/>
    Exemple 4: L renvoie 50 <br/>
    Exemple 5: C renvoie 100 <br/>
    Exemple 6: D renvoie 500 <br/>
    Exemple 7: M renvoie 1000 <br/>
    Exemple 8: III renvoie 3 <br/>
    Exemple 9: IV renvoie 4 <br/>
    Exemple 10: MCMLXXXVIII renvoie 1988 <br/>
    Exemple 11: MMXXII renvoie 2022 <br/>
    Exemple 12: MMMCMXCIX renvoie 3999 <br/>
    """

    def test_roman_I_to_integer_1_optimal_solution(self):
        expected = 1
        actual = EasyProblems.convert_roman_to_integer_optimal_solution('I')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_III_to_integer_3_optimal_solution(self):
        expected = 3
        actual = EasyProblems.convert_roman_to_integer_optimal_solution('III')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_IV_to_integer_4_optimal_solution(self):
        expected = 4
        actual = EasyProblems.convert_roman_to_integer_optimal_solution('IV')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_MMMMCMXCIX_to_integer_1988_optimal_solution(self):
        expected = 1988
        actual = EasyProblems.convert_roman_to_integer_optimal_solution('MCMLXXXVIII')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_MMXXII_to_integer_2022_optimal_solution(self):
        expected = 2022
        actual = EasyProblems.convert_roman_to_integer_optimal_solution('MMXXII')
        self.assertEqual(expected, actual)  # add assertion here

    def test_roman_MMMCMXCIX_to_integer_3999_optimal_solution(self):
        expected = 3999
        actual = EasyProblems.convert_roman_to_integer_optimal_solution('MMMCMXCIX')
        self.assertEqual(expected, actual)  # add assertion here

    """
    014 Longest Common Prefix
    Exemple 1: ['django', 'python', 'exit', 'framework'] renvoie ''
    Exemple 2: ['papaye', 'python', 'papa', 'pater'] renvoie 'p'
    Exemple 3: ['examen', 'example', 'examinateur', 'examiner'] renvoie 'exam'
    """

    def test_find_empty_string(self):
        expected = ''
        actual = EasyProblems.find_longest_common_prefix(['django', 'python', 'exit', 'framework'])
        self.assertEqual(expected, actual)  # add assertion here

    def test_find_p(self):
        expected = 'p'
        actual = EasyProblems.find_longest_common_prefix(['papaye', 'python', 'papa', 'pater'])
        self.assertEqual(expected, actual)  # add assertion here

    def test_find_exam(self):
        expected = 'exam'
        actual = EasyProblems.find_longest_common_prefix(['examen', 'example', 'examinateur', 'examiner'])
        self.assertEqual(expected, actual)  # add assertion here

    """
    014 Longest Common Prefix
    Exemple 1: ['django', 'python', 'exit', 'framework'] renvoie ''
    Exemple 2: ['papaye', 'python', 'papa', 'pater'] renvoie 'p'
    Exemple 3: ['examen', 'example', 'examinateur', 'examiner'] renvoie 'exam'
    """

    def test_find_empty_string_optimal_solution(self):
        expected = ''
        actual = EasyProblems.find_longest_common_prefix_optimal_solution(['django', 'python', 'exit', 'framework'])
        self.assertEqual(expected, actual)  # add assertion here

    def test_find_p_optimal_solution(self):
        expected = 'p'
        actual = EasyProblems.find_longest_common_prefix_optimal_solution(['papaye', 'python', 'papa', 'pater'])
        self.assertEqual(expected, actual)  # add assertion here

    def test_find_exam_optimal_solution(self):
        expected = 'exam'
        actual = EasyProblems.find_longest_common_prefix_optimal_solution(['examen', 'example', 'examinateur', 'examiner'])
        self.assertEqual(expected, actual)  # add assertion here

if __name__ == '__main__':
    unittest.main()
