"""
class Student:
    counter = 0
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program

        Student.counter += 1


    def setName(self, name):
        self.name = name

while(True):
    new_name = input("Enter a student's name: ")
    new_age = input("Enter the student's age: ")
    new_program = input("Enter student's degree program: ")

    student = Student(new_name, new_age, new_program)

    contin = input("Do you wish to continue? (Y / N)").upper()

    if contin == "N":
        break

print(f"Amount of students in class is {Student.counter}")
"""

"""
class Authors:
    def __init__(self, author, book):
        self.author = author
        self.book = book


class Books:
    def __init__(self, title, year):
        self.title = title
        self.year = year


auth1 = Authors("J.K. Rowling", (Books("Harry Potter", "IDK")))
auth2 = Authors("Nicolas Samuel Lietzau", (Books("Dreams of the Dying", 2020)))

print(f"{auth1.author} has published: ")
print(f"{auth1.book.title} in year {auth1.book.year}\n")

print(f"{auth2.author} has published: ")
print(f"{auth2.book.title} in year {auth2.book.year}")
"""

class Students:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def printCourses(self):
        print(f"{self.name} is in {self.courses}")


class Courses:
    def __init__(self, room, subject):
        self.room = room
        self.subject = subject


student1 = Students(1, "Evan")
student2 = Students(2, "Not Evan")
student3 = Students(3, "Amir")

course1 = Courses(100, "Python")
course2 = Courses(451, "English")
course3 = Courses(112, "Finnish")

student1.enroll(course1.subject)
student1.enroll(course2.subject)

student1.printCourses()

