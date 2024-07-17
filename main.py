import customtkinter as ct
import tkinter as tk


class PiggyBank:
    def __init__(self):
        # Configuration Section
        self.WIDTH = 1200
        self.HEIGHT = 600
        self.root = ct.CTk()
        self.root.iconbitmap("Images/piggy bank.ico")
        self.root.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT)+"+100+100")
        self.root.title("FPB - Fat Piggy Bank")

        # Menu Section
        self.menubar = tk.Menu(self.root)
        # File Section in the Menu
        self.fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=exit, font=('Arial', 11))
        # Menu Configuration Section
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.root.configure(menu=self.menubar)

        # Frame Section
        self.mainframe = ct.CTkFrame(self.root)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.columnconfigure(2, weight=1)
        self.btn = ct.CTkButton(self.mainframe, text="1")
        self.btn1 = ct.CTkButton(self.mainframe, text="2")
        self.btn.grid(row=0, column=1, sticky=ct.W+ct.E)
        self.btn1.grid(row=1, column=0, sticky=ct.W+ct.E)

        self.mainframe.pack(fill='x')



        self.root.mainloop()


PiggyBank()
