FILEPATH = r"/home/piotr/Documents/VS Program/Kurs-Python-EN/CW1/todos.txt"

def get_todos(filepath=FILEPATH):

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
