import os
import pickle
import datetime


# Define task class
class Task:
    def __init__(self, title, priority, due_date=None):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = False


# Define the ToDoList class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority, due_date=None):
        task = Task(title, priority, due_date)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Incomplete"
            due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "N/A"
            print(
                f"{index + 1}. Title: {task.title} | Priority: {task.priority} | Due Date: {due_date} | Status: {status}")

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)


# Main function
def main():
    todo_list = ToDoList()
    data_file = "tasks.pickle"

    # Load tasks from file, if it exists
    todo_list.load_from_file(data_file)

    while True:
        print("\n*** To-Do List ***")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            todo_list.add_task(title, priority, due_date)
            print("Task added successfully.")

        elif choice == '2':
            index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(index)
            print("Task removed successfully.")

        elif choice == '3':
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
            print("Task marked as completed.")

        elif choice == '4':
            todo_list.list_tasks()

        elif choice == '5':
            todo_list.save_to_file(data_file)
            print("Tasks saved. Goodbye!")
            break


if __name__ == "__main__":
    main()
