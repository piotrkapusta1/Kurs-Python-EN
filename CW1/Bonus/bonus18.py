import PySimpleGUI as sg

label1 = sg.Text("Select archive")
input1= sg.Input()
add_button = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
add_button = sg.FolderBrowse("Choose", key="folder")

