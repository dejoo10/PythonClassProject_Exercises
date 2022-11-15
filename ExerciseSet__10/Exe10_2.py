import sys


class Elevator:
    def __init__(self, floors, current_floor = 0):
        self.floors = floors
        self.current_floor = current_floor

    def floor_up(self):
        self.current_floor += 1
        print(f'Going up, current floor is {self.current_floor}')

    def floor_down(self):
        self.current_floor -= 1
        print(f'Going down, current floor is {self.current_floor}')

    def go_to_floor(self, selected_floor):
        if self.current_floor < selected_floor and selected_floor <= self.floors:
            for i in range(selected_floor):
                self.floor_up()

        elif self.current_floor > selected_floor and self.current_floor - selected_floor > 0:
            for i in range(self.current_floor - selected_floor):
                self.floor_down()

#when building is created, the building creates the required elevators
class Building:
    def __init__(self, floors, elevator):
        self.floors = floors
        self.elevator = elevator

    @property
    def elevators(self):
        elevs = []
        for i in range(self.elevator):
            elevs.append(Elevator(self.floors))
        return elevs

    def run_elevator(self, floor, elevators):
        for elevator in self.elevators[:elevators]:
            elevator.go_to_floor(floor)

build = Building(10, 5)
print(build.floors)
print(build.elevators)
build.run_elevator(5,2)



sys.exit(0)