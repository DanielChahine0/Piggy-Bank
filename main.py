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
        self.themeBtnSize = 35

        # Configuration Section
        self.root = ct.CTk()
        self.root.iconbitmap("Images/piggy bank.ico")
        self.root.geometry(str(self.WIDTH) + "x" + str(self.HEIGHT)+"+100+100")
        self.root.title("FPB - Fat Piggy Bank")
        ct.set_appearance_mode("Light")
        ct.set_default_color_theme("dark-blue")
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
        self.themeMenu = tk.Menu(self.viewMenu, tearoff=0)
        # self.themeMenu.add_command(label="Red",
        #                            command=self.red_theme,
        #                            font=('Arial', 11))
        # self.themeMenu.add_command(label="Orange",
        #                            command=self.orange_theme,
        #                            font=('Arial', 11))
        # self.themeMenu.add_command(label="Yellow",
        #                            command=self.yellow_theme,
        #                            font=('Arial', 11))
        # self.themeMenu.add_command(label="Green",
        #                            command=self.green_theme,
        #                            font=('Arial', 11))
        # self.themeMenu.add_command(label="Blue",
        #                            command=self.blue_theme,
        #                            font=('Arial', 11))

        # Menu Configuration Section
        self.menubar.add_cascade(menu=self.fileMenu, label="File")
        self.menubar.add_cascade(menu=self.viewMenu, label="View")
        self.viewMenu.add_cascade(menu=self.appearance, label="Change Appearance", font=('Arial', 11))
        # self.viewMenu.add_cascade(menu=self.themeMenu, label="Change Theme", font=('Arial', 11))
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
        self.amountText.place(x=self.WIDTH - self.margin * 5 - self.amountInputWidth,
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

        # Guide Button
        self.guideBtn = ct.CTkButton(self.root, width=self.btnWidth, height=self.btnHeight,
                                     text="GUIDE", font=('Arial', 18, "bold"), command=self.open_guide)
        self.guideBtn.place(x=self.WIDTH - 4.5 * self.margin - self.btnWidth,
                            y=self.pigSize+self.habitInputHeight*2 + self.btnHeight + 5*self.margin)

        # Switch Appearance Button
        self.switchAppearanceBtn = ct.CTkButton(self.root,
                                                text="",
                                                fg_color="#000",
                                                hover_color="#292929",
                                                command=self.switch_appearance,
                                                corner_radius=self.themeBtnSize,
                                                width=self.themeBtnSize,
                                                height=self.themeBtnSize)
        self.switchAppearanceBtn.place(x=self.WIDTH - self.margin//5 - self.themeBtnSize,
                                       y=self.HEIGHT - self.margin//5 - self.themeBtnSize)

        self.root.mainloop()

    def open_guide(self):
        guideWindow = tk.Toplevel()
        guideWindow.title("Guide")
        guideWindow.resizable(False, False)
        guideWindowWidth = 500
        guideWindowHeight = 500
        guideWindow.geometry(""+str(guideWindowWidth)+"x"+str(guideWindowHeight)+"+"
                             + str(100+self.WIDTH//2)+"+"
                             + str(300))
        guideText = self.getText()
        label = ct.CTkLabel(guideWindow, text=guideText, font=('Arial', 15))
        label.pack()

    def getText(self):
        return "HI"

    def change_theme(self):
        themeWindow = tk.Toplevel()
        themeWindow.title("Change Theme")
        themeWindowWidth = 500
        themeWindowHeight = 500
        themeWindow.geometry("" + str(themeWindowWidth) + "x" + str(themeWindowHeight) + "+"
                             + str(100 + self.WIDTH // 2) + "+"
                             + str(300))

    def red_theme(self):
        ct.set_default_color_theme("red")

    def orange_theme(self):
        ct.set_default_color_theme("orange")

    def yellow_theme(self):
        ct.set_default_color_theme("yellow")

    def green_theme(self):
        ct.set_default_color_theme("green")

    def blue_theme(self):
        ct.set_default_color_theme("blue")


    def switch_appearance(self):
        if ct.get_appearance_mode() == "Light":
            self.change_to_dark()
        else:
            self.change_to_light()

    def change_to_light(self):
        ct.set_appearance_mode("Light")
        self.switchAppearanceBtn.configure(fg_color="#000000", hover_color="#292929")

    def change_to_dark(self):
        ct.set_appearance_mode("Dark")
        self.switchAppearanceBtn.configure(fg_color="#ffffff", hover_color="#b8b8b8")


PiggyBank()
