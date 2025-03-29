from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze")
        self.__canvas = Canvas(master=self.__root, width=width, height=height, bg="white")
        self.__canvas.pack(fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def screen_size(self, num_rows, num_cols):
        remaining_height = (self.height - 20) % num_rows
        remaining_width = (self.width - 20) % num_cols
        cell_row_size = ((self.width - 20) // num_rows) + (remaining_height // 2)
        cell_column_size = ((self.height - 20) // num_cols) + (remaining_width // 2)
        print(remaining_height)
        print(remaining_width)
        print(f"cell row size {cell_row_size}")
        print(f"cell column size {cell_column_size}")
        return cell_row_size, cell_column_size

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()



    def close(self):
        self.__running = False


    def draw_line(self, line, colour):
        line.draw(self.__canvas, colour)
        self.redraw()



    