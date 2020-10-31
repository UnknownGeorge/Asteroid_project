# Import tkinter module
from tkinter import *

class health:
    def __init__(self, canvas, max = 10):

        '''
        initializes elements of the health class
        PARAMETERS:
        -----------
        imgList_health: list
            list containing images of the health bars
        imgList_lives: list
            list containing images of the remaining lives
        max_health: int
            maximum amount of health the user can have
        lives: int
            number of lives the user has
        curremtImg_health: PhotoImage
            Image of the current number of hitpoints the user has remaining
        currentImg_lives: PhotoImage
            Image of the current number of lives the user has remaining
        xpos: int
            xposition of the images
        ypos: int
            yposition of the images
        '''
        self.__canvas = canvas
        self.__imgList_health = [PhotoImage(file="images/health0.png"), PhotoImage(file="images/health1.png"), 
            PhotoImage(file="images/health2.png"), PhotoImage(file="images/health3.png"), 
            PhotoImage(file="images/health4.png"), PhotoImage(file="images/health5.png"), 
            PhotoImage(file="images/health6.png"), PhotoImage(file="images/health7.png"), 
            PhotoImage(file="images/health8.png"), PhotoImage(file="images/health9.png"), 
            PhotoImage(file="images/health10.png"), ]
        self.__imgList_lives = [PhotoImage(file = "images/lives1.png"),
            PhotoImage(file = "images/lives2.png"),PhotoImage(file = "images/lives3.png")]
        self.max_health = max
        self.health = self.max_health
        self.lives = 2
        self.__currentImg_health = self.__imgList_health[self.health]
        self.__currentImg_lives= self.__imgList_lives[self.lives]
        self.__xpos = canvas.winfo_reqwidth()-50
        self.__ypos = self.__imgList_health[0].height()
        self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, 
            image =self.__currentImg_health, anchor="ne")
        self.__imgLives = self.__canvas.create_image(self.__xpos, self.__ypos+20, 
            image =self.__currentImg_lives, anchor="ne")
    
    def getX(self):
        '''
        Returns the x position of the health bar
        RETURNS:
        --------
        int
            The x position of the health bar
        '''
        return self.__xpos
    
    def getY(self):
        '''
        Returns the y position of the health bar
        RETURNS:
        --------
        int
            The y position of the health bar
        '''
        return self.__ypos
    
    def getHeight(self):        
        '''
        Returns the height of the health bar image
        RETURNS:
        --------
        int
            The height of the health bar image
        '''
        return self.__currentImg_health.height()
    
    def getWidth(self):
        '''
        Returns the width of the health bar image
        RETURNS:
        --------
        int
            The width of the health bar image
        '''
        return self.__currentImg_health.width()
    
    def setX(self, x):
        '''
        Sets the x-position of the health bar
        PARAMETERS:
        -----------
        xpos: int
            The x-position of the health bar
        '''
        self.__xpos = x
        self.__canvas.coords(self.__imgHealth, self.__xpos, self.__ypos)
    
    def setY(self, y):
        '''
        Sets the y-position of the health bar
        PARAMETERS:
        -----------
        ypos: int
            The y-position of the health bar
        '''        
        self.__ypos = y
        self.__canvas.coords(self.__imgHealth, self.__xpos, self.__ypos)
    
    def setImage(self, num):
        '''
        Sets the image of the health bar
        PARAMETERS:
        -----------
        currentImg_health: int
            The image of the health bar
        '''
        self.__currentImg_health = self.__imgList_health[num]
    
    def getLocation(self):
        '''
        Returns the location of the healthbar.
        RETURNS:
        --------
        list
            The coordinates containing the locations of the top bottom, left, and right of the healthbar
        '''
        self.__coordinates = [self.getX(), self.getX() + self.getWidth(), self.getY(), self.getY() + self.getHeight()]
        return self.__coordinates
    
    def lose_health(self, ship):
        '''
        Makes user lose a hitpoint.
        PARAMETERS:
        -----------
        health: int
            The amount of health the user has
        currentImg_health: PhotoImage
            Displays the image with the user's current hitpoints
        lives: int
            The number of lives the user has
        currentImg_lives: PhotoImage
            Displays the image with the user's current number of lives
        '''
        if self.health > 0:
            self.health -= 1
            self.__currentImg_health = self.__imgList_health[self.health]
            self.__currentImg_lives= self.__imgList_lives[self.lives]
            self.__canvas.delete(self.__currentImg_lives)
            self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, 
                image =self.__currentImg_health, anchor="ne")
            
        if  self.health == 0:
            if self.lives > 0:
                self.lives -= 1
                ship.explode()
                self.__currentImg_lives= self.__imgList_lives[self.lives]
                self.__canvas.delete(self.__imgLives)
                if self.lives >= 0:
                    self.__imgLives = self.__canvas.create_image(self.__xpos, self.__ypos+20, 
                        image =self.__currentImg_lives, anchor="ne")
                    self.__canvas.coords(self.__imgLives, self.__xpos, self.__ypos+20)
                    self.health = self.max_health
                    self.__currentImg_health = self.__imgList_health[self.health]
                    self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, 
                        image =self.__currentImg_health, anchor="ne")
                return [False, self.lives+1, True]
            else:
                return [True, self.lives+1, True]
        return [False, self.lives+1, False]
    
    def lose_live(self):
        '''
        Makes user lose a life.
        PARAMETERS:
        -----------
        lives: int
            The number of lives the user has
        currentImg_lives: PhotoImage
            Displays the image with the user's current number of lives
        health: int
            The amount of health the user has
        currentImg_health: PhotoImage
            Displays the image with the user's current hitpoints
        '''
        if self.lives > 0:
            self.lives -= 1
            self.__currentImg_lives= self.__imgList_lives[self.lives]
            self.__canvas.delete(self.__imgLives)
            if self.lives >= 0:
                self.__imgLives = self.__canvas.create_image(self.__xpos, self.__ypos+20, 
                    image = self.__currentImg_lives, anchor="ne")
                self.__canvas.coords(self.__imgLives, self.__xpos, self.__ypos+20)
                self.health = self.max_health
                self.__currentImg_health = self.__imgList_health[self.health]
                self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, 
                    image = self.__currentImg_health, anchor="ne")
        else:
            return True
        return False
    
    def set_health(self, heal):
        '''
        Sets the visible health of the user
        PARAMETERS:
        -----------
        max_health: int
            The max health the player can have
        currentImg_health: PhotoImahe
            Image of the current player health
        '''
        self.max_health = heal
        self.health = self.max_health
        self.__currentImg_health = self.__imgList_health[self.health]
        self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, 
            image = self.__currentImg_health, anchor="ne")
    
    def restart_health(self):
        '''
        Resets health and lives
        PARAMETERS:
        -----------
        lives: int
            The number of lives the user has
        health: int
            The number of hitpoints the user has
        currentImg_lives: PhotoImage
            The current image set to show lives
        currentImg_health: PhotoImage
            The current image set to show health
        '''
        self.lives = 2
        self.helth = self.max_health
        self.__canvas.delete(self.__imgLives)
        self.__canvas.delete(self.__currentImg_lives)
        self.__currentImg_lives= self.__imgList_lives[self.lives]
        self.__currentImg_health = self.__imgList_health[self.health]
        self.__imgLives = self.__canvas.create_image(self.__xpos, self.__ypos+20, 
            image = self.__currentImg_lives, anchor="ne")
        self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, 
            image = self.__currentImg_health, anchor="ne")

    def get_lives(self):
        '''
        Returns the number of lives the user has
        RETURNS:
        --------
        int
            The number of lives that the user has
        '''
        return self.lives
