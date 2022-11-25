import sys
import random

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

max_speed = random.randint(100, 200)
speed = random.randint(-10, 15)
distance = []
cars = []


for i in range(1, 11):
    cars.append(Car(f'ABC-{i}', max_speed))

while len([x for x in distance if x >= 10000]) == 0:
    for car in cars:
        car.accelerate(speed)
        car.drive(1)
        distance.append(car.travelled_distance)
        print(car.registration_number)
        print(car.travelled_distance)
        print(car.max_speed)



sys.exit(0)


