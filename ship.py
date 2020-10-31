from tkinter import PhotoImage, Canvas
from health import *
import random
import pygame

class ship:
    def __init__(self, x, y, canvas, speed = 20):
        '''
        Initializes elements of the ship class.

        PARAMETERS:
        -----------
        xpos: int
            x location of the ship.
        ypos: int
            y location of the ship.
        speed: int
            Travelling speed of the ship.
        imagelist: list
            List of images for the spaceship.
        bang: str -> img
            Is empty, but will contain the img of the blown up ship.
        imgShip: img
            Contains the image of the ship and creates an object with that image at a specific location.
        currentImg: img
            Contains the current image that the ship should have.
        canvas: canvas object
            Is the canvas containing the images and objects.
        '''
        self.__canvas = canvas
        self.__xpos = x
        self.__ypos = y
        self.__speed = speed
        self.__bang = ""
        self.__imagelist = [PhotoImage(file="images/spaceship.png"), PhotoImage(file="images/exploded_ship.png")]
        self.__currentImg = self.__imagelist[0]
        self.__imgShip = self.__canvas.create_image(self.__xpos,self.__ypos, image = self.__currentImg, anchor="nw")
    def getX(self):
        '''
        Gets the xposition of the ship.

        RETURNS:
        --------
        int
            The x position of the ship.
        '''
        return self.__xpos
    def getY(self):
        '''
        Gets The xposition of the ship.

        RETURNS:
        --------
        int
            The y position of the ship.
        '''
        return self.__ypos
    def setX(self, x):
        '''
        Sets the x position of the ship.


        PARAMETERS:
        --------
        xpos: int
            The x position of the ship.
        canvas: canvas object
            The canvas containing the images & objects.
        '''
        self.__xpos = x
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def setY(self, y):
        '''
        Sets the y position of the ship.


        PARAMETERS:
        --------
        xpos: int
            The y position of the ship.
        canvas: canvas object
            The canvas containing the images & objects.
        '''
        self.__xpos = y
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def getHeight(self):
        '''
        Gets the Height of the ship.

        RETURNS:
        --------
        int
            the Height of the ship.
        '''
        return self.__currentImg.height()
    def getWidth(self):
        '''
        Gets the Width of the ship.

        RETURNS:
        --------
        int
            The Width position of the ship.
        '''
        return self.__currentImg.width()
    def getSpeed(self):
        '''
        Gets speed of the ship.

        RETURNS:
        --------
        int
            The speed of the ship.
        '''
        return self.__speed
    def setSpeed(self, speed):
        '''
        Sets the speed of the ship.

        PARAMETERS:
        --------
        speed: int
            The speed of the ship:
        '''
        self.__speed = speed
    def move(self, x=0, y=0):
        '''
        Moves the ship and checks if the ship has been exploded, then deletes the explosion image

        PARAMETERS:
        --------
        xpos: int
            The x position of the ship.
        ypos: int
            The y position of the ship.
        canvas: canvas object
            The canvas containing the images & objects.
        bang: img
            Contains the image of the explosion
        '''
        if not self.__bang == "":
            return
        else:
            self.__xpos += x
            self.__ypos += y
            self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def setLocation(self, x, y):
        '''
        Sets the Location of the ship.

        PARAMETERS:
        --------
        xpos: int
            The x position of the ship.
        ypos: int
            The y position of the ship.
        canvas: canvas object
            The canvas containing the images and objects.
        '''
        self.__xpos = x
        self.__ypos = y
        self.__canvas.coords(self.__imgShip, self.__xpos, self.__ypos)
    def getLocation(self):
        '''
        Gets the Location of the ship.

        PARAMETERS:
        --------
        coordinates: list
            Contains a list of all the coordinates needed

        RETURNS:
        -------
        coordinates
            contains all the coordinates
        '''
        self.__coordinates = [self.getX(), self.getX() + self.getWidth(), self.getY(), self.getY() + self.getHeight()]
        return self.__coordinates
    def explode(self):
        '''
        Creates an image of an explosion and play sound of explosion.

        PARAMETERS:
        -----------
        explodyNoise: int
            random number that determines which acursed sound plays
        audioFiles: list
            lists audiofiles for exploding "sounds"
        explodySound: list/Sound
            lists soundFiles for exploding "sounds:
        baaam: int
            not really a parameter, but just a reminder that george didn't like zoom because zoom was
            "too cringe". zoom is cool
        xpos: int
            the x position of the ship
        ypos: int
            the y position of the ship
        imagelist: list
            contains the list of all the images for the ship
        '''
        self.__bang = self.__canvas.create_image(self.__xpos + 10,self.__ypos - 20, image= self.__imagelist[1], anchor="nw")
        # Cue Acursed Noises
        pygame.mixer.init()
        self.explodyNoise = random.randint(0,4)
        self.audioFiles = ['Audio_Files/booom1.ogg','Audio_Files/booom2.ogg','Audio_Files/booom3.ogg',
        'Audio_Files/booom4.ogg','Audio_Files/booom5.ogg']
        self.explodySound = [0] * 5
        for baaam in range(len(self.explodySound)):
            self.explodySound[baaam] = pygame.mixer.Sound(self.audioFiles[baaam])
        pygame.mixer.Sound.play(self.explodySound[self.explodyNoise])
        self.__canvas.update()
    def is_exploded(self):
        '''
        Checks if the user has exploded or not, then returns a value to check

        PARAMETERS:
        ----------
        bang: img
            contains an image of the exploded ship

        RETURNS:
        -------
        true/false: boolean
            just returns either true or false back to the line that called this
        '''
        if not self.__bang == "":
            return True
        else:
            return False
