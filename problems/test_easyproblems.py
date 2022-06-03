"""
EasyProblem class tests.
unittest identifies test classes by the prefix 'Test'
unittest identifies test methods by the prefix 'test_'
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
        actual = EasyProblems.find_longest_common_prefix_optimal_solution(
            ['examen', 'example', 'examinateur', 'examiner'])
        self.assertEqual(expected, actual)  # add assertion here

    """
    020 Valid Parentheses
    Exemple 1 :
    Entrée : s = "()"
    Sortie : true
    
    Exemple 2 :   
    Entrée : s = "()[]{}"
    Sortie : true
    
    Exemple 3 :   
    Entrée : s = "(]"
    Sortie : false
    
    Contraintes :  
    1 <= s.length <= 104
    s se compose uniquement de parenthèses '()[]{}'.
    """

    def test_valid_parentheses_1(self):
        expected = True
        actual = EasyProblems.valid_parentheses("()")
        self.assertEqual(expected, actual)  # add assertion here

    def test_valid_parentheses_2(self):
        expected = True
        actual = EasyProblems.valid_parentheses("()[]{}")
        self.assertEqual(expected, actual)  # add assertion here

    def test_valid_parentheses_3(self):
        expected = False
        actual = EasyProblems.valid_parentheses("(]")
        self.assertEqual(expected, actual)  # add assertion here

    def test_valid_parentheses_4(self):
        expected = True
        actual = EasyProblems.valid_parentheses("{[()]}")
        self.assertEqual(expected, actual)  # add assertion here

    def test_valid_parentheses_5(self):
        expected = True
        actual = EasyProblems.valid_parentheses("{}[()]")
        self.assertEqual(expected, actual)  # add assertion here

    """
    Fusionner deux listes triées
    On vous donne les têtes de deux listes chaînées triées, list1 et list2.
    Fusionnez les deux listes en une seule liste triée. La liste doit être faite en épissant les noeuds des deux 
    premières listes.
    Retournez la tête de la liste fusionnée.
    
    Exemple 1 :
    Entrée : liste1 = [1,2,4], liste2 = [1,3,4].
    Sortie : [1,1,2,3,4,4]
    
    Exemple 2 :
    Entrée : list1 = [], list2 = []
    Sortie : []
    
    Exemple 3 :
    Entrée : list1 = [], list2 = [0]
    Sortie : [0]
    
    Contraintes :
    Le nombre de nœuds dans les deux listes est compris dans l'intervalle [0, 50].
    -100 <= Node.val <= 100
    La liste1 et la liste2 sont triées dans un ordre non décroissant.
    """

    def test_merge_two_sorted_lists_1(self):
        expected = [1, 1, 2, 3, 4, 4]
        actual = EasyProblems.merge_two_sorted_lists(queue1=[1, 2, 4], queue2=[1, 3, 4])
        self.assertEqual(expected, actual, "Test case 1: Should return the 2 listed sorted.")

    def test_merge_two_sorted_lists_2(self):
        expected = []
        actual = EasyProblems.merge_two_sorted_lists(queue1=[], queue2=[])
        self.assertEqual(expected, actual, "Test case 2: Empty input lists should returns an empty list.")

    def test_merge_two_sorted_list_3(self):
        expected = [0]
        actual = EasyProblems.merge_two_sorted_lists(queue1=[], queue2=[0])
        self.assertEqual(expected, actual, "Test case 3: With an empty input list, the second one should be returned.")

    def test_merge_two_sorted_list_4(self):
        expected = [1, 10, 12, 14, 20, 23, 25, 27, 30]
        actual = EasyProblems.merge_two_sorted_lists(queue1=[1, 20, 23, 25, 27], queue2=[10, 12, 14, 30])
        self.assertEqual(expected, actual, "Test case 4: should return the 2 lists sorted.")

    """
    Fails during execution because the list object has no attribute 'val'
    
    def test_merge_two_sorted_lists_optimal_solution_1(self):
        expected = [1, 1, 2, 3, 4, 4]
        actual = EasyProblems.merge_two_sorted_lists_optimal_solution(linkedlist1=[1, 2, 4], linkedlist2=[1, 3, 4])
        self.assertEqual(expected, actual)  # add assertion here

    def test_merge_two_sorted_lists_optimal_solution_2(self):
        expected = []
        actual = EasyProblems.merge_two_sorted_lists_optimal_solution(linkedlist1=[], linkedlist2=[])
        self.assertEqual(expected, actual)  # add assertion here

    def test_merge_two_sorted_lists_optimal_solution_3(self):
        expected = [0]
        actual = EasyProblems.merge_two_sorted_lists_optimal_solution(linkedlist1=[], linkedlist2=[0])
        self.assertEqual(expected, actual)  # add assertion here

    def test_merge_two_sorted_lists_optimal_solution_4(self):
        expected = [1, 10, 12, 14, 20, 23, 25, 27, 30]
        actual = EasyProblems.merge_two_sorted_lists_optimal_solution(linkedlist1=[1, 20, 23, 25, 27],
                                                                      linkedlist2=[10, 12, 14, 30])
        self.assertEqual(expected, actual)  # add assertion here
    """

    """
    Easy 026 Remove Duplicates from Sorted Array 
    Juge personnalisé :
    Le juge testera votre solution avec le code suivant :
    int[] nums = [...] ; // Tableau d'entrée
    int[] expectedNums = [...] ; // La réponse attendue avec la longueur correcte
    int k = removeDuplicates(nums) ; // Appelle votre implémentation
    assert k == expectedNums.length ;
    for (int i = 0 ; i < k ; i++) {
    assert nums[i] == expectedNums[i] ;
    }
    Si toutes les assertions passent, alors votre solution sera acceptée.
    
    #### Exemple 1 :
    Entrée : nums = [1,1,2]
    Sortie : 2, nums = [1,2,_]
    Explication : Votre fonction doit retourner k = 2, les deux premiers éléments de nums étant respectivement 1 et 2.
    Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).
    
    #### Exemple 2 :
    Entrée : nums = [0,0,1,1,1,2,2,3,3,4]
    Sortie : 5, nums = [0,1,2,3,4,,,,,_]
    Explication : Votre fonction devrait renvoyer k = 5, les cinq premiers éléments de nums étant respectivement 0, 1, 2, 3 et 4.
    Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).
    
    #### Contraintes :
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums est trié dans un ordre non décroissant.
    """

    def test_remove_duplicates_1(self):
        nums = [1, 1, 2]
        expected_nums = [1, 2]
        actual = EasyProblems.remove_duplicates(nums)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1

    def test_remove_duplicates_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_nums = [0, 1, 2, 3, 4]
        actual = EasyProblems.remove_duplicates(nums)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1

    def test_remove_duplicates_solution_leetcode_1(self):
        nums = [1, 1, 2]
        expected_nums = [1, 2]
        actual = EasyProblems.remove_duplicates_solution_leetcode(nums)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1

    def test_remove_duplicates_solution_leetcode_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_nums = [0, 1, 2, 3, 4]
        actual = EasyProblems.remove_duplicates_solution_leetcode(nums)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1

    """
    027 Remove Element - Supprimer un élément 
    
    Le juge testera votre solution avec le code suivant :
    int[] nums = [...] ; // Tableau d'entrée
    int val = ... ; // Valeur à supprimer
    int[] expectedNums = [...] ; // La réponse attendue avec la longueur correcte.
    // Elle est triée et aucune valeur n'est égale à val.
    
    int k = removeElement(nums, val) ; // Appelle votre implémentation
    
    assert k == expectedNums.length ;
    sort(nums, 0, k) ; // Trie les k premiers éléments de nums
    for (int i = 0 ; i < actualLength ; i++) {
    assert nums[i] == expectedNums[i] ;
    }
    Si toutes les assertions passent, alors votre solution sera acceptée.
    
    Exemple 1 :
    Entrée : nums = [3,2,2,3], val = 3
    Sortie : 2, nums = [2,2,,]
    Explication : Votre fonction doit renvoyer k = 2, les deux premiers éléments de nums étant 2.
    Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).
    
    Exemple 2 :
    Entrée : nums = [0,1,2,2,3,0,4,2], val = 2
    Sortie : 5, nums = [0,1,4,0,3,,,_]
    Explication : Votre fonction devrait retourner k = 5, avec les cinq premiers éléments de nums contenant 0, 0, 1, 3, et 4.
    Notez que les cinq éléments peuvent être retournés dans n'importe quel ordre.
    Ce que vous laissez au-delà de k retourné n'a pas d'importance (d'où les caractères de soulignement).
    
    Contraintes :
    0 <= nums.length <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100
    """

    def test_remove_element_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        actual = EasyProblems.remove_element(nums, val)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1

    def test_remove_element_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_nums = [0, 1, 3, 0, 4]
        actual = EasyProblems.remove_element(nums, val)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1

    def test_remove_element_leetcode_solution_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        actual = EasyProblems.remove_element_leetcode_solution(nums, val)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1

    def test_remove_element_leetcode_solution_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_nums = [0, 1, 3, 0, 4]
        actual = EasyProblems.remove_element_leetcode_solution(nums, val)
        assert actual == len(expected_nums)
        i = 0
        while i < len(expected_nums):
            assert nums[i] == expected_nums[i]
            i += 1




if __name__ == '__main__':
    unittest.main()
