from tkinter import PhotoImage, Canvas
import random

class asteroids:
    def __init__(self, x, y, canvas, speed=50):
        self.__canvas = canvas
        self.__xpos = x
        self.__ypos = y
        self.__imagelist = []
        self.__speed = speed
        self.__asteroidlist = [PhotoImage(file="images/asteroid0.png"), PhotoImage(file="images/asteroid1.png"), PhotoImage(file="images/asteroid2.png")] 
        self.__explodeylist = [PhotoImage(file="images/explosion0.png"), PhotoImage(file="images/explosion1.png"), PhotoImage(file="images/explosion2.png")]
        self.__size = random.randint(0,2)
        self.__asteroidImage = self.__canvas.create_image(x,y,image=self.__asteroidlist[self.__size])


    def getLocation(self):
        self.coordinates = [self.__xpos, self.__xpos + self.__asteroidlist[self.__size].width(), self.__ypos, self.__ypos + self.__asteroidlist[self.__size].height()]
        return self.coordinates
