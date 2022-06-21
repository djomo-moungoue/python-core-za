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

    @classmethod
    def remove_duplicates(cls, nums):
        """
        Algorithme :
        Parcourir la liste d'entrée de la gauche vers la droite.
        Repérer les plages d'éléments identiques et les effacer.
        Stopper dès que l'extrêmité droite de la liste est atteint.
        Temps: O(n)
        Espace: O(1)
        Note: this solution works only for mutable sequences
        :param nums:
        :return: len(nums)
        """
        current_index = 0
        next_index = 1
        while next_index < len(nums):
            if nums[current_index] != nums[next_index]:
                del nums[current_index + 1:next_index]
                current_index += 1
                next_index = current_index + 1
            next_index += 1
        return len(nums)

    @classmethod
    def remove_duplicates_solution_leetcode(cls, nums):
        """
        Algorithme :
        Maintient un pointeur vers le prochain index à remplir avec un nouveau nombre. Vérifier chaque nombre par
        rapport au nombre précédent (s'il y en a un) et s'il est différent, se déplacer vers l'index next_new.
        Temps: O(n)
        Espace: O(1)
        Note: this solution works for mutable and immutable sequences
        :param nums:
        :return: len(nums)
        """
        next_new = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[next_new] = nums[i]
                next_new += 1
        return next_new

    @classmethod
    def remove_element(cls, nums, val):
        """
        Algorithme:
        Parcourir la liste d'entrée de la gauche vers la droite.
        Avancer le pointer si l'élément actuel est different de val.
        Sinon effacer l'élément et pointer au même endroit car les listes sont mutables en Python.
        Temps: O(n)
        Espace: O(1)
        :param nums:
        :param val:
        :return: number of val occurrences removed
        """
        i = 0
        while i < len(nums):
            if nums[i] != val:
                i += 1
            else:
                nums.remove(val)
        return len(nums)

    @classmethod
    def remove_element_leetcode_solution(cls, nums, val):
        """
        Algorithme:
        Parcourir la liste d'entrée de la gauche vers la droite.
        Avancer le pointer si l'élément actuel est different de val.
        Sinon effacer l'élément et pointer au même endroit car les listes sont mutables en Python.
        Temps: O(n+k)
        Espace: O(1)
        :param nums:
        :param val:
        :return: number of val occurrences removed
        """
        pointer = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[pointer] = num
                pointer += 1
        return pointer

    @classmethod
    def str_str(cls, haystack, needle):
        """
        Algorithme:
        (0) Si needle es vide renvoyer 0
        (1) Pointer sur la première lettre de needle;
        (2) Parcourir haystack de la gauche vers la droite et comparer ses lettres avec celle de needle pointée;
        (3) Si une lettre est identique de part et d'autre, pointer sur la lettre suivante et répéter (2);
        (4) Si une lettre est différente de part et d'autre, pointer à nouveau sur la première lettre de needle;
        (5) Si le bout de needle est atteint (pointeur = len(needle) - 1), renvoyer la différence entre l'index actuel
        et le pointeur.
        (6) Sinon renvoyer -1
        Temps: O(n) - n étant le nombre de caractères de haystack
        Espace: O(1)
        :param haystack: str
        :param needle: str
        :return: int
        """
        if needle != "":
            pointer = 0
            for index, character in enumerate(haystack):
                if needle[pointer] != character:
                    pointer = 0
                elif pointer != len(needle) - 1:
                    pointer += 1
                else:
                    return index - pointer
            return -1
        else:
            return 0

    @classmethod
    def str_str_leetcode(cls, haystack, needle):
        """
        Algorithme:
        Pour chaque point de départ possible dans la botte de foin, vérifier que les caractères correspondent à
        l'aiguille et les briser si ce n'est pas le cas.
        Alternativement, l'algorithme de Knuth-Morris-Pratt (KMP) améliorerait la complexité temporelle attendue.
        (6) Sinon renvoyer -1
        Temps: O(n^2) - n étant le nombre de caractères de haystack
        Espace: O(1)
        :param haystack: str
        :param needle: str
        :return: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1

    @classmethod
    def KPMSearch(cls, haystack, needle):
        """
        Algorithme:
        Contrairement à l'algorithme naïf, dans lequel nous faisons glisser le motif d'un cran et comparons tous les
        caractères à chaque décalage, nous utilisons une valeur de lps[] pour décider des prochains caractères à faire
        correspondre. L'idée est de ne pas faire correspondre un caractère dont nous savons qu'il le sera de toute façon.
        Comment utiliser lps[] pour décider des prochaines positions (ou pour connaître un nombre de caractères à sauter) ?
        + Nous commençons la comparaison de pat[j] avec j = 0 avec les caractères de la fenêtre actuelle du texte.
        + Nous continuons à comparer les caractères txt[i] et pat[j] et à incrémenter i et j pendant que pat[j] et
        txt[i] continuent à correspondre.
        + Lorsque nous voyons une non-concordance
            + Nous savons que les caractères pat[0..j-1] correspondent à txt[i-j...i-1] (Notez que j commence par 0
            et n'est incrémenté que lorsqu'il y a une correspondance).
            + Nous savons également (d'après la définition ci-dessus) que lps[j-1] est le nombre de caractères de
            pat[0...j-1] qui sont à la fois préfixe et suffixe corrects.
            + De ces deux points, nous pouvons conclure que nous n'avons pas besoin de faire correspondre ces caractères
            lps[j-1] avec txt[i-j...i-1] car nous savons que ces caractères correspondront de toute façon.
        Temps: O(n)
        Espace: O(1)
        :param haystack:
        :param needle:
        :return:
        """
        if needle == "":
            return 0
        len_needle = len(needle)
        len_haystack = len(haystack)
        longest_prefix_suffix = [0] * len_needle
        index_needle = 0

        EasyProblems.compute_longest_prefix_suffix_array(needle, len_needle, longest_prefix_suffix)
        index_haystack = 0
        while index_haystack < len_haystack:
            if needle[index_needle] == haystack[index_haystack]:
                index_haystack += 1
                index_needle += 1
            if index_needle == len_needle:
# These 2 lines replace the return statement if we want to find all occurences
#                print("Pattern found at index"+ str(i-j))
#                index_needle = longest_prefix_suffix[index_needle - 1]
                return index_haystack - index_needle
            elif index_haystack < len_haystack and needle[index_needle] != haystack[index_haystack]:
                if index_needle != 0:
                    index_needle = longest_prefix_suffix[index_needle - 1]
                else:
                    index_haystack += 1
        return -1

    @classmethod
    def compute_longest_prefix_suffix_array(cls, needle, len_needle, longest_prefix_suffix):
        len_previous = 0
        longest_prefix_suffix[0]
        index = 1
        while index < len_needle:
            if needle[index] == needle[len_previous]:
                len_previous += 1
                longest_prefix_suffix[index] = len_previous
                index += 1
            else:
                if len_previous != 0:
                    len_previous = longest_prefix_suffix[len_previous - 1]
                else:
                    longest_prefix_suffix[index] = 0
                    index += 1

    @classmethod
    def search_insert(cls, haystack, needle, right=False, delta=0):
        """
        Cibler récursivement l'élément situé au milieu tableau car celui-ci est trié. (1)
        Si l'élément cibler n'est pas notre cible, répéter (1) dans la moitié gauche du tableau
        si l'élément ciblé est supérieur à notre cible. Dans le cas contraire, répéter (1) dans la
        moitié droite du tableau.
        Si l'élément ciblé est notre cible, renvoyer son index. Sinon renvoyer l'index où il devrait
        être inséré afin que le tableau reste trier.
        Temps: O(log(n))
        Espace: O(1)
        :param delta:
        :param right:
        :param haystack:
        :param needle:
        :return: index of target
        """
        len_haystack = len(haystack)
        index = len_haystack//2
        if needle == haystack[index]:  # target found
            if not right:
                return index
            if right:
                return delta
        if index == 0:  # target not found
            if not right:
                return index+1
            if right:
                return delta+1
        if needle < haystack[index]:  # target probably on the left side of the array
            delta = index
            return EasyProblems.search_insert(haystack[0:index], needle, right, delta)
        if needle > haystack[index]:  # target probably on the right side of the array
            right = True
            delta += index
            return EasyProblems.search_insert(haystack[index:len_haystack], needle, right, delta)

    @classmethod
    def search_insert_optimal_solution(cls, haystack, needle):
        """
        Recherche binaire itérative jusqu'à ce que gauche > droite ou que gauche ou droite sortent du tableau.
        Retourne left (le plus grand index), qui serait le nouvel index de l'entrée insérée (pourrait être len(nums) mais pas -1.
        Temps - O(log n)
        Espace - O(1)
        :param haystack:
        :param needle:
        :return:
        """
        left = 0
        right = len(haystack)
        while left <= right and left < len(haystack) and right >= 0:
            mid = (left + right) // 2
            if needle == haystack[mid]:
                return mid
            if needle < haystack[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    @classmethod
    def max_subarray(cls, haystack):
        """
        Aller de la gauche vers la droite du tableau.
        Pointer sur un nombre et faire itérativement la somme à partir du nombre pointé.
        Comparer parallèlement chaque nouvelle somme au maximum actuel. Si celle-ci est supérieure, elle devient le
        nouveau maximum.
        Renvoyer le maximum lorsque l'extrémité droite de la séquence est atteinte.
        Temps - O(N²)
        Espace - O(1)
        :param haystack:
        :return: max_sum
        """
#        pointer, hay, sum_, max_sum = 0, 0, 0, 0
        max_sum = float('-inf')
        pointer, hay, sum_ = 0, 0, 0
        while pointer < len(haystack):
            for hay in haystack[pointer:]:
                sum_ += hay
#                if sum_ > max_sum:
#                   max_sum = sum_
                max_sum = max(max_sum, sum_)
            pointer += 1
            sum_ = 0
        return max_sum

    @classmethod
    def max_subarray_optimal_solution(cls, haystack):
        """
        Pour chaque numéro, calculez la somme maximale du sous-bloc se terminant par ce numéro, soit le numéro
        seul (si la somme précédente était négative), soit le numéro + la somme précédente (si la somme précédente
        était positive).
        Temps - O(N)
        Espace - O(1)
        :param haystack:
        :return: max_sum
        """
        overall_max = float('-inf')
        max_ending_here = 0
        for hay in haystack:
            if max_ending_here > 0:
                max_ending_here += hay
            else:
                max_ending_here = hay
            overall_max = max(overall_max, max_ending_here)
        return overall_max


if __name__ == '__main__':
    pass
