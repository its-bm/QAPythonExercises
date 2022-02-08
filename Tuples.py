# Tuples
# Reasons to use: makes clear to other devs that we do not want these values to change
# Reasons to use: More memory efficient
# Defined with (), immutable (read only)
sports = ('Sportball', 'Fight Club' 'Horse Fight', 'Dog Run')

# Does not support item assignment
# sports[0] = 'Murderball'

# Can reference
name = 'its bm'
print(name[2:4])

# Does not support item assignment
# sports[0] = 'Murderball'
animals = 'Fox', 'Rabbit', 'Dog', 'Cat'
# animals[3] = 'change'

# Can assign the tuple values to variables as tuple length will not change
animal1, animal2, animal3, animal4 = animals
print(animals)

