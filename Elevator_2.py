
import pygame
import numpy
import threading
from collections import deque


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
        

    def elevators_builder(self, lift_num, screen):
        x = self.FLOOR_WIDTH + lift_num * self.ELEVATOR_WIDTH 
        y = self.SCREEN_HEIGHT - self.FLOOR_HEIGHT 
        screen.blit(self.elevator_img, (x, y))
        self.elevator_position = x, y
        pygame.display.flip()

    def choose_an_elevator(self, building, num_Invitation, screen):
        for i in range(len(building.array_elevators)):
            possibility = building.array_elevators[i]
            x2, y2 = possibility.elevator_position
            y2 = (possibility.SCREEN_HEIGHT - y2)//(possibility.FLOOR_HEIGHT + possibility.LINE_HEIGHT)
            z = abs(num_Invitation - y2)
            building.array_possibility.append(z)
            possibility_time = building.array_elevators[i]
            time = possibility_time.finish_time
            building.array_possibility_time.append(time)
        for i in range(len(building.array_possibility)):
            d = building.array_possibility[i]
            t = building.array_possibility_time[i]
            building.array_options.append(d + t)
        min_value = min(building.array_options)
        min_value_dis = min(building.array_possibility)
        min_index = building.array_options.index(min_value)
        building.array_possibility.clear()
        building.array_possibility_time.clear()
        building.array_options.clear()
        building.array_elevators[min_index].que.append(num_Invitation)
        lift = building.array_elevators[min_index]
        thread = threading.Thread(target = self.timer, args = (min_value_dis, num_Invitation, screen, lift))
        thread.start()
        return min_index, min_value 
    
         
    def move_elevator(self, screen, num_Invitation, lift, building):
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
            floor.back_to_original(screen, num_Invitation)
       
        







        


    


        





















