"""
Software 2 - Python Module 11
Inheritance
"""


# Task 1

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        print(f"{self.name} : {self.author} : {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"{self.name} : {self.chief_editor}")


book = Book("Compartment No.6", "Rosa Liksom", "192 pages")

mag = Magazine("Donald Duck", "Aki Hyyppä")

book.print_information()

mag.print_information()


# Task 2

class Car:
    def __init__(self, regist, max_speed, speed=0, distance=0):
        self.regist = regist
        self.max_speed = int(max_speed)
        self.speed = speed
        self.distance = distance

    def accelerate(self, change):
        self.speed = self.speed + change
        if self.speed > self.max_speed:
            self.speed = self.max_speed

        elif self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance = self.distance + (self.speed * hours)


class ElectricCar(Car):
    def __init__(self, regist, max_speed, bat_capacity, speed=60, distance=0):
        super().__init__(regist, max_speed, speed, distance)
        self.bat_capacity = bat_capacity


class GasolineCar(Car):
    def __init__(self, regist, max_speed, tank_capacity, speed=100, distance=0):
        super().__init__(regist, max_speed, speed, distance)
        self.tank_capacity = tank_capacity


elec = ElectricCar("ABC-15", 180, 52.5)

gas = GasolineCar("ACD-123", 165, 32.3)

elec.drive(3)

gas.drive(3)

print(elec.distance)

print(gas.distance)
