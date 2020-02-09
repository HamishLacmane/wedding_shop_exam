# created using Python 3.7.6 env
# purpose wedding shop exam 
# Author: Hamish Lacmane
'''
Written on windows machine - incase space issues or so

Assumtions:
- rovers do not collide into each other
- when rover hits the boundaries, it does no move for that instrcuction
- input is as per task sheet
- write 'done' into "Input rover start coord and direction e.g. 0 0 N \n or enter 'done':"
  when you are happy with your current rovers set

'''

# setting some permantent/immutable vars
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

LEFT_TURN = 'L'
RIGHT_TURN = 'R'
MOVE_FORWARD = 'M'

# dictionary to save effort or if statement, 
# we can just parse in which way to turn from current direction
# note: the use of already set vars will just set the keys appropriately
# use of this is as follows, based on turn_dict[current_direction][how_to_turn] = resulting direction
turn_dict = {
    NORTH: {
        LEFT_TURN: WEST,
        RIGHT_TURN: EAST
    },
    EAST: {
        LEFT_TURN: NORTH,
        RIGHT_TURN: SOUTH
    },
    SOUTH: {
        LEFT_TURN: EAST,
        RIGHT_TURN: WEST
    },
    WEST: {
        LEFT_TURN: SOUTH,
        RIGHT_TURN: NORTH
    }
}

ROVER_CLASS_KEY = 'ROVER'
GRID_CLASS_KEY = 'GRID'
base_class_min_coord = {
    ROVER_CLASS_KEY: 0,
    GRID_CLASS_KEY: 1
}

# import regex to validate input
import re

# check rover instructions are correct
pattern_rover_instructions = re.compile(r'([LMR])+')

# zeros are dealt with when validating so not checking here
# check grid and rover start input
pattern_grid_input = re.compile(r'^\d+ \d+$')
pattern_rover_start_input = re.compile(r'^\d+ \d+ [NESW]$')


# used in main to convert input appropriately
def convert_input_coords(str_coord_input):
    processing = str_coord_input.split(" ")
    # returns x and y as ints
    return int(processing[0]), int(processing[1])

def convert_rover_start(str_rover_start):
    # we know the last 2 have to be space and dir so this will work
    rover_start_dir = str_rover_start[-1]
    rover_start_coords = str_rover_start[:-2]
    
    x, y = convert_input_coords(rover_start_coords)

    return x, y, rover_start_dir

# method here to use in both rover and grid is done correctly
def validate_x_y(x, y, base_class):
    #if grid is set to size 0,0 then error
    #if rover at any point is less than 0 for either x or y, then error

    if x < base_class_min_coord[base_class]:
        raise ValueError("x cooridinate of " + base_class + " too low / out of bounds")
    if y < base_class_min_coord[base_class]:
        raise ValueError("y cooridinate of " + base_class + " too low / out of bounds")



# grid class - basically the planet class
class Grid:
    def __init__(self, x_length, y_length):
        self.max_x = x_length
        self.max_y = y_length

    #standard getters
    def get_max_x(self):
        return self.max_x
    
    def get_max_y(self):
        return self.max_y


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



def main():
    #get grid size input
    grid_size_input = input("input grid size e.g. 5 5 : ")

    #raise error if input is incorrect
    if not pattern_grid_input.match(grid_size_input):
        raise ValueError("Input to set grid size in incorrect format")
    
    grid_max_x, grid_max_y = convert_input_coords(grid_size_input)
    validate_x_y(grid_max_x, grid_max_y, GRID_CLASS_KEY)

    # create the planet i.e. mars
    mars = Grid(grid_max_x, grid_max_y)

    #list of rovers and instructions
    rovers = []
    rovers_instructions = []
    while True:

        current_rover_start_input = input("Input rover start coord and direction e.g. 0 0 N \n or enter 'done': ")

        # validate input
        if not pattern_rover_start_input.match(current_rover_start_input):

            if current_rover_start_input == "done":
                # break out of while true and make rovers move
                break
            else:
                # input incorrect
                raise ValueError(
                    "Starting input for rover in incorrect format, no trailing or preceeding spaces please"
                )
            
        else:
            
            rover_x, rover_y, rover_dir = convert_rover_start(current_rover_start_input)
            current_rover_instructions_input = input("Input rover instructions e.g. MRMML : ")

            # validate input
            if not pattern_rover_instructions.match(current_rover_instructions_input):
                raise ValueError("Directions input for rover in incorrect format")
            
            #add to rovers
            rovers.append(Rover(rover_x, rover_y, rover_dir, mars))
            rovers_instructions.append(current_rover_instructions_input)
    
    # let the rovers complete instructions
    for i in range(len(rovers)):
        for instruction in rovers_instructions[i]:
            rovers[i].move_forward(instruction)
        
        #print their positions
        rovers[i].print_curr_pos()


if __name__ == "__main__":
    main()