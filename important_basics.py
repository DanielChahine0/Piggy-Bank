import tkinter as tk
import customtkinter as ct

# Main window
root = tk.Tk()

# root configurations
root.geometry("750x500")
root.title("Piggy Bank")

# label will represent the text in the window
label = tk.Label(root, text="Hello World", font=('Arial', 15))
label.pack(padx=20, pady=20)

# Textbox is the place where the user enter text
textbox = tk.Text(root, height=3, font=('Arial', 15))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)

# button = tk.Button(root, text="Click ME!", font=('Arial', 15))
# button.pack(pady=5)

# Entry is where it is 1 line and can't press ENTER to have multiple lines
# myEntry = tk.Entry(root)
# myEntry.pack()

root.mainloop()
