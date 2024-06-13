
import pygame
import time
from saving_variables import *

class Floor:
    def __init__(self,):
        self.button = 0
        self.number_position = 0
        self.SCREEN_HEIGHT = 0
        self.elevator_on_the_way = False
        self.start_timer = 0
        self.timer = 0
        self.timer_floor_num = 0

    # Builds all floors, black line, button color, button, and number floor
    def floors_builder(self, SCREEN_HEIGHT, floor_num, screen):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.floors_builder_brick(floor_num, screen)              # floor builder
        self.floors_builder_draw_batten(floor_num, screen)        # draw batten
        self.floors_builder_write_a_number(floor_num, screen)     # write a number on each floor
        self.floors_builder_mark_black_line(floor_num, screen)    # mark black line
        pygame.display.flip() 

    # floor builder brick
    def floors_builder_brick(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - (floor_num + 1) * FLOOR_HEIGHT - LINE_HEIGHT * floor_num   
        x = 0
        screen.blit(floor_img, (x, y))

    # draw batten
    def floors_builder_draw_batten(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - floor_num * FLOOR_HEIGHT - LINE_HEIGHT * floor_num - FLOOR_HEIGHT/2       
        x = FLOOR_WIDTH / 3
        pygame.draw.circle(screen, CONTROL_COLOR, [x, y], button_radius ) 
        self.button = x, y

    # write a number on each floor
    def floors_builder_write_a_number(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - floor_num * FLOOR_HEIGHT - (floor_num + 1) *  LINE_HEIGHT  - FLOOR_HEIGHT//2   
        if floor_num <= 9:
            x = 39
        elif floor_num <= 99:
            x = 35.5 
        else:
            x = 30
        self.number_display(floor_num, x, y, BLACK, screen)
        self.number_position = x, y

    # mark black line
    def floors_builder_mark_black_line(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - (floor_num + 1) * FLOOR_HEIGHT - LINE_HEIGHT * floor_num - LINE_HEIGHT / 2  
        x = 0
        pygame.draw.line(screen, BLACK, [x, y], [FLOOR_WIDTH-1, y], LINE_HEIGHT)
        pygame.draw.line(screen, BLACK, [FLOOR_WIDTH, 0], [FLOOR_WIDTH, self.SCREEN_HEIGHT], 3)
        pygame.draw.line(screen, BLACK, [89, 0], [89, self.SCREEN_HEIGHT], 3)

    # number display on the screen 
    def number_display(self, number, x_location, y_location, color, screen):
        font = pygame.font.Font(None, 25)
        number = font.render(f"{number}", True, (color))
        screen.blit(number, (x_location, y_location))

    # Paints the floor and updates the class of the building to look for the most efficient elevator
    def floor_button(self, screen, floor_num, building):
        """
        Checks if there is an elevator on the floor, or on the way, 
        and if not, colors the floor's button green,
        and sends a request to search for an efficient elevator 
        """
        for lift in building.array_elevators:                                 # checks if there is an elevator on the floor
            x_elevator, y_elevator =lift.elevator_position
            if self.SCREEN_HEIGHT - ((FLOOR_HEIGHT + LINE_HEIGHT) * (floor_num + 1) - LINE_HEIGHT) == y_elevator:
                return None
        if self.elevator_on_the_way == False:                                 # checks if there is an elevator on the way
            self.elevator_on_the_way = True
            x_button_location, y_button_location = self.button
            pygame.draw.circle(screen, GREEN, [x_button_location, y_button_location], button_radius ) 
            x_num_location, y_num_location = self.number_position 
            self.number_display(floor_num, x_num_location, y_num_location, BLACK, screen)
            building.choose_an_elevator(floor_num, screen)

    # Updates the values ​​of the clock
    def keeps_value_for_the_timer(self, min_value,  floor_num):
        self.timer = min_value
        self.timer_floor_num = floor_num
        self.start_timer = time.time()
        
    # presents the time on the screen
    def displays_the_stopwatch(self, screen):
        if self.timer > 0:
            self.number_display_for_timer(self.timer, self.SCREEN_HEIGHT - self.timer_floor_num * FLOOR_HEIGHT - LINE_HEIGHT * self.timer_floor_num -  FLOOR_HEIGHT/ 2 - 5 , RED, screen)
            self.timer -= time.time() - self.start_timer
            self.start_timer = time.time()
            self.number_display_for_timer(self.timer, self.SCREEN_HEIGHT - self.timer_floor_num * FLOOR_HEIGHT - LINE_HEIGHT * self.timer_floor_num -  FLOOR_HEIGHT/ 2 - 5 , RED, screen)
        if self.timer <= 0:
            self.draws_a_circle_around_the_timer(screen)
            pygame.display.flip() 

    # number display on the screen only fot the timer
    def number_display_for_timer(self, number, y_location_of_the_timer, color, screen):
        self.draws_a_circle_around_the_timer(screen)
        font = pygame.font.Font(None, 25)
        timer_display = int(number*10)/10
        number = font.render(f"{timer_display}", True, (color))
        screen.blit(number, (x_location_of_the_timer, y_location_of_the_timer))
        pygame.display.flip()

    # Draws a circle on the timer in the color of the background
    def draws_a_circle_around_the_timer(self, screen):
        y = self.SCREEN_HEIGHT - self.timer_floor_num * FLOOR_HEIGHT - LINE_HEIGHT * self.timer_floor_num -  FLOOR_HEIGHT/ 2 + 3
        x = x_location_circle_around_the_timer
        pygame.draw.circle(screen, sky_blue, [x, y], timer_radius)
    
    # After the elevator is finished, sending to "change_button_color" to returns the original button color , and play the ringer
    def back_to_original(self, screen, floor_num):
        self.elevator_on_the_way = False
        x_button_location, y_button_location = self.button
        x_num_location, y_num_location = self.number_position 
        self.change_button_color(screen, x_button_location, y_button_location, floor_num, x_num_location, y_num_location)
        pygame.mixer.music.load("ding.mp3")
        pygame.mixer.music.play()
        pygame.display.flip() 

    # After the elevator is finished, returns the original button color 
    def change_button_color(self, screen, x_button_location, y_button_location, floor_num, x_num_location, y_num_location):
        pygame.draw.circle(screen, CONTROL_COLOR, [x_button_location, y_button_location], button_radius )
        self.number_display(floor_num, x_num_location, y_num_location, BLACK, screen)  
   
            

   
        
        
    






