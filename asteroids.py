from tkinter import PhotoImage, Canvas
import random

class asteroids:
    def __init__(self, x, y, canvas, speed=50):
        self.__canvas = canvas
        self.__imagelist = []
        self.__speed = speed
        self.__asteroidlist = [PhotoImage(file="images/asteroid0.png"), PhotoImage(file="images/asteroid1.png"), PhotoImage(file="images/asteroid2.png")]
        self.__explodeylist = [PhotoImage(file="images/explosion0.png"), PhotoImage(file="images/explosion1.png"), PhotoImage(file="images/explosion2.png")]
        self.__size = random.randint(0,2)
        self.__xpos =  x
        self.__ypos = y
        self.__mxpos = self.__xpos
        self.__mypos = self.__ypos
        self.__asteroidImage = self.__canvas.create_image(x,y,image=self.__asteroidlist[self.__size], anchor="nw")
        #self.move()

    def set_pos(self, x = 0, y = 0):
        if not x == 0:
            self.__xpos = x
        if not y == 0:
            self.__ypos = y
        self.__mxpos = self.__xpos
        self.__mypos = self.__ypos
        self.__canvas.coords(self.__asteroidImage, self.__xpos, self.__ypos)
    def getLocation(self):
        self.coordinates = [self.__xpos, self.__xpos + self.__asteroidlist[self.__size].width(), self.__ypos, self.__ypos + self.__asteroidlist[self.__size].height()]
        return self.coordinates
    def move(self):
        self.__xpos -=10
        self.__canvas.coords(self.__asteroidImage, self.__xpos, self.__ypos)
    def health(self):
        self.__size -= 1
        if not self.__size == -1:
            self.__asteroidImage = self.__canvas.create_image(self.__xpos,self.__ypos,image=self.__asteroidlist[self.__size], anchor="nw")
        else:
            self.__asteroidImage = self.__canvas.create_image(self.__xpos,self.__ypos,image=self.__explodeylist[self.__size], anchor="nw")
            self.__canvas.after(1000, self.remake)

    def remake(self):
        self.__xpos = self.__mxpos
        self.__ypos = self.__mypos
        self.__size = random.randint(0,2)
        self.__asteroidImage = self.__canvas.create_image(self.__xpos,self.__ypos,image=self.__asteroidlist[self.__size], anchor="nw")
