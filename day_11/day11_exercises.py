# Write a function which checks if all the items of the list are of the same data type.
def same_type(list):
    last_type = type(list[0])
    for i in list:
        if type(i) != last_type and type(i) is not None:
            return False
        last_type = type(i)
    return True


print(same_type([3, 4, 5]))
print(same_type([3, 4, 5.5]))

# Write a function which check if provided variable is a valid python variable
from keyword import iskeyword


def valid_variable(item):
    return item.isidentifier() and not iskeyword(item)


print(valid_variable('print'))
print(valid_variable('2x'))
print(valid_variable('type_good'))
print(valid_variable('not'))
