class ToDoList:
    def __init__(self):
        self.tasks = []  

    def add_task(self, task_name):
        task = {"task": task_name}
        self.tasks.append(task)
        print(f"Task '{task_name}' added to the list.")

    def update_task(self, task_index, new_task_name):
        if 0 <= task_index < len(self.tasks):
            old_task_name = self.tasks[task_index]["task"]
            self.tasks[task_index]["task"] = new_task_name
            print(f"Task '{old_task_name}' updated to '{new_task_name}'.")
        else:
            print("Invalid task index. Please provide a valid index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['task']}' removed from the list.")
        else:
            print("Invalid task index. Please provide a valid index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task['task']} - {task['status']}")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a new task")
    print("2. Update a task")
    print("3. Remove a task")
    print("4. View all tasks")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = int(input("Choose an option (1-5): "))

        if choice == 1:
            task_name = input("Enter the task name: ")
            todo_list.add_task(task_name)

        elif choice == 2:
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task number to update: ")) - 1
                new_task_name = input("Enter the new task name: ")
                todo_list.update_task(task_index, new_task_name)
            except ValueError:
                print("Invalid input! Please enter a valid task number.")

        elif choice == 3:
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(task_index)
            except ValueError:
                print("Invalid input! Please enter a valid task number.")

        elif choice == 4:
            todo_list.view_tasks()

        elif choice == 5:
            print("Exiting the To-Do List program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 5.")

main()
