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



h = Elevator(-1, 10, 0)

Floor_select = int(input("select the floor you going to:"))
h.go_to_floor(Floor_select)
h.go_to_floor(4)
h.go_to_floor(9)
h.go_to_floor(0)

sys.exit(0)