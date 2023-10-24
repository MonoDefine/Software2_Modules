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


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = {}

    def buystock(self, stock, amount):
        self.stocks.update({stock : amount})

    def sellstock(self, stock):
        self.stocks.remove(stock)

    def printPortfolio(self):
        for x in self.stocks:
            x.displ()


class Stock:
    def __init__(self, nam, amount, value):
        self.nam = nam
        self.amount = amount
        self.value = value

    def print(self):
        print(f"You have {self.amount} {self.nam} with value {self.value}")


p = Portfolio("Porty")
s1 = Stock("Nokia", 100, 500)
s2 = Stock("Motorola", 200, 1000)

p.printPortfolio()
