import pygame
from Building import Building
from Floor import Floor

NUM_FLOORS = 10
NUM_ELEVATORS = 6
ELEVATOR_IMAGE = "elv(1).png"
elevator_img = pygame.image.load(ELEVATOR_IMAGE)
CONTROL_COLOR = (128,128,128)
FLOOR_HEIGHT = 50
LINE_HEIGHT = 7
SCREEN_HEIGHT = (FLOOR_HEIGHT + LINE_HEIGHT) * NUM_FLOORS - LINE_HEIGHT
SCREEN_WIDTH = 750
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
        x1, y1 = pygame.mouse.get_pos()
        num_Invitation = (SCREEN_HEIGHT - y1)//(FLOOR_HEIGHT + LINE_HEIGHT)
        for floor in building.array_floors:
            x2, y2 = floor.button
            if (x1 - x2)**2 + (y1 - y2)**2 <= floor.button_radius**2:
                floor.floor_button(screen, num_Invitation, building )
                            

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        button(building )
     
pygame.quit()

# NUM_FLOORS = int(input("please enter how many floors yuo want in the building: "))
# while NUM_FLOORS < 1 and NUM_FLOORS > 13:
#     NUM_FLOORS = int(input("please enter a number of floors greater then 1: "))
# NUM_ELEVATORS = int(input("please enter the number of lifts you want: "))
# while NUM_ELEVATORS < 0 or NUM_ELEVATORS > 10: 
#     NUM_ELEVATORS = int(input("please enter a number of lifts greater then 0: "))

