
import pygame
from collections import deque
import time
from Saving_constant_values import *


class Elevator:
    def __init__(self):
        self.ny_queue = deque()
        self.SCREEN_HEIGHT = 0
        self.elevator_position = 0
        self.finish_time = 0
        self.time_start = 0
        self.position_of_last_floor = 0
        self.start_move = None
        self.start_timer_finish_time = None
        self.time_to_end = 0

    # Starts the stopwatch to finish time
    def stopwatch_for_finish_time(self):
        if self.start_timer_finish_time == None:                                                   # Checks if this is the first iteration
            self.start_timer_finish_time = time.time()                                             
        elif self.finish_time > 0:
            self.finish_time -= time.time() - self.start_timer_finish_time
            self.start_timer_finish_time = time.time()     
        else:
            self.start_timer_finish_time = None

    # Builds all the elevators
    def elevators_builder(self, SCREEN_HEIGHT, lift_num, screen):
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        x = FLOOR_WIDTH + lift_num * ELEVATOR_WIDTH + 5
        y = self.SCREEN_HEIGHT - FLOOR_HEIGHT 
        screen.blit(elevator_img, (x, y))                                                          # Pastes the image of the elevator
        self.elevator_position = x, y                                                              # Saves the location of the elevator
        pygame.display.flip()

    # Moves the elevator according to the amount of time left to reach the destination on time
    def move_elevator(self, screen, floor_num, floor):
        time_end = time.time()                                                                     # Checks if two seconds have passed since the elevator reached its destination
        if time_end - self.time_start >= two_seconds:
            if self.start_move == None:                                                            # If this is the first iteration of the elevator, 
                self.calculates_the_time(floor_num)                                                # it updates start_move, and calculates the time it will take for the elevator to arrive.
            past_time = time.time() - self.start_move                                              # Calculates the time that has already passed
            updates_the_time = self.time_to_end - past_time                                        # Updates the remaining time
            x_elevator_position, y_elevator_position = self.elevator_position                      # Updates the location of the elevator
            target_y = self.SCREEN_HEIGHT - (Total_floor_height * (floor_num + 1) - LINE_HEIGHT)
            if y_elevator_position != target_y:                                                    # If the elevator has not yet reached its destination
                if target_y > y_elevator_position:
                    new_y = target_y - Total_floor_height * (updates_the_time / 0.5)
                    y_elevator_position = new_y if new_y <= target_y else target_y                 # A computer with the new_y took the place of target_y
                else:
                    new_y = target_y + Total_floor_height * (updates_the_time / 0.5)               # A computer with the new_y took the place of target_y
                    y_elevator_position = new_y if new_y >= target_y else target_y
                self.updates_the_location_of_the_elevator(x_elevator_position, y_elevator_position, screen)
            else:
                self.update_the_end_of_operations(floor, screen, floor_num)

    # Calculates the time the elevator needs to move so that each floor has a time of two seconds
    def calculates_the_time(self, floor_num):
        self.start_move = time.time()
        y_elevator_position = self.elevator_position[1]
        elevator_floor =  (self.SCREEN_HEIGHT - y_elevator_position)//Total_floor_height
        self.time_to_end = abs(elevator_floor - floor_num) / 2                                     # calculates the time it will take for the elevator to arrive

    # Updates the elevator on the screen in the new location, and saves the location of the elevator
    def updates_the_location_of_the_elevator(self, x_elevator_position, y_elevator_position, screen):
        pygame.draw.line(screen, sky_blue, [x_elevator_position + ELEVATOR_WIDTH/2, self.SCREEN_HEIGHT], [x_elevator_position + ELEVATOR_WIDTH/2, start_screen], width_elevator)
        screen.blit(elevator_img, (x_elevator_position,y_elevator_position))                       # Pastes the image of the elevator
        pygame.display.flip()
        self.elevator_position = x_elevator_position, y_elevator_position                          # Updates the location of the elevator

    # When the elevator reached its destination, it updates the queue, and the class of the floor
    def update_the_end_of_operations(self, floor,  screen, floor_num):
        self.ny_queue.popleft()                                                                    # Removes the floor from the elevator queue
        floor.back_to_original(screen, floor_num)
        self.time_start = time.time()
        self.start_move = None




        


    


        





















