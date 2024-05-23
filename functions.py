def get_todos(filepath='todos.txt'):
    """read the text fiel and return the todos list with smile"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg,file_path='todos.txt'):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
