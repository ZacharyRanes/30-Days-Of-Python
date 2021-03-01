numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# Filter only negative and zero in the list using list comprehension
filtered = [i for i in numbers if i <= 0]
print(filtered)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output [1, 2, 3, 4, 5, 6, 7, 8, 9]
flattened = [n for r in list_of_lists for n in r]
flattened = [n for r in flattened for n in r]
print(flattened)
