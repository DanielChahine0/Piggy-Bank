import tkinter as tk
import customtkinter as ct

# Main window
root = ct.CTk()

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
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

# anotherbtn = tk.Button(root, text="TEST")
# anotherbtn.place(x=200, y=200, height=100,width=100)


# button = tk.Button(root, text="Click ME!", font=('Arial', 15))
# button.pack(pady=5)

# Entry is where it is 1 line and can't press ENTER to have multiple lines
# myEntry = tk.Entry(root)
# myEntry.pack()

root.mainloop()
