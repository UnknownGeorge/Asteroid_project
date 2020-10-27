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
# def create_menu():
#     main_menu = Toplevel()
#     main_menu.title("Main Menu")
#     main_menu.config(padx=10)
#     canvas2 = Canvas(main_menu)
#     main_menu.geometry("%dx%d+%d+%d" % (canvas2.winfo_reqwidth(), canvas2.winfo_reqheight(),main_menu.winfo_screenwidth()//2 - canvas2.winfo_reqwidth() //2, main_menu.winfo_screenheight()//2- canvas2.winfo_reqheight() // 2))
#     main_menu.grab_set()
#     return canvas2
# canvas2 = create_menu()

root = Tk()
root.title('Asterpocalypse')
root.protocol('WM_DELETE_WINDOW', lambda:Game.exit_program())
imgBackground = PhotoImage(file='images/space_background.png')
imgTitle = PhotoImage(file='images/asterpocalypse.png')

root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2,
    root.winfo_screenheight() // 2 - imgBackground.height() // 2))

canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
canvas.pack()

main_menu = Toplevel()
main_menu.title("Main Menu")
main_menu.config(padx=10)
main_menu.geometry("%dx%d+%d+%d" % (canvas.winfo_reqwidth(), canvas.winfo_reqheight(),main_menu.winfo_screenwidth()//2 - canvas.winfo_reqwidth() //2, main_menu.winfo_screenheight()//2- canvas.winfo_reqheight() // 2))
main_menu.grab_set()

root.deiconify()

background_list = [0] * 2
xpos = [0, imgBackground.width()]

for i in range(len(background_list)):
    background_list[i] = canvas.create_image(xpos[i], 0, image=imgBackground, anchor='nw')

canvas.create_image(canvas.winfo_reqwidth() // 2 - imgTitle.width() // 2, 10, image=imgTitle, anchor='nw')

Game = Game(canvas, root,  background_list)

main_menu.mainloop()
background_timer()
root.mainloop()
