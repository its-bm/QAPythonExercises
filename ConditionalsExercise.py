# Conditionals exercises
devs_money = 100
dev_can_play_smash = False

if devs_money > 10 and dev_can_play_smash:
    print('Dev enters a smash tournament!')
elif devs_money < 10 and dev_can_play_smash:
    print('Dev is too poor to enter')
else:
    print('Dev can\'t play smash')

# Write a program that does the following:
# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"
# Try to do this both with and without elif statements.

# With elif
mark = int(input('What is your mark? '))
if mark >= 85:
    print('Distinction')
elif mark >= 65:
    print('Pass')
else:
    print('Fail')

# Without elif
course_mark = int(input('What is your mark? '))
if course_mark >= 85:
    print('Distinction')
if course_mark >= 65:
    print('Pass')
else:
    print('Fail') 