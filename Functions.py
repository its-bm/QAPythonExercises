# Procedures 
# A loop is useful if you want to repeat a block of code, but they only allow you to repeat that code at that time.
# To repeat the code later on we need to use a procedure

# 'def' keyword to start the definition of a procedure, followed by the name of the procedure.
def greets(first_name, last_name):
    print(f'Hello, {first_name} {last_name}.')
greets('Vitalik', 'Buterin')

# Functions
# When a procedure is called, it will simply run all of its code and then finish. However, we often want a value to be output at the end of the code block so we can use it in other parts of our code.
# This is what is known as a function.
# Functions contain at least one line of code to return a value to the point in the code that invoked it.
# We can do many things with the return value, including:
# Store it in a variable
# Use it in a calculation
# Use it as a parameter in another procedure/function.

# Functions are defined identically to procedures, using the 'def' keyword, a name and parameters.
# The only difference is the use of the return keyword that is used to output the value.

# def greetss(first_name, last_name):
#   return f'Hello {first_name} {last_name}'
# print(greetss('Vitalik Buterin'))

# Setup the same way as a procedure but will return a value which can be used later on
def shout(greeting, name):
    gr = str(greeting).upper()
    na = str(name).upper()
    return f'{greeting} {name}'

print(shout('Hello', 'Vitalik'))

# Inputs for functions
# Print() and Input() are designed for terminal usage, therefore should only be used outside of functions.
userinput = input('Enter your name ')

def greet1(name):
    return f'Hello {name}'
print(greet1(userinput))

# Default Values
# We can provide default values for parameters for procedures or functions by including an = beside the parameter and putting in a value which we want to default to
def greet2(name = 'Vitalik'):
    return f'Hello {name}'
print(greet2())


