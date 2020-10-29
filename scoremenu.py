from tkinter import *
from GameFunc import exit_program

class scoremenu:
    def __init__(self, Game):
        self.Game = Game
        self.menu = Toplevel()
        self.menu.title("Main Menu")
        self.menu.protocol('WM_DELETE_WINDOW', lambda:self.Game.exit_program())
        self.imgBackground = PhotoImage(file='images/space_background.png')
        self.menu.config(padx=10, background="black")
        self.canvas = Canvas(self.menu, width=self.imgBackground.width(), height=self.imgBackground.height())
        self.menu.geometry("%dx%d+%d+%d" % (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.menu.winfo_screenwidth()//2 - self.canvas.winfo_reqwidth() //2, self.menu.winfo_screenheight()//2- self.canvas.winfo_reqheight() // 2))
        self.menu.grab_set()
        self.canvas.pack()