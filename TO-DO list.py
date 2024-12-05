import os
import json

# File to store tasks
FILE_NAME = "todo_list.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. {task['task']} [Status: {status}]")
    print()

# Update a task
def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter the task number to update: "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return
        new_task = input("Enter the updated task: ").strip()
        if not new_task:
            print("Task cannot be empty.")
            return
        tasks[task_no - 1]["task"] = new_task
        print("Task updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Mark a task as completed
def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter the task number to mark as completed: "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return
        tasks[task_no - 1]["completed"] = True
        print("Task marked as completed.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_no = int(input("Enter the task number to delete: "))
        if task_no < 1 or task_no > len(tasks):
            print("Invalid task number.")
            return
        deleted_task = tasks.pop(task_no - 1)
        print(f"Task '{deleted_task['task']}' deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main menu
def main():
    print("To-Do List Application")
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
