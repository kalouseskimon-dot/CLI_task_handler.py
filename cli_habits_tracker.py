import json


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successfully!")




def load_tasks():
    global tasks

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []



tasks = []
task = {
    "id": 1,
    "title": "Study Python",
    "category": "Programming",
    "priority": "high",
    "completed": False
}
tasks.append(task)


def add_task():
    title = input("Your task: ")
    category = input("Category: ")
    priority = input("Priority: high, medium or low? ")
    completed = False
    task_1 = {
        "id": len(tasks) + 1,
        "title": title,
        "category": category,
        "priority": priority,
        "completed": completed
    }
    tasks.append(task_1)
    save_tasks()


def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- YOUR TASKS ---")

    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Category: {task['category']}")
        print(f"Priority: {task['priority']}")
        print(f"Completed: {task['completed']}")
        print("------------------")

def complete_task():
    id = input("Please enter the id of the task you want to mark as completed ")
    id = int(id)
    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            print("Congratulations on completing your task!")
            return
    print("ID not found, try another one!")
        
def delete_task():
    id = input("Please enter the id of the task you want to delete ")
    id = int(id)
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("ID not found, try another one!")


def search_task():
    name = input("Search the name of the task you want to find")
    found = False
    for task in tasks: 
        if name.lower() in task["title"].lower():
            print("There is a task named ", task["title"])
            found = True
    if found == False:
        print("There is no task called this way.")

def filter_tasks_by_priority():
    priority = input("Please type the priority of the tasks you wish to see: ")
    priority_list = []
    found = False
    for task in tasks:
        if task["priority"] == priority:
            priority_list.append(task)
            found = True
    if found:
        print("Here are the tasks you have marked as ", priority, ": ", priority_list)
    else:
        print("No matching results")


def show_statistics():
    total_tasks = len(tasks)

    completed_count = sum(1 for task in tasks if task["completed"])

    incomplete_count = total_tasks - completed_count

    print("Total tasks:", total_tasks)
    print("Completed tasks:", completed_count)
    print("Incomplete tasks:", incomplete_count)


load_tasks()