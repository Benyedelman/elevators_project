
from Elevator_2 import Elevator
from Floor_2 import Floor
class Building:
    def __init__(self):
        self.array_elevators = []
        self.array_floors = []
        self.array_possibility = []
        self.array_possibility_time = []
        self.array_options = []

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
            floor.floors_builder(floor_num, screen)
            
    def architect(self, NUM_ELEVATORS, NUM_FLOORS, screen):
        self.elevators_architect(NUM_ELEVATORS, screen)
        self.floors_architect(NUM_FLOORS, screen)

    def update_all_elevators(self, screen, building):
        for lift in self.array_elevators:
            if lift.que:
                first_element = lift.que[0]
                Elevator.move_elevator(self, screen, first_element, lift, building)


            








