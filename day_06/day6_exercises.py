"""
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_staff_lt list
Delete the food_staff_tp tuple completely
Check if an item exists in tuple:
    Check if 'Estonia' is a nordic country
    Check if 'Iceland' is a nordic country
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"""

empty = tuple()

brother = ('john',)
sister = ('kate',)

siblings = brother + sister

print(len(siblings))

family_members = siblings + ('Sarah', 'Mark')

siblings2 = family_members[:2]
parents = family_members[2:]

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

