"""
Software 2 - Python Module 10
Association
"""


# Task 1 + 2

class Building:
    def __init__(self, bottom, top, amount):
        self.bottom = bottom
        self.top = top
        i = 1
        self.elev_lst = []

        while i < (amount + 1):
            self.elev_lst.append(Elevator(f"elev{i}", bottom, top))
            i += 1

    def run_elevator(self, number, destination):
        for elev in self.elev_lst:
            if elev.name == f"elev{number}":
                elev.go_to_floor(destination)

    # Task 3
    def fire_alarm(self):
        print("\n!!!FIRE!!!\n")
        for elev in self.elev_lst:
            elev.go_to_floor(0)


class Elevator:
    def __init__(self, name, bottom, top):
        self.name = name
        self.bottom = bottom
        self.top = top
        self.floor = bottom

    def go_to_floor(self, dest):
        if self.floor < dest:
            print(f"******\n{self.name} going up!\n******")
            while self.floor != dest:
                self.floor_up()

        elif self.floor > dest:
            print(f"******\n{self.name} going down!\n******")
            while self.floor != dest:
                self.floor_down()

    def floor_up(self):
        self.floor += 1
        print(self.floor)

    def floor_down(self):
        self.floor -= 1
        print(self.floor)


h = Elevator("elev", 0, 10)

h.go_to_floor(int(input("Which floor to go to? 0 - 10 ")))

h.go_to_floor(0)

building = Building(0, 10, 3)

building.run_elevator(1, 3)

building.run_elevator(2, 5)

building.run_elevator(3, 10)

building.fire_alarm()

# Task 4

import random


class Race:
    def __init__(self, name, dist, cars):
        print(f"\nWelcome to {name}!\n")
        self.name = name
        self.dist = dist
        self.cars = cars

    def hour_passes(self):
        for veh in self.cars:
            speed = random.randint(-10, 15)
            veh.accelerate(speed)

            veh.drive(1)

    def print_status(self):
        for veh in self.cars:
            print(veh.registration, f"{veh.max_speed}km/h", veh.speed, veh.distance)

    def race_finished(self):
        for veh in self.cars:
            if veh.distance >= self.dist:
                print(f"\n We have a winner! ({veh.registration}) \n")
                self.print_status()
                return True


class Car:
    def __init__(self, registration, max_speed, speed=0, distance=0):
        self.registration = registration
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


i = 1

f = True

car_lst = []

while i < 11:
    car = Car(f"ABC-{i}", f"{random.randint(100, 200)}")
    car_lst.append(car)

    i += 1

race = Race("Grand Demolition Derby", 8000, car_lst)

p = 0

while f:
    race.hour_passes()
    p += 1
    if p % 10 == 0:
        race.print_status()

    if race.race_finished():
        break
