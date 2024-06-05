
import pygame
from Elevator_2 import Elevator
import time
import threading
class Floor:
    def __init__(self,):
        self.NUM_FLOORS = 10
        self.FLOORS_IMAGE = "Screenshot from 2024-05-29 10-47-25.png"
        self.floor_img = pygame.image.load(self.FLOORS_IMAGE)
        self.CONTROL_COLOR = (128,128,128)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 190, 0)
        self.RED = (200, 0, 0)
        self.FLOOR_WIDTH = 133.5
        self.FLOOR_HEIGHT = 50
        self.LINE_HEIGHT = 7
        self.button = 0
        self.number_position = 0
        self.button_radius  = 10
        self.SCREEN_HEIGHT = (self.FLOOR_HEIGHT + self.LINE_HEIGHT) * self.NUM_FLOORS - self.LINE_HEIGHT
        self.sky_blue = (135, 206, 235)
       
    def floors_builder(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - (floor_num + 1) * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num   #floor builder
        x = 0
        screen.blit(self.floor_img, (x, y))
        y = self.SCREEN_HEIGHT - floor_num * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num - self.FLOOR_HEIGHT/2        # draw batten
        x = self.FLOOR_WIDTH / 3
        pygame.draw.circle(screen, self.CONTROL_COLOR, [x, y], 10) 
        self.button = x, y
        y = self.SCREEN_HEIGHT - floor_num * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num  #write a number on each floor
        font = pygame.font.Font(None, 25)
        number = font.render(f"{floor_num}", True, (self.BLACK))
        screen.blit(number, (39, y - 33))
        self.number_position = 39, y - 33
        y = self.SCREEN_HEIGHT - (floor_num + 1) * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num - self.LINE_HEIGHT / 2   # mark black line
        x = 0
        pygame.draw.line(screen, self.BLACK, [x, y], [self.FLOOR_WIDTH-1, y], self.LINE_HEIGHT)
        pygame.display.flip() 

    def change_button_color(self, screen, x_button_location, y_button_location, num_Invitation, x_num_location, y_num_location):
        pygame.draw.circle(screen, self.CONTROL_COLOR, [x_button_location, y_button_location], 10) 
        font = pygame.font.Font(None, 25)
        number = font.render(f"{num_Invitation}", True, (self.BLACK))
        screen.blit(number, (x_num_location,y_num_location))

    def timer(self, min_value, num_Invitation, screen, lift):
        # timer = min_value / 2
        timer =  lift.finish_time + min_value / 2
        lift.finish_time = lift.finish_time + timer
        font = pygame.font.Font(None, 25)
        number = font.render(f"{timer}", True, (self.RED))
        screen.blit(number, (100, self.SCREEN_HEIGHT - num_Invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_Invitation -  self.FLOOR_HEIGHT/ 2 - 5 ))
        pygame.display.flip() 
        while timer > 0:
            timer -= 0.5
            time.sleep(0.5)
            lift.finish_time = lift.finish_time - 0.5
            pygame.draw.circle(screen, self.sky_blue, [110, self.SCREEN_HEIGHT - num_Invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_Invitation -  self.FLOOR_HEIGHT/ 2 - 5  + 10], 20)
            font = pygame.font.Font(None, 25)
            number = font.render(f"{timer}", True, (self.RED))
            screen.blit(number, (100, self.SCREEN_HEIGHT - num_Invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_Invitation -  self.FLOOR_HEIGHT/ 2 - 5 ))
            pygame.display.flip() 
        pygame.draw.circle(screen, self.sky_blue, [110, self.SCREEN_HEIGHT - num_Invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_Invitation -  self.FLOOR_HEIGHT/ 2 - 5  + 10], 20)
        pygame.display.flip() 

    def back_to_original(self, screen, num_Invitation):
        x_button_location, y_button_location = self.button
        x_num_location, y_num_location = self.number_position 
        self.change_button_color(screen, x_button_location, y_button_location, num_Invitation, x_num_location, y_num_location)
        pygame.mixer.music.load("ding.mp3")
        pygame.mixer.music.play()
        pygame.display.flip() 
   
    def floor_button(self, screen, num_Invitation, building):
        x_button_location, y_button_location = self.button
        pygame.draw.circle(screen, self.GREEN, [x_button_location, y_button_location], 10) 
        x_num_location, y_num_location = self.number_position 
        font = pygame.font.Font(None, 25)
        number = font.render(f"{num_Invitation}", True, (self.BLACK))
        screen.blit(number, (x_num_location, y_num_location))
        min_index, min_value  = Elevator.choose_an_elevator(self, building, num_Invitation, screen)
        lift = building.array_elevators[min_index]
        Elevator.move_elevator(self, screen, num_Invitation, lift, building)
        
        
    






