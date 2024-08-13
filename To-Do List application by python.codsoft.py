import json
import os

TODO_FILE = 'todos.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos, start=1):
        status = "✔️" if todo['done'] else "❌"
        print(f"{i}. {status} {todo['task']}")

def add_todo(todos):
    task = input("Enter the task: ")
    todos.append({"task": task, "done": False})
    print("Task added.")

def update_todo(todos):
    list_todos(todos)
    index = int(input("Enter the number of the task to update: ")) - 1
    if 0 <= index < len(todos):
        todos[index]['done'] = not todos[index]['done']
        print("Task updated.")
    else:
        print("Invalid task number.")

def main():
    todos = load_todos()
    while True:
        print("\nTo-Do List Menu")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_todo(todos)
            save_todos(todos)
        elif choice == '3':
            update_todo(todos)
            save_todos(todos)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
