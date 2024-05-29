import pygame

ELEVATOR_IMAGE = "elv(1).png"
FLOORS_IMAGE = "Screenshot from 2024-05-29 10-47-25.png"

def elevators_builder(num_elevators, screen):
    array_elevators = []
    for i in range(1, num_elevators + 1):  
        array_elevators.append(i)
    elevator_img = pygame.image.load(ELEVATOR_IMAGE)
    for i in range(len(array_elevators)):
        x = 103 + i * 64
        screen.blit(elevator_img, (x, 580))
                                        #??????????????

def floors_builder(num_floors, screen):
    array_floors = []
    for i in range(1, num_floors + 1):
        array_floors.append(i)
    floor_img = pygame.image.load(FLOORS_IMAGE)
    for i in range(len(array_floors)):
        y = 600 - i * 50
        screen.blit(floor_img, (0, y))
        pygame.display.flip()  


          

     
     

num_floors = int(input("please enter how many floors yuo want in the building: "))
while num_floors < 1 and num_floors > 13:
    num_floors = int(input("please enter a number of floors greater then 1: "))
num_elevators = int(input("please enter the number of lifts you want: "))
while num_elevators < 0 or num_elevators > 10: 
    num_elevators = int(input("please enter a number of lifts greater then 0: "))


SCREEN_WIDTH = 750
SCREEN_HEIGHT = 650

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("the elevator challenge")
maroon = (128, 90, 32)
screen.fill(maroon)
elevators_builder(num_elevators, screen) 
floors_builder(num_floors, screen)



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()









# def main():


