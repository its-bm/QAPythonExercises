# In a new Python file, create a class of students.
# It should contain the following attributes: name, age, and class with default value "student".
# It should also contain a method which takes in 3 test scores and prints the students average test score.

class Student:
    def __init__(self, name = 'Student', age = 'Student', class_ = 'Student'):
        self.name = name
        self.age = age
        self.class_ = class_

def average(self, s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    return f'{self.name} your average score is {avg}'

student1 = Student('Sophie', 23, 'Computer Science')

print(student1.avg(20, 32, 36))

