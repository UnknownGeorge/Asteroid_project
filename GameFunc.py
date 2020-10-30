from tkinter import *
from tkinter import font, messagebox
from ship import *
from beam import *
from health import *
from asteroids import *
import random
from scoremenu import *
class Game():
    def __init__(self, canvas, root, background_list, main_menu):
        self.canvas = canvas
        self.root = root
        self.background_list =background_list

        #binds for key presses
        root.bind('<KeyPress>',  self.onkeypress)
        root.bind('<Button-1>', self.onmouse)

        #create a call to run the other classes
        self.asteroidship = ship(0, self.canvas.winfo_reqheight()//2, self.canvas)
        self.health = health(self.canvas)
        #add custom font

        #create vars that will be used in this class
        self.beam_num = 10
        self.score = 0
        self.stop = False
        self.beam_avalible = []
        self.name = ""
        self.mainmenu = main_menu

        self.astroids = random.randint(10,20)
        self.astroids_avalible = []

        #run setup functions
        self.__beams()
        self.scores_txt = self.canvas.create_text(150,40, text=str(self.score), fill ="#ff8000", font=("Bold", 30))
        self.astroids_create()
    def set_name(self, name):
        self.name = name
        print(self.name)
    def getAsteroidship(self):
        return self.asteroidship
    def __beams(self):
        for i in range(self.beam_num):
            self.beam_avalible.append(Beam(self.canvas))
    def score_add(self, value):
        print(self.score + value)
        self.score += value
        self.canvas.delete(self.scores_txt)
        self.scores_txt = self.canvas.create_text(150,40, text=str(self.score), fill ="#ff8000", font=("Bold", 30))
        pass
    def onkeypress(self, event):
        pos = self.asteroidship.getLocation()
        if event.char == "w":
            if not pos[2] <= 70:
                self.asteroidship.move(y=-self.asteroidship.getSpeed())
            else:
                pass
        elif event.char == "a":
            if not pos[0] <= 0:
                self.asteroidship.move(x=-self.asteroidship.getSpeed())
            else:
                pass
        elif event.char == "s":
            if not pos[3]+20 >= self.canvas.winfo_reqheight():
                self.asteroidship.move(y=self.asteroidship.getSpeed())
            else:
                pass
        elif event.char == "d":
            if not pos[1]+20 >= self.canvas.winfo_reqwidth():
                self.asteroidship.move(x=self.asteroidship.getSpeed())
            else:
                pass
    def onmouse(self, event):
        self.beam_num -= 1
        self.beam_avalible[self.beam_num].shoot(self.asteroidship.getLocation()[1], self.asteroidship.getY()+10)
        if self.beam_num == -1:
            self.beam_num = 4
        #Shoot the bullet :D

    def start(self):
        for i in self.astroids_avalible:
            i.move()

        self.check_colisions()
    def astroids_create(self):
        rand_x, rand_y = random.randint(500, self.astroids *110), random.randint(100, 420)
        self.astroids_avalible.append(asteroids(rand_x, rand_y, self.canvas))
        for i in range(self.astroids -1):
            rand_x, rand_y = random.randint(500, self.astroids *110), random.randint(100, 420)
            new = asteroids(rand_x, rand_y, self.canvas)
            for x in range(60):
                for z in self.astroids_avalible:
                    if ( z.getLocation()[1] >= new.getLocation()[0]   and z.getLocation()[0] <= new.getLocation()[1] or  z.getLocation()[0] <= new.getLocation()[0]   and z.getLocation()[1] >= new.getLocation()[1] ):
                        if  z.getLocation()[3] >= new.getLocation()[2]  and z.getLocation()[2] <= new.getLocation()[3] or z.getLocation()[2]<= new.getLocation()[2]  and z.getLocation()[3] >= new.getLocation()[3]:
                            rand_x, rand_y = random.randint(500, self.astroids *150), random.randint(100, 420)
                            new.set_pos(x=rand_x, y = rand_y)


            self.astroids_avalible.append(new)
    def check_colisions(self):
        for z in self.astroids_avalible:
            if ( z.getLocation()[1] >= self.asteroidship.getLocation()[0]   and z.getLocation()[0] <= self.asteroidship.getLocation()[1] or  z.getLocation()[0] <= self.asteroidship.getLocation()[0]   and z.getLocation()[1] >= self.asteroidship.getLocation()[1] ):
                if  z.getLocation()[3] >= self.asteroidship.getLocation()[2]  and z.getLocation()[2] <= self.asteroidship.getLocation()[3] or z.getLocation()[2]<= self.asteroidship.getLocation()[2]  and z.getLocation()[3] >= self.asteroidship.getLocation()[3]:
                    if z.hurt_player():
                        if self.health.lose_health():
                            self.goEndScreen()



        #check for colision between the bean and astroid
        for x  in self.beam_avalible:
            if x.check_isthere():
                for index, z in enumerate(self.astroids_avalible):


                    if ( z.getLocation()[1] >= x.get_pos()[0]   and z.getLocation()[0] <= x.get_pos()[1] or  z.getLocation()[0] <= x.get_pos()[0]   and z.getLocation()[1] >= x.get_pos()[1] ):
                        if  z.getLocation()[3] >= x.get_pos()[2]  and z.getLocation()[2] <= x.get_pos()[3] or z.getLocation()[2]<= x.get_pos()[2]  and z.getLocation()[3] >= x.get_pos()[3]:
                            x.stop()
                            self.score_add(z.get_val())
                            z.health(self.astroids_avalible, index)





        for index, i in enumerate(self.astroids_avalible):
            if i.getLocation()[0] <= 0:
                i.remake(self.astroids_avalible, index)
                if self.health.lose_health():
                    self.goEndScreen()
        for i in self.beam_avalible:
            i.inside()
        for i in self.astroids_avalible:
            i.move()
        print(self.name)
        if not self.stop:
            self.timer = self.canvas.after(100, self.check_colisions)
    def exit_program(self):
        answer = messagebox.askyesno("Asteroid", "Are you sure you want to quit?")
        if answer == True:
            quit()
        else:
            pass
    def setHealth(self, heal):
        self.health.set_health(heal)
    def getScore(self):
        return self.score
    def goEndScreen(self):
        self.canvas.after_cancel(self.timer)
        self.canvas.update()
        self.stop = True
        scoremenu(self.score, self.mainmenu)
