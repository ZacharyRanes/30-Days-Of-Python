empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('key2' in dct)  # True
print('key5' in dct)  # False

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(len(person))  # 7

print(person['first_name'])  # Asabeneh
print(person['country'])  # Finland
print(person['skills'])  # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Space street
print(person['city'])  # Error

print(person.get('first_name'))  # Asabeneh
print(person.get('country'))  # Finland
print(person.get('skills'))  # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))  # None

'''
    pop(key): removes the item with the specified key name:
    popitem(): removes the last item
    del: removes an item with specified key name
'''
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.pop('key1')  # removes key1 item
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()  # removes the last item
del dct['key2']  # removes key2 item

print(dct.clear())  # None

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
keys = dct.keys()
print(keys)  # dict_keys(['key1', 'key2', 'key3', 'key4'])
values = dct.values()
print(values)  # dict_values(['value1', 'value2', 'value3', 'value4'])


