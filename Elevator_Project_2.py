
import pygame
from Building_2 import Building
from Floor_2 import Floor

NUM_FLOORS = 10
NUM_ELEVATORS = 1
ELEVATOR_IMAGE = "elv(1).png"
elevator_img = pygame.image.load(ELEVATOR_IMAGE)
CONTROL_COLOR = (128,128,128)
FLOOR_HEIGHT = 50
LINE_HEIGHT = 7
SCREEN_HEIGHT = (FLOOR_HEIGHT + LINE_HEIGHT) * NUM_FLOORS - LINE_HEIGHT
SCREEN_WIDTH = 700
# sky_blue = (128,128,128)
sky_blue = (135, 206, 235)
building = Building()
floor = Floor()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("the elevator challenge")
screen.fill(sky_blue)
building.architect(NUM_ELEVATORS, NUM_FLOORS, screen)

    
def button(building ):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x_mouse, y_mouse = pygame.mouse.get_pos()
        num_Invitation = (SCREEN_HEIGHT - y_mouse)//(FLOOR_HEIGHT + LINE_HEIGHT)
        for floor in building.array_floors:
            x_button_location, y_button_location = floor.button
            if (x_mouse - x_button_location)**2 + (y_mouse - y_button_location)**2 <= floor.button_radius**2:
                floor.floor_button(screen, num_Invitation, building)
                            
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        button(building)
    building.update_all_elevators(screen, building)
pygame.quit()

# NUM_FLOORS = int(input("please enter how many floors yuo want in the building: "))
# while NUM_FLOORS < 1 and NUM_FLOORS > 13:
#     NUM_FLOORS = int(input("please enter a number of floors greater then 1: "))
# NUM_ELEVATORS = int(input("please enter the number of lifts you want: "))
# while NUM_ELEVATORS < 0 or NUM_ELEVATORS > 10: 
#     NUM_ELEVATORS = int(input("please enter a number of lifts greater then 0: "))

