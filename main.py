from window import *
from pointLine import *


win = Window(800, 600)
line1_point_1 = Point(400, 200)
line1_point_2 = Point(300, 200)
line1 = Line(line1_point_1, line1_point_2)

line2_point_1 = Point(400, 200)
line2_point_2 = Point(400, 100)
line2 = Line(line2_point_1, line2_point_2)

line3_point_1 = Point(300, 200)
line3_point_2 = Point(300, 100)
line3 = Line(line3_point_1, line3_point_2)

line4_point_1 = Point(300, 100)
line4_point_2 = Point(400, 100)
line4 = Line(line4_point_1, line4_point_2)

lines = [line1, line2, line3, line4]

for line in lines:
    win.draw_line(line, "black")
win.wait_for_close()