from constants import *
from functions import *

print(f"You can only create {MAX_TODOS} todos")
welcome_message = ("Enter 'c' to create a todo, 'd' to delete a todo, 'p' to print all todos, 'e' to edit a todo, "
                   "'q' to quit:")

todos = []
retry_count = 0

while retry_count < RETRY_LIMIT:
    user_action = input(welcome_message).strip().lower()

    match user_action:
        case "c":
            while len(todos) < MAX_TODOS:
                user_todo = input("Enter a todo, type 'qx' to exit: ").strip()
                if user_todo.lower() == "qx":
                    print_todos(todos)
                    break
                else:
                    create_todos(todos, user_todo)
            else:
                print(f"You can only create {MAX_TODOS} todos")
                print_todos(todos)
        case "d":
            if has_todos(todos):
                print_todos(todos)
                try:
                    todo_id = int(input("Enter the todo id to delete: "))
                    delete_todos(todos, todo_id)
                except ValueError:
                    print("Invalid input. Please enter a number.")
        case "p":
            print_todos(todos)
        case "e":
            if has_todos(todos):
                print_todos(todos)
                try:
                    todo_id = int(input("Enter the todo id to edit: "))
                    if 1 <= todo_id <= len(todos):
                        replacement_todo = input("Enter new todo: ").strip()
                        edit_todos(todos, todo_id, replacement_todo)
                    else:
                        print("Invalid todo id")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        case "q":
            break
        case _:
            print("Invalid input.")
            retry_count += 1

print("Goodbye!")
