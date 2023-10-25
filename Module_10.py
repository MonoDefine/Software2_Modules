"""
Software 2 - Python Module 10
Association (I am disassociating actually :D)
"""


# Task 1
class Elevator:
    def __init__(self, name, floor=0):
        self.name = name
        self.floor = floor

    def go_to_floor(self, dest):
        x = self.floor
        if x < dest:
            while x < dest:
                self.floor = Elevator.floor_up(self.floor)
                x += 1
            print(f"You reached floor {dest}")
        elif x > dest:
            while x > dest:
                self.floor = Elevator.floor_down(self.floor)
                x -= 1
            print(f"You reached floor {dest}")
        elif x == dest:
            print("You are already at this floor!")

    def floor_up(flor):
        flor += 1
        print(flor)
        return flor

    def floor_down(flor):
        flor -= 1
        print(flor)
        return flor

class Building:
    def __init__(self, bottom, top):
        pass

building = Building(0, 10)

elev1 = Elevator("One")
elev2 = Elevator("Two")

elev1.go_to_floor(5)

elev1.go_to_floor(0)

elev2.go_to_floor(13)
