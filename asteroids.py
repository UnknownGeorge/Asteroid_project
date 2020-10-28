from tkinter import PhotoImage, Canvas

class asteroids:
    def __init__(self, x, y, canvas, speed=50):
        self.__canvas = canvas
        self.__xpos = x
        self.__ypos = y
        self.__imagelist = []
        self.__speed = speed
        self.__imagelist = [PhotoImage(file="images/asteroid0.png"), PhotoImage(file="images/asteroid1.png"), PhotoImage(file="images/asteroid2.png"), 
            PhotoImage(file="images/explosion0.png"), PhotoImage(file="images/explosion1.png"), PhotoImage(file="images/explosion2.png")]
        self.__asteroidlist = [0] * 21


    