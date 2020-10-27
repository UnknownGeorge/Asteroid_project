from tkinter import *

class Game():
    def __init__(self, canvas, root, asteroidship, beam, background_list):
        self.background_list =background_list
        self.canvas = canvas
        self.root = root
        self.asteroidship = asteroidship
        self.beam = beam
        root.bind('<KeyPress>',  self.onkeypress)
        root.bind('<Button-1>', self.onmouse)
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
        self.beam.shoot(self.asteroidship.getX(), self.asteroidship.getY())
        #Shoot the bullet :D
    def checkCollision(self, event):
        pass
    def exit_program(self):
        quit()
