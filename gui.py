import PySimpleGUI as sg
import functions
import time
import os
if not os.path.exists("todos.txt"):
 with open("todos.txt","w") as file:
     pass

sg.theme('Black')
clock = sg.Text('', key='clock')  # Changed the key to 'clock'
welcome_message = sg.Text('Welcome to My To-Do List Manager')
input_box = sg.InputText(tooltip='Enter your to-do item here', key='todo')
add_button = sg.Button('Add', tooltip='Add a new to-do item')

list_box = sg.Listbox(values=functions.get_todos(), size=[40, 10], enable_events=True, key='todos')

edit_button = sg.Button('Edit', tooltip='Edit the selected to-do item')
remove_button = sg.Button('Remove', tooltip='Remove the selected to-do item')
exit_button = sg.Button('Exit')
complete_button = sg.Button('Complete')


layout = [[clock], [input_box, add_button],
          [welcome_message],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('To-Do List Manager', layout, font=('Helvetica', 20))


while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))  # Updated the key to 'clock'
    print(event)
    print(values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add':
        todos = functions.get_todos()
        new_todo = values['todo']
        if new_todo:
            todos.append(new_todo + '\n''')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
    elif event == 'Edit':
        try:
            edit_todo = values['todos'][0]
            new_todo = values['todo'].strip()
            if new_todo:  # Ensure the new to-do item is not empty
                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item to edit.")
        except Exception as e:
            sg.popup(f"An error occurred: {e}")

    elif event == 'todos':
        window['todo'].update(value=values['todos'][0].strip())
    elif event == 'Complete':
        try:
            complete_todos = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(complete_todos)
            todos.pop(index)

            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            continue

    elif event == 'Exit':
        break

window.close()
