import os
import time
import FreeSimpleGUI as sg
import functions

# Ensure file exists
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w'):
        pass

# Theme
sg.theme('DarkBlue')

# Layout
clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")

add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(
    values=functions.get_todo(),
    key="todos",
    enable_events=True,
    size=(45, 10)
)

layout = [
    [clock],
    [label],
    [input_box, add_button],
    [list_box, edit_button, complete_button],
    [exit_button]
]

window = sg.Window("My To-do App", layout, font=('Helvetica', 20))

# Event Loop
while True:
    event, values = window.read(timeout=200)

    # Update clock
    window["clock"].update(time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case sg.WIN_CLOSED | "Exit":
            break

        case "Add":
            todo = values["todo"].strip()
            if todo:
                todos = functions.get_todo()
                todos.append(todo + "\n")
                functions.write_todo(todos)

                window["todos"].update(values=todos)
                window["todo"].update("")
            else:
                sg.popup("Please enter a to-do item.")

        case "Edit":
            try:
                selected = values["todos"][0]
                new_todo = values["todo"].strip()

                if new_todo:
                    todos = functions.get_todo()
                    index = todos.index(selected)
                    todos[index] = new_todo + "\n"

                    functions.write_todo(todos)
                    window["todos"].update(values=todos)
                else:
                    sg.popup("Please enter a new value.")

            except IndexError:
                sg.popup("Please select an item first.")

        case "Complete":
            try:
                selected = values["todos"][0]
                todos = functions.get_todo()

                todos.remove(selected)
                functions.write_todo(todos)

                window["todos"].update(values=todos)
                window["todo"].update("")

            except IndexError:
                sg.popup("Please select an item first.")

        case "todos":
            window["todo"].update(values["todos"][0])

window.close()