
from Elevator_2 import Elevator
from Floor_2 import Floor
import pygame
import threading
class Building:
    def __init__(self):
        self.array_elevators = []
        self.array_floors = []
        self.array_possibility = []
        self.array_possibility_time = []
        self.array_options = []
        self.LINE_HEIGHT = 7
        self.FLOOR_HEIGHT = 50
        self.FLOOR_WIDTH = 133.5


    def elevators_architect(self, SCREEN_HEIGHT, NUM_ELEVATORS, screen):
        for lift_num in range(NUM_ELEVATORS):  
            lift = Elevator()
            self.array_elevators.append(lift)
            lift.elevators_builder(SCREEN_HEIGHT, lift_num, screen)


    def floors_architect(self, SCREEN_HEIGHT, NUM_FLOORS, screen):
        for floor_num in range(NUM_FLOORS):
            floor = Floor()
            self.array_floors.append(floor)
            pygame.draw.line(screen, (0,0,0), [self.FLOOR_WIDTH, 0], [self.FLOOR_WIDTH, SCREEN_HEIGHT], 3)
            pygame.draw.line(screen, (0,0,0), [89., 0], [89, SCREEN_HEIGHT], 3)
            floor.floors_builder(SCREEN_HEIGHT, floor_num, screen)


    def architect(self, SCREEN_HEIGHT, NUM_ELEVATORS, NUM_FLOORS, screen):
        self.elevators_architect(SCREEN_HEIGHT, NUM_ELEVATORS, screen)
        self.floors_architect(SCREEN_HEIGHT, NUM_FLOORS, screen)


    def update_all_elevators(self, screen, building):
        for lift in self.array_elevators:
            if lift.queue:
                first_element = lift.queue[0]
                Elevator.move_elevator(self, screen, first_element, lift, building)


    def merge_for_minimum(self, num_invitation):
        for i in range(len(self.array_elevators)):
            possibility = self.array_elevators[i]
            y = possibility.position_of_last_floor
            dist = abs(num_invitation - y)
            self.array_possibility.append(dist/2)
            time = possibility.finish_time
            self.array_possibility_time.append(time)
            d = self.array_possibility[i]
            t = self.array_possibility_time[i]
            self.array_options.append(d + t)

    # chooses the best elevator
    def choose_an_elevator(self, num_invitation, screen):
        floor = self.array_floors[num_invitation]
        self.merge_for_minimum(num_invitation)
        min_value = min(self.array_options)
        min_index = self.array_options.index(min_value)
        min_value_dis = self.array_possibility[min_index]
        self.array_elevators[min_index].queue.append(num_invitation)
        self.array_possibility.clear()
        self.array_possibility_time.clear()
        self.array_options.clear()
        lift = self.array_elevators[min_index]
        thread = threading.Thread(target = floor.timer, args = (num_invitation, screen, lift))
        thread.start()
        lift.position_of_last_floor = num_invitation
        return min_index
        
            








