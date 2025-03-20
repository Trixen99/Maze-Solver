from cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if self._win is None:
            return
        else:
            self._animate()

    def _create_cells(self):
        self._cells = [[Cell(1,1,1,1,self._win) for col in range(self.num_rows)] for row in range(self.num_cols)]
        for column_number in range(len(self._cells)):
            current_column = self._cells[column_number]
            for cell_number in range(len(current_column)):
                current_cell = current_column[cell_number]
                self._draw_cell(current_cell, column_number, cell_number)

    
    def _draw_cell(self, cell, column_number, row_number):
        x1 = self._x1 + (self.cell_size_x * column_number)
        y1 = self._y1 + (self.cell_size_y * row_number)
        x2 = self._x1 + (self.cell_size_x * (column_number + 1))
        y2 = self._y1 + (self.cell_size_y * (row_number + 1))
        cell._x1 = x1
        cell._x2 = x2
        cell._y1 = y1
        cell._y2 = y2
        cell.draw()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)




        
        

        