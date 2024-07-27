import customtkinter as ct
from PIL import Image
import tkinter as tk


class PiggyBank:
    def __init__(self):
        # shared variables
        self.guideAmount = None
        self.guideHabit = None
        self.textLabel = None
        self.total = self.get_total()

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

        # Amount inside the piggy bank1
        self.totalLabel = ct.CTkLabel(self.root,
                                      text="${:,.2f}".format(self.total),
                                      font=('Arial', 45, "bold"),
                                      bg_color="#FFA4A0",
                                      fg_color="transparent")
        self.totalLabel.place(x=self.WIDTH - self.pigSize - self.margin + self.pigSize // 2,
                              y=self.margin*2 + self.pigSize // 2,
                              anchor="center")

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
        self.amountText.bind("<KeyRelease>", self.validate_input)

        # Add and Remove Buttons
        self.addAmountBtn = ct.CTkButton(self.root,
                                         width=self.btnWidth,
                                         height=self.btnHeight,
                                         text="ADD",
                                         font=('Arial', 18, "bold"),
                                         command=self.add_to_bank)
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

        # Scrollable frame to display the latest updates
        self.update_frame_width = 250
        self.update_frame_height = self.HEIGHT - self.margin * 3
        self.update_frame = ct.CTkScrollableFrame(self.root,
                                                  width=self.update_frame_width,
                                                  height=self.update_frame_height)
        self.update_frame.place(x=self.WIDTH - self.pigSize - self.margin * 3 - self.update_frame_width,
                                y=self.margin)
        # Text inside the scrollable frame
        self.update_text = ct.CTkLabel(self.update_frame,
                                       width=10,
                                       font=('Arial', 15))
        self.update_text.pack()
        self.update_root()

        self.root.mainloop()

    def add_to_bank(self):
        # Convert the input into text
        habit_text = self.habitText.get("1.0", "end-1c").strip()
        amount_text = self.amountText.get("1.0", "end-1c").strip()

        # Check if the inputs are not empty
        if habit_text and amount_text:
            f = open("Data/data.txt", "a")
            text = habit_text + " #-# " + amount_text + "\n"
            f.write(text)
            f.close()

            # Clear the input fields after the inputs has been added
            self.habitText.delete("1.0", "end-1c")
            self.amountText.delete("1.0", "end-1c")

            # Update the total
            self.total = self.get_total()
            self.total += int(amount_text)
            self.save_total()
            self.update_root()

    def save_total(self):
        with open("Data/total.txt", "r") as f:
            lines = f.readlines()
        with open("Data/total.txt", "w") as f:
            f.write(str(self.total) + "\n")
            f.writelines(lines)

    def update_root(self):
        self.update_updateFrame()
        self.update_total()

    def update_updateFrame(self):
        with open("Data/data.txt", "r") as f:
            text = ""
            for line in f:
                habit, amount = line.split("#-#")
                habit = habit.strip()
                amount = amount.strip()
                text += "["+str(self.total)+"]"+amount + " " + habit + "\n"
                self.update_text.configure(text=text)

    def update_total(self):
        self.total = self.get_total()
        self.totalLabel.configure(text="${:,.2f}".format(self.total))

    def get_total(self):
        with open("Data/total.txt", "r") as f:
            lines = f.readlines()
            if lines:
                return int(lines[0].strip())
            return 0

    def validate_input(self, event):
        new_value = self.amountText.get("1.0", "end-1c")
        if not new_value.isdigit():
            self.amountText.delete("1.0", "end")
            self.amountText.insert("1.0", ''.join(filter(str.isdigit, new_value)))

    def open_guide(self):
        # Create a new window
        guideWindow = ct.CTkToplevel()
        guideWindow.title("Guide")
        guideWindow.resizable(False, False)
        guideMargin = 25
        guideWindowWidth = 500
        guideWindowHeight = 550
        guideWindow.geometry(""+str(guideWindowWidth)+"x"+str(guideWindowHeight)+"+"
                             + str(200+self.WIDTH//2-guideWindowWidth//2)+"+"
                             + str(150))

        # Make a frame
        scrollable_frame = ct.CTkScrollableFrame(guideWindow,
                                                 width=guideWindowWidth,
                                                 height=guideWindowHeight-175)
        scrollable_frame.pack(pady=20, padx=20)

        # Get the text from the txt file and display it
        guideText = self.getText()
        fontSize = 15  # Ensure the font size is at least 10
        self.textLabel = ct.CTkLabel(scrollable_frame,
                                     width=10,
                                     text=guideText,
                                     font=('Arial',  fontSize))
        self.textLabel.pack()

        # ADD and CLEAR Buttons
        btnHeight = 40
        btnWidth = (guideWindowWidth - 7 * guideMargin)//2
        guideAddBtn = ct.CTkButton(guideWindow,
                                   width=btnWidth,
                                   height=btnHeight,
                                   text="ADD",
                                   font=('Arial', 15),
                                   corner_radius=30,
                                   command=self.add_to_guide)
        guideAddBtn.place(x=3*guideMargin,
                          y=guideWindowHeight-guideMargin-btnHeight)
        guideClearBtn = ct.CTkButton(guideWindow,
                                     width=btnWidth,
                                     height=btnHeight,
                                     text="CLEAR",
                                     font=('Arial', 15),
                                     corner_radius=30,
                                     command=self.clear_guide)
        guideClearBtn.place(x=4*guideMargin + btnWidth,
                            y=guideWindowHeight-guideMargin-btnHeight)

        # Guide Input & Amount Text
        guideHabitWidth = 300
        guideHabitHeight = guideAmountHeight = 30
        guideAmountWidth = guideWindowWidth - 3 * guideMargin - guideHabitWidth
        self.guideHabit = ct.CTkTextbox(guideWindow,
                                        height=guideHabitHeight,
                                        width=guideHabitWidth,
                                        font=('Arial', 15))
        self.guideHabit.place(x=guideMargin,
                              y=guideWindowHeight - 2*guideMargin - guideHabitHeight - btnHeight)

        self.guideAmount = ct.CTkTextbox(guideWindow,
                                         height=guideAmountHeight,
                                         width=guideAmountWidth,
                                         font=('Arial', 15))
        self.guideAmount.place(x=guideMargin * 2 + guideHabitWidth,
                               y=guideWindowHeight - 2 * guideMargin - guideHabitHeight - btnHeight)

        # put the focus on the window to make it on top
        guideWindow.lift()
        guideWindow.focus_force()
        guideWindow.grab_set()

    def add_to_guide(self):
        # Convert the input into text
        habit_text_guide = self.guideHabit.get("1.0", "end-1c").strip()
        amount_text_guide = self.guideAmount.get("1.0", "end-1c").strip()

        # Check if the inputs are not empty
        if habit_text_guide and amount_text_guide:
            f = open("Data/guide.txt", "a")
            text = habit_text_guide + " #-# " + amount_text_guide + "\n"
            f.write(text)
            f.close()
            # Clear the input fields after the inputs has been added
            self.guideAmount.delete("1.0", "end-1c")
            self.guideHabit.delete("1.0", "end-1c")

        self.update_guide_text()

    def clear_guide(self):
        f = open("Data/guide.txt", "w")
        f.write("")
        f.close()
        self.update_guide_text()

    def update_guide_text(self):
        guideText = self.getText()
        self.textLabel.configure(text=guideText)

    def getText(self):
        text = ""
        f = open("Data/guide.txt", "r")
        counter = 0
        for line in f:
            counter += 1
            habit, amount = line.split("#-#")
            habit = habit.strip()
            amount = amount.strip()
            text += habit + " " + amount + "$\n"
        f.close()
        return text

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
