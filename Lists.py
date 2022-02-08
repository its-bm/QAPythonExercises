# Lists
myFruit = ['Apple', 'Banana', 'Orange']

# list.append() appends object to end of list
myFruit.append('Melon')
print(myFruit)

# list.remove() removes object from list
myFruit.remove('Banana')
print(myFruit)

# list.pop() removes and returns item at index
myFruit.pop(-1)
print(myFruit)

# list.insert() insert object before index
myFruit.insert(0, 'Mango')
print(myFruit)

# list.extend can extend list by another list or any iterable
myFruit2 = ['Strawberry', 'Kiwi']
myFruit.extend(myFruit2)
print(myFruit)

# list.index() Return the first index of the value
print(myFruit.index('Strawberry'))

# list.count() Return the number of occurences of a value in a list
print(myFruit.count('Strawberry'))

# list.sort()  Lists in ascending order
myFruit.sort()
print(myFruit)

# Sorts smallest value length to largest
myFruit.sort(key=len)
print(myFruit)

# Join list elements (add ',' or '&' for example)
print(', '.join(myFruit))