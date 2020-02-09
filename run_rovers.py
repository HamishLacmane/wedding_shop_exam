'''
# created using Python 3.7.6 env
# purpose wedding shop exam 
# Author: Hamish Lacmane
Written on windows machine - incase space issues or so

Assumtions:
- rovers do not collide into each other
- when rover hits the boundaries, it does no move for that instrcuction
- input is as per task sheet
- write 'done' into "Input rover start coord and direction e.g. 0 0 N \n or enter 'done':"
  when you are happy with your current rovers set

'''

from Rover import Rover
from Grid import Grid
# for exam purpose we will do this and time limit but in future should explicitly import each one
from common import *
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