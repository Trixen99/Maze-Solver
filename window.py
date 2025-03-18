from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("hello")
        self.__canvas = Canvas(master=self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()



    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()



    def close(self):
        self.__running = False


    def draw_line(self, line, colour):
        line.draw(self.__canvas, colour)



    