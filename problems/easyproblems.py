"""
Easy Problems class.
001 - Two Sum
"""
import difflib

from PIL._imaging import outline


class EasyProblems:

    @classmethod
    def sum_two_numbers(cls, numbers, target):
        """
        :param numbers: a list of integers
        :param target: a number to be summed up to
        :return: a list containing the indices of the two numbers [x, y] if there found else an empty list []
        Runtime complexity = O(n) to iterate over the numbers
        Space complexity = O(n) to store numbers_indices in the memory
        """
        numbers_indices = {}
        for index, number in enumerate(numbers):
            difference = target - number
            if difference in numbers_indices:
                return [numbers_indices[difference], index]
            numbers_indices[number] = index
        return []

    @classmethod
    def reverse_integer(cls, my_integer):
        """
        :param my_integer:
        :return: my_integer reversed
        Runtime complexity: O(n) to iterate over all digits
        Space complexity: O(n) to store reversed on the disk
        """
        is_negative = my_integer < 0  # save the sign of the input
        my_integer = abs(my_integer)
        reversed_input = 0  # placeholder of the output
        while my_integer != 0:
            reversed_input = reversed_input * 10 + my_integer % 10
            my_integer //= 10
        if is_negative:
            return -reversed_input
        else:
            return reversed_input

    @classmethod
    def is_palindrome(cls, x):
        """
        Vérifiez l'équivalence du premier et du dernier caractère, en allant vers l'intérieur.
        Temps - O(n)
        Espace - O(1)
        :param x:
        :return:
        """
        s = str(x)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    @classmethod
    def convert_roman_to_integer(cls, roman):
        """
        Temps: O(n) pour parcourir la liste des nombres entiers dérivés des nombres romains.
        Espace: O(n) pour sauvegarder la list contenant les nombres entiers dérivés des nombres romains.
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
        :param roman:
        :return integer:
        """
        int_roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        int_list = []
        result = 0
        for r in roman:
            int_list.append(int_roman_dict.get(r))
        current = 0
        next_nbr = 1
        smaller_than = False  # indicate if the before last number was smaller than the last number.
        while next_nbr < len(int_list):
            if int_list[current] < int_list[next_nbr]:
                result += int_list[next_nbr] - int_list[current]
                current += 2
                next_nbr += 2
                smaller_than = True
            else:
                result += int_list[current]
                current += 1
                next_nbr += 1
                smaller_than = False
        if not smaller_than:
            result += int_list[current]
        return result

    @classmethod
    def convert_roman_to_integer_optimal_solution(cls, roman):
        """
        Explication:
        Itère le long de roman, en vérifiant si les 2 caractères suivants correspondent à un chiffre romain valide.
        Si c'est le cas, ajoute la valeur du chiffre au résultat. Sinon, le caractère suivant doit correspondre à un
        chiffre, qui est ajouté au résultat.
        Temps: O(n) pour parcourir les n chiffre romains.
        Espace: O(1)
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
        :param roman:
        :return integer:
        """
        single_roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        double_roman_dict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        result = 0
        i = 0
        while i < len(roman):
            if roman[i:i + 2] in double_roman_dict:
                result += double_roman_dict.get(roman[i:i + 2])
                i += 2
            else:
                result += single_roman_dict.get(roman[i])
                i += 1
        return result

    @classmethod
    def find_longest_common_prefix(cls, string_list):
        """
        Explication:
        Trier la liste de chaînes de caractères par ordre de longueur croissante.
        Itérer sur les caractères de la première chaîne de la liste.
        Comparer de facon incrémentielle les sous-chaînes de cette chaîne avec ceux des autres chaînes.
        Arrêter la comparaison dès qu'une sous-chaîne n'apparait pas dans toutes les chaînes ou dès que le bout
        de la première chaîne est atteinte
        Renvoyer la sous-chaîne précédente.
        Temps: O(k*n) parcourt la liste d'entrées contenant n chaînes de caractères maximal k fois. k étant le nombre
        de caractères du plus court mot de la liste d'entrée.
        Espace: O(1)
        Exemple 1: ['django', 'python', 'exit', 'framework'] renvoie ''
        Exemple 2: ['papaye', 'python', 'papa', 'pater'] renvoie 'p'
        Exemple 3: ['examen', 'example', 'examinateur', 'examiner'] renvoie 'exam'
        :param string_list:
        :return: longest_common_substring
        """
        longest_common_substring = ''
        string_list.sort(key=len)  # nlog(n) - Timsort
        string_list_len = len(string_list)
        first_string = string_list[0]
        first_string_len = len(first_string)
        i = 0  # index of the last character of the first_string
        while i <= first_string_len:
            previous_substring = first_string[0:i]
            current_substring = first_string[0:i + 1]
            j = 1  # index of the current string being compared
            while j < string_list_len:
                if not string_list[j].startswith(current_substring):
                    longest_common_substring = previous_substring
                    return longest_common_substring
                j += 1
            i += 1
        return longest_common_substring

    @classmethod
    def find_longest_common_prefix_optimal_solution(cls, string_list):
        """
        Trier les chaînes de caractères et trouver le préfixe le plus long de la première et de la dernière, qui sont
        les plus différentes.
        On peut aussi insérer toutes les chaînes de caractères dans un arbre et trouver le premier nœud ayant plus
        d'un enfant.
        C'est l'heure : O(k*n log(n)) où k est la longueur de la plus longue chaîne et n est le nombre de chaînes.
        Espace: O(1)
        Exemple 1: ['django', 'python', 'exit', 'framework'] renvoie ''
        Exemple 2: ['papaye', 'python', 'papa', 'pater'] renvoie 'p'
        Exemple 3: ['examen', 'example', 'examinateur', 'examiner'] renvoie 'exam'
        :param string_list:
        :return: longest_common_substring
        """
        longest_common_substring = ''
        string_list.sort()  # O(nlog(n)) - Timsort
        first_string = string_list[0]
        last_string = string_list[-1]
        first_string_len = len(first_string)
        i = 0  # index of the last character of the first_string and the last_string
        while i <= first_string_len:
            previous_substring = first_string[0:i]
            current_substring = first_string[0:i + 1]
            if not last_string.startswith(current_substring):
                longest_common_substring = previous_substring
                return longest_common_substring
            i += 1
        return longest_common_substring

    @classmethod
    def valid_parentheses(cls, brackets):
        """
        Explication:
        Maintain a stack of opening brackets. For each closing brackets pop the head of the stack and check it matches.
        Time: O(n)
        Space: O(n)
        :param brackets:
        :return: valid or not
        """
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for b in brackets:
            if b in match:
                stack.append(b)
            else:
                if not stack or match[stack.pop()] != b:
                    return False
        return not stack

    @classmethod
    def merge_two_sorted_lists(cls, queue1, queue2):
        """
        Explication:
        Aussi longtemps qu'aucune file d'attente n'est vide, pousser le plus petit parmi chaque premier élément des
        2 files d'attentes sur la pile.
        Si une des files d'attende est vide, pousser tous les éléments de l'autre file sur la pile.
        Temps: O(m+n)
        Espace: O(n+m)
        :param queue1:
        :param queue2:
        :return:
        """
        stack = []
        while queue1 and queue2:
            """
            equivalent to while len(queue1) > 0 and len(queue2) > 0:
            or while bool(queue1) and bool(queue2):
            because bool([]) = False and bool(['not empty']) = True
            """
            if queue1[0] < queue2[0]:
                stack.append(queue1.pop(0))
            else:
                stack.append(queue2.pop(0))
        stack.extend(queue1 or queue2)
        """
        equivalent to if queue1: stack.extend(queue1) else: stack.extend(queue2)
        """
        return stack

    """
    Explication:
    Tant qu'il y a des noeuds dans les deux listes, on établit un lien avec le noeud de tête le plus bas et on
    incrémente cette liste. Enfin, établissez un lien avec la liste des noeuds restants.
    Temps: O(m+n)
    Espace: O(1)
    :param linkedlist1:
    :param linkedlist2:
    :return:
    Fail during execution because the list object has no attribute 'val'

    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    @classmethod
    def merge_two_sorted_lists_optimal_solution(cls, linkedlist1, linkedlist2):
  

        prev = dummy = EasyProblems.ListNode(None)
        while linkedlist1 and linkedlist2:
            if linkedlist1.val < linkedlist2.val:
                prev.next = linkedlist1
                linkedlist1 = linkedlist1.next
            else:
                prev.next = linkedlist2
                linkedlist2 = linkedlist2.next
        prev.next = linkedlist1 or linkedlist2
        return dummy.next
    """

if __name__ == '__main__':
    pass

