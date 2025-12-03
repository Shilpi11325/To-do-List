import json
import os

FILE_NAME= "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r")as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME,"w")as f:
        json.dump(tasks,f,indent=4)

def add_task(task):
    tasks= laod_tasks()
    tasks.append ({"task":task,"completed":false})
    save_tasks(tasks)
    print ("TASK ADDED!")

def delete_task(task_no):
    tasks= load_tasks()
    if 1<=task_no<=len(tasks):
        tasks.pop(task_no-1)
        save_tasks(tasks)
        print ("TASK DELETED")
    else:
        print ("INVALID TASK NUMBER")

def mark_completed(task_no):
    tasks= laod_tasks()
    if 1<=task_no<=len(tasks):
        tasks[task_no-1]["completed"]=True
        save_tasks(tasks)
        print ("TASK MARKS AS COMPLETED")
    else:
        print ("INVALID TASK NUMBER")

def show_tasks():
    tasks = load_tasks()
    print("\n--- To-Do List ---")
    for i, t in enumerate(tasks, 1):
        status = "Completed" if t["completed"] else "Pending"
        print(f"{i}. {t['task']} [{status}]")
    print()

while True:
    print ("1.ADD Task")
    print ("2.DELETE Task")
    print ("3.MARK TASK COMPLETED")
    print ("4.SHOW TASK")
    print ("5.EXIT")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        add_task(task)

    elif choice == 2:
        show_tasks()
        num = int(input("Enter task number to delete: "))
        delete_task(num)

    elif choice == 3:
        show_tasks()
        num = int(input("Enter task number to mark completed: "))
        mark_completed(num)

    elif choice == 4:
        show_tasks()

    elif choice == 5:
        print("Exiting")
        break

    else:
        print("Invalid choice! Try again.\n")

