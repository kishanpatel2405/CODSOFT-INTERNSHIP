'''TO-DO LIST
TASK 1
A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists
'''
import tkinter as tk

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []

        self.task_list = tk.Listbox(root, width=40)
        self.task_list.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(padx=10, pady=10)

    def add_task(self):
        task = self.entry.get()
        self.tasks.append(task)
        self.task_list.insert(tk.END, task)
        self.entry.delete(0, tk.END)

    def update_task(self):
        index = self.task_list.curselection()[0]
        new_task = self.entry.get()
        self.tasks[index] = new_task
        self.task_list.delete(index)
        self.task_list.insert(index, new_task)
        self.entry.delete(0, tk.END)

    def delete_task(self):
        index = self.task_list.curselection()[0]
        del self.tasks[index]
        self.task_list.delete(index)

root = tk.Tk()
root.title("To-Do List")
app = ToDoList(root)
root.mainloop()









