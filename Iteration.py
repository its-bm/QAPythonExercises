# Iteration is another word for loops, they repeat a block of code again and again without having to write it multiple times.
# Two main types of loop: while loop and for loop

# A while loop will continue to execute a block of code while a condition is True. If the conidition is never True then the while loop will not ever start.
# counter = 0, code will be executed as 0 < 5
# Prints 0, then adds 1 to counter
# Continues until value of counter is no longer < 5, blocks stops of code will not be executed.
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# A for loop will iterate over any iterable, or collection, such as a list.
# This is useful for when we want to use data in a collection, and do something baased on each element individually.
# When using a for loop, we need to specify the loop variable that will hold the value the current iteration.

my_fruit = ['Mango', 'Lime', 'Kiwi']

# On first iteration, fruit will take Mango as its value and print result of fruit.upper() then continue to next iteration until there are no elements left in the list.
for fruit in my_fruit:
    print(fruit.upper())


# Numeric Range
# To iterate over numbers, we can use the built-in function 'range'.
# Range will generate an iterable of numbers based on specific values.

# range(stop) - starts from 0, continues until stop, but doesn't include it.
# tuple(range(5))
# (0, 1, 2, 3, 4)

# range(start, stop) - starts from start, continues until stop but doesn't include it.
# tuple(range(2, 5))
# (2, 3, 4)

# range(start, stop, step) - starts from start, continues until stop in increments of step, but doesn't include the stop.
# tuple(range(1, 5, 2))
# (1, 3)
for number in range(5):
    print(number)


# Iterating Strings
# Strings can be iterated in the same way as other collection types, where we iterate each character in the string.
for char in 'Hello World':
    print(char)

# If we wanted to print each word in the string, we can split the string first.
for word in 'Hello World'.split():
    print(word)

# Iterating Dictionaries
# When iterating a dictionary, by default we will just iterate the keys in the dictionary.
for key in {'key':'value'}:
    print(key)

# If we want to return the values in the dictionary, we can use 'dict.values':
for value in {'key':'value'}.values():
    print(value)

# If we want to know both then we can use 'dict.items':
for key, value in {'key':'value'}.items():
    print(key, value)


# List Comprehension
# Can use an alternative syntax for 'for' loops, allowing us to create lsits, or other collections in a single statement.
# Create a list of the range between 0 and 5
result = []
for x in range(5):
    result.append(x)

# Loop Functionality
# Breaking loops
# For 'while' loops, this is the condition that we specify at the start, and for 'for' loops this is when we reach the end of a given iterable.
# There are some key words in Python which can be used to break out of loops early, or to modify their behaviour.
# 'break' - break the loop and stop iterating
# 'continue' - break the current iteration, but not the loop.

# Print the numbers 0-5, and then stop. As soon as i is equal to 5, Python breaks out of the loop.
for i in range(10):
    print(i)
    if i == 5:
        break
#  Print the numbers 0-9, except for the number 5.
# When i is equal to 5, Python will break out of the current iteration and continue with the next iteration.
for i in range(10):
    if i == 5:
        continue

    print(i)


# Nested Loops
# Can nest loops
# Print the first 4 entries of the 1, 2 and 3 times tables.
for i in range(3):
    for j in range(4):
        print(i, 'x', j, '=', i * j)
