from tkinter import *
from GameFunc import *

class scoremenu:
    def __init__(self):
        self.menu = Toplevel()
        self.menu.title("Main Menu")
        self.menu.protocol('WM_DELETE_WINDOW', lambda:self.exit_program())
        self.imgBackground = PhotoImage(file='images/space_background.png')
        self.menu.config(padx=10, background="black")
        self.canvas = Canvas(self.menu, width=self.imgBackground.width(), height=self.imgBackground.height())
        self.menu.geometry("%dx%d+%d+%d" % (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.menu.winfo_screenwidth()//2 - self.canvas.winfo_reqwidth() //2, self.menu.winfo_screenheight()//2- self.canvas.winfo_reqheight() // 2))
        self.menu.grab_set()
        self.background_list = [0] * 2
        self.xpos = [0, self.imgBackground.width()]

        for i in range(len(self.background_list)):
            self.background_list[i] = self.canvas.create_image(self.xpos[i], 0, image=self.imgBackground, anchor='nw')
        self.background_timer(self.menu)

        self.canvas.pack()

        self.lblLost = Label(self.canvas, font=('neuropol', 14), text="You have lost, But you got the score:", fg="white")
        self.lblLost.place(x=self.canvas.winfo_reqwidth() // 2, y= self.canvas.winfo_reqheight())
    def exit_program(self):
        answer = messagebox.askyesno("Asterpocalypse", "Are you sure you want to quit?")
        if answer == True:
            quit()
        else:
            pass
    def background_timer(self):
        global btid
        for i in range(len(self.background_list)):
            self.canvas.coords(self.background_list[i], self.xpos[i] - 5, 0)
            self.xpos[i] -= 5
        btid = self.menu.after(100, lambda: self.background_timer())

        if self.xpos[0] + self.imgBackground.width() <= 0:
            self.xpos[0] = self.xpos[1] + self.imgBackground.width()
        if self.xpos[1] + self.imgBackground.width() <= 0:
            self.xpos[1] = self.xpos[0] + self.imgBackground.width()