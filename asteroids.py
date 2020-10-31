from tkinter import PhotoImage, Canvas
import random
import pygame

class asteroids:
    def __init__(self, x, y, canvas, speed=10):
        '''
        Initializes elements of the asteroids class.
        PARAMETERS:
        -----------
        canvas: canvas
            The canvas surrounding the asteroid - gives hitbox
        speed: int
            The speed at which the asteroid travels across the screen
        asteroidlist: list
            List of asteroid images
        explodeylist: list 
            List of asteroid explosions (only the smallest one is used. we thought that using all 
            three for each decreasing level might be visually distracting to the user and make the user 
            experience worse)
        size: int
            Determine the size of the asteroid
        value: int
            Determines the point value of destroying an asteroid
        xpos: int
            Determine the x position of the asteroid
        ypos: int
            Determine the y position of the asteroid
        has_hurt: bool
            Determines if the asteroid has been hit or not
        happend: bool
            Determines if the asteroid has been fully ended and is gone
        can_be: bool
            Detemines if the asteroid can be hit by the laser
        '''
        self.__canvas = canvas
        self.__imagelist = []
        self.__speed = speed
        self.__asteroidlist = [PhotoImage(file="images/asteroid0.png"), 
            PhotoImage(file="images/asteroid1.png"), PhotoImage(file="images/asteroid2.png")]
        self.__explodeylist = [PhotoImage(file="images/explosion0.png"), 
            PhotoImage(file="images/explosion1.png"), PhotoImage(file="images/explosion2.png")]
        self.__size = random.randint(0,2)
        self.value = (self.__size + 1) * 10
        self.__xpos =  x
        self.__ypos = y
        self.__asteroidImage = self.__canvas.create_image(x,y,image = self.__asteroidlist[self.__size], anchor="nw")
        self.has_hurt = True
        self.happend = False
        self.can_be = True

    def set_pos(self, x = 0, y = 0):
        '''
        Sets the name of the student.
        PARAMETERS:
        -----------
        x: int 
            x value of the asteroid
        xpos: int
            x position of the asteroid
        y: int
            y position of the asteroid
        ypos: int
            y position of the asteroid
        canvas: canvas
            coordinates of the canvas - determines hitbox
        '''
        if not x == 0:
            self.__xpos = x
        if not y == 0:
            self.__ypos = y
        self.__canvas.coords(self.__asteroidImage, self.__xpos, self.__ypos)
    
    def getLocation(self):
        '''
        Get the location of the asteroid.
        RETURNS:
        --------
        list
            List of asteroid hitbox locations
        '''
        self.coordinates = [self.__xpos, self.__xpos + self.__asteroidlist[self.__size].width(), self.__ypos, 
            self.__ypos + self.__asteroidlist[self.__size].height()]
        return self.coordinates
    
    def move(self):
        '''
        Movement of the Asteroid
        PARAMETERS:
        -----------
        xpos: int
            the x position of the asteroid
        canvas: canvas
            the hitbox of the asteroid
        '''
        self.__xpos -=self.__speed
        self.__canvas.coords(self.__asteroidImage, self.__xpos, self.__ypos)
    
    def health(self, astroids_avalible, index):
        '''
        Sets the name of the student.
        PARAMETERS:
        -----------
        name: str
            The name of the student
        size: int
            contains the size of the current asteroid
        canvas: canvas
            contains the canvas of the game
        ypos: int
            contains the y position of the asteroid
        asteroidImage: img
            contains the image of the current asteroid
        asteroidlist: list
            contains the list of current asteroids
        can_be: boolean
            checks if the asteroid can be hit by the beam
        explodyNoise: int
            random number generated to play a sound
        audioFiles: list
            list containing the list of audio files
        explodySound: int
            list of sounds that need to be appended to
        '''
        if not self.__size <= 0:
            self.__size -= 1
            self.__canvas.delete(self.__asteroidImage)
            self.__ypos =  self.__asteroidlist[self.__size].height() //2 +self.__ypos
            self.__asteroidImage = self.__canvas.create_image( self.__xpos, self.__ypos, 
                image = self.__asteroidlist[self.__size], anchor="nw")
        else:
            '''
            Returns the age of the student.
            RETURNS:
            --------
            int
                The age of the student
            '''
            self.can_be = False
            self.__canvas.delete(self.__asteroidImage)
            self.__asteroidImage = self.__canvas.create_image(self.__xpos,self.__ypos, 
                image = self.__explodeylist[self.__size], anchor="nw")
            self.__canvas.after(500, lambda: self.remake(astroids_avalible, index))
            # Cue Acursed Noises
            pygame.mixer.init()
            self.explodyNoise = random.randint(0,4)
            self.audioFiles = ['Audio_Files/booom1.ogg','Audio_Files/booom2.ogg','Audio_Files/booom3.ogg',
            'Audio_Files/booom4.ogg','Audio_Files/booom5.ogg']
            self.explodySound = [0] * 5
            for baaam in range(len(self.explodySound)):
                self.explodySound[baaam] = pygame.mixer.Sound(self.audioFiles[baaam])
            pygame.mixer.Sound.play(self.explodySound[self.explodyNoise])
            return True

    def remake(self, astroids_avalible, index):
        '''
        Resets the asteroid(s).
        PARAMETERS:
        -----------
        can_be: bool
            Detemines if the asteroid can be hit by the laser
        has_hurt: bool
            Determines if the asteroid has been hit or not
        happend: bool
            Determines if the asteroid has been fully ended and is gone
        canvas: canvas
            The canvas hitbox
        size: int
            The randomly generated size of the asteroid
        value: int
            point value of the asteroid when destroyed
        xpos: int
            the x position of the asteroid
        ypos: int
            the y position of the asteroid
        asteroids_available: list
            the number of asteroids that can be spawned
        '''
        self.can_be = True
        self.has_hurt = True
        self.happend = False
        self.__canvas.delete(self.__asteroidImage)
        self.__size = random.randint(0,2)
        self.value = (self.__size + 1) * 10
        rand_x, rand_y = random.randint(1100, len(astroids_avalible) * 160), random.randint(100, 400)
        self.__xpos = rand_x
        self.__ypos = rand_y
        self.__asteroidImage = self.__canvas.create_image(rand_x, rand_y , 
            image = self.__asteroidlist[self.__size], anchor="nw")
        for i in range(10):
            for loc, z in enumerate(astroids_avalible):
                if not loc == index:
                    if (z.getLocation()[1] >= self.getLocation()[0] and 
                        z.getLocation()[0] <= self.getLocation()[1] or 
                        z.getLocation()[0] <= self.getLocation()[0] and 
                        z.getLocation()[1] >= self.getLocation()[1] ):
                        if (z.getLocation()[3] >= self.getLocation()[2] and 
                            z.getLocation()[2] <= self.getLocation()[3] or 
                            z.getLocation()[2]<= self.getLocation()[2] and 
                            z.getLocation()[3] >= self.getLocation()[3]):
                            rand_x, rand_y = random.randint(1100, len(astroids_avalible) * 160), random.randint(100, 400)
                            self.set_pos(x=rand_x, y = rand_y)

    def hurt_player(self):
        '''
        Returns if an asteroid has hit the player
        RETURNS:
        --------
        bool
            Has the asteroid hit the user
        '''
        x = self.has_hurt
        self.has_hurt = False
        return x

    def get_val(self):
        '''
        Gets point value of the asteroid when destroyed
        RETURNS:
        --------
        int
            returns point value of the asteroid when destroyed 
        '''

        if self.__size  == 0 and self.happend == False:
            self.happend = True
            return self.value
        else:
            return 0

    def set_speed(self, speed):
        '''
        Sets the speed of the asteroid
        PARAMETERS:
        -----------
        speed: int
            The speed of the asteroid
        '''
        self.__speed =  speed

    def can_beam(self):
        '''
        checks if the asteroid can be destroyed
        RETURNS:
        --------
        bool
            can the asteroid be destroyed
        '''

        return self.can_be
