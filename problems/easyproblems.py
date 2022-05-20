"""
Easy Problems class.
001 - Two Sum
"""


class EasyProblems:

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
