import sys
import random
from tabulate import tabulate

class Car:
    def __init__(self, registration_number, max_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, speed):
        self.current_speed = self.current_speed + speed

    def drive(self, hours):
        self.travelled_distance += speed*hours
#        print(f"Total distance now traveled is {self.travelled_distance}Km at a speed of {speed}km/h")
        return

class Race:

    def __init__(self, name, distance_km, list_cars):
        self.name = name
        self.distance_km = distance_km
        self.list_cars = list_cars

    def hour_passes(self, hour=1):
        self.list_cars.accelerate(random.randint(-10, 15))
        self.list_cars.drive(hour)

    def print_status(self):
        print(tabulate([self.registration_number],[self.travelled_distance],headers =['registration_number', 'travelled_distance']))

    def race_finished(self,):
        for cars in self.list_cars:
            if self.distance_km >= 10000:
                return True
            else:
                return False


#Main program
#Grand Demolition Derby
max_speed = random.randint(100, 200)
speed = random.randint(-10, 15)

race = Race( 'Grand_demolition_Derby',8000, 10 )
cars = []
for i in range(1, 11):
    cars.append(Car(f'ABC-{i}', max_speed))

while len(cars) == 10:
    for car in cars:
        i = 0
        while i < 11:
            race.hour_passes(i)
            i = i+1
        if car.race_finished() == True:
            car.print_status()

sys.exit(0)





