import customtkinter as ct
import tkinter as tk
from tkinter import font


class PiggyBank:
    def __init__(self):
        self.root = ct.CTk()
        self.root.iconbitmap("Images/piggy bank.ico")
        # Configuration Section
        self.root.geometry("800x600")
        self.root.title("FPB - Fat Piggy Bank")

        # Menu Section
        self.menubar = tk.Menu(self.root)
        self.fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=exit, font=('Arial', 11))

        # Menu Configuration Section
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.root.configure(menu=self.menubar)


        self.root.mainloop()


PiggyBank()
