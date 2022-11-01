
import sys



class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor):
        self.bottom_floor = bottom_floor
        self.top_floor=top_floor
        self.current_floor=current_floor
    def floor_up(self):
        if self.current_floor<self.top_floor:
            self.current_floor +=1
    def floor_down(self):
        if self.current_floor>self.bottom_floor:
            self.current_floor -=1
    def go_to_floor(self, floor:int):
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
        print(f"you are presently in floor {self.current_floor}")



h = Elevator(-1, 10, 0)

Floor_select = int(input("select the floor you going to:"))
h.go_to_floor(Floor_select)
h.go_to_floor(3)
h.go_to_floor(0)







sys.exit(0)