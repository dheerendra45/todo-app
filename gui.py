import PySimpleGUI as sg
import functions

# Define the UI elements
welcome_message = sg.Text('Welcome to My To-Do List Manager')
input_box = sg.InputText(tooltip='Enter your to-do item here', key='todo')
add_button = sg.Button('Add', tooltip='Add a new to-do item')

list_box=sg.Listbox(values=functions.get_todos(),size=[40,10] ,enable_events=True,key='todos')





edit_button = sg.Button('Edit', tooltip='Edit the selected to-do item')
remove_button = sg.Button('Remove', tooltip='Remove the selected to-do item')

# Define the layout
layout = [
    [welcome_message],[list_box],
    [input_box],
    [add_button, edit_button, remove_button]
]

# Create the window with the specified title and layout
window = sg.Window('To-Do List Manager', layout ,font=('Helvetica', 20))

# Start the event loop
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add':
        todos = functions.get_todos()
        new_todo = values['todo'].strip() + '\n'
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == 'Edit':
        edit_todo=values['todos'][0]
        new_todo=values['todo']

        todos=functions.get_todos()
        index=todos.index(edit_todo)
        todos[index]=new_todo

        functions.write_todos(todos)
        window['todos'].update(values=todos)

    elif event=='todos':
        window['todo'].update(value='todos')
    elif event == 'Remove':
        # Add your remove logic here
        pass



window.close()
