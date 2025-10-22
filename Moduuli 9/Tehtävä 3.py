class Car:
    def __init__(self, license_plate, maxinum_speed=0, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maxinum_speed
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