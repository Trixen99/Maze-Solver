#Import the required Libraries
from tkinter import *
from tkinter import ttk

class input_window():
    def __init__(self):
        self.win = Tk()
        self.win.title("Input Width")
        self.win.geometry("720x250")
        width_label = Label(self.win, text="Screen Width")
        width_label.pack()
        self.entry = Entry(self.win, font=('MS_Sans_Serif'), width=20)
        self.entry.pack()

        self.width = None
        
        height_label = Label(self.win, text="Screen Height")
        height_label.pack()

        self.entry2 = Entry(self.win, font=('MS_Sans_Serif'), width=20)
        self.entry2.pack()

        height_label = Label(self.win, text="Rows")
        height_label.pack()

        self.entry3 = Entry(self.win, font=('MS_Sans_Serif'), width=20)
        self.entry3.pack()

        height_label = Label(self.win, text="Columns")
        height_label.pack()

        self.entry4 = Entry(self.win, font=('MS_Sans_Serif'), width=20)
        self.entry4.pack()

        button = ttk.Button(self.win, text="Continue",width=20, command= self.close_window)
        button.pack()

        self.win.mainloop()



    def close_window(self):
        self.width = int(self.entry.get())
        self.height = int(self.entry2.get())
        self.rows = int(self.entry3.get())
        self.columns = int(self.entry4.get())
        self.win.destroy()


        

        

