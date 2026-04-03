
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
print("Add input box")
input_box = sg.InputText(tooltip = "Enter a to-do", key = "todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App', layout = [[label],[input_box, add_button]],
                   font = ('Helvetica', 20),)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()
