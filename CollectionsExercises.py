# Create a book dictionary
books = {'Anna Karenina':'Leo Tolstoy','War and Peace':'Leo Tolstoy','The Great Gatsby':'F. Scott Fitzgerald','In Search of Lost Time':'Marcel Proust','Hamlet':'William Shakespeare','Great Expectations':'Charles Dickens'}
print(books)

# Query an author of a book
print(books['War and Peace'])

# Cannot query which author has written which book(s). Author is a value, not a key.
# print(books['Leo Tolstoy'])

# Task:
# Write a program which will do the following:
# Create a list which contains the first name of everyone in your cohort and store it in a variable called team.
# Add your trainer to the list without manually editing it.
# Print the list to the terminal.
# Print only the 5th person in the list to your terminal.
team = ['Baki', 'Ira', 'Feruza', 'Nicolas', 'George', 'Aidan', 'Asawer', 'Oluwatosin', 'Leon', 'Hassan', 'Joseph', 'Daniel', 'Sunil', 'Juliana', 'Martyn', 'Kenan', 'Irwin', 'Sebastian', 'Joan', 'Nabil']
team.append('Ryan')
print(team)
print(team[4])
