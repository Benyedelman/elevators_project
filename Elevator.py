import pygame
import numpy


class Elevator:
    def __init__(self):
        self.NUM_FLOORS = 10
        self.ELEVATOR_IMAGE = "elv(1).png"
        self.elevator_img = pygame.image.load(self.ELEVATOR_IMAGE)
        self.SCREEN_WIDTH = 750
        self.ELEVATOR_WIDTH = 64
        self.FLOOR_WIDTH = 140
        self.LINE_HEIGHT = 7
        self.FLOOR_HEIGHT = 50
        self.SCREEN_HEIGHT = (self.FLOOR_HEIGHT + self.LINE_HEIGHT) * self.NUM_FLOORS - self.LINE_HEIGHT
        self.elevator_position = 0
        self.val = 5
        self.sky_blue = (135, 206, 235)
        self.clock = pygame.time.Clock()
        self.REFRESH_RATE = 111
        self.timer = 0
        # self.array_possibility = []

    def elevators_builder(self, lift_num, screen):
        x = self.FLOOR_WIDTH + lift_num * self.ELEVATOR_WIDTH 
        y = self.SCREEN_HEIGHT - self.FLOOR_HEIGHT 
        screen.blit(self.elevator_img, (x, y))
        self.elevator_position = x, y
        pygame.display.flip()

    def choose_an_elevator(self, building, Invitation):
        for i in range(len(building.array_elevators)):
            possibility = building.array_elevators[i]
            x2, y2 = possibility.elevator_position
            y2 = (possibility.SCREEN_HEIGHT - y2)//(possibility.FLOOR_HEIGHT + possibility.LINE_HEIGHT)
            z = abs(Invitation - y2)
            building.array_possibility.append(z)
        min_value = min(building.array_possibility)
        min_index = building.array_possibility.index(min_value)
        building.array_possibility.clear()
        return min_index, min_value 

            

    def move_elevator(self, screen, num_Invitation, building):
        min_index, min_value  = Elevator.choose_an_elevator(self, building, num_Invitation)
        lift = building.array_elevators[min_index]
        self.timer(min_value, num_Invitation, screen)
        x, y = lift.elevator_position
        pygame.display.flip()
        new_y = lift.SCREEN_HEIGHT - num_Invitation * (lift.FLOOR_HEIGHT + lift.LINE_HEIGHT) - lift.FLOOR_HEIGHT 
        while y != new_y:
            if new_y < y:
                y -= 1
            else:
                y +=1
            pygame.draw.line(screen, lift.sky_blue, [x + lift.ELEVATOR_WIDTH/2, lift.SCREEN_HEIGHT], [x + lift.ELEVATOR_WIDTH/2, 0], 70)
            screen.blit(lift.elevator_img, (x,y))
            pygame.display.flip()
            lift.clock.tick(lift.REFRESH_RATE)
            # Elevator.set_current_floor(y)
            lift.elevator_position = x, y
       
        


            

     






# class ManagerElevators:
#     def __init__(self):  
#         self.__ring = "/home/beny/Downloads/ding.mp3"
#         self.__time = 0
#         self.__num_elevators = 0                           #??????????????
#         self.__location_elevator = 0                         #????????????
#         self.__list_actions = 0
#         self.__array_elevators = []
#         self.__queue = deque()
#         self.__array_elevators_time = []

#     def elevators_time(self, num_elevators):
#         for lift in range(1, num_elevators + 1):  
#             self.array_elevators_time.append(0)

                              
#     def manager(self, invitation):
#         for lift in range(len(self.array_elevators_time)):
#             time_try = self.array_elevators_time[lift] +  abs((invitation - self.location_elevator) / 2)


#         self.time = abs((invitation - self.location_elevator) / 2) + self.list_actions

#         self.list_actions += self.time

#         self.location_elevator = invitation            #                            עד שהמעלית תגיע להוסיף את הזמן עצמו

#     def insert_queue(self):
#         self.queue.append('invitation')

#     def remove_queue(self):
#         self.queue.popleft()

        
    # def go_up(self):

    # def go_down(self):






        


    


        





















