import functions

while True:
    user_promt=input('enter add,show or exit from loop and also write what u want add')
    user_promt=user_promt.strip()
    if user_promt.startswith('add'):
        todos=functions.get_todos()
        todo=user_promt[4:]
        todos.append(todo+'\n')
        functions.write_todos(todos)

    elif user_promt.startswith('show'):
        todos = functions.get_todos()
        for index,item in enumerate(todos):
            row=item.strip('\n')
            print(f"{index+1}-{row}")

    elif user_promt.startswith('edit'):
        try:
            number=int(user_promt[:5])
            index=number-1
            todos = functions.get_todos()
            new_todo=input("enter the new todo")
            todos[index]=new_todo+'\n'
            functions.write_todos(todos)
            print(todos)
        except ValueError:
            continue

    elif user_promt.startswith('complete'):
        try:
            number=int(user_promt[:9])
            index=number-1
            todos = functions.get_todos()
            todos.pop(index)
            functions.write_todos(todos)
            print(todos)
        except IndexError:
            continue

    elif 'exit' in user_promt:
        break
    else:
        print("please read again program than write something")
print('done')

