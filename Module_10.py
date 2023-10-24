"""
Software 2 - Python Module 10
Association (I am disassociating actually)
"""


# Task 1
class Elevator:
    def __init__(self, name, floor=0):
        self.name = name
        self.floor = floor

    def go_to_floor(self, dest):
        for x in dest:
            Elevator.floor_up()

    def floor_up(self):
        self.floor += 1
        print(self.floor)

    def floor_down(self):
        pass


elev1 = Elevator("One")
elev2 = Elevator("Two")

Elevator.go_to_floor(elev1, 5)

