# Dictionaries
# Key Value Pairs - key must be unique and have a value
# Defined with {key:value, key2:value2}

noises = {'cow':'moo', 'sheep':'baa', 'chicken':'cluck'}
# Returns 'cluck'
print(noises['chicken'])

# How to add values to dictionary
noises['cat'] = 'meow'
print(noises)

# How to overwrite values in dictionary
noises['cat'] = 'blep'
print(noises)

# Return list of keys
print(list(noises.keys()))

# Return tuples containing key value pairs
print(list(noises.values()))

# Return list of items
print(list(noises.items()))

# Returns false as 'moo' not in keys
print('moo' in noises)

# Returns true
print('moo' in noises.values())

my_words = {'hello':'hola', 'thank you': 'gracias'}

# .get() used to return value if key is in dictionary
print(my_words.get('hello'))

# .pop() used to remove specified key and return value
print(my_words.pop('thank you'))

# .update() used to update or replace key
my_words.update({'yes':'si'})
print(my_words)