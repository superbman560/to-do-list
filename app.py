from random import random

print("Hello World")

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter a to-do")
button = sg.Button("Add")

window = sg.Window('My To-do App', layout = [[label],[input_box, button]])

window.read()
