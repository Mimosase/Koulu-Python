import random
change = random.randint(-10,15)

class Car:
    def __init__(self, license_plate, maximum_speed=0, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        return

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
        return

    def race(self):
        cars = [Car("ABC-1", random.randint(100, 200)), Car("ABC-2", random.randint(100, 200)),
            Car("ABC-3", random.randint(100, 200)), Car("ABC-4", random.randint(100, 200)),
            Car("ABC-5", random.randint(100, 200)), Car("ABC-6", random.randint(100, 200)),
            Car("ABC-7", random.randint(100, 200)), Car("ABC-8", random.randint(100, 200)),
            Car("ABC-9", random.randint(100, 200)), Car("ABC-10", random.randint(100, 200))]

        goal = False
        hours = 0

        while goal != True:
            hours += 1
            car.accelerate(random.randint(-10,15)):
            car.drive():

        if self.travelled_distance >= 10000:
            goal = True