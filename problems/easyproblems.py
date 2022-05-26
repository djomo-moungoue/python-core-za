"""
Easy Problems class.
001 - Two Sum
"""
from PIL._imaging import outline


class EasyProblems:

    @classmethod
    def sum_two_numbers(self, numbers, target):
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
    def reverse_integer(self, my_integer):
        """
        :param my_integer:
        :return: my_integer reversed
        Runtime complexity: O(n) to iterate over all digits
        Space complexity: O(n) to store reversed on the disk
        """
        is_negative = my_integer < 0  # save the sign of the input
        my_integer = abs(my_integer)
        reversed = 0  # placeholder of the output
        while my_integer != 0:
            reversed = reversed * 10 + my_integer % 10
            my_integer //= 10
        if is_negative:
            return -reversed
        else:
            return reversed

    @classmethod
    def is_palindrome(self, x):
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
    def convert_roman_to_integer(self, roman):
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
    def convert_roman_to_integer_optimal_solution(self, roman):
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
            if roman[i:i+2] in double_roman_dict:
                result += double_roman_dict.get(roman[i:i+2])
                i += 2
            else:
                result += single_roman_dict.get(roman[i])
                i += 1
        return result
