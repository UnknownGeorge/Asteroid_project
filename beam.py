# Import Modules
from tkinter import *
import random
import pygame

class Beam():
    def __init__(self, canvas, img="images/laserbeam_red.png"):
        '''
        Initializes elements of the beam class.
        RETURNS:
        --------
        '''
        self.canvas = canvas
        self.img = PhotoImage(file=img)
        self.x = 0
        self.y = 0
        self.speed = 15
        self.shot = 0
        self.is_there = False
        self.inside()


    def shoot(self, x, y, speed = 15):
        '''
        Returns the age of the student.
        PARAMETERS:
        -----------
        laserNoise: int 
            random number that determines which acursed sound plays
        audioFiles: list
            lists audiofiles for laser "sounds"
        laserSound: list/Sound
            lists soundFiles for laser "sounds:
        bloop: int
            not really a parameter, i just wanted to mention that George didn't like zoom and zap, so
            now it's called bloop. haha @George
        x: int
            determines the x coordinate of the beam
        y: int
            determines the y coordinate of the beam
        speed: int
            determines the speed at which the laser travels
        shot: int/image
             creates the image of the beam
        is_there: boolean
            determines if a laser is available to be shot
        '''
        if self.is_there == False:
            pygame.mixer.init()
            self.laserNoise = random.randint(0,4)
            self.audioFiles = ['Audio_Files/laser1.ogg','Audio_Files/laser2.ogg','Audio_Files/laser3.ogg',
            'Audio_Files/laser4.ogg','Audio_Files/laser5.ogg']
            self.laserSound = [0] * 5
            for bloop in range(len(self.laserSound)):
                self.laserSound[bloop] = pygame.mixer.Sound(self.audioFiles[bloop])
            pygame.mixer.Sound.play(self.laserSound[self.laserNoise])
            self.x = x + 20
            self.y = y
            self.speed = speed
            self.shot = self.canvas.create_image(self.x, self.y, image = self.img, anchor="ne")
            self.is_there =True
            self.move()
        else:
            pass

    def move(self):
        if self.is_there == True:
            self.x += 10
            self.canvas.coords(self.shot, self.x, self.y)
            self.mover = self.canvas.after(self.speed, lambda:self.move())

        else:
            pass

    def get_pos(self):
        pos = [self.x, self.x+self.img.width(), self.y,  self.y+self.img.height()]
        return pos

    def inside(self):
        if self.is_there:
            pos = self.get_pos()
            if pos[0]>= self.canvas.winfo_reqwidth():
                self.canvas.delete(self.shot)
                self.is_there = False
                self.canvas.after_cancel(self.mover)

    def stop(self):
        self.canvas.delete(self.shot)
        self.is_there = False
        self.canvas.after_cancel(self.mover)

    def check_isthere(self):
        return self.is_there
