
import pygame
from Building_2 import Building
from Floor_2 import Floor
from saving_variables import *

NUM_FLOORS = 11
NUM_ELEVATORS = 4
SCREEN_HEIGHT = (FLOOR_HEIGHT + LINE_HEIGHT) * NUM_FLOORS - LINE_HEIGHT
SCREEN_WIDTH = 700
building = Building()
floor = Floor()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("the elevator challenge")
screen.fill(sky_blue)
building.constructor(SCREEN_HEIGHT, NUM_ELEVATORS, NUM_FLOORS, screen)  # Sends to the building class and from there sends to the class their elevators and floors
           
# Receives mouse input and translates from which floor the request was sent  
def button():
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == click_left:
        x_mouse, y_mouse = pygame.mouse.get_pos()
        floor_num = (SCREEN_HEIGHT - y_mouse)//(FLOOR_HEIGHT + LINE_HEIGHT)
        floor = building.array_floors[floor_num]
        x_button_location, y_button_location = floor.button             # Performs an action only if the floor button is pressed
        if (x_mouse - x_button_location) ** 2 + (y_mouse - y_button_location) ** 2 <= button_radius ** 2:
            floor.floor_button(screen, floor_num, building)             # Sends to the floor class the floor where the order was received


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        button()
    building.update_all_elevators(screen)                               # Updates the queue of elevators inside the loop while
    building.update_all_timer(screen)                 
pygame.quit()


