from tkinter import *

class health:
    def __init__(self, canvas, x, y):
        self.__xpos = x
        self.__ypos = y
        self.__canvas = canvas
        self.__imgList = [PhotoImage(file="images/health0.png"), PhotoImage(file="images/health1.png"), PhotoImage(file="images/health2.png"), 
            PhotoImage(file="images/health3.png"), PhotoImage(file="images/health4.png"), PhotoImage(file="images/health5.png"), 
            PhotoImage(file="images/health6.png"), PhotoImage(file="images/health7.png"), PhotoImage(file="images/health8.png"), 
            PhotoImage(file="images/health9.png"), PhotoImage(file="images/health10.png"), ]
        self.__currentImg = self.__imgList[0]
        self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, image =self.__currentImg, anchor="nw")
    def getX(self):
        return self.__xpos
    def getY(self):
        return self.__ypos
    def getHeight(self):
        return self.__currentImg.height()
    def getWidth(self):
        return self.__currentImg.widht()
    def setX(self, x):
        self.__xpos = x
        self.__canvas.coords(self.__imgHealth, self.__xpos, self.__ypos)
    def setY(self, y):
        self.__ypos = y
        self.__canvas.coords(self.__imgHealth, self.__xpos, self.__ypos)
    def setImage(self, num):
        self.__currentImg = self.__imgList[num]
    def getLocation(self):
        self.__coordinates = [self.getX(), self.getX() + self.getWidth(), self.getY(), self.getY() + self.getHeight()]
        return self.__coordinates
