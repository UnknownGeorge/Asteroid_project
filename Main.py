from tkinter import Tk, Canvas, PhotoImage
from ship import ship

def onkeypress(event):
    if event.char == "w":
        asteroidship.move(y=-20)
    elif event.char == "a":
        asteroidship.move(x=-20)
    elif event.char == "s":
        asteroidship.move(y=20)
    elif event.char == "d":
        asteroidship.move(x=20)
def onmouse(event):
    print("casualty")
    #Shoot the bullet :D
def checkCollision(event):
    pass
def exit_program():
    root.after_cancel(btid)
    exit()

def background_timer():
    global btid
    for i in range(len(background_list)):
        canvas.coords(background_list[i], xpos[i] - 5, 0)
        xpos[i] -= 5

    btid = root.after(50, lambda: background_timer())
    root.update()

    if xpos[0] + imgBackground.width() <= 0:
        xpos[0] = xpos[1] + imgBackground.width()
    if xpos[1] + imgBackground.width() <= 0:
        xpos[1] = xpos[0] + imgBackground.width()

root = Tk()
root.title('Asterpocalypse')
root.bind('<KeyPress>', onkeypress)
root.bind('<Button-1>', onmouse)
root.protocol('WM_DELETE_WINDOW', exit_program)

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

asteroidship = ship(0, 0, canvas)

background_timer()

root.mainloop()
