"""
Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""

for i in range(8):
    for ii in range(7):
        print("# ", end=" ")
    else:
        print("#")


# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)

fruits_r = []

for fruit in fruits:
    fruits_r.insert(0, fruit)

print(fruits_r)
