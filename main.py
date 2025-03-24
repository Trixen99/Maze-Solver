from window import *
from pointLine import *
from cell import *
from maze import *


win = Window(1000, 1000)
my_maze = Maze(10,10,35,35,25,25,win)
my_maze._break_entrance_and_exit()
my_maze._break_walls_r()
my_maze._reset_cells_visited()
#my_maze._cells[0][0].draw_move(my_maze._cells[-1][-1])
my_maze.solve()
#my_cell = Cell(win, 200,200,400,400)
#my_cell2 = Cell(win, 400,200,600,400)
#my_cell.draw()
#my_cell2.draw()
#my_cell.draw_move(my_cell2)
win.wait_for_close()
