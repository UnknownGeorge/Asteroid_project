from tkinter import *
# Create an exit to main menu button when the user loses all health
# Make all the healths of the seperate lives the same as you've set it

class health:
    def __init__(self, canvas):

        self.__canvas = canvas
        self.__imgList_health = [PhotoImage(file="images/health0.png"), PhotoImage(file="images/health1.png"), PhotoImage(file="images/health2.png"),
            PhotoImage(file="images/health3.png"), PhotoImage(file="images/health4.png"), PhotoImage(file="images/health5.png"),
            PhotoImage(file="images/health6.png"), PhotoImage(file="images/health7.png"), PhotoImage(file="images/health8.png"),
            PhotoImage(file="images/health9.png"), PhotoImage(file="images/health10.png"), ]
        self.__imgList_lives = [PhotoImage(file = "images/lives1.png"),
            PhotoImage(file = "images/lives2.png"),PhotoImage(file = "images/lives3.png")]
        self.health = 10
        self.lives = 2
        self.__currentImg_health = self.__imgList_health[self.health]
        self.__currentImg_lives= self.__imgList_lives[self.lives]
        self.__xpos = canvas.winfo_reqwidth()-50
        self.__ypos = self.__imgList_health[0].height()
        self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, image =self.__currentImg_health, anchor="ne")
        self.__imgLives = self.__canvas.create_image(self.__xpos, self.__ypos+20, image =self.__currentImg_lives, anchor="ne")
    def getX(self):
        return self.__xpos
    def getY(self):
        return self.__ypos
    def getHeight(self):
        return self.__currentImg_health.height()
    def getWidth(self):
        return self.__currentImg_health.width()
    def setX(self, x):
        self.__xpos = x
        self.__canvas.coords(self.__imgHealth, self.__xpos, self.__ypos)
    def setY(self, y):
        self.__ypos = y
        self.__canvas.coords(self.__imgHealth, self.__xpos, self.__ypos)
    def setImage(self, num):
        self.__currentImg_health = self.__imgList_health[num]
    def getLocation(self):
        self.__coordinates = [self.getX(), self.getX() + self.getWidth(), self.getY(), self.getY() + self.getHeight()]
        return self.__coordinates
    def lose_health(self):
        if self.health >= 0:
            self.health -= 1
            self.__currentImg_health = self.__imgList_health[self.health]
            self.__currentImg_lives= self.__imgList_lives[self.lives]
            self.__canvas.delete(self.__currentImg_lives)
            self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, image =self.__currentImg_health, anchor="ne")
            #self.__imgLives = self.__canvas.create_image(self.__xpos, self.__ypos+20, image =self.__currentImg_lives, anchor="ne")

        if  self.health <= 0:
            if self.lives >= 0:
                self.lives -= 1
                self.__currentImg_lives= self.__imgList_lives[self.lives]
                self.__canvas.delete(self.__imgLives)
                if self.lives >= 0:
                    self.__imgLives = self.__canvas.create_image(self.__xpos, self.__ypos+20, image =self.__currentImg_lives, anchor="ne")
                    self.__canvas.coords(self.__imgLives, self.__xpos, self.__ypos+20)
                    self.health = 10
                    self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, image =self.__currentImg_health, anchor="ne")

            else:
                return True
        return False
    def set_health(self, heal):
        self.health = heal
        self.__currentImg_health = self.__imgList_health[heal]
        self.__imgHealth = self.__canvas.create_image(self.__xpos, self.__ypos, image =self.__currentImg_health, anchor="ne")
