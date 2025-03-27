from window import *
from pointLine import *
from cell import *
from maze import *

width, height = 1000, 1000
num_rows = 30
num_cols = 10
win = Window(width, height)
size = win.screen_size(num_rows, num_cols)
print(size)

#######Maze(x1,y1,num_rows,num_cols,cell_size_x,cell_size_y=, win, seed)
my_maze = Maze(10,10,num_rows,num_cols,size[1],size[0],win, seed=22255552)
my_maze._break_entrance_and_exit()
my_maze._break_walls_r()
my_maze._reset_cells_visited()
my_maze.solve()
#print(screen_size())
#my_maze._cells[0][0].draw_move(my_maze._cells[-1][-1])
#
#my_cell = Cell(win, 200,200,400,400)
#my_cell2 = Cell(win, 400,200,600,400)
#my_cell.draw()
#my_cell2.draw()
#my_cell.draw_move(my_cell2)
win.wait_for_close()
