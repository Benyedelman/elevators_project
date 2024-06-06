
import pygame
import numpy
import threading
from collections import deque
import time


class Elevator:
    def __init__(self):
        self.NUM_FLOORS = 10
        self.ELEVATOR_IMAGE = "elv(1).png"
        self.elevator_img = pygame.image.load(self.ELEVATOR_IMAGE)
        self.SCREEN_WIDTH = 750
        self.ELEVATOR_WIDTH = 64
        self.FLOOR_WIDTH = 140
        self.LINE_HEIGHT = 7
        self.FLOOR_HEIGHT = 50
        self.SCREEN_HEIGHT = (self.FLOOR_HEIGHT + self.LINE_HEIGHT) * self.NUM_FLOORS - self.LINE_HEIGHT
        self.elevator_position = 0
        self.val = 5
        self.sky_blue = (135, 206, 235)
        self.clock = pygame.time.Clock()
        self.REFRESH_RATE = 111
        self.timer = 0
        self.que = deque()
        self.finish_time = 0
        self.t1 = 0
        self.position_of_last_floor = 0
        
    # Builds all the elevators
    def elevators_builder(self, lift_num, screen):
        x = self.FLOOR_WIDTH + lift_num * self.ELEVATOR_WIDTH 
        y = self.SCREEN_HEIGHT - self.FLOOR_HEIGHT 
        screen.blit(self.elevator_img, (x, y))
        self.elevator_position = x, y
        pygame.display.flip()

    
    # Moves the elevator
    def move_elevator(self, screen, num_Invitation, lift, building):
        t0 = time.perf_counter()
        if t0 - lift.t1 >= 2:
            x, y = lift.elevator_position
            new_y = lift.SCREEN_HEIGHT - num_Invitation * (lift.FLOOR_HEIGHT + lift.LINE_HEIGHT) - lift.FLOOR_HEIGHT 
            if y != new_y:
                if new_y < y:
                    y -= 1
                else:
                    y +=1
                pygame.draw.line(screen, lift.sky_blue, [x + lift.ELEVATOR_WIDTH/2, lift.SCREEN_HEIGHT], [x + lift.ELEVATOR_WIDTH/2, 0], 70)
                screen.blit(lift.elevator_img, (x,y))
                pygame.display.flip()
                lift.clock.tick(lift.REFRESH_RATE)
                lift.elevator_position = x, y
            if y == new_y:
                lift.que.popleft()
                floor = building.array_floors[num_Invitation]
                floor.elevator_on_the_way = False
                floor.back_to_original(screen, num_Invitation)
                lift.t1 = time.perf_counter()
                lift.finish_time += 2
       
        







        


    


        





















