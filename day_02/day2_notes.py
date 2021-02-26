#Day 2: 30 Days of python programming

first_name, last_name = 'Zachary', 'Ranes'  # str
country, city = 'USA', 'Alexandria'         # str
age = 27                                    # int
year = 2021                                 # int
is_married = False                          # bool
is_true = False                             # bool
is_light_on = True                          # bool


print(type(first_name))
print(type(age))
print(type(is_true))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

variable_total = num_one + num_two
variable_diff = num_one - num_two
variable_division = num_one / num_two
variable_remainder = num_one % num_two
variable_exp = num_one ** num_two
variable_floor_division = num_one // num_two

radius = float(input('What is the radius of the circle? '))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print('The area of the circle is ', area_of_circle, 'The circumference is ', circum_of_circle )
