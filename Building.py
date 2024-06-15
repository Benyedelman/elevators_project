
from Elevator import Elevator
from Floor import Floor
from Saving_constant_values import *

class Building:
    def __init__(self):
        self.array_elevators = []
        self.array_floors = []        

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
    def choose_an_elevator(self, floor_num, floor):
        min_value, min_index = self.merge_for_minimum(floor_num) # Checking which elevator is the most efficient and how long it will take to arrive
        lift = self.array_elevators[min_index]                   # The best elevator
        lift.ny_queue.append(floor_num)                          # Adding the floor_num to the elevator queue
        lift.position_of_last_floor = floor_num                  # Updates the last location where the elevator will stop, for subsequent checks
        lift.finish_time = min_value + two_seconds               # Updates the end time of the elevator
        floor.keeps_value_for_the_timer(min_value, floor_num)    # Updates the floor's stopwatch how much time it has

    # Merges the distance and finish time to get the minimum
    def merge_for_minimum(self, floor_num):
        array_dist_and_time = []
        for lift in range(len(self.array_elevators)):
            possibility = self.array_elevators[lift]
            floor = possibility.position_of_last_floor
            dist = abs(floor_num - floor) / 2
            time = possibility.finish_time
            array_dist_and_time.append(dist + time)
        min_value = min(array_dist_and_time)
        min_index = array_dist_and_time.index(min_value)
        array_dist_and_time.clear()
        return min_value, min_index

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









