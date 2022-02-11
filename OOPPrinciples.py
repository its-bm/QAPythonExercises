# Object Oriented Programming Principles
# 4 Principles
# Inheritence - An object acquires all properties and behaviours of a parent object
# Polymorphism - Performing a single action in different ways
# Abstraction - Hiding the implementation details and showing only functionality to the user
# Encapsulation - Wrapping code together and data together into a single unit for data integrity 

# Superclass and Subclass
# In OOP we can inherit attributes and methods - they are context dependant
# Superclass (parent) - class that is being inherited from
# Subclass (child)- class that is inheriting attributes and methods

# Inheritence

# Can create a hierarchy of inheritance.
# Lets us re-use code and overall write less, making our actual code much more readable.
# When a child class inherits from a parents class, and there is no default constructors.
# The first thing the child class should do is run the parent constructor.

class Musician:
    def __init__(self, name):
        self.name = name

class Bassist(Musician):
    def __init__(self, name, band):
        super().__init__(name)
        self.band = band

band_member1 = Musician('Flea', 'Red Hot Chili Peppers')
print(band_member1.band)

# Polymorphism means many forms
# Different child classes may act differently in regards to an attribute or method inherited from the superclass

class Bassist(Musician):
    def __init__(self, name, band):
        super().__init__(name)
        self.band = self.band

# Encapsulation
# Python doesn't have a way to encapsulate attributes but we can use single leading underscores to signifiy that an attribute is for private or internal use only.

class BankAccount:
    _money = 0

    def deposit(self, money, password):
        if (authenticate(password)):
            self._money += money
        else:
            print('Wrong Password')

    def withdraw(self, money, password):
        if (authenticate(password)):
            self._money -= money
        else:
            print('Wrong Password')

bank = BankAccount()
bank.desposit(5000, 'password')
print(bank, money)

# Abstraction
# Abstraction allows us to create the lowest level blueprint of a class without anyone being able to create an instance of that class.
# Can create nstances of the child classes
# Abstract Base Classes (abc) library which contains the infrastructure for us to create our own abstract classes. Any abstract class we create is a subclass of the abstract base class, ABC.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Mammal(Animal):
    def eat(self):
        return "Nom nom"

mam = Mammal()
print(mam.eat())