# Classes and Objects
# Class is a blueprint that will contain attributes and methods
# Object is an instance of the class
# Attributes are data attached to the class
# Methods are procedures or functions attached to the class

# Allows us to have many instances of the class as we desire

from io import BufferedReader
from unicodedata import name


class Dog:
        number_of_legs = 4
        breed = 'Labrador'
        fur_colour = 'Golden'

def speak(self):
    print('Woof')

bilbo_waggins = Dog()
bilbo_waggins.speak()
print(bilbo_waggins.breed) 

# Class constructor is set by a variable name then the name of the class followed by paranthesis
jeff = Dog()

# __init__ method - a special method that will be called whenever we create an instance of the given class. Good for setting attributes that may differ from object to object
class Dog:
    def __init__(self, name, breed, number_of_legs):
     self.name = name
     self.breed = breed
     self.number_of_legs = number_of_legs

dog1 = Dog('Jeff', 'Pug', 4)
print(dog1.number_of_legs)

# Single leading underscore
# Used to signify a private or internal variable, these variables should not be accessed.
# _money = 1,000,000 as someone's balance is private.

# Single trailing underscore
# Used to avoid conflicts with Python keywords.
# class_ = "QAC Intake", but as we know class is a keyword in Python so we must avoid conflicting with it.

# Double leading underscore
# A double leading underscore applies name mangling to the attribute.
# This is where the interpreter changes the name of the attribute to make it harder to create collisions when the class is extended.
# Access attributes using the following
# _ClassName__AttributeName

class Feline:
    __family = "Felidae"

kitty = Feline()
print(kitty._Feline__family)
