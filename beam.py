from tkinter import *

class Beam():
    def __init__(self, canvas, img="images/laserbeam_red.png"):
        self.canvas = canvas
        self.img = PhotoImage(file=img)
        self.x = 0
        self.y = 0
        self.speed = speed = 10
        self.shot = 0
        self.is_there = False
    def shoot(self, x, y, speed = 10):
        if self.is_there == False:
            self.x = x
            self.y = y
            self.speed = speed
            self.shot = self.canvas.create_image(self.x, self.y, image = self.img)
            self.is_there =True
            self.move()
        else:
            pass

    def move(self):
        if self.is_there == True:
            self.x += 1
            self.canvas.coords(self.shot, self.x, self.y)
            mover = self.canvas.after(self.speed, lambda:self.move())
        else:
            pass
