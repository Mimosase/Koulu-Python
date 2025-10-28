class Elevator:

    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.floor = min_floor

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1

    def go_to_floor(self,request):
        if request > self.floor:
            while self.floor != request:
                self.floor_up()

        if request < self.floor:
            while self.floor != request:
                self.floor_down()

        return