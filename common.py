
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