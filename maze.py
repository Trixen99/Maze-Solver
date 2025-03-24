from cell import Cell
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
        if self.seed != None:
            random.seed(self.seed)
        self._create_cells()
        
    


    def _create_cells(self):
        self._cells = [[Cell(1,1,1,1,self._win) for col in range(self.num_rows)] for row in range(self.num_cols)]
        for column_number in range(len(self._cells)):
            current_column = self._cells[column_number]
            for cell_number in range(len(current_column)):
                current_cell = current_column[cell_number]
                self._draw_cell(current_cell, column_number, cell_number)

    
    def _draw_cell(self, cell, column_number=None, row_number=None):
        if column_number != None and row_number != None:
            x1 = self._x1 + (self.cell_size_x * column_number)
            y1 = self._y1 + (self.cell_size_y * row_number)
            x2 = self._x1 + (self.cell_size_x * (column_number + 1))
            y2 = self._y1 + (self.cell_size_y * (row_number + 1))
            cell._x1 = x1
            cell._x2 = x2
            cell._y1 = y1
            cell._y2 = y2
            
        cell.draw()
        if self._win == None:
            return
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cells[-1][-1])


    def _break_walls_r(self, i=None, j=None):
        if i == None and j == None:
            i = random.randrange(self.num_cols)
            j = random.randrange(self.num_rows)
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if j + 1 < self.num_cols and self._cells[i][j + 1].visited == False:
                to_visit.append([self._cells[i][j + 1], "bottom"])

            if j - 1 >= 0 and  self._cells[i][j - 1].visited == False:
                to_visit.append([self._cells[i][j - 1], "top"])

            if i + 1 < self.num_rows and self._cells[i + 1][j].visited == False:
                to_visit.append([self._cells[i + 1][j], "right"])
                
            if i - 1 >= 0 and self._cells[i - 1][j].visited == False:
                to_visit.append([self._cells[i - 1][j], "left"])

            if to_visit == []:
                return
            chosen = to_visit[random.randrange(len(to_visit))]
            chosen_cell = chosen[0]
            chosen_direction = chosen[1]
            match chosen_direction:
                case "bottom":
                    chosen_cell.has_top_wall = False
                    self._draw_cell(chosen_cell)
                    current_cell.has_bottom_wall = False
                    self._draw_cell(current_cell)
                    self._break_walls_r(i, j + 1)
                case "top":
                    chosen_cell.has_bottom_wall = False
                    self._draw_cell(chosen_cell)
                    current_cell.has_top_wall = False
                    self._draw_cell(current_cell)
                    self._break_walls_r(i, j - 1)
                case "right":
                    chosen_cell.has_left_wall = False
                    self._draw_cell(chosen_cell)
                    current_cell.has_right_wall = False
                    self._draw_cell(current_cell)
                    self._break_walls_r(i + 1, j)
                case "left":
                    chosen_cell.has_right_wall = False
                    self._draw_cell(chosen_cell)
                    current_cell.has_left_wall = False
                    self._draw_cell(current_cell)
                    self._break_walls_r(i - 1, j)
                    

            
    def _reset_cells_visited(self):
        for maze_column in self._cells:
            for cell in maze_column:
                cell.visited = False

    def solve(self):
        if self._solve_r(0,0) == True:
            return True
        return False
    
    def _solve_r(self, i, j, came_from=None):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._cells[-1][-1]:
            return True
        
        if current_cell.has_top_wall == False and came_from != None and self._cells[i][j - 1] != came_from:
            current_cell.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1, current_cell) == True:
                return True
            current_cell.draw_move(self._cells[i][j - 1], True)

        if current_cell.has_bottom_wall == False and self._cells[i][j + 1] != came_from:
            current_cell.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1, current_cell) == True:
                return True
            current_cell.draw_move(self._cells[i][j + 1], True)

        if current_cell.has_left_wall == False and self._cells[i - 1][j] != came_from:
            current_cell.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j, current_cell) == True:
                return True
            current_cell.draw_move(self._cells[i - 1][j], True)
        
        if current_cell.has_right_wall == False and self._cells[i + 1][j] != came_from:
            current_cell.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j, current_cell) == True:
                return True
            current_cell.draw_move(self._cells[i + 1][j], True)
        
        return False








        




        
        

        