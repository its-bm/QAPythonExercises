# Task
# Times Table Grid
# Given an integer n, write a python application which returns a times table grid for all the integers between 1 and n.
# The grid should be separated by tabs and new lines.
# For example, given n = 4 it should return the grid
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

n = int(input('Please enter a number: '))
for r in range(1, n + 1):
    for c in range(1, 5):
        print('{:2d}'.format(r * c), end= ' ')
    print()