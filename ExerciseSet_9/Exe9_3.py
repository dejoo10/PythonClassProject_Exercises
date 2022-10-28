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
    def drive(self, hours):

        self.Travelled_distance += speed*hours
        print(f"Total distance now traveled is {self.Travelled_distance}Km at a speed of {speed}km/h")
        return

distance = int(input("Enter the initial distance traveled"))
Max_speed = 142
speed = int(input("Enter the speed"))
car1 = Car("ABC-123", Max_speed,)
car1.Max_speed = 142
car1.Travelled_distance = distance
hours = float(input("Enter the number of hours traveled"))
car1.drive(hours)

