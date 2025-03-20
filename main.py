from window import *
from pointLine import *
from cell import *
from maze import *


win = Window(800, 600)
my_maze = Maze(10,10,4,4,100,100,win)
#my_cell = Cell(win, 200,200,400,400)
#my_cell2 = Cell(win, 400,200,600,400)
#my_cell.draw()
#my_cell2.draw()
#my_cell.draw_move(my_cell2)
win.wait_for_close()
