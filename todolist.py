import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

tasks = []

# Functions 
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty")
    else:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    
    if not selected:
        messagebox.showerror("Error", "Please select a task to delete")
        return
    
    index = selected[0]
    tasks.pop(index)
    update_listbox()

def update_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Please select a task first")
        return

    index = selected[0]
    new_task = entry.get()

    if new_task.strip() == "":
        messagebox.showwarning("Warning", "Enter updated task")
    else:
        tasks[index] = new_task
        update_listbox()
        entry.delete(0, tk.END)

# Autofill entry when selecting task
def fill_entry(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        entry.delete(0, tk.END)
        entry.insert(0, tasks[index])

# UI Elements
title = tk.Label(root, text="My To-Do List", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

update_btn = tk.Button(root, text="Update Task", width=20, command=update_task)
update_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

# Bind selection event
listbox.bind("<<ListboxSelect>>", fill_entry)

# Run app
root.mainloop()