# To-Do List Application

todo_list = []

def show_tasks():
    print("To-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    task_number = int(input("Enter the task number to delete: "))
    del todo_list[task_number - 1]
    print("Task deleted!")

while True:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")