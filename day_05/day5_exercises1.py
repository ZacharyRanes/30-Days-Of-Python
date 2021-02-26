"""
Declare an empty list

Declare a list with more than 5 items

Find the length of your list

Get the first item, the middle item and the last item of the list

Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

Print the list using print()

Print the number of companies in the list

Print the first, middle and last company

Print the list after modifying one of the companies

Add an IT company to it_companies

Insert an IT company in the middle of the companies list

Change one of the it_companies names to uppercase (IBM excluded!)

Join the it_companies with a string '#;  '

Check if a certain company exists in the it_companies list.

Sort the list using sort() method

Reverse the list in descending order using reverse() method

Slice out the first 3 companies from the list

Slice out the last 3 companies from the list

Slice out the middle IT company or companies from the list

Remove the first IT company from the list

Remove the middle IT company or companies from the list

Remove the last IT company from the list

Remove all IT companies from the list

Destroy the IT companies list

Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
"""

# 1
list1 = list()

# 2
list2 = ['test1', 'tes2', 'test3', 'test4', 'test5']

# 3
list2_length = len(list2)

# 4
list2_first = list2[0]
list2_middle = list2[list2_length // 2]
list2_last = list2[-1]

# 5
mixed_data_types = ['Zachary', 27, 6.0, False, '5720 Metro View']

# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# 10
it_companies[-2] = 'SunSoft'
print(it_companies)

# 11
it_companies.append('BitDance')

# 12
it_companies.insert(it_companies[len(it_companies) // 2], 'Oracle')

