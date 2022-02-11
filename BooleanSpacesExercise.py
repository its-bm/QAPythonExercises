# Given three ints, a b c, one of them is small, one is medium and one is large.
# Return the boolean True if the three values are evenly spaced, so the
# difference between small and medium is the same as the difference between
# medium and large.
# Do not assume the ints will come to you in a reasonable order.
# <EXAMPLES># seven(2, 4, 6) → True
# 
# # seven(4, 6, 2) → True
# # seven(4, 6, 3) → False
# # seven(4, 60, 9) → False
# # <HINT>
# # There is a function for lists called sort.

# Sort numbers from input
numbers = sorted(int(input('Please enter an integer: ')) for _ in range(3))
print(numbers[1] - numbers[0] == numbers[2] - numbers[1])


if abs(numbers - numbers) == abs(numbers - numbers):
    print("True")
else:
    print("False")