
def get_todos():
    try:
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        return todos
    except Exception as e:
        sg.popup(f"An error occurred while reading the file: {e}")
        return []

def write_todos(todos):
    try:
        with open("todos.txt", "w") as file:
            file.writelines(todos)
    except Exception as e:
        sg.popup(f"An error occurred while writing to the file: {e}")
