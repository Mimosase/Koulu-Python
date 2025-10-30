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

    def __str__(self):
        return f"{self.license_plate} {self.maximum_speed} {self.current_speed} {self.travelled_distance}"

class Race:

    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            self.race_finished()
            return

    def print_status(self):
        for car in self.cars:
            print(car)

    def race_finished(self):
        goal = False

        for car in self.cars:
            if car.travelled_distance >= self.distance:
                goal = True
                break

        return goal


#def race():
#    cars = [Car("ABC-1", random.randint(100, 200)), Car("ABC-2", random.randint(100, 200)),
#        Car("ABC-3", random.randint(100, 200)), Car("ABC-4", random.randint(100, 200)),
#        Car("ABC-5", random.randint(100, 200)), Car("ABC-6", random.randint(100, 200)),
#        Car("ABC-7", random.randint(100, 200)), Car("ABC-8", random.randint(100, 200)),
#        Car("ABC-9", random.randint(100, 200)), Car("ABC-10", random.randint(100, 200))]
#
#
#    hours = 0
#
#    while goal != True:
#        hours += 1
#        for car in cars:
#            car.accelerate(random.randint(-10, 15))
#            car.drive(1)
#            if car.travelled_distance >= 10000:
#                goal = True
#
#    cars.sort(key = lambda x: x.travelled_distance, reverse=True)
#   return cars