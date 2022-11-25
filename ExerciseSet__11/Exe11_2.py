import random
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

        self.Travelled_distance += self.Current_speed * hours
#        print(f"Total distance now traveled is {self.Travelled_distance}Km at a speed of {self.Current_speed}km/h")
        return

class ElectricCar(Car):
    def __int__(self, registration_number, Max_speed, battery):
        super(). __init__((registration_number, Max_speed))
        self.battery = battery

class GasolineCar(Car):
    def __init__(self,registration_number,Max_speed, tank):
        super(). __init__(registration_number, Max_speed)
        self.tank = tank

speed1 = random.randint(50,120)
speed2 = random.randint(20,100)
electric = ElectricCar('ABC-15',180,52.5)
gasoline = GasolineCar('ABC-123', 165, 32.3)
electric.Current_speed=120
electric.drive(speed1)

gasoline.Current_speed=150
gasoline.drive(speed2)

print(electric.Travelled_distance)
print(gasoline.Travelled_distance)
