from GameFunc import *
from beam import *
from ship import *
from health import *
from tkinter import *

class options:
    def __init__(self, options_menu, Game, main_menu, health):
        self.menu = options_menu
        self.__speedoption = 20
        self.__healthoption = 10
        self.__bulletoption = 5
        self.Game = Game
        self.Health = health
        self.background_list = [0] * 2
        self.imgBackground = PhotoImage(file='images/space_background.png')
        self.xpos = [0, self.imgBackground.width()]
        self.canvas3 = Canvas(main_menu, width=self.imgBackground.width(), height=self.imgBackground.height())
        self.canvas3.pack()

        for i in range(len(self.background_list)):
            self.background_list[i] = self.canvas3.create_image(self.xpos[i], 0, image=self.imgBackground, anchor='nw')
        self.background_timer(self.menu)

        self.lblSpeed = Label(self.menu, width=60, font=('neuropol', 14), anchor="c", text="Set the speed you want your \n ship to move at (max is 200):", bg="black", fg="white")
        self.lblSpeed.place(x=self.menu.winfo_reqwidth() * 2 - self.lblSpeed.winfo_reqwidth() // 2 - 30, y=self.menu.winfo_reqheight() // 2)
        self.entrySpeed = Entry(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat')
        self.entrySpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() + 20, y=self.menu.winfo_reqheight() // 2)
        self.btnSetSpeed = Button(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat', text="OK", command=lambda:self.setSpeedShip())
        self.btnSetSpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() + 25, y=self.menu.winfo_reqheight() // 2 + 40)
        self.lblHealth = Label(self.menu, width=60, font=('neuropol', 14), anchor="c", text="Set the amount of health you \n have at each life (max is 10):", bg="black", fg="white")
        self.lblHealth.place(x=self.menu.winfo_reqwidth() * 2 - self.lblSpeed.winfo_reqwidth() // 2 - 30, y=self.menu.winfo_reqheight() // 2 + 100)
        self.entryHealth = Entry(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat')
        self.entryHealth.place(x=self.menu.winfo_reqwidth() * 2 + self.entryHealth.winfo_reqwidth() + 20, y=self.menu.winfo_reqheight() // 2 + 100)
        self.btnSetHealth = Button(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat', text="OK", command=lambda:self.setHealthShip())
        self.btnSetHealth.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() + 25, y=self.menu.winfo_reqheight() // 2 + 140)
        self.btnBack = Button(self.menu, width= 12, font=('neuropol', 10), justify='center', text="BACK",command=lambda:self.goBack(main_menu))
        self.btnBack.place(x=self.btnBack.winfo_reqwidth() // 2, y=self.menu.winfo_reqheight()*2)


    def setSpeedShip(self):
        try:
            if int(self.entrySpeed.get()) > 200:
                messagebox.showinfo("Asteroid", "Sorry dude, that is way too fast.")
            else:
                self.Game.getAsteroidship().setSpeed(int(self.entrySpeed.get()))
                messagebox.showinfo("Asteroid", "You have successfully changed your speed to: " + str(self.entrySpeed.get()))
        except:
            messagebox.showerror("Asteroid", "Please input an Integer!")
    def goBack(self, main_menu):
        main_menu.grab_set()
        self.menu.withdraw()
    def setHealthShip(self):
        if int(self.entryHealth.get()) > 10:
            messagebox.showinfo("Asteroid", "Can't do more than 10 health buddy.")
        else:
            self.Game.setHealth(int(self.entryHealth.get()))
            messagebox.showinfo("Asteroid", "You have successfully changed your health to: " + str(self.entryHealth.get()) + "!")
    def background_timer(self, main_menu):
        global btid
        for i in range(len(self.background_list)):
            self.canvas3.coords(self.background_list[i], self.xpos[i] - 5, 0)
            self.xpos[i] -= 5
        btid = main_menu.after(100, lambda: self.background_timer(main_menu))

        if self.xpos[0] + self.imgBackground.width() <= 0:
            self.xpos[0] = self.xpos[1] + self.imgBackground.width()
        if self.xpos[1] + self.imgBackground.width() <= 0:
            self.xpos[1] = self.xpos[0] + self.imgBackground.width()

