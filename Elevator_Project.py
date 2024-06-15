
import pygame
from Building import Building
from Floor import Floor
from Saving_constant_values import *


NUM_FLOORS = 11
NUM_ELEVATORS = 3
SCREEN_HEIGHT = Total_floor_height * NUM_FLOORS - LINE_HEIGHT           # The height of the screen depends on the number of floors
SCREEN_WIDTH = 700
building = Building()
floor = Floor()

# start of game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         # Initializes the screen size
pygame.display.set_caption("the elevator challenge")
screen.fill(sky_blue)                                                   # Sets the screen background
building.constructor(SCREEN_HEIGHT, NUM_ELEVATORS, NUM_FLOORS, screen)  # Sends to the building class and from there sends to the class their elevators and floors
           


# Receives mouse input and translates from which floor the request was sent  
def button():
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == click_left:
        x_mouse, y_mouse = pygame.mouse.get_pos()                       # x and y coordinates
        floor_num = (SCREEN_HEIGHT - y_mouse)//Total_floor_height       # Calculate on which floor the button was pressed
        floor = building.array_floors[floor_num]                        # Calls the class of the current floor
        x_button_location, y_button_location = floor.button_location    # Performs an action only if the floor button is pressed, using the Pythagorean theorem
        if (x_mouse - x_button_location) ** 2 + (y_mouse - y_button_location) ** 2 <= button_radius ** 2:
            floor.floor_button(screen, floor_num, building)             # Sends to the floor class the floor where the order was received


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        button()
    building.update_all_elevators(screen)                               # Updates the queue of elevators inside the loop while
    building.update_all_timer(screen)                                   # Updates all clocks of all floors    
pygame.quit()



