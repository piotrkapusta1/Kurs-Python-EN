import PySimpleGUI as sg

feet = sg.Text("Enter feet:")
feetInput = sg.Input(key="feet")

inches = sg.Text("Enter inches:")
inchesInput = sg.Input(key="inches")

convertButton = sg.Button("Convert")
output = sg.Text(key="output")

window = sg.Window("Convertor",
                   layout=[[feet, feetInput],
                           [inches, inchesInput],
                           [convertButton, output]])

while True:
    event, values = window.read()
    meters = (float(values["feet"]) * 0.3048) + (float(values["inches"]) * 0.0254)
    window["output"].update(value= str(meters) + " m")
    
window.close
