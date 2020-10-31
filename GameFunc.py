from tkinter import *
from tkinter import font, messagebox
from ship import *
from beam import *
from health import *
from asteroids import *
import random
from scoremenu import *
from File import *
class Game():
    def __init__(self, canvas, root,  main_menu, get_top10):
        '''
        Initializes elements of the Game class.

        PARAMETERS:
        -----------
        self.canvas: canvas():
            holds the key to the widget canvas
        self.root: root():
            holds the key to the widget root
        self.get_top10: top10():
            holds the key to the function top10
        self.file: top_file():
            holds the key to the class top10
        self.main_menu: Toplevel():
            holds the key to the toplevel
        self.asteroidship: ship():
            holds the key to the class to ship
        self.health : health():
            holds the key to the class health
        self.beam_num: int
            holds the number of beams can spawn
        self.score: int
            stores the score of the player
        self.stop: bool:
            stores a boolean to stop time loop
        self.beam_avalible: list:
            stores beams class keys
        self.name: string:
            stores players name
        self.astroidtime: int
            counter to decide when the astroids should speed up
        self.astroidspeed: int
            the speed that the astroid move at
        self.astroids: int
            stores a random number of astroids to be generated
        self.astroids_avalible: list :
            stores astroids_avalible class key
        '''

        self.canvas = canvas
        self.root = root
        self.get_top10= get_top10
        self.file = top_file()
        self.mainmenu = main_menu

        #binds for key presses
        root.bind('<KeyPress>',  self.onkeypress)
        root.bind('<Button-1>', self.onmouse)

        #create a call to run the other classes
        self.asteroidship = ship(0, self.canvas.winfo_reqheight()//2, self.canvas)
        self.health = health(self.canvas)
        #add custom font

        #create vars that will be used in this class
        self.beam_num = 5
        self.score = 0
        self.stop = False
        self.beam_avalible = []
        self.name = ""
        self.astroidtime = 0
        self.astroidspeed = 10

        self.astroids = random.randint(10,20)
        self.astroids_avalible = []

        #run setup functions
        self.__beams()
        self.scores_txt = self.canvas.create_text(150,40, text=str(self.score), fill ="#ff8000", font=("Bold", 30))
        self.astroids_create()
    def set_name(self, name):
        ''' Changes the value of name

        PARAMETERS:
        -----------
        self.name: string:
            changes the name to users name
        '''
        self.name = name
    def getAsteroidship(self):
        ''' Returns key to the class asteroidship
        RETURNS:
        -----------
        self.asteroidship
            returns key to the class asteroidship

        '''
        return self.asteroidship
    def __beams(self):
        '''creates and stores key to class beams into a list equal to the self.beam_num
        PARAMETERS:
        -----------
        i : int:
            itterates threw self.beam_num
        self.beam_num: int
            holds the number of beams can spawn
        self.self.beam_avalible: list:
            stores and creates a key to class beam  for the length of self.beam_num
         '''
        for i in range(self.beam_num):
            self.beam_avalible.append(Beam(self.canvas))
    def score_add(self, value):
        '''creates and stores key to class beams into a list equal to the self.beam_num
        PARAMETERS:
        -----------
        i : int:
            itterates threw self.beam_num
        self.beam_num: int
            holds the number of beams can spawn
        self.self.beam_avalible: list:
            stores and creates a key to class beam  for the length of self.beam_num
         '''
        self.score += value
        self.canvas.delete(self.scores_txt)
        self.scores_txt = self.canvas.create_text(150,40, text=str(self.score), fill ="#ff8000", font=("Bold", 30))
    def onkeypress(self, event):
        ''' when keyboard key is pressed
        PARAMETERS:
        -----------
        pos: list
            holds the postion of where the ship is

        '''
        pos = self.asteroidship.getLocation()
        #if user presses w move up a move left s move down d move right
        if event.char == "w":
            #check if player can move to the top and move them if they can
            if not pos[2]+self.asteroidship.getSpeed()-20 <= 70:
                self.asteroidship.move(y=-self.asteroidship.getSpeed())
            else:
                pass
        elif event.char == "a":
            #check if player can move to the left and move them if they can
            if not pos[0]+self.asteroidship.getSpeed()-20 <= 0:
                self.asteroidship.move(x=-self.asteroidship.getSpeed())
            else:
                pass
        elif event.char == "s":
            #check if player can move to the down and move them if they can
            if not pos[3]+self.asteroidship.getSpeed() >= self.canvas.winfo_reqheight():
                self.asteroidship.move(y=self.asteroidship.getSpeed())
            else:
                pass
        elif event.char == "d":
            #check if player can move to the right and move them if they can
            if not pos[1]+self.asteroidship.getSpeed()>= self.canvas.winfo_reqwidth():
                self.asteroidship.move(x=self.asteroidship.getSpeed())
            else:
                pass
    def onmouse(self, event):
        '''When let key on mouse is pressed
        PARAMETERS
        ----------
        self.beam_num: int
            holds the number of beams can spawn
        self.self.beam_avalible: list:
            stores key to class beam  for the length of self.beam_num
        '''
        #chec if the player is still alive  if so shoot the location
        if not self.asteroidship.is_exploded():
            self.beam_num -= 1
            self.beam_avalible[self.beam_num].shoot(self.asteroidship.getLocation()[1], self.asteroidship.getY()+10)
            if self.beam_num == -1:
                self.beam_num = len(self.beam_avalible)
        #Shoot the bullet :D

    def start(self):
        ''' Starts timers and begins the movment for astroids
        PARAMETERS
        ----------
        i: astroid():
            itreation and use of every key to class astroid in self.astroids_avalible
        self.astroids_avalible(): list:
            list containg key to astroids()
        '''
        #move evry avalible list
        for i in self.astroids_avalible:
            i.move()
        #begin the timer
        self.check_colisions()
    def astroids_create(self):
        '''Creates all the astroids randomly but not stacked on each other
        PARAMETERS
        ----------
        rand_x: int:
            random number for the x pos of nw cornor
        rand_y: int:
            random number for the y pos of nw cornor
        self.astroids_avalible: list:
            stores a list of keys to astroid
        self.astroids: int
            stores a random number of astroids to be generated
         new: asteroid():
            stores the key to the astorid we would like to place on the screen
        '''

        #create a astroid in a random location and check that no other astroid spaws at the same location it checks it 60 times to be sure
        #store the new astroid's key in a list
        for i in range(self.astroids -1):
            rand_x, rand_y = random.randint(500, self.astroids *110), random.randint(100, 400)
            new = asteroids(rand_x, rand_y, self.canvas)
            for x in range(60):
                for z in self.astroids_avalible:
                    if ( z.getLocation()[1] >= new.getLocation()[0]   and z.getLocation()[0] <= new.getLocation()[1] or  z.getLocation()[0] <= new.getLocation()[0]   and z.getLocation()[1] >= new.getLocation()[1] ):
                        if  z.getLocation()[3] >= new.getLocation()[2]  and z.getLocation()[2] <= new.getLocation()[3] or z.getLocation()[2]<= new.getLocation()[2]  and z.getLocation()[3] >= new.getLocation()[3]:
                            rand_x, rand_y = random.randint(500, self.astroids *150), random.randint(100, 400)
                            new.set_pos(x=rand_x, y = rand_y)
            self.astroids_avalible.append(new)

    def check_colisions(self):
        '''Timer of the game: check any possible colisions
        PARAMETERS
        ----------
        self.astroids_avalible: list:
            stores a list of keys to astroid
        self.health: health():
            contains the key to the class health
        self.self.beam_avalible: list:
            stores keys to class beam  for the length of self.beam_num
        val: list :
            stores the returns from health conatining 2 bools and an int
        self.astroidtime: int
            counter to decide when the astroids should speed up
         self.stop: boolean:
            decides weather or not to stop the timer
        '''
        for z in self.astroids_avalible:
            if ( z.getLocation()[1] >= self.asteroidship.getLocation()[0]   and z.getLocation()[0] <= self.asteroidship.getLocation()[1] or  z.getLocation()[0] <= self.asteroidship.getLocation()[0]   and z.getLocation()[1] >= self.asteroidship.getLocation()[1] ):
                if  z.getLocation()[3] >= self.asteroidship.getLocation()[2]  and z.getLocation()[2] <= self.asteroidship.getLocation()[3] or z.getLocation()[2]<= self.asteroidship.getLocation()[2]  and z.getLocation()[3] >= self.asteroidship.getLocation()[3]:
                    if not self.asteroidship.is_exploded():
                        if z.can_beam():
                            if z.hurt_player():
                                self.asteroidship.explode()
                                if  self.health.get_lives() >= 0:
                                    self.restartPosition()
                                    messagebox.showinfo("Life gone", "You lost a life \n you have %d lives left" %(self.health.get_lives()))
                                if self.health.lose_live():
                                    self.goEndScreen()




        #check for colision between the bean and astroid
        for x  in self.beam_avalible:
            if x.check_isthere():
                for index, z in enumerate(self.astroids_avalible):
                    if ( z.getLocation()[1] >= x.get_pos()[0]   and z.getLocation()[0] <= x.get_pos()[1] or  z.getLocation()[0] <= x.get_pos()[0]   and z.getLocation()[1] >= x.get_pos()[1] ):
                        if  z.getLocation()[3] >= x.get_pos()[2]  and z.getLocation()[2] <= x.get_pos()[3] or z.getLocation()[2]<= x.get_pos()[2]  and z.getLocation()[3] >= x.get_pos()[3]:
                            if z.can_beam():
                                x.stop()
                                self.score_add(z.get_val())
                                z.health(self.astroids_avalible, index)





        for index, i in enumerate(self.astroids_avalible):
            if i.getLocation()[1] <= 0:
                i.remake(self.astroids_avalible, index)
                if i.can_beam():
                    val = self.health.lose_health(self.asteroidship)
                    if val[2]:
                        if  self.health.get_lives()+1 > 0:
                            self.restartPosition()
                            messagebox.showinfo("Life gone", "You lost a life \n you have %d lives left" %(val[2]))
                        if val[0]:
                         self.goEndScreen()


        self.astroidtime +=1
        if self.astroidtime == 100:
            self.astroidspeed += 1
            if self.astroidspeed <= 30:
                for i in self.astroids_avalible:
                    i.set_speed(self.astroidspeed)
                    self.astroidtime = 0


        for i in self.beam_avalible:
            i.inside()

        for i in self.astroids_avalible:
            i.move()

        if not self.stop:
            self.timer = self.canvas.after(100, self.check_colisions)
            
    def exit_program(self):
        '''
        exits the entire program

        PARAMETERS:
        -----------
        answer: boolean
            contains a boolean value that should ask the user if they want to exit or not
        '''
        answer = messagebox.askyesno("Asteroid", "Are you sure you want to quit?")
        if answer == True:
            quit()
        else:
            pass

    def setHealth(self, heal):
        '''
        sets the health of the user

        PARAMETERS:
        -----------
        health: health function
            passes the current canvas of the game and the current health to be set.
        '''
        self.health = health(self.canvas, heal)
    def getScore(self):
        '''
        gets the score of the user

        PARAMETERS:
        -----------
        score: int
            contains the score of the user
        '''
        return self.score
    def goEndScreen(self):
        '''
        writes the score into the file, restarts the game but makes the timers still stop

        PARAMETERS:
        -----------
        canvas: canvas object
            contains the canvas of the game
        stop: boolean
            tells the program whether or not to stop the program
        file: File function
            calls the file function to write inside of it
        restartGame: function
            calls the restart function which resets the game
        '''
        self.canvas.after_cancel(self.timer)
        self.canvas.update()
        self.stop = True
        self.file.writer(self.name, self.score)
        scoremenu(self.score, self.mainmenu, self.get_top10)
        self.restartGame()
    def restartGame(self):
        '''
        restarts most of the variables and the game

        PARAMETERS:
        -----------
        canvas: canvas object
            contains the canvas of the game
        asteroidship: ship function
            resets the ship and calls a new ship to be it's replacement
        score: int
            contains the new score for the user
        beam_num: int
            contains the new amount of beams the user should have
        beam_available: list
            contains the available beams
        health: health function
            contains the health function which currently calls the restarting function, restarting the health
        beams: beam function
            creates the beam
        scores_txt: txt
            creates a text variable that shows the score that the user should reset to
        astroids_create: function
            creates the astroids again
        '''
        self.asteroidship = ship(0, self.canvas.winfo_reqheight()//2, self.canvas)
        self.beam_num = 5
        self.score = 0
        self.beam_avalible = []

        self.astroids = random.randint(10,20)
        self.astroids_avalible = []
        self.health.restart_health()

        self.__beams()
        self.canvas.delete(self.scores_txt)
        self.scores_txt = self.canvas.create_text(150,40, text=str(self.score), fill ="#ff8000", font=("Bold", 30))
        self.astroids_create()
    def setStop(self, vals):
        '''
        restarts most of the variables and the game

        PARAMETERS:
        -----------
        stop: boolean
            sets the stop to true or false
        '''
        self.stop = vals
    def restartPosition(self):
        '''
        restarts most of the variables and the game

        PARAMETERS:
        -----------
        asteroidship: ship function
            resets the ship and calls a new ship to be it's replacement
        beam_num: int
            contains the new amount of beams the user should have
        beam_available: list
            contains the available beams
        health: health function
            contains the health function which currently calls the restarting function, restarting the health
        beams: beam function
            creates the beam
        astroids_create: function
            creates the astroids again
        '''
        self.asteroidship = ship(0, self.canvas.winfo_reqheight()//2, self.canvas, speed = self.asteroidship.getSpeed())
        for i in self.beam_avalible:
            if i.check_isthere():
                i.stop()
        self.beam_num = 5
        self.stop = False
        self.beam_avalible = []

        self.astroids = random.randint(10,20)
        self.astroids_avalible = []

        self.__beams()
        self.astroids_create()
