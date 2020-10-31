from tkinter import *
from GameFunc import *

class usernamemenu:
    def __init__(self, main_menu):
        '''
        Initializes the top level of entering your username
        
        PARAMETERS:
        -----------
        score: int
            contains the score that the user has
        menu: Toplevel()
            username menu that asks you what your username is
        imgBackground: img
            contains an image of the moving background
        canvas: canvas object
            contains the canvas that stores all the images and objects of the main menu
        xpos: int
            the ex position of the background
        lblUsername: Label()
            variable containing and initializing the label that contains text telling you to enter your username
        entryUsername: Entry()
            contains the entry widget of the username to be entered
        btnEnter: btn()
            contains the button that enters the username and passes it to the game function
        value: int
            contains the indexing for reading a file
        username: str
            contains the name of the user
        backgroundlist: list
            contains a list of all the backgrounds
        imgBackground: img
            contains the img of the current background
        
        '''
        self.mainmenu = main_menu
        self.menu = Toplevel()
        self.menu.title("Main Menu")
        self.menu.protocol('WM_DELETE_WINDOW', lambda:self.exit_program())
        self.imgBackground = PhotoImage(file='images/space_background.png')
        self.menu.config(padx=10, background="black")
        self.canvas = Canvas(self.menu, width=self.imgBackground.width(), height=self.imgBackground.height())
        self.menu.geometry("%dx%d+%d+%d" % (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.menu.winfo_screenwidth()//2 - self.canvas.winfo_reqwidth() //2, self.menu.winfo_screenheight()//2- self.canvas.winfo_reqheight() // 2))
        self.menu.grab_set()
        self.background_list = [0] * 2
        self.username = ""
        self.xpos = [0, self.imgBackground.width()]

        for i in range(len(self.background_list)):
            self.background_list[i] = self.canvas.create_image(self.xpos[i], 0, image=self.imgBackground, anchor='nw')
        self.background_timer()

        self.canvas.pack()

        self.lblUsername = Label(self.canvas, font=('neuropol', 28), text="Insert your username here!:", fg="white", bg="black", anchor="c")
        self.lblUsername.place(x=self.canvas.winfo_reqwidth() // 4 - 100, y= self.canvas.winfo_reqheight() // 2 - 100)
        self.entryUsername = Entry(self.canvas, width=20, font = ('neuropol', 20))
        self.entryUsername.place(x=self.canvas.winfo_reqwidth() // 4 - 20, y= self.canvas.winfo_reqheight() // 2 - 25)
        self.btnEnter = Button(self.canvas, font=('neuropol', 20), text="ENTER", anchor="c", command=lambda:self.EnterUsername())
        self.btnEnter.place(x= self.canvas.winfo_reqwidth() // 4 + 175, y=self.canvas.winfo_reqheight() - self.canvas.winfo_reqheight() // 2 + 50)
        
        self.menu.resizable(False, False)

    def exit_program(self):
        '''
        exits the entire program

        PARAMETERS:
        -----------
        answer: boolean
            contains a boolean value that should ask the user if they want to exit or not
        '''
        answer = messagebox.askyesno("Asterpocalypse", "Are you sure you want to quit?")
        if answer == True:
            quit()
        else:
            pass
    def background_timer(self):
        '''
        moves the background every 100 milliseconds

        PARAMETERS:
        -----------
        canvas: canvas object
            contains a canvas that contains all the objects and images inside the username menu
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
            self.canvas.coords(self.background_list[i], self.xpos[i] - 5, 0)
            self.xpos[i] -= 5
        btid = self.menu.after(100, lambda: self.background_timer())

        if self.xpos[0] + self.imgBackground.width() <= 0:
            self.xpos[0] = self.xpos[1] + self.imgBackground.width()
        if self.xpos[1] + self.imgBackground.width() <= 0:
            self.xpos[1] = self.xpos[0] + self.imgBackground.width()
    def EnterUsername(self):
        '''
        Enters the username and sets the username to what the user inputted into the entry widget

        PARAMETERS:
        -----------
        entryUsername: entry widget
            is an entrywidget that contains the username that the user wishes to enter
        username: str
            the name of the user
        mainmenu: topLevel()
            the main menu containing the buttons to play the game, options to set settings and quit to quit the entire program
        '''
        if self.entryUsername.get() == "":
            messagebox.showinfo("Asterpocalypse", "Please enter username!")
        else:
            self.username = self.entryUsername.get()
            self.menu.withdraw()
            self.mainmenu.grab_set()
    def getUsername(self):
        '''
        Gets the username of the player

        RETURNS:
        -----------
        username: str
            contains the name of the user
        '''
        return self.username
