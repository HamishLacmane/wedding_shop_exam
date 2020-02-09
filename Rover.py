from common import *

# rover class
class Rover:

    def __init__(self, x, y, direction, planet):
        self.x = x
        self.y = y
        self.direction = direction
        
        #could be for any future planet
        self.planet = planet
    
    # standard getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction
    
    # print current position and direction
    def print_curr_pos(self):
        print("{0} {1} {2}".format(self.get_x(), self.get_y(), self.get_direction()))

    def move_north(self):
        self.y += 1

    def move_east(self):
        self.x += 1

    def move_south(self):
        self.y -= 1

    def move_west(self):
        self.x -= 1

    # check if next move is possible
    def possible(self):
        if self.direction == NORTH:
            if self.y == self.planet.get_max_y():
                return False

        elif self.direction == EAST:
            if self.x == self.planet.get_max_x():
                return False

        elif self.direction == SOUTH:
            if self.y == base_class_min_coord[ROVER_CLASS_KEY]:
                return False

        elif self.direction == WEST:
            if self.x == base_class_min_coord[ROVER_CLASS_KEY]:
                return False

        return True

    # rotate the rover based on the turn dict and instruction
    def rotate(self, instruction):
        self.direction = turn_dict[self.direction][instruction]

    # move forward by one
    def move_forward(self, instruction):

        if instruction != MOVE_FORWARD:
            self.rotate(instruction)
        else:
            if self.possible():
                if self.direction == NORTH:
                    self.move_north()
                elif self.direction == EAST:
                    self.move_east()
                elif self.direction == SOUTH:
                    self.move_south()
                elif self.direction == WEST:
                    self.move_west()
            else:
                print("hit edge, not moving")
