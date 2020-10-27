from tkinter import *
from ship import *
from beam import *

class Game():
    def __init__(self, canvas, root, background_list):
        self.canvas = canvas
        self.root = root
        self.background_list =background_list

        #binds for key presses
        root.bind('<KeyPress>',  self.onkeypress)
        root.bind('<Button-1>', self.onmouse)

        #create a call to run the other classes
        self.asteroidship = ship(0, 0, self.canvas)

        #create vars that will be used in this class
        self.beam_num = 5
        self.beam_avalible = []

        #run setup functions
        self.__beams()
    def __beams(self):
        for i in range(self.beam_num):
            self.beam_avalible.append(Beam(self.canvas))
    def onkeypress(self, event):
        if event.char == "w":
            self.asteroidship.move(y=-20)
        elif event.char == "a":
            self.asteroidship.move(x=-20)
        elif event.char == "s":
            self.asteroidship.move(y=20)
        elif event.char == "d":
            self.asteroidship.move(x=20)
    def onmouse(self, event):
        print("casualty")
        self.beam_num -= 1
        self.beam_avalible[self.beam_num].shoot(self.asteroidship.getX(), self.asteroidship.getY())
        #Shoot the bullet :D
    def checkCollision(self, event):
        pass

    def game_time(self):
        for i in self.beam_avalible:
            pos = i.get_pos()
            if pos[0]:
                pass


        root.after(1, self.game_time)
    def exit_program(self):
        quit()
