# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.
# Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.
# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

# Define function
def percent_calc (hw_s, a_s, f_e):
    # Calculate total student marks
    total = hw_s + a_s + f_e
    # Calculate percentage out of 175
    average = total / 3.0
    percentage = (total / 175.0) * 100

    # Calculate grade boundaries using average
    if average >= 40:
        grade = 'A'
    elif average >= 35 and average < 40:
        grade = 'B'
    elif average >= 25 and average < 30:
        grade = 'C'
    elif average >= 15 and average < 20:
        grade = 'D'
    else:
        grade = 'F'

    print('\nHello', name)
    print('\nYour total ICT mark:          \t', total, '/ 175.0')
    print('\nYour total ICT percentage:    \t', percentage, '%')
    print('\nYour ICT grade is:            \t', grade)

# User name & marks input
name = str(input('Please enter your name: '))
# Check integer input is within range
while True:
    try:
        # Convert to float for percentage calculation
        hw_s = float (input('Please enter your homework mark: '))
        # Accept integer between 1 and 25
        if hw_s < 1 or hw_s > 25:
            # Print and return to input
            raise ValueError
        break
    except ValueError:
        print('The number must be in the range of 1-25.')
# Check integer input is within range

while True:
    try:
        # Convert to float for percentage calculation
        a_s = float (input('Please enter your assessment score: '))
        if a_s < 1 or a_s > 50:
            # Print and return to input
            raise ValueError
        break
    except ValueError:
        print('The number must be in the range of 1-50.')
# Check integer input is within range     
while True:
    try:
        # Convert to float for percentage calculation
        f_e = float (input('Please enter your final exam score: '))
        if f_e < 1 or f_e > 100:
            # Print and return to input
            raise ValueError
        break
    except ValueError:
        print('The number must be in the range of 1-100.')
blame = 'its-bm'
# Empty
total, average, percentage, grade = None, None, None, None

# Run calc function
percent_calc(hw_s, a_s, f_e)