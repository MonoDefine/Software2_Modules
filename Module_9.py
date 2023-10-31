"""
Software 2 - Python Module 9
Fundamentals of Object-Oriented Programming
"""


# Task 1

class Car:
    def __init__(self, registration, max_speed, speed=0, distance=0):
        self.registration = registration
        self.max_speed = int(max_speed)
        self.speed = speed
        self.distance = distance


    # Task 2
    def accelerate(self, change):
        self.speed = self.speed + change
        if self.speed > self.max_speed:
            self.speed = self.max_speed

        elif self.speed < 0:
            self.speed = 0

    # Task 3
    def drive(self, hours):
        self.distance = self.distance + (self.speed * hours)


car = Car("ABC-123", "142")

print(car.registration, f"{car.max_speed}km/h", car.speed, car.distance)

car.accelerate(30)
car.drive(1.5)
car.accelerate(70)
car.drive(3)
car.accelerate(50)
car.drive(1)
car.accelerate(-200)
car.drive(5)

# Task 4
import random

i = 1

f = True

car_lst = []

while i < 11:
    car = Car(f"ABC-{i}", f"{random.randint(100, 200)}")
    car_lst.append(car)

    i += 1

while f:
    for veh in car_lst:
        speed = random.randint(-10, 15)
        veh.accelerate(speed)

        veh.drive(1)

        if veh.distance >= 10000:
            print(f"Car {veh.registration} is our winner!")
            f = False

for veh in car_lst:
    print(veh.registration, f"{veh.max_speed}km/h", veh.speed, veh.distance)
