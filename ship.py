from tkinter import PhotoImage, Canvas
from health import *

class ship:
    def __init__(self, x, y, canvas, speed = 20):
        self.__canvas = canvas
        self.__xpos = x
        self.__ypos = y
        self.__imagelist = []
        self.__speed = speed
        self.__bang = ""
        self.__imagelist = [PhotoImage(file="images/spaceship.png"), PhotoImage(file="images/exploded_ship.png")]
        self.__currentImg = self.__imagelist[0]
        self.__imgShip = self.__canvas.create_image(self.__xpos,self.__ypos, image = self.__currentImg, anchor="nw")
    def getX(self):
        return self.__xpos
    def getY(self):
        return self.__ypos
    def setX(self, x):
        self.__xpos = x
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def setY(self, y):
        self.__xpos = y
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def getHeight(self):
        return self.__currentImg.height()
    def getWidth(self):
        return self.__currentImg.width()
    def getSpeed(self):
        return self.__speed
    def setSpeed(self, speed):
        self.__speed = speed
    def move(self, x=0, y=0):
        if not self.__bang == "":
            self.__canvas.after(300)
            self.__canvas.delete(self.__bang)
            self.__bang = ""
        self.__xpos += x
        self.__ypos += y
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def setLocation(self, x, y):
        self.__xpos = x
        self.__ypos = y
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def getLocation(self):
        self.__coordinates = [self.getX(), self.getX() + self.getWidth(), self.getY(), self.getY() + self.getHeight()]
        return self.__coordinates
    def explode(self):
        self.__bang = self.__canvas.create_image(self.__xpos,self.__ypos, image= self.__imagelist[1], anchor="nw")
        #self.move()
        #self.__imgShip = self.__canvas.itemconfig(self.__imgShip, image= self.__imagelist[0])
    def is_exploded(self):
        if not self.__bang == "":
            return True
        else:
            return False
