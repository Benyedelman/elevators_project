
from Elevator_2 import Elevator
from Floor_2 import Floor
import threading
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

    def merge_for_minimum(self, num_Invitation):
        for i in range(len(self.array_elevators)):
            possibility = self.array_elevators[i]
            x2, y2 = possibility.elevator_position
            y2 = (possibility.SCREEN_HEIGHT - y2)//(possibility.FLOOR_HEIGHT + possibility.LINE_HEIGHT)
            dist = abs(num_Invitation - y2)
            self.array_possibility.append(dist)
            time = possibility.finish_time
            self.array_possibility_time.append(time)
            d = self.array_possibility[i]
            t = self.array_possibility_time[i]
            self.array_options.append(d + t)

    # chooses the best elevator
    def choose_an_elevator(self, num_Invitation, screen):
        floor = self.array_floors[num_Invitation]
        # if floor.elevator_on_the_way == False:
        #     floor.elevator_on_the_way = True
        self.merge_for_minimum(num_Invitation)
        min_value = min(self.array_options)
        min_index = self.array_options.index(min_value)
        min_value_dis = self.array_possibility[min_index]
        self.array_elevators[min_index].que.append(num_Invitation)
        self.array_possibility.clear()
        self.array_possibility_time.clear()
        self.array_options.clear()
        lift = self.array_elevators[min_index]
        # floor = self.array_floors[num_Invitation]
        thread = threading.Thread(target = floor.timer, args = (num_Invitation, screen, lift))
        thread.start()
        lift.position_of_last_floor = num_Invitation
        return min_index
        
            








