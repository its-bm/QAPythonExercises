# Modules are Python files that we can use to extend the functionality of scripts. Also known as libraries
# Can import existing modules or create our own
# Must import first - at top of script
import random
import math

# Don't have to specify every object from the corresponding module, we can specify the exact objects we want to use.
# Can import multiple modules by using comma seperation - more efficient when calling the object within the script
from math import sqrt, degrees, floor
from random import randint

# Can import objects from other modules that are located in the same directory by importing the filename and specifying the object we want to use

# math
number = float(input('Please input number: '))
answer = math.sqrt(number)
print(answer)

# random
def random_pi():
    return math.ceil(random.randint(1, 15) * math.pi)

for _ in range(5):
    print(random_pi())
