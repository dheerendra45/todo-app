def get_todos(filepath='todos.txt'):
    """Read the text file and return the todos list"""
    try:
        with open(filepath, 'r') as file:
            todos = file.readlines()
    except FileNotFoundError:
        todos = []
    return [todo.strip() + '\n' for todo in todos]

def write_todos(todos, filepath='todos.txt'):
    """Write the list of todos to the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)
