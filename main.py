import customtkinter as ct
from PIL import Image
import tkinter as tk


class PiggyBank:
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 600
        self.pigSize = 250
        self.pigMargin = 20

        # Configuration Section
        self.root = ct.CTk()
        self.root.iconbitmap("Images/piggy bank.ico")
        self.root.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT)+"+100+100")
        self.root.title("FPB - Fat Piggy Bank")
        ct.set_appearance_mode("Light")
        self.root.resizable(False, False)

        # Menu Section
        self.menubar = tk.Menu(self.root)
        # File Section in the Menu
        self.fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=exit, font=('Arial', 11))
        # Menu Configuration Section
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.root.configure(menu=self.menubar)

        # Piggy Bank Photo
        self.img = Image.open("Images/piggy bank.png")
        self.image = ct.CTkImage(light_image=self.img, size=(self.pigSize, self.pigSize))
        self.panel = ct.CTkLabel(self.root, image=self.image, text='')
        self.panel.place(x=self.WIDTH-self.pigSize-self.pigMargin*3, y=self.pigMargin)

        # Habit Input Text


        self.root.mainloop()


PiggyBank()
