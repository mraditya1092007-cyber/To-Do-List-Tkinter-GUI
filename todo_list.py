from tkinter import *
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get().strip()

    if task:
        task_listbox.insert(END, "• " + task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Do you want to clear all tasks?"):
        task_listbox.delete(0, END)

# Main Window
root = Tk()
root.title("To-Do List Application")
root.geometry("450x650")
root.configure(bg="#f4f6f8")

# Heading
title = Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 24, "bold"),
    bg="#f4f6f8",
    fg="#2c3e50"
)
title.pack(pady=15)

# Input Frame
input_frame = Frame(root, bg="#f4f6f8")
input_frame.pack(pady=10)

task_entry = Entry(
    input_frame,
    width=25,
    font=("Arial", 14)
)
task_entry.grid(row=0, column=0, padx=5)

add_btn = Button(
    input_frame,
    text="ADD TASK",
    font=("Arial", 11, "bold"),
    bg="#27ae60",
    fg="white",
    width=10,
    command=add_task
)
add_btn.grid(row=0, column=1)

# List Frame
list_frame = Frame(root)
list_frame.pack(pady=15)

scrollbar = Scrollbar(list_frame)

task_listbox = Listbox(
    list_frame,
    width=40,
    height=15,
    font=("Arial", 13),
    selectbackground="#3498db",
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=task_listbox.yview)

scrollbar.pack(side=RIGHT, fill=Y)
task_listbox.pack(side=LEFT)

# Delete Button
delete_btn = Button(
    root,
    text="DELETE SELECTED TASK",
    font=("Arial", 11, "bold"),
    bg="#e74c3c",
    fg="white",
    width=25,
    command=delete_task
)
delete_btn.pack(pady=10)

# Clear Button
clear_btn = Button(
    root,
    text="CLEAR ALL TASKS",
    font=("Arial", 11, "bold"),
    bg="#f39c12",
    fg="black",
    width=25,
    command=clear_tasks
)
clear_btn.pack()

# Footer
footer = Label(
    root,
    text="Python Tkinter To-Do List",
    font=("Arial", 10),
    bg="#f4f6f8",
    fg="gray"
)
footer.pack(side=BOTTOM, pady=15)

root.mainloop()
