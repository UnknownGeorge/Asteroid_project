# Import modules
from tkinter import Tk, Canvas, PhotoImage, simpledialog, scrolledtext, END
from ship import ship
from beam import *
from GameFunc import *
from options import *
from health import *
from usernamemenu import *
from File import *
import pygame

# Create frame that has highscores
# Make scoremenu work!

# Makes the game start
def play(main_menu, root):
    root.deiconify()
    main_menu.deiconify()
    root.grab_set()
    Game.set_name(name.getUsername())
    Game.setStop(False)
    Game.start()

# Open Option Menu
def openOptions(Game, main_menu):
    main_menu.deiconify()
    options_menu = Toplevel()
    options_menu.title("Options")
    options_menu.protocol('WM_DELETE_WINDOW', lambda:Game.exit_program())
    options_menu.config(padx=10, background="black")
    options_menu.geometry("%dx%d+%d+%d" % (canvas.winfo_reqwidth(), canvas.winfo_reqheight(),options_menu.winfo_screenwidth()//2 - canvas.winfo_reqwidth() //2, options_menu.winfo_screenheight()//2- canvas.winfo_reqheight() // 2))
    options_menu.grab_set()
    options_menu.resizable(False,False)
    canvas2.coords(475, 99)
    menuOptions = options(options_menu, Game, main_menu, health)

# Background timer for root menu
def background_timer():
    global btid
    for i in range(len(background_list)):
        canvas.coords(background_list[i], xpos[i] - 5, 0)
        xpos[i] -= 5
    btid = root.after(100, lambda: background_timer())

    if xpos[0] + imgBackground.width() <= 0:
        xpos[0] = xpos[1] + imgBackground.width()
    if xpos[1] + imgBackground.width() <= 0:
        xpos[1] = xpos[0] + imgBackground.width()

# Background timer for main menu
def background_timer2(main_menu):
    global btid
    for i in range(len(background_list)):
        canvas2.coords(background_list[i], xpos[i] - 5, 0)
        xpos[i] -= 5
    btid = main_menu.after(100, lambda: background_timer2(main_menu))

    if xpos[0] + imgBackground.width() <= 0:
        xpos[0] = xpos[1] + imgBackground.width()
    if xpos[1] + imgBackground.width() <= 0:
        xpos[1] = xpos[0] + imgBackground.width()

# Retrieve High Scores
def get_top10():
    value = 0

    files = top_file()
    txtOutput.config(state="normal")
    txtOutput.delete('0.0', END)
    txtOutput.insert(END, "{0:<5s}{1:<15s}{2:<10s}\n".format("Rank", "Name","Score"))
    for y in range(len(files.top10())):

        for index, x in enumerate(files.top10()[y]):
            if not index % 2 == 0:
                txtOutput.config(state="normal")
                txtOutput.insert(END, "{0:<5d}{1:<15s}{2:<10s}\n".format(value + 1, x.get('name'), str(x.get('score'))))
                value += 1
                txtOutput.config(state="disabled")



# Initialize Window
root = Tk()
root.title('Asterpocalypse')
root.resizable(False, False)
imgBackground = PhotoImage(file='images/space_background.png')
imgTitle = PhotoImage(file='images/asterpocalypse.png')
root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2,
    root.winfo_screenheight() // 2 - imgBackground.height() // 2))
# Initialize Background Music
pygame.mixer.init()
pygame.mixer.music.load("Audio_Files/Battle_Against_a_Weird_Opponent.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 2.00)
root.protocol('WM_DELETE_WINDOW', lambda:Game.exit_program())

# Initialize Canvas
canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
canvas.pack()

# Create Moving Background
background_list = [0] * 2
xpos = [0, imgBackground.width()]
for i in range(len(background_list)):
    background_list[i] = canvas.create_image(xpos[i], 0, image=imgBackground, anchor='nw')

# Create top level frame (Main Menu)
canvas.create_image(canvas.winfo_reqwidth() // 2 - imgTitle.width() // 2, 10, image=imgTitle, anchor='nw')
root.deiconify()
main_menu = Toplevel()
Game = Game(canvas, root, main_menu, get_top10)
background_timer()
root.update()
main_menu.title("Main Menu")
main_menu.protocol('WM_DELETE_WINDOW', lambda:Game.exit_program())
main_menu.config(padx=10, background="black")
main_menu.geometry("%dx%d+%d+%d" % (canvas.winfo_reqwidth(), canvas.winfo_reqheight(),main_menu.winfo_screenwidth()//2 - canvas.winfo_reqwidth() //2, main_menu.winfo_screenheight()//2- canvas.winfo_reqheight() // 2))
main_menu.grab_set()
canvas2 = Canvas(main_menu, width=imgBackground.width(), height=imgBackground.height())
canvas2.pack()
background_timer2(main_menu)
main_menu.resizable(False,False)

# Create Moving Background again
for i in range(len(background_list)):
    background_list[i] = canvas2.create_image(xpos[i], 0, image=imgBackground, anchor='nw')

# Create components:
# Asteroid Picture
lblAsteroid = canvas2.create_image(main_menu.winfo_reqwidth() * 2 + 75, 99, image=imgTitle)
# Play, Quit and Options Buttons
btnPlay = Button(main_menu, width= 20, height=1, text="PLAY", font="neuropol 20", anchor = "c", command=lambda:play(main_menu, root))
btnPlay.place( x= main_menu.winfo_reqwidth() // 2 + btnPlay.winfo_reqwidth() - 475, y=main_menu.winfo_reqheight())
btnQuit = Button(main_menu, width= 20, height=1, text="QUIT", font="neuropol 20", anchor="c", command=lambda:Game.exit_program())
btnQuit.place(x=main_menu.winfo_reqwidth() // 2 + btnQuit.winfo_reqwidth() - 475, y=main_menu.winfo_reqheight() + 150)
btnOptions = Button(main_menu, width= 20, height=1, text="OPTIONS", font="neuropol 20", anchor="c", command=lambda:openOptions(Game, main_menu))
btnOptions.place(x=main_menu.winfo_reqwidth() // 2 + btnOptions.winfo_reqwidth() - 475, y=main_menu.winfo_reqheight() + 75)
# Highscore label + Output
lblHighscores = LabelFrame(main_menu, width=300, height=350, bg="black", font="neuropol 14", text="Top 10 Highscores", fg="White")
lblHighscores.place(x=main_menu.winfo_reqwidth() // 2 + lblHighscores.winfo_reqwidth() + 200, y=main_menu.winfo_reqheight() - 22)
txtOutput = scrolledtext.ScrolledText(lblHighscores, width=30, height=12, font="Courier 10", padx=5, pady=5, state="disabled", bg="black", fg="white")
txtOutput.pack()
get_top10()
name = usernamemenu(main_menu)


root.mainloop()
