import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QMessageBox, \
    QInputDialog

from constants import *
from functions import *

todos = []


def refresh_todos(todo_list):
    listbox.clear()
    for index, todo in enumerate(todo_list, start=1):
        listbox.addItem(f"{index}: {todo}")


def add_todo():
    if len(todos) > MAX_TODOS:
        QMessageBox.critical(window, "Error", f"You can only have a maximum of {MAX_TODOS} todos")
        return
    new_todo, ok = QInputDialog.getText(window, "Add todo", "What do you want to do?")
    if ok and new_todo and not is_duplicate(todos, new_todo):
        create_todos(todos, new_todo)
        refresh_todos(todos)


def delete_todo():
    selected = listbox.currentRow()
    if selected == -1:
        QMessageBox.critical(window, "Selection Error", "Select a todo to delete")
        return
    delete_todos(todos, selected)
    refresh_todos(todos)


def edit_todo():
    selected = listbox.currentRow()
    if selected == -1:
        QMessageBox.critical(window, "Selection Error", "Select a todo to edit")
        return
    new_todo, ok = QInputDialog.getText(window, "Edit Todo", "Enter the new todo:")
    if ok and new_todo:
        edit_todos(todos, selected, new_todo)
        refresh_todos(todos)


# Initialize the main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Todo App")

# Create UI components
main_layout = QVBoxLayout()

listbox = QListWidget()
main_layout.addWidget(listbox)

button_layout = QHBoxLayout()

add_button = QPushButton("Add Todo")
add_button.clicked.connect(add_todo)
button_layout.addWidget(add_button)

edit_button = QPushButton("Edit Todo")
edit_button.clicked.connect(edit_todo)
button_layout.addWidget(edit_button)

delete_button = QPushButton("Delete Todo")
delete_button.clicked.connect(delete_todo)
button_layout.addWidget(delete_button)

main_layout.addLayout(button_layout)
window.setLayout(main_layout)

# Show the window
window.show()

# Start the PyQt event loop
sys.exit(app.exec())
