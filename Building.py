from Elevator import Elevator
from Floor import Floor

class Building:
    def __init__(self):
        self.array_elevators = []
        self.array_floors = []
        self.array_possibility = []

    def array_elevators(self):
        return self.array_elevators

    def elevators_architect(self, NUM_ELEVATORS, screen):
        for lift_num in range(NUM_ELEVATORS):  
            lift = Elevator()
            self.array_elevators.append(lift)
            lift.elevators_builder(lift_num, screen)

    def floors_architect(self, NUM_FLOORS, screen):
        for floor_num in range(NUM_FLOORS):
            floor = Floor()
            self.array_floors.append(floor)
            # floor.writes_a_number(floor_num, screen)
            floor.floors_builder(floor_num, screen)
            if floor_num != NUM_FLOORS:
                floor.mark_line(floor_num, screen)
    
    def architect(self, NUM_ELEVATORS, NUM_FLOORS, screen):
        self.elevators_architect(NUM_ELEVATORS, screen)
        self.floors_architect(NUM_FLOORS, screen)





