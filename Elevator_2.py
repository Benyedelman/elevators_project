
import pygame
from collections import deque
import time


class Elevator:
    def __init__(self):
        self.ELEVATOR_IMAGE = "elv(1).png"
        self.elevator_img = pygame.image.load(self.ELEVATOR_IMAGE)
        self.ELEVATOR_WIDTH = 64
        self.FLOOR_WIDTH = 140
        self.LINE_HEIGHT = 7
        self.FLOOR_HEIGHT = 50
        self.SCREEN_HEIGHT = 0
        self.elevator_position = 0
        self.sky_blue = (135, 206, 235)
        self.clock = pygame.time.Clock()
        self.REFRESH_RATE = 111
        self.queue = deque()
        self.finish_time = 0
        self.time_start = 0
        self.position_of_last_floor = 0
        self.start_move = None
        self.start_timer_finish_time = None

    #Starts the stopwatch to finish time
    def stopwatch_for_finish_time(self):
        if self.start_timer_finish_time == None:
            self.start_timer_finish_time = time.time()
        elif self.finish_time > 0:
            self.finish_time -= time.time() - self.start_timer_finish_time
            self.start_timer_finish_time = time.time()
            print(self.finish_time)                                                    # ???????????????????????????
        else:
            self.start_timer_finish_time = None

    # Builds all the elevators
    def elevators_builder(self, SCREEN_HEIGHT, lift_num, screen):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        x = self.FLOOR_WIDTH + lift_num * self.ELEVATOR_WIDTH 
        y = self.SCREEN_HEIGHT - self.FLOOR_HEIGHT 
        screen.blit(self.elevator_img, (x, y))  #Pastes the image of the elevator
        self.elevator_position = x, y   #Saves the location of the elevator
        pygame.display.flip()

    # Moves the elevator
    def move_elevator(self, screen, num_invitation, building):
        time_end = time.perf_counter()                        #Checks if two seconds have passed since the elevator reached its destination
        if time_end - self.time_start >= 2:
            x, y = self.elevator_position                     #Updates the location of the elevator
            current_y = self.SCREEN_HEIGHT - num_invitation * (self.FLOOR_HEIGHT + self.LINE_HEIGHT) - self.FLOOR_HEIGHT    # Calculate the location where the elevator should reach 
            if y != current_y:
                if current_y < y:
                    y -= 1
                else:
                    y +=1
                pygame.draw.line(screen, self.sky_blue, [x + self.ELEVATOR_WIDTH/2, self.SCREEN_HEIGHT], [x + self.ELEVATOR_WIDTH/2, 0], 70)
                screen.blit(self.elevator_img, (x,y))         #Pastes the image of the elevator
                pygame.display.flip()
                self.clock.tick(self.REFRESH_RATE)            #Defines the speed the elevator moves per second
                self.elevator_position = x, y                 #Updates the location of the elevator
            else:
                self.queue.popleft()                          #Removes the floor from the elevator queue
                floor = building.array_floors[num_invitation]
                floor.elevator_on_the_way = False
                floor.back_to_original(screen, num_invitation)
                self.time_start = time.perf_counter()
                
       
        






























    # def move_elevator(self, screen, num_invitation, lift, building):
    #     time_end = time.perf_counter() #Checks if two seconds have passed since the elevator reached its destination
    #     if time_end - lift.time_start >= 2:
    #         if lift.start_move == None:
    #             lift.start_move = pygame.time.get_ticks()
    #             x_elevator_position, y_elevator_position = lift.elevator_position
    #             elevator_floor =  (lift.SCREEN_HEIGHT - y_elevator_position)//(lift.FLOOR_HEIGHT + lift.LINE_HEIGHT)
    #             # elevator_floor = lift.position_of_last_floor
    #             lift.time_to_end = abs(elevator_floor - num_invitation) * 500
    #             print(elevator_floor)
    #         past_time = pygame.time.get_ticks() - lift.start_move
            # updates_the_time = lift.time_to_end - past_time 
            # x_elevator_position, y_elevator_position = lift.elevator_position    #Updates the location of the elevator
            # # current_y = lift.SCREEN_HEIGHT - (57 * (num_invitation + 1) - 7)
            # current_y = lift.SCREEN_HEIGHT - num_invitation * (lift.FLOOR_HEIGHT + lift.LINE_HEIGHT) - lift.FLOOR_HEIGHT    # Calculate the location where the elevator should reach 
            # if y_elevator_position != current_y:
            #     if current_y < y_elevator_position:
            #         y_elevator_position = current_y - (updates_the_time / 500) * 57
            #     else:
            #         y_elevator_position = current_y + (updates_the_time / 500) * 57
            #     pygame.draw.line(screen, lift.sky_blue, [x_elevator_position + lift.ELEVATOR_WIDTH/2, lift.SCREEN_HEIGHT], [x_elevator_position + lift.ELEVATOR_WIDTH/2, 0], 70)
            #     screen.blit(lift.elevator_img, (x_elevator_position,y_elevator_position))    #Pastes the image of the elevator
            #     pygame.display.flip()
            #     lift.elevator_position = x_elevator_position, y_elevator_position   #Updates the location of the elevator
            # if y_elevator_position == current_y:
            #     lift.queue.popleft()    #Removes the floor from the elevator queue
            #     floor = building.array_floors[num_invitation]
            #     floor.elevator_on_the_way = False
            #     floor.back_to_original(screen, num_invitation)
            #     lift.time_start = time.perf_counter()
            #     lift.start_move = None





        


    


        





















