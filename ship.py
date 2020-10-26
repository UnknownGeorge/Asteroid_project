from tkinter import PhotoImage

class ship:
    def __init__(self, x, y, canvas, speed = 20):
        self.__canvas = canvas
        self.__xpos = x
        self.__ypos = y
        self.__imagelist = []
        self.__speed = speed
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
    def setSpeed(self, speed):
        self.__speed = speed
    def move(self, x=1, y=1):
        self.__xpos += x
        self.__ypos += y
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def setLocation(self, x, y):
        self.__xpos = x
        self.__ypos = y
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    
