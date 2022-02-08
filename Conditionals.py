# Conditionals
# if, elif, else
# Allows code to branch off and execute if certain conditions are met

# Boolean conditional
# Returns 'Boolean is false' as my_boolean = 0
my_boolean = False
if my_boolean:
    print('Not going to print')
else:
    print('Boolean is false')

# Comparators
# Equal to - ==
# Not equal to - !=
# Less than - <
# Less than or equal to - <=
# Greater than - >
# Greater than or equal to >=

# Useful for creating branching paths based on numerical values
# Can also use logical operators to include multiple conditions can be included when executing code

my_money = 10

if my_money <= 10:
    print('Seek employment')
else:
    print('Wealthy!')

#
deposit = 100
password = '^(*£kjGftv"{433\.&343£$\:d'

if 0 < deposit <= 100 and password == '^(*£kjGftv"{433\.&343£$\:d':
    print(f'Thank you for depositing {deposit}')
else:
    print('Error')

# Check username and convert to lowercase
username = ''
username_lower = username.lower()

if username in ('root', 'admin'):
    print('Unacceptable username')
else:
    print(f'Welcome {username}')

# Prompt age and return age range using elif

age = int(input('What is your age?'))

if age >= 75:
    print('75 or older')
elif age >= 65:
    print('Between 65 and 75')
elif age >= 55:
    print('Between 55 and 65')
elif age >= 45:
    print('Between 45 and 55')
else:
    print('Below 45')