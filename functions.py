def is_duplicate(todos: list, new_todo: str) -> bool:
    return new_todo in todos


def has_todos(todos: list) -> bool:
    if not todos:
        print("No todos found")
        return False
    return True


def create_todos(todos: list, todo: str) -> None:
    if is_duplicate(todos, todo):
        print("Previous todo already exists")
    else:
        todos.append(todo)


def delete_todos(todos: list, todo_id: int) -> None:
    try:
        todos.pop(todo_id - 1)
    except IndexError:
        print("Invalid ID")


def print_todos(todos: list) -> None:
    if not has_todos(todos):
        return
    for index, todo in enumerate(todos, start=1):
        print(f"{index}: {todo}")


def edit_todos(todos: list, todo_id: int, new_todo: str) -> None:
    try:
        if is_duplicate(todos, new_todo):
            print("Previous todo already exists")
        else:
            todos[todo_id - 1] = new_todo
            print(f"Todo {todo_id} has been edited to {new_todo}")
            print_todos(todos)
    except IndexError:
        print("Invalid ID")
