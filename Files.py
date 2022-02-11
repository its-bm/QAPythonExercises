# We can interact with files in python by doing the following
# Open file
file = open('filename.ext', 'mode')
# Close the file
file.close('filename', 'mode,')

# Reading files
# readline() - reads current line and moves onto next
# read() - reads from the current line to the end of the file
# Specifying a numerical parameter for either readline or read will read that number of characters and then stop.
# seek() - not a way to read a file but useful when reading files.
# When run, file.seek(num) will start at the beginning of the file, and navigate through the specified number of characters.
# A common use of this is to navigate to the start of the file using file.seek(0).
print(file.readline())
file.readline()
print(file.readline())
file.seek(0)
print(file.readline())

file.close()

# All lines in a file can be read at once and stored into a list using the 'readlines' function
file = open('filename.txt', 'r')
lines = file.readlines()
print(lines)
file.close()

# Writing files
# To write a file, it  must be open in write-only mode
# Python will open but delete all contents of a duplicate file name
# Write to files - file.write() - parameter passed will be written to the file
# write() command will write wherever it was left off
file = open('filename.txt', 'w')

for n in range(1,11):
    newline = 'This is line' + str(n) + '\n'
    file.write(newline)

file.close()

# Manually opening and closing can allow for more failure points when working with files, especially if it involves a high number of operations
# 'with' statement allows us to work with the file in its own context
# Once executed, Python will automatically close the file. Any error thrown within the context will exit context rather than whole program
with open('filename.txt', 'w') as file:
    for n in range(1,11):
        newline = 'This is line' + str(n) + '\n'
        file.write(newline)

# Amending files
# Open in read-only mode
# Store variables we want to keep
# Create variables for data we wish to add
# Open in write-only mode
# Write the data from variables into the blank file
file = open('filename.txt', 'r')
# Variable which we are storing data we want to keep
outfile = ''

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        # Skips lines which are odd
        file.readline()

file = open('filename.txt', 'w')
file.write(outfile)
file.close()

