import tkinter as tk
from tkinter import messagebox

# Function to add a task!
def addTask():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to remove the task!
def removeTask():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Function to Update The Task!
def updateTask():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Updated task cannot be empty!")
    except:
        messagebox.showwarning("Warning", "Please select a task to update!")

# function to exit the program!
def exitAPP():
    root.destroy()

# define root!
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="#f5f5f5")

# Entry Field!
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Buttons Field!
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Task", width=10, command=addTask).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Remove Task", width=10, command=removeTask).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Update Task", width=10, command=updateTask).grid(row=0, column=2, padx=5)
tk.Button(root, text="Exit", width=10, command=exitAPP).pack(pady=5)

# Task List!
listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
listbox.pack(pady=10)

# run!
root.mainloop()
