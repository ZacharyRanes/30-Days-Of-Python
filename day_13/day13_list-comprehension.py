"""
List comprehension in Python is a compact way of creating a list from a sequence.
It is a short way to create a new list.
List comprehension is considerably faster than processing a list using the for loop.

[i for i in iterable if expression]
"""

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
three_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in three_dimen_list for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32

