
from Elevator_2 import Elevator
from Floor_2 import Floor
from saving_variables import *

class Building:
    def __init__(self):
        self.array_elevators = []
        self.array_floors = []
        self.array_dist_and_time = []
        

    # Responsible for the construction of all floors and elevators 
    def constructor(self, SCREEN_HEIGHT, NUM_ELEVATORS, NUM_FLOORS, screen):
        self.elevators_constructor(SCREEN_HEIGHT, NUM_ELEVATORS, screen)
        self.floors_constructor(SCREEN_HEIGHT, NUM_FLOORS, screen)

    # Responsible for the construction of all elevators
    def elevators_constructor(self, SCREEN_HEIGHT, NUM_ELEVATORS, screen):
        for lift_num in range(NUM_ELEVATORS):  
            lift = Elevator()
            self.array_elevators.append(lift)
            lift.elevators_builder(SCREEN_HEIGHT, lift_num, screen)

    # Responsible for the construction of all floors
    def floors_constructor(self, SCREEN_HEIGHT, NUM_FLOORS, screen):
        for floor_num in range(NUM_FLOORS):
            floor = Floor()
            self.array_floors.append(floor)
            floor.floors_builder(SCREEN_HEIGHT, floor_num, screen)

    # chooses the best elevator
    def choose_an_elevator(self, floor_num, screen):
        floor = self.array_floors[floor_num]
        self.merge_for_minimum(floor_num)
        min_value = min(self.array_dist_and_time)
        min_index = self.array_dist_and_time.index(min_value)
        self.array_dist_and_time.clear()
        lift = self.array_elevators[min_index]
        lift.ny_queue.append(floor_num)
        lift.position_of_last_floor = floor_num
        lift.finish_time = min_value + two_seconds
        floor.keeps_value_for_the_timer(min_value, floor_num)

    # Merges the distance and finish time to get the minimum
    def merge_for_minimum(self, floor_num):
        for i in range(len(self.array_elevators)):
            possibility = self.array_elevators[i]
            y = possibility.position_of_last_floor
            dist = abs(floor_num - y) / 2
            time = possibility.finish_time
            self.array_dist_and_time.append(dist + time)

    # Responsible for advancing the queue of each elevator all the time
    def update_all_elevators(self, screen):
        for lift in self.array_elevators:
            lift.stopwatch_for_finish_time()
            if lift.ny_queue:
                first_floor = lift.ny_queue[0]
                floor = self.array_floors[first_floor]
                Elevator.move_elevator(lift, screen, first_floor, floor)

    # Updates the clock on each floor to be a stopwatch
    def update_all_timer(self, screen):
        for floor in self.array_floors:
            if floor.timer > 0:
                floor.displays_the_stopwatch(screen)









