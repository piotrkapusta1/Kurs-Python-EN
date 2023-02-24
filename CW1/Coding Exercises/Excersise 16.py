
import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
label2 = sg.Text("Enter inches: ")
input_box1 = sg.InputText(tooltip = "Enter todo")
input_box2 = sg.InputText(tooltip = "Enter todo")
add_button = sg.Button("Convert")

window = sg.Window('Convertor', layout=[[label1, input_box1], [label2, input_box2], [add_button]])
window.read()
window.close()