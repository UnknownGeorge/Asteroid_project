from GameFunc import *
from beam import *
from ship import *
from health import *
from tkinter import *

class options:
    def __init__(self, options_menu, Game, main_menu):
        self.menu = options_menu
        self.__speedoption = 20
        self.__healthoption = 10
        self.__bulletoption = 5
        self.Game = Game

        self.lblSpeed = Label(self.menu, width=60, font=('Arial', 14), anchor="c", text="Set the speed you want your character to move at (max is 200):", bg="black", fg="white")
        self.lblSpeed.place(x=self.menu.winfo_reqwidth() * 2 - self.lblSpeed.winfo_reqwidth() // 2 - 100, y=self.menu.winfo_reqheight() // 2)
        self.entrySpeed = Entry(self.menu, width=12, font=('Arial', 10), justify='center', borderwidth=5, relief='flat')
        self.entrySpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() * 2 + 40, y=self.menu.winfo_reqheight() // 2)
        self.btnSetSpeed = Button(self.menu, width=12, font=('Arial', 10), justify='center', borderwidth=5, relief='flat', text="OK", command=lambda:self.setSpeedShip())
        self.btnSetSpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() * 2 + 30, y=self.menu.winfo_reqheight() // 2 + 40)
        self.lblHealth = Label(self.menu, width=60, font=('Arial', 14), anchor="c", text="Set the amount of health you have at each life (max is 10):", bg="black", fg="white")
        self.lblHealth.place(x=self.menu.winfo_reqwidth() * 2 - self.lblSpeed.winfo_reqwidth() // 2 - 120, y=self.menu.winfo_reqheight() // 2 + 100)
        self.entryHealth = Entry(self.menu, width=12, font=('Arial', 10), justify='center', borderwidth=5, relief='flat')
        self.entryHealth.place(x=self.menu.winfo_reqwidth() * 2 + self.entryHealth.winfo_reqwidth() * 2 + 40, y=self.menu.winfo_reqheight() // 2 + 100)
        self.btnSetHealth = Button(self.menu, width=12, font=('Arial', 10), justify='center', borderwidth=5, relief='flat', text="OK", command=lambda:self.setHealthShip())
        self.btnSetHealth.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() * 2 + 30, y=self.menu.winfo_reqheight() // 2 + 140)
        self.btnBack = Button(self.menu, width= 12, font=('Arial', 10), justify='center', text="BACK",command=lambda:self.goBack(main_menu))
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
        try:
            if int(self.entryHealth.get()) > 10:
                messagebox.showinfo("Asteroid", "Can't do more than 10 health buddy.")
            else:
                self.Game.getAsteroidship().setHealth(int(self.entryHealth.get()))
                messagebox.showinfo("Asteroid", "You have successfully changed your speed to: " + str(self.entryHealth.get()) + "!")
        except:
            messagebox.showerror("Asteroid", "Please input an Integer!")
