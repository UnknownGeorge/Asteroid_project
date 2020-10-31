from GameFunc import *
from beam import *
from ship import *
from health import *
from tkinter import *

class options:
    def __init__(self, options_menu, Game, main_menu, health):
        '''
        Initializes the top level of options
        
        PARAMETERS:
        -----------
        score: int
            contains the score that the user has
        game: Game function
            contains the game currently being played, and all it's values
        menu: Toplevel()
            contains the menu for the options
        imgBackground: img
            contains an image of the moving background
        canvas3: canvas object
            contains the canvas that stores all the images and objects of the options menu
        xpos: int
            the ex position of the background
        lblSpeed: Label()
            variable containing and initializing the label that contains text 
        lblHealth: Lable()
            variable containing and initializing the label that contains text
        btnSetSpeed: btn()
            variable containing and initializing the button that sets the speed of the ship
        btnSetHealth: btn()
            variable containing and initializing the button that sets the health of the ship
        background_list: list
            contains the list of the background
        updatedSpeed: int
            contains the updated speed of the ship
        healthoption: int
            contains the base stats for the health
        bulletoption: int
            contains the base stats for the bullet amount
        mainmenu: toplevel()
            contains the main menu
        btnBack: btn()
            variable containing a button that send you back to the main menu
        entrySpeed: entry()
            variable containing the entry widget that should contain what the user wants to change the speed to
        entryHealth: entry()
            variable containing the entry widget that should contain what the user wants to change the health to
        health: int
            contains the health of the ship
        '''
        self.menu = options_menu
        self.__speedoption = 20
        self.__healthoption = 10
        self.__bulletoption = 5
        self.Game = Game
        self.Health = health
        self.background_list = [0] * 2
        self.imgBackground = PhotoImage(file='images/space_background.png')
        self.xpos = [0, self.imgBackground.width()]
        self.canvas3 = Canvas(self.menu, width=self.imgBackground.width(), height=self.imgBackground.height())
        self.mainmenu = main_menu
        self.updatedSpeed = 20

        for i in range(len(self.background_list)):
            self.background_list[i] = self.canvas3.create_image(self.xpos[i], 0, image=self.imgBackground, anchor='nw')
        self.background_timer()

        self.lblSpeed = Label(self.menu, width=60, font=('neuropol', 14), anchor="c", text="Set the speed you want your \n ship to move at (max is 50):", bg="black", fg="white")
        self.lblSpeed.place(x=self.menu.winfo_reqwidth() * 2 - self.lblSpeed.winfo_reqwidth() // 2 - 30, y=self.menu.winfo_reqheight() // 2)
        self.entrySpeed = Entry(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat')
        self.entrySpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() + 10, y=self.menu.winfo_reqheight() // 2)
        self.btnSetSpeed = Button(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat', text="OK", command=lambda:self.setSpeedShip())
        self.btnSetSpeed.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() + 15, y=self.menu.winfo_reqheight() // 2 + 40)
        self.lblHealth = Label(self.menu, width=60, font=('neuropol', 14), anchor="c", text="Set the amount of health \n you have (max is 10):", bg="black", fg="white")
        self.lblHealth.place(x=self.menu.winfo_reqwidth() * 2 - self.lblSpeed.winfo_reqwidth() // 2 - 30, y=self.menu.winfo_reqheight() // 2 + 100)
        self.entryHealth = Entry(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat')
        self.entryHealth.place(x=self.menu.winfo_reqwidth() * 2 + self.entryHealth.winfo_reqwidth() + 10, y=self.menu.winfo_reqheight() // 2 + 100)
        self.btnSetHealth = Button(self.menu, width=12, font=('neuropol', 10), justify='center', borderwidth=5, relief='flat', text="OK", command=lambda:self.setHealthShip())
        self.btnSetHealth.place(x=self.menu.winfo_reqwidth() * 2 + self.entrySpeed.winfo_reqwidth() + 15, y=self.menu.winfo_reqheight() // 2 + 140)
        self.btnBack = Button(self.menu, width= 12, font=('neuropol', 10), justify='center', text="BACK",command=lambda:self.goBack())
        self.btnBack.place(x=self.btnBack.winfo_reqwidth() // 2, y=self.menu.winfo_reqheight()*2 + 100)
        self.canvas3.pack()
        self.mainmenu.resizable(False, False)


    def setSpeedShip(self):
        '''
        Set the speed of the ship

        PARAMETERS:
        -----------
        entrySpeed: entry widget
            contains the users preferable speed
        updatedSpeed: int
            contains the updated speed
        '''
        try:
            if int(self.entrySpeed.get()) > 50:
                messagebox.showinfo("Asteroid", "Sorry dude, that is way too fast.")
            else:
                self.updatedSpeed = self.Game.getAsteroidship().setSpeed(int(self.entrySpeed.get()))
                messagebox.showinfo("Asteroid", "You have successfully changed your speed to: " + str(self.entrySpeed.get()))
        except:
            messagebox.showerror("Asteroid", "Please input an Integer!")
    def goBack(self):
        '''
        goes back to the main menu by withdrawing the current menu and grabbing the new menu

        PARAMETERS:
        -----------
        menu: toplevel()
            contains the toplevel of the options menu
        '''
        self.mainmenu.grab_set()
        self.menu.withdraw()
    def setHealthShip(self):
        '''
        Set the health of the ship

        PARAMETERS:
        -----------
        Game: Game function
            contains the game function and all its attributes
        
        entryHealth: entry
            contains the preferred health of the user
        '''
        if int(self.entryHealth.get()) > 10:
            messagebox.showinfo("Asteroid", "Can't do more than 10 health buddy.")
        else:
            self.Game.setHealth(int(self.entryHealth.get()))
            messagebox.showinfo("Asteroid", "You have successfully changed your health to: " + str(self.entryHealth.get()) + "!")
    def background_timer(self):
        '''
        moves the background every 100 milliseconds

        PARAMETERS:
        -----------
        canvas: canvas object
            contains a canvas that contains all the objects and images inside the options menu
        btid: timer
            contains a timer that re calls the function
        xpos: int
            contains the xposition of the backgroundlist
        menu: top_level()
            contains the top level menu for username menu
        imgBackground: img()
            contains the img of the background
        '''
        global btid
        for i in range(len(self.background_list)):
            self.canvas3.coords(self.background_list[i], self.xpos[i] - 5, 0)
            self.xpos[i] -= 5
        btid = self.mainmenu.after(100, lambda: self.background_timer())

        if self.xpos[0] + self.imgBackground.width() <= 0:
            self.xpos[0] = self.xpos[1] + self.imgBackground.width()
        if self.xpos[1] + self.imgBackground.width() <= 0:
            self.xpos[1] = self.xpos[0] + self.imgBackground.width()
    
