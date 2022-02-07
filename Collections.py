# Collections
# Mutable and immutable
# list1[0] = 'Adam', list1[1] = 'Andrew', list1[2] = 'Annabelle'
list1 = ['Adam', 'Andrew', 'Annabelle']

# Can reference the list element by putting the index in [] after the variable name
print(list1[1])

# Can reference the last list element by using [-1] after the variable name
print(list1[-1])

# Can slice the list into smaller sections by using [x:y] after the variable name x=starting index:y=stopping index
print(list1[1:2])

# Returns 'Andrew' and 'Annabelle' as not stopping point defined
print(list1[1:])

# Change element in list we set a new value to the list index as followers
list1[0] = 'Ben'
print(list1)

# We can delete elements from the list with the del keyword and defining the list index (-1 = end value)
del list1[-1]
print(list1)

# Check if an element is in a list (in)
print('Ben' in list1)

# Checkif an element is not in a list (not in)
print('Ben' not in list1)

list2 = ['Sarah', 'Sophie', 'Sandra']
list3 = ['Matt', 'Mike', 'Melvin']

# Contain lists within lists and different data types
listlist = [list1, list2, list3]

# Return 'Sophie' as index 1 in variable listlist
print(listlist[1][1])
