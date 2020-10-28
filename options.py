from GameFunc import *
from beam import *
from ship import *
from health import *
from tkinter import *

class options:
    def __init__(self, options_menu):
        self.__speedoption = 20
        self.__healthoption = 10
        self.__bulletoption = 5
        # self.entrySpeed = Entry(options_menu, width=12, font=('Century Gothic', 10, 'bold'), justify='center', borderwidth=5, relief='flat')

    def setSpeed(self):
        Game.getAsteroidship().setSpeed(self.entrySpeed.get())

