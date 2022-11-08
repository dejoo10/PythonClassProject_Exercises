import sys

class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor = 0):
        self.bottom_floor = bottom_floor
        self.top_floor=top_floor
        self.current_floor= current_floor
    def floor_up(self):
        if self.current_floor<self.top_floor:
            self.current_floor +=1
            print(f"Going up, current floor is {self.current_floor}")
    def floor_down(self):
        if self.current_floor>self.bottom_floor:
            self.current_floor -=1
            print(f"Going down, current floor is {self.current_floor}")
    def go_to_floor(self, floor):

        if (int(floor)>self.top_floor) or (int(floor)<self.bottom_floor):
            print( f"Select the correct floor between {self.bottom_floor} and {self.top_floor}")
        elif int(floor)>self.current_floor:
            while int(floor)>(self.current_floor):
                self.floor_up()
        elif int(floor)<self.current_floor:
            while int(floor)<self.current_floor:
                self.floor_down()
        elif int(floor) == self.current_floor:
            print ("You are already in the selected floor")
        print(f"you have arrived at floor {self.current_floor}")

class Building:
    def __init__(self,bottom_floor, top_floor, number_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.number_elevators = number_elevators


    @property
    def elevators(self):
        elev = []
        for i in range(self.number_elevators):
            elev.append(Elevator(self.top_floor))
            return elev

    def run_elevator(self, floor, number_elevator):
        for number_elevators in self.elevators[:number_elevator]:
            number_elevators.go_to_floor(floor)



build = Building(0, 10, 5)
build.run_elevator(3,5)



sys.exit(0)