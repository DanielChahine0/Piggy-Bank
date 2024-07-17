import customtkinter as ct
from PIL import Image
import tkinter as tk


class PiggyBank:
    def __init__(self):
        # Size Configuration
        self.WIDTH = 1200
        self.HEIGHT = 600
        self.pigSize = 300
        self.margin = 25
        self.habitInputWidth = 250
        self.habitInputHeight = self.amountInputHeight = 30
        self.amountInputWidth = 100
        self.btnWidth = 125
        self.btnHeight = 40

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
        # View Section in the Menu
        self.viewMenu = tk.Menu(self.menubar, tearoff=0)
        self.appearance = tk.Menu(self.viewMenu, tearoff=0)
        self.appearance.add_command(label="Dark Mode",
                                    command=self.change_to_dark,
                                    font=('Arial', 11))
        self.appearance.add_command(label="Light Mode",
                                    command=self.change_to_light,
                                    font=('Arial', 11))
        self.appearance.add_command(label="System Mode",
                                    command=self.change_to_system,
                                    font=('Arial', 11))
        # Menu Configuration Section
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.menubar.add_cascade(menu=self.viewMenu, label="View")
        self.viewMenu.add_cascade(menu=self.appearance, label="Change Appearance", font=('Arial', 11))
        self.root.configure(menu=self.menubar)

        # Piggy Bank Photo
        self.img = Image.open("Images/piggy bank.png")
        self.image = ct.CTkImage(light_image=self.img, size=(self.pigSize, self.pigSize))
        self.panel = ct.CTkLabel(self.root, image=self.image, text='')
        self.panel.place(x=self.WIDTH-self.pigSize-self.margin,
                         y=self.margin)

        # Habit Input Text
        self.habitText = ct.CTkTextbox(self.root, height=self.habitInputHeight, width=self.habitInputWidth,
                                       font=('Arial', 15))
        self.habitText.place(x=self.WIDTH-self.margin*2-self.habitInputWidth,
                             y=self.pigSize+2*self.margin)

        # Amount Input Text
        self.amountText = ct.CTkTextbox(self.root, height=self.amountInputHeight, width=self.amountInputWidth,
                                        font=('Arial', 15))
        self.amountText.place(x=self.WIDTH - self.margin*5 - self.amountInputWidth,
                              y=self.pigSize + self.margin * 3 + self.habitInputHeight)

        # Add and Remove Buttons
        self.addAmountBtn = ct.CTkButton(self.root, width=self.btnWidth, height=self.btnHeight,
                                         text="ADD", font=('Arial', 18, "bold"))
        self.addAmountBtn.place(x=self.WIDTH - self.margin * 2.5 - self.btnWidth * 2,
                                y=self.margin*4 + self.pigSize + self.habitInputHeight + self.amountInputHeight)
        self.removeAmountBtn = ct.CTkButton(self.root, width=self.btnWidth, height=self.btnHeight,
                                            text="REMOVE", font=('Arial', 18, "bold"))
        self.removeAmountBtn.place(x=self.WIDTH - self.margin * 1.5 - self.btnWidth,
                                   y=self.margin*4 + self.pigSize + self.habitInputHeight + self.amountInputHeight)

        self.root.mainloop()

    def change_to_light(self):
        ct.set_appearance_mode("Light")

    def change_to_dark(self):
        ct.set_appearance_mode("Dark")

    def change_to_system(self):
        ct.set_appearance_mode("System")

PiggyBank()
