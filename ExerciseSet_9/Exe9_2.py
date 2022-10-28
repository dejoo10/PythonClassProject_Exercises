import sys



class Car:

    def __init__(self, registration_number, Max_speed, Current_speed = 0, Travelled_distance = 0):
        self.registration_number = registration_number
        self.Max_speed = Max_speed
        self.Current_speed = Current_speed
        self.Travelled_distance = Travelled_distance

    def accelerate(self, speed = 0):
        self.Current_speed += speed

        if (self.Current_speed > 0) and (self.Current_speed <= self.Max_speed):
            print(f"The current speed is {self.Current_speed} Km/h.")
        elif self.Current_speed <= 0:
            print(f"The current speed is 0 Km/h")
            print(f"you have forced a break of {speed}Km/h ")
            print("Your car will now stop")
        else:
            print(f"The current speed is {self.Max_speed} Km/h.")

distance = 0
Max_speed = 142
speed = int(input("Enter the speed:"))
car1 = Car("ABC-123", Max_speed)
car1.Max_speed = 142

while speed != 0:
    car1.accelerate(speed)
    speed = int(input("Enter the speed:"))


#print(f"current speed is {car1.Current_speed}(Km/h)")



sys.exit(0)