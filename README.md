# To-Do Web App

## Overview

This is a simple To-Do web application that allows users to add, edit, remove, and display their to-do items. The app utilizes a basic GUI built using **PySimpleGUI** for easy interaction and file handling in Python. The to-dos are stored in a text file (`todos.txt`) for persistent data storage.

## Technologies Used

- **Python**: The programming language used for the application.
- **PySimpleGUI**: A Python library for creating graphical user interfaces (GUIs).
- **Text Files**: Used for storing to-do items (`todos.txt`).

## Features

- **Add Todo**: Users can add new to-do items.
- **Edit Todo**: Users can edit existing to-do items by selecting their number.
- **Remove Todo**: Users can delete completed to-do items.
- **Display Todos**: Users can view a list of all their to-do items.

## Working

### 1. Frontend (GUI)

The GUI of the application is built using **PySimpleGUI**, which is simple and intuitive. The interface has:
- A label displaying a greeting message.
- An input box where users can type new to-do items.
- Buttons for adding, editing, and removing to-do items.

### 2. Backend

- **get_todos**: This function reads the `todos.txt` file and returns the list of to-do items.
- **write_todos**: This function writes the updated to-do list to the `todos.txt` file.

### 3. Main Workflow

- The application prompts the user through a simple command-line interface to enter the action they want to perform (add, show, edit, or complete).
- Upon adding a to-do item, it is written to `todos.txt`.
- The list of to-dos can be displayed in the terminal.
- Items can be edited or removed by specifying the corresponding index.
- The program will keep running until the user types 'exit' to quit the app.
