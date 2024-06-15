
import pygame
import time
from Saving_constant_values import *

class Floor:
    def __init__(self,):
        self.button_location = 0
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
        x = start_screen
        screen.blit(floor_img, (x, y))

    # draw batten
    def floors_builder_draw_batten(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - floor_num * FLOOR_HEIGHT - LINE_HEIGHT * floor_num - FLOOR_HEIGHT / 2       
        x = FLOOR_WIDTH / 3
        pygame.draw.circle(screen, CONTROL_COLOR, [x, y], button_radius ) 
        self.button_location = x, y

    # write a number on each floor
    def floors_builder_write_a_number(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - floor_num * FLOOR_HEIGHT - (floor_num + 1) *  LINE_HEIGHT  - FLOOR_HEIGHT // 2   
        if floor_num <= 9:                                      # Changes the position of the number according to the number of digits to be in the center.
            x = x_to_one_digit
        elif floor_num <= 99:
            x = x_to_two_digits
        else:
            x = x_to_three_digits
        self.number_display(floor_num, x, y, BLACK, screen)
        self.number_position = x, y

    # mark black line
    def floors_builder_mark_black_line(self, floor_num, screen):
        y = self.SCREEN_HEIGHT - (floor_num + 1) * FLOOR_HEIGHT - LINE_HEIGHT * floor_num - LINE_HEIGHT / 2  
        x = start_screen
        pygame.draw.line(screen, BLACK, [x, y], [FLOOR_WIDTH-1, y], LINE_HEIGHT)
        pygame.draw.line(screen, BLACK, [FLOOR_WIDTH, start_screen], [FLOOR_WIDTH, self.SCREEN_HEIGHT], width_line)
        pygame.draw.line(screen, BLACK, [brick_width, start_screen], [brick_width, self.SCREEN_HEIGHT], width_line)

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
        for lift in building.array_elevators:                                                         # checks if there is an elevator on the floor
            y_elevator =lift.elevator_position[1]
            if self.SCREEN_HEIGHT - (Total_floor_height * (floor_num + 1) - LINE_HEIGHT) == y_elevator:
                return None
        if self.elevator_on_the_way == False:                                                         # checks if there is an elevator on the way
            self.elevator_on_the_way = True
            x_button_location, y_button_location = self.button_location             
            pygame.draw.circle(screen, GREEN, [x_button_location, y_button_location], button_radius ) # Paints the button green
            x_num_location, y_num_location = self.number_position 
            self.number_display(floor_num, x_num_location, y_num_location, BLACK, screen)             # Writes the floor number on the button back
            building.choose_an_elevator(floor_num, self)                                            # Sends a call to the building to check which elevator is the most efficient

    # Updates the values ​​of the clock
    def keeps_value_for_the_timer(self, min_value,  floor_num):
        self.timer = min_value
        self.timer_floor_num = floor_num
        self.start_timer = time.time()
        
    # presents the time on the screen
    def displays_the_stopwatch(self, screen):
        if self.timer > 0:
            y_location_of_the_timer = self.SCREEN_HEIGHT - self.timer_floor_num * FLOOR_HEIGHT - LINE_HEIGHT * self.timer_floor_num - Total_floor_height / 2 
            self.number_display_for_timer(self.timer, y_location_of_the_timer, RED, screen)          # Writes the initial number of the stopwatch
            self.timer -= time.time() - self.start_timer                                             # Calculates the time left for the stopwatch
            self.start_timer = time.time()
            self.number_display_for_timer(self.timer, y_location_of_the_timer, RED, screen)          # Constantly updates the stopwatch on the screen
        if self.timer <= 0:
            self.draws_a_circle_around_the_timer(screen)                                             # When the stopwatch runs out, it deletes the last number
            pygame.display.flip() 

    # number display on the screen only fot the timer
    def number_display_for_timer(self, number, y_location_of_the_timer, color, screen):
        self.draws_a_circle_around_the_timer(screen)                                                 # Deletes the stopwatch from the screen
        font = pygame.font.Font(None, 25)
        timer_display = int(number*10)/10                                                            # Displays the stopwatch only up to one digit after the period
        number = font.render(f"{timer_display}", True, (color))
        screen.blit(number, (x_location_of_the_timer, y_location_of_the_timer))                      # Shows the updated time
        pygame.display.flip()

    # Draws a circle on the timer in the color of the background
    def draws_a_circle_around_the_timer(self, screen):
        y = self.SCREEN_HEIGHT - self.timer_floor_num * FLOOR_HEIGHT - LINE_HEIGHT * self.timer_floor_num -   FLOOR_HEIGHT// 2 + 3 
        x = x_location_circle_around_the_timer
        pygame.draw.circle(screen, sky_blue, [x, y], timer_radius)
    
    # After the elevator is finished, sending to "change_button_color" to returns the original button color , and play the ringer
    def back_to_original(self, screen, floor_num):
        self.elevator_on_the_way = False                                                             # Updates that there is no elevator on the way to the floor
        x_button_location, y_button_location = self.button_location
        x_num_location, y_num_location = self.number_position 
        self.change_button_color(screen, x_button_location, y_button_location, floor_num, x_num_location, y_num_location) # Updates the color of the button to the original color
        pygame.mixer.music.load("ding.mp3")                                                           
        pygame.mixer.music.play()                                                                    # Activates the ringer
        pygame.display.flip() 

    # After the elevator is finished, returns the original button color 
    def change_button_color(self, screen, x_button_location, y_button_location, floor_num, x_num_location, y_num_location):
        pygame.draw.circle(screen, CONTROL_COLOR, [x_button_location, y_button_location], button_radius ) # Updates the color of the button to the original color
        self.number_display(floor_num, x_num_location, y_num_location, BLACK, screen)                # Writes back the floor number
   
            

   
        
        
    






