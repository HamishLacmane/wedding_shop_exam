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