
import pygame
from Elevator_2 import Elevator
import time
import threading
class Floor:
    def __init__(self,):
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
        self.SCREEN_HEIGHT = 0
        self.sky_blue = (135, 206, 235)
        self.elevator_on_the_way = False
        self.button_radius = 10

    #floor builder brick
    def floors_builder_brick(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - (floor_num + 1) * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num   
        x = 0
        screen.blit(self.floor_img, (x, y))

     # draw batten
    def floors_builder_draw_batten(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - floor_num * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num - self.FLOOR_HEIGHT/2       
        x = self.FLOOR_WIDTH / 3
        pygame.draw.circle(screen, self.CONTROL_COLOR, [x, y], self.button_radius ) 
        self.button = x, y

    #write a number on each floor
    def floors_builder_write_a_number(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - floor_num * self.FLOOR_HEIGHT + 1  - (floor_num + 1) *  self.LINE_HEIGHT  - self.FLOOR_HEIGHT/2   
        if floor_num <= 9:
            x = 39
        else:
            x = 35.5 
        self.number_display(floor_num, x, y, self.BLACK, screen)
        self.number_position = x, y

     # mark black line
    def floors_builder_mark_black_line(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - (floor_num + 1) * self.FLOOR_HEIGHT - self.LINE_HEIGHT * floor_num - self.LINE_HEIGHT / 2  
        x = 0
        pygame.draw.line(screen, self.BLACK, [x, y], [self.FLOOR_WIDTH-1, y], self.LINE_HEIGHT)

    #  Builds all floors, black line, button color, button, and number floor
    def floors_builder(self, SCREEN_HEIGHT, floor_num, screen):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.floors_builder_brick(floor_num, screen)              #floor builder
        self.floors_builder_draw_batten(floor_num, screen)        # draw batten
        self.floors_builder_write_a_number(floor_num, screen)     # write a number on each floor
        self.floors_builder_mark_black_line(floor_num, screen)    # mark black line
        pygame.display.flip() 

    # number display on the screen 
    def number_display(self, number, x_location, y_location, color, screen):
        font = pygame.font.Font(None, 25)
        number = font.render(f"{number}", True, (color))
        screen.blit(number, (x_location, y_location))

    # number display on the screen only fot the timer
    def number_display_for_timer(self, number, x_location, y_location, color, screen):
        font = pygame.font.Font(None, 25)
        timer_display = int(number*10)/10
        number = font.render(f"{timer_display}", True, (color))
        screen.blit(number, (x_location, y_location))
        pygame.display.flip()

    # After the elevator is finished, returns the original button color 
    def change_button_color(self, screen, x_button_location, y_button_location, num_invitation, x_num_location, y_num_location):
        pygame.draw.circle(screen, self.CONTROL_COLOR, [x_button_location, y_button_location], self.button_radius )
        self.number_display(num_invitation, x_num_location, y_num_location, self.BLACK, screen) 

    # presents the time on the screen
    def timer(self, min_value,  num_invitation, screen):
        timer = min_value
        if timer > 0:
            self.number_display_for_timer(timer, 100, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 - 5 , self.RED, screen)
        while timer > 0:
            timer -= 0.1
            time.sleep(0.1)
            pygame.draw.circle(screen, self.sky_blue, [112, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 + 3], 20)
            pygame.display.flip()
            self.number_display_for_timer(timer, 100, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 - 5 , self.RED, screen)
        pygame.draw.circle(screen, self.sky_blue, [112, self.SCREEN_HEIGHT - num_invitation * self.FLOOR_HEIGHT - self.LINE_HEIGHT * num_invitation -  self.FLOOR_HEIGHT/ 2 + 3], 20)
        pygame.display.flip() 
    
    # After the elevator is finished, returns the original button color , and play the ringer
    def back_to_original(self, screen, num_invitation):
        x_button_location, y_button_location = self.button
        x_num_location, y_num_location = self.number_position 
        self.change_button_color(screen, x_button_location, y_button_location, num_invitation, x_num_location, y_num_location)
        pygame.mixer.music.load("ding.mp3")
        pygame.mixer.music.play()
        pygame.display.flip() 
   

    def floor_button(self, screen, num_invitation, building):
        """
        Checks if there is an elevator on the floor, or on the way, 
        and if not, colors the floor's button green,
        and sends a request to search for an efficient elevator 
        """
        for lift in building.array_elevators:                                 #checks if there is an elevator on the floor
            x, y =lift.elevator_position
            if lift.SCREEN_HEIGHT - num_invitation * (lift.FLOOR_HEIGHT + lift.LINE_HEIGHT) - lift.FLOOR_HEIGHT  == y:
                return None
        floor = building.array_floors[num_invitation]
        if floor.elevator_on_the_way == False:                                #checks if there is an elevator on the way
            floor.elevator_on_the_way = True
            x_button_location, y_button_location = self.button
            pygame.draw.circle(screen, self.GREEN, [x_button_location, y_button_location], self.button_radius ) 
            x_num_location, y_num_location = self.number_position 
            self.number_display(num_invitation, x_num_location, y_num_location, self.BLACK, screen)
            building.choose_an_elevator(num_invitation, screen)
            

   
        
        
    






