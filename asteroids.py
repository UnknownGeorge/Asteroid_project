from tkinter import PhotoImage, Canvas
import random

class asteroids:
    def __init__(self, x, y, canvas, speed=50):
        self.__canvas = canvas
        self.__imagelist = []
        self.__speed = speed
        self.__asteroidlist = [PhotoImage(file="images/asteroid0.png"), PhotoImage(file="images/asteroid1.png"), PhotoImage(file="images/asteroid2.png")]
        self.__explodeylist = [PhotoImage(file="images/explosion0.png"), PhotoImage(file="images/explosion1.png"), PhotoImage(file="images/explosion2.png")]
        self.__size = random.randint(0,2)
        self.value = (self.__size +1) *10
        self.__xpos =  x
        self.__ypos = y
        self.__mxpos = self.__xpos
        self.__mypos = self.__ypos
        self.__asteroidImage = self.__canvas.create_image(x,y,image=self.__asteroidlist[self.__size], anchor="nw")
        self.has_hurt = True
        self.happend = False
        #self.move()

    def set_pos(self, x = 0, y = 0):
        if not x == 0:
            self.__xpos = x
        if not y == 0:
            self.__ypos = y
        self.__mxpos = self.__xpos
        self.__mypos = self.__ypos
        self.__canvas.coords(self.__asteroidImage, self.__xpos, self.__ypos)
    def getLocation(self):
        self.coordinates = [self.__xpos, self.__xpos + self.__asteroidlist[self.__size].width(), self.__ypos, self.__ypos + self.__asteroidlist[self.__size].height()]
        return self.coordinates
    def move(self):
        self.__xpos -=10
        self.__canvas.coords(self.__asteroidImage, self.__xpos, self.__ypos)
    def health(self, astroids_avalible, index):

        if not self.__size <= 0:
            self.__size -= 1
            self.__canvas.delete(self.__asteroidImage)
            self.__ypos =  self.__asteroidlist[self.__size].height() //2 +self.__ypos
            self.__asteroidImage = self.__canvas.create_image( self.__xpos, self.__ypos,image=self.__asteroidlist[self.__size], anchor="nw")

        else:
            self.__canvas.delete(self.__asteroidImage)
            self.__asteroidImage = self.__canvas.create_image(self.__xpos,self.__ypos,image=self.__explodeylist[self.__size], anchor="nw")
            self.__canvas.after(500, lambda: self.remake(astroids_avalible, index))
            return True



    def remake(self, astroids_avalible, index):
        self.has_hurt = True
        self.happend = False
        self.__canvas.delete(self.__asteroidImage)
        self.__size = random.randint(0,2)
        self.value = (self.__size +1) *10
        rand_x, rand_y = random.randint(900, len(astroids_avalible) * 150), random.randint(100, 420)
        self.__xpos = rand_x
        self.__ypos = rand_y
        self.__asteroidImage = self.__canvas.create_image(rand_x, rand_y ,image=self.__asteroidlist[self.__size], anchor="nw")
        for i in range(60):
            for loc, z in enumerate(astroids_avalible):
                if not loc == index:
                    if ( z.getLocation()[1] >= self.getLocation()[0]   and z.getLocation()[0] <= self.getLocation()[1] or  z.getLocation()[0] <= self.getLocation()[0]   and z.getLocation()[1] >= self.getLocation()[1] ):
                        if  z.getLocation()[3] >= self.getLocation()[2]  and z.getLocation()[2] <= self.getLocation()[3] or z.getLocation()[2]<= self.getLocation()[2]  and z.getLocation()[3] >= self.getLocation()[3]:
                            rand_x, rand_y = random.randint(900, len(astroids_avalible) * 150), random.randint(100, 420)
                            self.set_pos(x=rand_x, y = rand_y)


    def hurt_player(self):
        x = self.has_hurt
        self.has_hurt = False
        return x

    def get_val(self):
        if self.__size  == 0 and self.happend == False:

            print(self.__size, self.value )
            self.happend = True
            return self.value
        else:
            return 0
        # self.__xpos = self.__mxpos
        # self.__ypos = self.__mypos
        # self.__size = random.randint(0,2)
        # self.__asteroidImage = self.__canvas.create_image(self.__xpos,self.__ypos,image=self.__asteroidlist[self.__size], anchor="nw")
