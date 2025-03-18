class Point:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y

class Line:
    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2
    
    def draw(self, canvas, colour):
        x1, y1 = self.__point_1.xcoord, self.__point_1.ycoord
        x2, y2 = self.__point_2.xcoord, self.__point_2.ycoord
        canvas.create_line(x1, y1, x2, y2, fill=colour, width=2)
