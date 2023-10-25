"""
Software 2 - Python Module 9
Fundamentals of object-oriented programming
"""


# Task 1
class Car:

    def __init__(self, register, max, current=0, distance=0):
        self.register = register
        self.max = max
        self.current = current
        self.distance = distance

    def accelerate(self, accel):
        self.current += accel

        if self.current > self.max:
            self.current = self.max

        if self.current < 0:
            self.current = 0
        print(f"Here is the current speed {self.current}")

    def drive(self, hours):
        new_distance = self.current * hours
        self.distance += new_distance
        print(f"Your current distance driven is {self.distance} after {hours} hours")



uRegister = input("Provide a registration number: ")
uMax = int(input("Provide the maximum speed: "))

car = Car(uRegister, uMax)

car.accelerate(30)
car.drive(2)
car.accelerate(70)
car.drive(1)
car.accelerate(50)
car.drive(1)
car.accelerate(-200)
car.drive(1)
print(car.register, car.max, "km/h", car.current, car.distance)

