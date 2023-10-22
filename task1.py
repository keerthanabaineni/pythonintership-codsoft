TASK-1 
tasks = []


def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")


def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


def remove_task(task_index):
    try:
        task_index = int(task_index) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid task index.")


while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = input("Enter the task index to remove: ")
        remove_task(task_index)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
