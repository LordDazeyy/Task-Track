class Task:
    def __init__(self, task_id, title):
        self.task_id = task_id
        self.title = title
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_counter = 1

    def add_task(self, title):
        task = Task(self.task_counter, title)
        self.tasks.append(task)
        self.task_counter += 1
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.task_id}. {task.title} - {status}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                print("Task marked as completed.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")


def main():
    task_manager = TaskManager()

    while True:
        print("\n--- TaskTrack Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            task_manager.add_task(title)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to complete: "))
            task_manager.complete_task(task_id)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)

        elif choice == "5":
            print("Exiting TaskTrack...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
