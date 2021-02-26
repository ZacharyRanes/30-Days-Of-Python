"""
    Create an empty dictionary called dog
    Add name, color, breed, legs, age to the dog dictionary
    Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
                                                country, city and address as keys for the dictionary
    Get the length of the student dictionary
    Get the value of skills and check the data type, it should be a list
    Modify the skills values by adding one or two skills
    Get the dictionary keys as a list
    Get the dictionary values as a list
    Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
"""

dog = {}

dog['name'] = 'doge'
dog['color'] = 'blue'
dog['breed'] = 'russian'
dog['legs'] = 4
dog['age'] = 2

student = {
    'first_name': 'Zachary',
    'last_name': 'Ranes',
    'gender': 'Male',
    'age': 27,
    'country': 'USA',
    'is_marred': False,
    'skills': ['JavaScript', 'C++', 'Docker', 'C#', 'Python'],
    'address': {
        'city': 'town vile',
        'street': 'Space street',
        'zipcode': '55555'
    }
}

print(len(student))

print(type(student['skills']))

print(student.keys())

print(student.values())

print(student.items())

del dog['legs']

del dog


