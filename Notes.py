from tkinter import *
from tkinter import simpledialog
from random import choice

root = Tk()
root.geometry("800x1000")
root.title("Regrigerator Notes")


def showPopupMenu(event):
    global mousex, mousey
    mousex = event.x_root
    mousey = event.y_root
    popupmenu.post(event.x_root, event.y_root)


def addLabel():
    Notes = simpledialog.askstring("Refrigerator Notes", "What do you want on you refrigerator?")
    MyLabel = Label(root, bg=choice(["red", "orange", "yellow", "green", "sky blue", "gray", "pink"]), text=Notes , height=2, width=int(len(Notes)/2+10))
    MyLabel.place(x=mousex-115, y=mousey-90)



popupmenu = Menu(root, tearoff=False)
popupmenu.add_command(label="New Note", command=addLabel, accelerator="Ctrl+N")


Refrigerator = PhotoImage(file="Refrigerator.gif")
BackGround = Label(root, image=Refrigerator)
BackGround.pack()


root.bind("<Button-3>", showPopupMenu)
root.mainloop()