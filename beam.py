from tkinter import *

class Beam():
    def __init__(self, canvas, img="images/laserbeam_red.png"):
        self.canvas = canvas
        self.img = PhotoImage(file=img)
        self.x = 0
        self.y = 0
        self.speed = 20
        self.shot =0
        self.is_there = False
        self.inside()

    def shoot(self, x, y, speed = 20):
        if self.is_there == False:
            self.x = x+20
            self.y = y
            self.speed = speed
            self.shot = self.canvas.create_image(self.x, self.y, image = self.img, anchor="ne")
            self.is_there =True
            self.move()
        else:
            pass

    def move(self):
        if self.is_there == True:
            self.x += 10
            self.canvas.coords(self.shot, self.x, self.y)
            mover = self.canvas.after(self.speed, lambda:self.move())

        else:
            pass

    def get_pos(self):
        pos = [self.x, self.y, self.x+self.img.width(), self.y+self.img.height()]
        return pos

    def inside(self):
        if self.is_there:
            pos = self.get_pos()
            if pos[0]>= self.canvas.winfo_reqwidth():
                self.canvas.delete(self.shot)
                self.is_there = False

        self.canvas.after(100, self.inside)
