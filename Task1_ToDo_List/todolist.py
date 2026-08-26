# CODSOFT Python Programming Internship
# Task 1 - To-Do List Application

tasks = []


def add_task():
    task = input("Enter task: ").strip()

    if task:
        tasks.append({
            "task": task,
            "completed": False
        })
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for index, item in enumerate(tasks, start=1):
        status = "Completed" if item["completed"] else "Pending"
        print(f"{index}. {item['task']} [{status}]")


def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to update: "))

        if 1 <= number <= len(tasks):
            new_task = input("Enter new task: ").strip()

            if new_task:
                tasks[number - 1]["task"] = new_task
                print("Task updated successfully.")
            else:
                print("Task cannot be empty.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print(f"Deleted: {deleted_task['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def mark_completed():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n==========================")
        print("       TO-DO LIST")
        print("==========================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            mark_completed()

        elif choice == "6":
            print("Thank you for using To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()