from level_1 import play
from level_2 import play1
from tkinter import *
from PIL import ImageTk, Image
import pygame

menu = Tk()
menu.geometry("418x500")
menu.title("Tic Tac Toe")
menu.iconbitmap("favicon (1).ico")
menu.resizable(False, False)
menu.img = Image.open("ggg.png")  # Setting up the background image
menu.bg = ImageTk.PhotoImage(menu.img)
welcome_frame = Label(menu, image=menu.bg)
welcome_frame.pack(fill=BOTH, expand=True)
pygame.mixer.init()

def level_one():
    menu.destroy()
    if __name__ == '__main__':
        play()

def level_two():
    menu.destroy()
    if __name__ == '__main__':
        play1()


himg = PhotoImage(file=r"heading.png")
head = Label(welcome_frame, image=himg, bg="#001d76", height=35)
head.pack(padx=10, pady=20)

b1img = PhotoImage(file=r"3grid.png")
Button(welcome_frame, text="Level-1", image=b1img, fg='black', font=('italic', 18), bg="#001d76",
       command=level_one).pack(padx=10,
                               pady=10,
                               side='left')

b2img = PhotoImage(file=r"5grid.png")
Button(welcome_frame, text="Level-2", image=b2img, fg='black', font=('italic', 18), bg="#001d76",
       command=level_two).pack(padx=20,
                               pady=10,
                               side='right')
limg = PhotoImage(file=r"select level.png")
level_1 = Label(menu, image=limg, fg="black", background="#001d76", padx=20, pady=10, font=("", 15))
level_1.place(x=98, y=138)

menu.mainloop()
