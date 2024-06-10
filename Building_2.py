
from Elevator_2 import Elevator
from Floor_2 import Floor
import pygame
import threading
class Building:
    def __init__(self):
        self.array_elevators = []
        self.array_floors = []
        self.array_dist_and_time = []
        self.LINE_HEIGHT = 7
        self.FLOOR_HEIGHT = 50
        self.FLOOR_WIDTH = 133.5


    def elevators_constructor(self, SCREEN_HEIGHT, NUM_ELEVATORS, screen):
        for lift_num in range(NUM_ELEVATORS):  
            lift = Elevator()
            self.array_elevators.append(lift)
            lift.elevators_builder(SCREEN_HEIGHT, lift_num, screen)


    def floors_constructor(self, SCREEN_HEIGHT, NUM_FLOORS, screen):
        for floor_num in range(NUM_FLOORS):
            floor = Floor()
            self.array_floors.append(floor)
            pygame.draw.line(screen, (0,0,0), [self.FLOOR_WIDTH, 0], [self.FLOOR_WIDTH, SCREEN_HEIGHT], 3)
            pygame.draw.line(screen, (0,0,0), [89., 0], [89, SCREEN_HEIGHT], 3)
            floor.floors_builder(SCREEN_HEIGHT, floor_num, screen)


    def constructor(self, SCREEN_HEIGHT, NUM_ELEVATORS, NUM_FLOORS, screen):
        self.elevators_constructor(SCREEN_HEIGHT, NUM_ELEVATORS, screen)
        self.floors_constructor(SCREEN_HEIGHT, NUM_FLOORS, screen)


    def update_all_elevators(self, screen, building):
        for lift in self.array_elevators:
            lift.stopwatch_for_finish_time()
            if lift.queue:
                first_element = lift.queue[0]
                Elevator.move_elevator(self, screen, first_element, lift, building)


    def merge_for_minimum(self, num_invitation):
        for i in range(len(self.array_elevators)):
            possibility = self.array_elevators[i]
            y = possibility.position_of_last_floor
            dist = abs(num_invitation - y) / 2
            time = possibility.finish_time
            self.array_dist_and_time.append(dist + time)
            

    # chooses the best elevator
    def choose_an_elevator(self, num_invitation, screen):
        floor = self.array_floors[num_invitation]
        self.merge_for_minimum(num_invitation)
        min_value = min(self.array_dist_and_time)
        min_index = self.array_dist_and_time.index(min_value)
        self.array_dist_and_time.clear()
        self.array_elevators[min_index].queue.append(num_invitation)
        lift = self.array_elevators[min_index]
        thread = threading.Thread(target = floor.timer, args = (min_value, num_invitation, screen, lift))
        thread.start()
        
        
            








