from tkinter import Tk, Canvas, PhotoImage
from ship import ship
from beam import *
from GameFunc import *
from options import *

def play(main_menu, root):
    main_menu.withdraw()
    root.grab_set()
def openOptions():
    options_menu = Toplevel()
    options_menu.title("Options")
    options_menu.protocol('WM_DELETE_WINDOW', lambda:Game.exit_program())
    options_menu.config(padx=10, background="black")
    options_menu.geometry("%dx%d+%d+%d" % (canvas.winfo_reqwidth(), canvas.winfo_reqheight(),options_menu.winfo_screenwidth()//2 - canvas.winfo_reqwidth() //2, options_menu.winfo_screenheight()//2- canvas.winfo_reqheight() // 2))
    options_menu.grab_set()
    options_menu.resizable(False,False)
    lblAsteroid.place(x=main_menu.winfo_reqwidth() // 2 + lblAsteroid.winfo_reqwidth() // 4, y=main_menu.winfo_reqheight() // 2 - lblAsteroid.winfo_height())
    menuOptions = options(options_menu, Game)



def background_timer():
    global btid
    for i in range(len(background_list)):
        canvas.coords(background_list[i], xpos[i] - 5, 0)
        xpos[i] -= 5

    btid = root.after(60, lambda: background_timer())
    root.update()

    if xpos[0] + imgBackground.width() <= 0:
        xpos[0] = xpos[1] + imgBackground.width()
    if xpos[1] + imgBackground.width() <= 0:
        xpos[1] = xpos[0] + imgBackground.width()

root = Tk()
root.title('Asterpocalypse')
root.protocol('WM_DELETE_WINDOW', lambda:Game.exit_program())
imgBackground = PhotoImage(file='images/space_background.png')
imgTitle = PhotoImage(file='images/asterpocalypse.png')

root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2,
    root.winfo_screenheight() // 2 - imgBackground.height() // 2))

canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
canvas.pack()

background_list = [0] * 2
xpos = [0, imgBackground.width()]

for i in range(len(background_list)):
    background_list[i] = canvas.create_image(xpos[i], 0, image=imgBackground, anchor='nw')

canvas.create_image(canvas.winfo_reqwidth() // 2 - imgTitle.width() // 2, 10, image=imgTitle, anchor='nw')

Game = Game(canvas, root,  background_list)
background_timer()

root.deiconify()
main_menu = Toplevel()
main_menu.title("Main Menu")
main_menu.protocol('WM_DELETE_WINDOW', lambda:Game.exit_program())
main_menu.config(padx=10, background="black")
main_menu.geometry("%dx%d+%d+%d" % (canvas.winfo_reqwidth(), canvas.winfo_reqheight(),main_menu.winfo_screenwidth()//2 - canvas.winfo_reqwidth() //2, main_menu.winfo_screenheight()//2- canvas.winfo_reqheight() // 2))
main_menu.grab_set()
main_menu.resizable(False,False)

lblAsteroid = Label(main_menu, image=imgTitle, background= "black", anchor="c")
lblAsteroid.place(x=main_menu.winfo_reqwidth() // 2 + lblAsteroid.winfo_reqwidth() // 4, y=main_menu.winfo_reqheight() // 2 - lblAsteroid.winfo_height())
btnPlay = Button(main_menu, width= 20, height=1, text="PLAY", font="Calibri 20", anchor = "c", command=lambda:play(main_menu, root))
btnPlay.place( x= main_menu.winfo_reqwidth() // 2 + btnPlay.winfo_reqwidth() - 50, y=main_menu.winfo_reqheight())
btnQuit = Button(main_menu, width= 20, height=1, text="QUIT", font="Calibri 20", anchor="c", command=lambda:Game.exit_program())
btnQuit.place(x=main_menu.winfo_reqwidth() // 2 + btnQuit.winfo_reqwidth() - 50, y=main_menu.winfo_reqheight() + 150)
btnOptions = Button(main_menu, width= 20, height=1, text="OPTIONS", font="Calibri 20", anchor="c", command=openOptions)
btnOptions.place(x=main_menu.winfo_reqwidth() // 2 + btnOptions.winfo_reqwidth() - 50, y=main_menu.winfo_reqheight() + 75)
# btnHighscores = Button(main_menu, width=30, height=2, text="HIGH SCORES",)



root.mainloop()
