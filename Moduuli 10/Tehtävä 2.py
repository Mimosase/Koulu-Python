class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self,request):
        if request > self.current_floor:
            while self.current_floor != request:
                self.floor_up()

        if request < self.current_floor:
            while self.current_floor != request:
                self.floor_down()

        return

class Building:

    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []

        for kpl in range(number_of_elevators):
            building_elevator = Elevator(bottom_floor,top_floor)
            self.elevators.append(building_elevator)

    def run_elevator(self, elevator_number, request):
        self.elevators[elevator_number].go_to_floor(request)