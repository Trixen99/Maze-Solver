#Import the required Libraries
from tkinter import *
from tkinter import ttk
class input_window():
    def __init__(self):
        self.win = Tk()
        self.win.title("Input Width")
        self.win.geometry("720x250")
        self.entry = Entry(self.win, font=('MS_Sans_Serif'), width=20)
        self.entry.pack()
        self.width = None
        button = ttk.Button(self.win, text="Continue",width=20, command= self.close_window)
        button.pack()
        self.win.mainloop()




    def close_window(self):
        self.width = self.entry.get()
        self.win.destroy()


        

        

