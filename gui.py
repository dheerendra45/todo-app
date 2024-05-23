import functions
import PySimpleGUI as sg

label=sg.Text('hello welcome to my todo  web app')
input_box=sg.Input('enter todo')
add_button=sg.Button('ADD')
edit_button=sg.Button('EDIT')
remove_button=sg.Button('REMOVE')

layout=[[label],[input_box],[add_button,edit_button,remove_button]]
window=sg.Window('this is my todo app',layout)
window.read()
window.close()
