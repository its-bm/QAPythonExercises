# Import random for use of randint
from random import randint
# Import dice1 from dice.py
from dice import dice1


# Generate random integer from 1 to 6
for _ in range(1):
	dice2 = randint(1, 6)
total = dice1 + dice2
    # Print dice1 and dice2
print('Dice one:', dice1, '\nDice two:', dice2, '\nTotal', total)
