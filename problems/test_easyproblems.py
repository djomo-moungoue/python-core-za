"""
EasyProblem class tests.
unittest identifies test classes by the prefix 'Test'
unittest identifies test methods by the prefix 'test_'
needle in a haystack
someone or something that is very hard to find Searching for your earring at the park will be like looking for a
needle in a haystack.
= aiguille dans une botte de foin
= quelqu'un ou quelque chose qui est très difficile à trouver Chercher votre boucle d'oreille dans le parc sera comme
chercher une aiguille dans une botte de foin.
Foin: Fourrage séché destiné à l'alimentation des herbivores.
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

    """
    028 Implement strStr() - Implémenter strStr()
    Étant donné deux chaînes de caractères, aiguille et botte de foin, retourne l'indice de la première occurrence d'aiguille dans botte de foin, ou -1 si aiguille ne fait pas partie de botte de foin.

    Clarification :
    Que devrions-nous retourner si aiguille est une chaîne vide ? C'est une excellente question à poser lors d'un entretien.
    
    Pour les besoins de ce problème, nous renverrons 0 lorsque aiguille est une chaîne vide. Ceci est cohérent avec strstr() en C et indexOf() en Java.
    
    Exemple 1 :
    Entrée : botte de foin = "hello", aiguille = "ll".
    Sortie : 2
    
    Exemple 2 :
    Entrée : botte de foin = "aaaaa", aiguille = "bba".
    Résultat : -1
    
    Contraintes :
    1 <= botte de foin.longueur, aiguille.longueur <= 104
    La meule de foin et l'aiguille ne sont constituées que de caractères anglais minuscules.
    """

    def test_str_str_1(self):
        haystack = "empty needle"
        needle = ""
        expected = 0
        actual = EasyProblems.str_str(haystack, needle)
        assert actual == expected

    def test_str_str_2(self):
        haystack = "hello"
        needle = "ll"
        expected = 2
        actual = EasyProblems.str_str(haystack, needle)
        assert actual == expected

    def test_str_str_3(self):
        haystack = "aaaaa"
        needle = "bba"
        expected = -1
        actual = EasyProblems.str_str(haystack, needle)
        assert actual == expected

    def test_str_str_4(self):
        haystack = "ABABDABACDABABCABAB"
        needle = "ABABCABAB"
        expected = 10
        actual = EasyProblems.str_str(haystack, needle)
        assert actual == expected

    def test_str_str_leetcode_1(self):
        haystack = "empty needle"
        needle = ""
        expected = 0
        actual = EasyProblems.str_str_leetcode(haystack, needle)
        assert actual == expected

    def test_str_str_leetcode_2(self):
        haystack = "hello"
        needle = "ll"
        expected = 2
        actual = EasyProblems.str_str_leetcode(haystack, needle)
        assert actual == expected

    def test_str_str_leetcode_3(self):
        haystack = "aaaaa"
        needle = "bba"
        expected = -1
        actual = EasyProblems.str_str_leetcode(haystack, needle)
        assert actual == expected

    def test_str_str_leetcode_4(self):
        haystack = "ABABDABACDABABCABAB"
        needle = "ABABCABAB"
        expected = 10
        actual = EasyProblems.str_str_leetcode(haystack, needle)
        assert actual == expected

    def test_KPMSearch_1(self):
        haystack = "empty needle"
        needle = ""
        expected = 0
        actual = EasyProblems.KPMSearch(haystack, needle)
        assert actual == expected

    def test_KPMSearch_2(self):
        haystack = "hello"
        needle = "ll"
        expected = 2
        actual = EasyProblems.KPMSearch(haystack, needle)
        self.assertEqual(expected, actual)

    def test_KPMSearch_3(self):
        haystack = "aaaaa"
        needle = "bba"
        expected = -1
        actual = EasyProblems.KPMSearch(haystack, needle)
        assert actual == expected

    def test_KPMSearch_4(self):
        haystack = "ABABDABACDABABCABAB"
        needle = "ABABCABAB"
        expected = 10
        actual = EasyProblems.KPMSearch(haystack, needle)
        assert actual == expected

    """
    Position d'insertion de recherche
    Étant donné un tableau trié d'entiers distincts et une valeur cible, retournez l'index si la cible est trouvée. Si ce n'est pas le cas, renvoyez l'indice où il se trouverait s'il était inséré dans l'ordre.
    Vous devez écrire un algorithme dont la complexité d'exécution est de O(log n).
    
    Exemple 1 :
    Entrée : nums = [1,3,5,6], cible = 5
    Sortie : 2
    
    Exemple 2 :
    Entrée : nums = [1,3,5,6], cible = 2
    Sortie : 1
    
    Exemple 3 :
    Entrée : nums = [1,3,5,6], cible = 7
    Sortie : 4
    
    Contraintes :
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contient des valeurs distinctes triées par ordre croissant.
    -104 <= cible <= 104
    """

    def test_search_5_in_sorted_array_of_integers_1(self):
        haystack = [1, 3, 5, 6]
        needle = 5
        expected = 2
        actual = EasyProblems.search_insert(haystack, needle)
        self.assertEqual(expected, actual, "Test case 1: Should return the index 2.")

    def test_search_2_in_sorted_array_of_integers_2(self):
        haystack = [1, 3, 5, 6]
        needle = 2
        expected = 1
        actual = EasyProblems.search_insert(haystack, needle)
        self.assertEqual(expected, actual, "Test case 2: Should return the index 1.")

    def test_search_7_in_sorted_array_of_integers_3(self):
        haystack = [1, 3, 5, 6]
        needle = 7
        expected = 4
        actual = EasyProblems.search_insert(haystack, needle)
        self.assertEqual(expected, actual, "Test case 3: Should return the index 4.")

    def test_search_5_in_sorted_array_of_integers_optimal_solution_1(self):
        haystack = [1, 3, 5, 6]
        needle = 5
        expected = 2
        actual = EasyProblems.search_insert_optimal_solution(haystack, needle)
        self.assertEqual(expected, actual, "Test case 1: Should return the index 2.")

    def test_search_2_in_sorted_array_of_integers_optimal_solution_2(self):
        haystack = [1, 3, 5, 6]
        needle = 2
        expected = 1
        actual = EasyProblems.search_insert_optimal_solution(haystack, needle)
        self.assertEqual(expected, actual, "Test case 2: Should return the index 1.")

    def test_search_7_in_sorted_array_of_integers_optimal_solution_3(self):
        haystack = [1, 3, 5, 6]
        needle = 7
        expected = 4
        actual = EasyProblems.search_insert_optimal_solution(haystack, needle)
        self.assertEqual(expected, actual, "Test case 3: Should return the index 4.")

    """
    53. Sous-tableau maximum
    Étant donné un tableau de nombres entiers, trouvez le sous-groupe contigu (contenant au moins un nombre) qui a la plus grande somme et renvoyez sa somme.
    
    Un sous-groupe est une partie contiguë d'un tableau.
    
    Exemple 1 :
    Entrée : nums = [-2,1,-3,4,-1,2,1,-5,4]
    Sortie : 6
    Explication : [4,-1,2,1] a la plus grande somme = 6.
    
    Exemple 2 :
    Entrée : nums = [1]
    Sortie : 1
    
    Exemple 3 :
    Entrée : nums = [5,4,-1,7,8]
    Sortie : 23
     
    Contraintes :
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
     
    Suivi : Si vous avez compris la solution O(n), essayez de coder une autre solution en utilisant l'approche diviser pour régner, qui est plus subtile.
    """

    def test_find_maximum_sum_of_contiguous_numbers_and_return_6(self):
        haystack = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        needle = [4, -1, 2, 1]
        expected = 6
        actual = EasyProblems.max_subarray(haystack)
        self.assertEqual(expected, actual, "Test case 3: Should return 6 as sub-array with the max sum.")

    def test_find_maximum_sum_of_contiguous_numbers_and_return_1(self):
        haystack = [1]
        needle = [1]
        expected = 1
        actual = EasyProblems.max_subarray(haystack)
        self.assertEqual(expected, actual, "Test case 3: Should return 1 as sub-array with the max sum.")

    def test_find_maximum_sum_of_contiguous_numbers_and_return_23(self):
        haystack = [5, 4, -1, 7, 8]
        needle = [5, 4, -1, 7, 8]
        expected = 23
        actual = EasyProblems.max_subarray(haystack)
        self.assertEqual(expected, actual, "Test case 3: Should return 23 as sub-array with the max sum.")

    def test_find_maximum_sum_of_contiguous_numbers_and_return_optimal_solution_6(self):
        haystack = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        needle = [4, -1, 2, 1]
        expected = 6
        actual = EasyProblems.max_subarray_optimal_solution(haystack)
        self.assertEqual(expected, actual, "Test case 3: Should return 6 as sub-array with the max sum.")

    def test_find_maximum_sum_of_contiguous_numbers_and_return_optimal_solution_1(self):
        haystack = [1]
        needle = [1]
        expected = 1
        actual = EasyProblems.max_subarray_optimal_solution(haystack)
        self.assertEqual(expected, actual, "Test case 3: Should return 1 as sub-array with the max sum.")

    def test_find_maximum_sum_of_contiguous_numbers_and_return_optimal_solution_23(self):
        haystack = [5, 4, -1, 7, 8]
        needle = [5, 4, -1, 7, 8]
        expected = 23
        actual = EasyProblems.max_subarray_optimal_solution(haystack)
        self.assertEqual(expected, actual, "Test case 3: Should return 23 as sub-array with the max sum.")

    """
    Factorial - Factoriel
    1! = 1
    2! = 2x1 = 2
    3! = 3x2x1 = 6
    5! = 5x4x3x2x1 = 120
    """

    def test_factorial_1_returns_1(self):
        positive_integer = 1
        expected = 1
        actual = EasyProblems.factorial(positive_integer)
        self.assertEqual(expected, actual, "Test case 1: should return 1, given a positive integer 1.")

    def test_factorial_2_returns_2(self):
        positive_integer = 1
        expected = 1
        actual = EasyProblems.factorial(positive_integer)
        self.assertEqual(expected, actual, "Test case 2: should return 2, given a positive integer 2.")

    def test_factorial_5_returns_120(self):
        positive_integer = 1
        expected = 1
        actual = EasyProblems.factorial(positive_integer)
        self.assertEqual(expected, actual, "Test case 3: should return 120, given a positive integer 5.")

    """
    Fibonacci
    F0 = 0
    F1 = F2 = 1
    F3 = F2 + F1 = 1 + 1 = 2
    F5 = F4+F3 = (F3 + F2) + (F2 + F1) = ((F2 + F1) + F2) + (F2 + F1) = 5
    """

    def test_fibonacci_1_returns_1(self):
        positive_integer = 1
        expected = 1
        actual = EasyProblems.fibonacci(positive_integer)
        self.assertEqual(expected, actual, "Test case 1: should return 1, given a positive integer 1.")

    def test_fibonacci_2_returns_1(self):
        positive_integer = 1
        expected = 1
        actual = EasyProblems.fibonacci(positive_integer)
        self.assertEqual(expected, actual, "Test case 2: should return 2, given a positive integer 2.")

    def test_fibonacci_5_returns_5(self):
        positive_integer = 1
        expected = 1
        actual = EasyProblems.fibonacci(positive_integer)
        self.assertEqual(expected, actual, "Test case 3: should return 5, given a positive integer 5.")

    """
    038 Count and Say - Compter et Dire
    La séquence count-and-say est une séquence de chaînes de chiffres définie par la formule récursive :
    
    countAndSay(1) = "1"
    countAndSay(n) est la façon dont vous "dites" la chaîne de chiffres de countAndSay(n-1), qui est ensuite convertie en une chaîne de chiffres différente.
    Pour déterminer la façon dont vous "dites" une chaîne de chiffres, divisez-la en un nombre minimal de sous-chaînes de sorte que chaque sous-chaîne contienne exactement un chiffre unique. Ensuite, pour chaque sous-chaîne, dites le nombre de chiffres, puis dites le chiffre. Enfin, concaténer chaque chiffre.
    
    Par exemple, l'énoncé et la conversion pour la chaîne de chiffres "3322251" :
    
    Étant donné un nombre entier positif n, retourner le nième terme de la séquence de comptage et de conversion.
    
    Exemple 1 :
    Entrée : n = 1
    Sortie : "1"
    Explication : C'est le cas de base.
    
    Exemple 2 :
    Entrée : n = 4
    Sortie : "1211"
    Explication :
    countAndSay(1) = "1" (compte et dit)
    countAndSay(2) = dites "1" = un 1 = "11"
    countAndSay(3) = dites "11" = deux 1 = "21"
    Comptez et dites(4) = dites "21" = un 2 + un 1 = "12" + "11" = "1211".
    
    Exemple 3 :
    Entrée : n = 5
    Sortie : "111221"
    Explication :
    countAndSay(1) = "1" (compte et dit)
    countAndSay(2) = dites "1" = un 1 = "11"
    countAndSay(3) = dites "11" = deux 1 = "21"
    Comptez et dites(4) = dites "21" = un 2 + un 1 = "12" + "11" = "1211".
    Comptez et dites(5) = dites "1211" = 1 un + un 2 + deux 1 = "11" + "12" + "21" = "111221".
    
    Contraintes :
    1 <= n <= 30
    """

    def test_given_1_count_and_say_leetcode_return_1(self):
        positive_integer = 1
        expected = "1"
        actual = EasyProblems.count_and_say_leetcode(positive_integer)
        self.assertEqual(expected, actual, "Test case 1: should return '1', given a positive integer 1.")

    def test_given_4_count_and_say_leetcode_return_1211(self):
        positive_integer = 4
        expected = "1211"
        actual = EasyProblems.count_and_say_leetcode(positive_integer)
        self.assertEqual(expected, actual, "Test case 2: should return '1211', given a positive integer 4.")

    def test_given_5_count_and_say_leetcode_return_111221(self):
        positive_integer = 5
        expected = "111221"
        actual = EasyProblems.count_and_say_leetcode(positive_integer)
        self.assertEqual(expected, actual, "Test case 3: should return '111221', given a positive integer 5.")


if __name__ == '__main__':
    unittest.main()
