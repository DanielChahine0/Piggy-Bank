import customtkinter as ct
from PIL import Image
import tkinter as tk
from tkcalendar import DateEntry
import json
import tkinter.messagebox as messagebox
# from datetime import date


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
        self.margin = 15
        self.habitInputWidth = self.pigSize - 110
        self.habitInputHeight = self.amountInputHeight = 30
        self.amountInputWidth = self.pigSize - 135
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
        self.fontname = 'Times New Roman'

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
                                      font=(self.fontname, 45, "bold"),
                                      bg_color="#FFA4A0",
                                      fg_color="transparent")
        self.totalLabel.place(x=self.WIDTH - self.pigSize - self.margin + self.pigSize // 2,
                              y=self.margin*3 + self.pigSize // 2,
                              anchor="center")

        # Habit Input Text
        self.HabitLabelWidth = 110
        self.habitLabel = ct.CTkLabel(self.root,
                                      text="Enter Habit: ",
                                      font=(self.fontname, 22))
        self.habitLabel.place(x=self.WIDTH-self.pigSize-self.margin,
                              y=self.pigSize+2*self.margin)
        self.habitText = ct.CTkTextbox(self.root, height=self.habitInputHeight,
                                       width=self.habitInputWidth,
                                       font=(self.fontname, 15))
        self.habitText.place(x=self.WIDTH-self.pigSize-self.margin+self.HabitLabelWidth,
                             y=self.pigSize+2*self.margin)

        # Amount Input Text
        self.amountLabelWidth = 135
        self.amountLabel = ct.CTkLabel(self.root,
                                       text="Enter Amount: ",
                                       font=(self.fontname, 22),
                                       width=self.amountLabelWidth)
        self.amountLabel.place(x=self.WIDTH-self.pigSize-self.margin,
                               y=self.pigSize+3*self.margin+self.habitInputHeight)
        self.amountText = ct.CTkTextbox(self.root,
                                        height=self.amountInputHeight,
                                        width=self.amountInputWidth,
                                        font=(self.fontname, 15))
        self.amountText.place(x=self.WIDTH-self.pigSize-self.margin+self.amountLabelWidth,
                              y=self.pigSize + self.margin * 3 + self.habitInputHeight)
        self.amountText.bind("<KeyRelease>", self.validate_input)

        # Add and Remove Buttons
        self.addAmountBtn = ct.CTkButton(self.root,
                                         width=self.btnWidth,
                                         height=self.btnHeight,
                                         text="ADD",
                                         font=(self.fontname, 20),
                                         command=self.add_to_bank)
        self.addAmountBtn.place(x=self.WIDTH-self.margin*2.5-self.btnWidth*2,
                                y=self.margin*4+self.pigSize+self.habitInputHeight+self.amountInputHeight)
        self.removeAmountBtn = ct.CTkButton(self.root,
                                            width=self.btnWidth,
                                            height=self.btnHeight,
                                            text="REMOVE",
                                            font=(self.fontname, 20),
                                            command=self.remove_from_bank)
        self.removeAmountBtn.place(x=self.WIDTH - self.margin * 1.5 - self.btnWidth,
                                   y=self.margin*4 + self.pigSize + self.habitInputHeight + self.amountInputHeight)

        # Clear Button
        self.clearBtn = ct.CTkButton(self.root, width=self.btnWidth, height=self.btnHeight,
                                     text="CLEAR", font=(self.fontname, 20), command=self.clear_data)
        self.clearBtn.place(x=self.WIDTH-self.margin*2.5-self.btnWidth*2,
                            y=self.pigSize+self.habitInputHeight*2+self.btnHeight+4.6*self.margin)

        # Guide Button
        self.guideBtn = ct.CTkButton(self.root, width=self.btnWidth, height=self.btnHeight,
                                     text="GUIDE", font=(self.fontname, 20), command=self.open_guide)
        self.guideBtn.place(x=self.WIDTH-self.margin*1.5 - self.btnWidth,
                            y=self.pigSize+self.habitInputHeight*2+self.btnHeight+4.6*self.margin)

        # Display Logs Button
        self.displayLogsBtn = ct.CTkButton(self.root,
                                           width=self.btnWidth*2+self.margin,
                                           height=self.btnHeight,
                                           command=self.display_logs,
                                           text="DISPLAY LOGS",
                                           font=(self.fontname, 20),
                                           corner_radius=self.btnWidth)
        self.displayLogsBtn.place(x=self.WIDTH-self.margin*2.5-self.btnWidth*2,
                                  y=self.HEIGHT-self.btnHeight-self.themeBtnSize-self.margin//2)

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

        # To-do list Label
        self.taskLabelHeight = 30
        self.taskLabel = ct.CTkLabel(self.root,
                                     text="Tasks",
                                     font=(self.fontname, 35),
                                     height=self.taskLabelHeight)
        self.taskLabel.place(x=self.WIDTH//2+50,
                             y=25,
                             anchor="center")

        # Date Entry
        self.dateEntryWidth = 7
        self.dateEntry = DateEntry(self.root,
                                   width=self.dateEntryWidth,
                                   font=(self.fontname, 18))
        self.dateEntry.place(x=self.WIDTH-self.pigSize+self.margin*4,
                             y=self.taskLabelHeight + 2*self.margin)

        # Task Entry
        self.taskEntryWidth = 300
        self.taskEntryHeight = 30
        self.taskEntry = ct.CTkEntry(self.root,
                                     width=self.taskEntryWidth,
                                     height=self.taskEntryHeight,
                                     font=(self.fontname, 15))
        self.taskEntry.place(x=self.WIDTH-self.margin*4-self.pigSize-self.taskEntryWidth-80,
                             y=self.margin+self.taskLabelHeight+1)
        # Bind the ENTER key to add_task function
        self.taskEntry.bind("<Return>", lambda event: self.add_task())

        # List of Tasks
        self.listboxWidth = 55
        self.listboxHeight = 25
        self.tasksToDo = []
        self.tasksToDo = self.get_tasks()
        self.listbox = tk.Listbox(self.root,
                                  width=self.listboxWidth,
                                  height=self.listboxHeight,
                                  borderwidth=5,
                                  font=(self.fontname, 14))
        self.display_tasks()

        self.listbox.place(x=self.WIDTH-self.pigSize-self.taskEntryHeight-self.margin-self.listboxWidth-230,
                           y=self.taskLabelHeight+self.taskEntryHeight+self.margin*3)

        # Remove all Tasks Button
        self.clearAllBtn = ct.CTkButton(self.root,
                                        text="CLEAR ALL TASKS",
                                        height=self.btnHeight,
                                        width=int(self.btnWidth*1.5),
                                        font=(self.fontname, 20),
                                        command=self.remove_all_tasks)
        self.clearAllBtn.place(x=self.WIDTH-self.pigSize-self.margin*3-self.btnWidth*1.5-5,
                               y=self.HEIGHT-40-self.margin)

        # Mark as Completed Button
        self.markCompleted = ct.CTkButton(self.root,
                                          text="COMPLETE TASK",
                                          height=self.btnHeight,
                                          font=(self.fontname, 20),
                                          command=self.remove_task)
        self.markCompleted.place(x=self.WIDTH-self.pigSize-self.margin*3-self.btnWidth*3-10,
                                 y=self.HEIGHT-40-self.margin)

        self.root.mainloop()

    def remove_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]

            del self.tasksToDo[selected_task_index]
            with open("Data/tasks.json", "w") as f:
                dictTask = {"abc": self.tasksToDo}
                json.dump(dictTask, f)

            self.listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to remove")

    def remove_all_tasks(self):
        self.tasksToDo.clear()
        with open("Data/tasks.json", "w") as f:
            dictTask = {"abc": self.tasksToDo}
            json.dump(dictTask, f)
        self.display_tasks()

    def display_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasksToDo:
            str_task = f"{task[3]} | Due: {task[0]}-{task[1]}-{task[2]}"
            self.listbox.insert(tk.END, str_task)

    def add_task(self):
        task_str = self.taskEntry.get().strip()
        date = self.dateEntry.get_date()
        if task_str:
            self.taskEntry.delete(0, "end")
            current_day = date.day
            current_month = date.month
            current_year = date.year
            task = [current_year, current_month, current_day, task_str]
            added = False
            for i in range(len(self.tasksToDo)):
                # If the year is before the earliest year
                if self.tasksToDo[i][0] > current_year:
                    self.tasksToDo.insert(i, task)
                    added = True
                    break
                # If the year is the same -> check the month
                elif self.tasksToDo[i][0] == current_year:
                    # if the month is before the earliest month
                    if self.tasksToDo[i][1] > current_month:
                        self.tasksToDo.insert(i, task)
                        added = True
                        break
                    # if it's in the same month -> check the day
                    elif self.tasksToDo[i][1] == current_month:
                        if self.tasksToDo[i][2] > current_day:
                            self.tasksToDo.insert(i, task)
                            added = True
                            break
            if not added:
                self.tasksToDo.append(task)
            print(self.tasksToDo)
            with open("Data/tasks.json", "w") as f:
                dictTask = {"abc": self.tasksToDo}
                json.dump(dictTask, f)
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def get_tasks(self):
        with open("Data/tasks.json", "r") as f:
            dictTask = json.load(f)
            return dictTask.get("abc")

    def display_logs(self):
        # Window settings
        logsWindow = ct.CTkToplevel()
        logsWindow.title("Current Logs")
        logsWindow.resizable(False, False)
        logsMargin = 10
        logsWindowWidth = 400
        logsWindowHeight = 550
        logsWindow.geometry("" + str(logsWindowWidth) + "x" + str(logsWindowHeight) + "+"
                            + str(200 + self.WIDTH // 2 - logsWindowWidth // 2) + "+"
                            + str(150))

        # Scrollable Frame
        update_frame_width = 350
        update_frame_height = logsWindowHeight - logsMargin * 3
        update_frame = ct.CTkScrollableFrame(logsWindow,
                                             width=update_frame_width,
                                             height=update_frame_height)
        update_frame.pack(pady=logsMargin)

        # Text inside the scrollable frame
        allData = self.get_data()
        update_text = ct.CTkLabel(update_frame,
                                  width=10,
                                  font=('Arial', 15),
                                  text=allData)
        update_text.pack()

        # Force the window to be on top
        logsWindow.lift()
        logsWindow.focus_force()
        logsWindow.grab_set()

    def get_data(self):
        with open("Data/data.txt", "r") as f:
            text = ""
            for line in f:
                text += line

        return text

    def clear_data(self):
        with open("Data/data.txt", "w") as f:
            f.write(" ")
        with open("Data/total.txt", "w") as f:
            f.write("")
        self.update_root()

    def remove_from_bank(self):
        # Convert the input into text
        habit_text = self.habitText.get("1.0", "end-1c").strip()
        amount_text = self.amountText.get("1.0", "end-1c").strip()

        # Check if the inputs are not empty
        if habit_text and amount_text:
            # Update the total
            self.total = self.get_total()
            self.total -= int(amount_text)
            self.save_total()

            with open("Data/data.txt", "r") as f:
                lines = f.readlines()
            with open("Data/data.txt", "w") as f:
                f.write(f"[{self.total:.2f}] {habit_text} -{amount_text}\n")
                f.writelines(lines)

            # Clear the input fields after the inputs has been added
            self.habitText.delete("1.0", "end-1c")
            self.amountText.delete("1.0", "end-1c")

            self.update_root()

    def add_to_bank(self):
        # Convert the input into text
        habit_text = self.habitText.get("1.0", "end-1c").strip()
        amount_text = self.amountText.get("1.0", "end-1c").strip()

        # Check if the inputs are not empty
        if habit_text and amount_text:
            # Update the total
            self.total = self.get_total()
            self.total += int(amount_text)
            self.save_total()

            with open("Data/data.txt", "r") as f:
                lines = f.readlines()
            with open("Data/data.txt", "w") as f:
                f.write(f"[{self.total:.2f}] {habit_text} +{amount_text}$\n")
                f.writelines(lines)

            # Clear the input fields after the inputs has been added
            self.habitText.delete("1.0", "end-1c")
            self.amountText.delete("1.0", "end-1c")

            self.update_root()

    def save_total(self):
        with open("Data/total.txt", "r") as f:
            lines = f.readlines()
        with open("Data/total.txt", "w") as f:
            f.write(str(self.total) + "\n")
            f.writelines(lines)

    def update_root(self):
        self.update_total()

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
