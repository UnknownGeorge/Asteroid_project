from tkinter import Tk, Canvas, PhotoImage
from ship import ship
from beam import *
from GameFunc import *

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

lblAsteroid = Label(main_menu, iamge=imgTitle)
lblAsteroid.place(x=main_menu.winfo_reqwidth() // 2 + lblAsteroid.winfo_reqwidth(), y=main_menu.winfo_reqheight() - 10)
btnPlay = Button(main_menu, width= 30, height=4, text="PLAY", font="Calibri", anchor = "c")
btnPlay.place( x= main_menu.winfo_reqwidth() // 2 + btnPlay.winfo_reqwidth(), y=main_menu.winfo_reqheight())



root.mainloop()

