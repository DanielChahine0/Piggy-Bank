import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import customtkinter as ctk

# lista = [1,2,3,4,5,6]
# lista.insert(6, 111)
# print(lista)

def add_task():
    task = entry.get()
    date = date_entry.get_date()
    if task:
        listbox.insert(tk.END, f"{task} (Due: {date})")
        entry.delete(0, tk.END)
        date_entry.set_date("")
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)

# Setting up the main application window
root = ctk.CTk()
root.title("To-Do List")

# Entry field for new tasks
entry = ctk.CTkEntry(root, width=250)
entry.pack(pady=10)

# Date entry for due date
date_entry = DateEntry(root, width=18, background='darkblue',
                       foreground='white', borderwidth=2)
date_entry.pack(pady=10)

# Add Task button
add_button = ctk.CTkButton(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Delete Task button
delete_button = ctk.CTkButton(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Clear All Tasks button
clear_button = ctk.CTkButton(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

# Start the main event loop
root.mainloop()
