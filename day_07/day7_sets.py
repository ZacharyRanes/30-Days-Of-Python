# Creating an empty set
# st = {}
# or
# st = set()

st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])

st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes the last element from the set

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)  # set()

st = {'item1', 'item2', 'item3', 'item4'}
del set

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)  # {'item3', 'item2'}

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)  # True
st1.issuperset(st2)  # True

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)  # set()
st1.difference(st2)  # {'item1', 'item4'} => st1\st2

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B)
st2.symmetric_difference(st1)  # {'item1', 'item4'}

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)  # False

