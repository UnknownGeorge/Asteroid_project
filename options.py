from GameFunc import *
from beam import *
from ship import *
from health import *
from tkinter import *

class options:
    def __init__(self, options_menu):
        self.menu = options_menu
        self.__speedoption = 20
        self.__healthoption = 10
        self.__bulletoption = 5

        self.lblSpeed = Label(self.menu, width=40, font=('Arial', 14), anchor="c", text="Set the speed you want your character to move at:", bg="black", fg="white")
        self.lblSpeed.place(x=self.menu.winfo_reqwidth() * 2 - self.lblSpeed.winfo_reqwidth() // 2 - 100, y=self.menu.winfo_reqheight() // 2)
        self.entrySpeed = Entry(self.menu, width=12, font=('Arial', 10), justify='center', borderwidth=5, relief='flat')
        self.entrySpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() * 2, y=self.menu.winfo_reqheight() // 2)
        self.btnSetSpeed = Button(self.menu, width=12, font=('Arial', 10), justify='center', borderwidth=5, relief='flat', text="OK", command=lambda:self.setSpeedShip())
        self.btnSetSpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.btnSetSpeed.winfo_reqwidth() , y=self.menu.winfo_reqheight() // 2 + 50)


    def setSpeedShip(self):
        Game.getAsteroidship().setSpeed(self.entrySpeed.get())

