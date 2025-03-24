from pointLine import Point, Line

class Cell:
    def __init__(self, x1=None, y1=None, x2=None, y2=None, window=None, left_wall=True, right_wall=True, bottom_wall= True, top_wall=True):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
        self.walls = []
        self.blank_walls = []
        self.visited = False

    def draw(self):
        def create_wall(x1, y1, x2, y2):
            point1 = Point(x1, y1)
            point2 = Point(x2, y2)
            wall = Line(point1, point2)
            return wall
        
        if self._win is None:
            return
        
        if self.has_top_wall == True:
            top_wall = create_wall(self._x1, self._y1, self._x2, self._y1)
            self.walls.append(top_wall)
        else:
            blank_top_wall = create_wall(self._x1, self._y1, self._x2, self._y1)
            self.blank_walls.append(blank_top_wall)

        
        if self.has_bottom_wall == True:
            bottom_wall = create_wall(self._x1, self._y2, self._x2, self._y2)
            self.walls.append(bottom_wall)
        else:
            blank_bottom_wall = create_wall(self._x1, self._y2, self._x2, self._y2)
            self.blank_walls.append(blank_bottom_wall)


        if self.has_right_wall == True:
            right_wall = create_wall(self._x2, self._y1, self._x2, self._y2)
            self.walls.append(right_wall)
        else:
            blank_right_wall = create_wall(self._x2, self._y1, self._x2, self._y2)
            self.blank_walls.append(blank_right_wall)


        if self.has_left_wall == True:
            left_wall = create_wall(self._x1, self._y1, self._x1, self._y2)
            self.walls.append(left_wall)
        else:
            blank_left_wall = create_wall(self._x1, self._y1, self._x1, self._y2)
            self.blank_walls.append(blank_left_wall)


        for wall in self.walls:
            self._win.draw_line(wall, "black")

        for wall in self.blank_walls:
            self._win.draw_line(wall, "white")
    
    @property
    def middle_coords(self):
        x = ((self._x2 - self._x1) / 2) + self._x1
        y = ((self._y2 - self._y1) / 2) + self._y1
        return x, y


    def draw_move(self, to_cell, undo=False):
        self_middle_x, self_middle_y = self.middle_coords[0], self.middle_coords[1]
        to_cell_middle_x, to_cell_middle_y = to_cell.middle_coords[0], to_cell.middle_coords[1]
        point1 = Point(self_middle_x, self_middle_y)
        point2 = Point(to_cell_middle_x, to_cell_middle_y)
        to_line = Line(point1, point2)
        if undo == False:
            self._win.draw_line(to_line, "red")
        else:
            self._win.draw_line(to_line, "grey")






