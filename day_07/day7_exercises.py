"""
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?
You did not learn loops yet you can do it manually.
"""

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['EA', 'Ubisoft'])
print(it_companies)

it_companies.remove('Oracle')
print(it_companies)

# .remove() will show error if it tries to remove something that is in the set
# .discard() works the same as .remove() but will not error if it tries to remove something that is not there

AuB = A.union(B)
print(AuB)

AnB = A.intersection(B)
print(AnB)

print(B.issubset(A))

print(A.isdisjoint(B))


