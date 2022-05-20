"""
Easy Problems class.
001 - Two Sum
"""


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
