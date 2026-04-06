FILEPATH = "todos.txt"

def get_todo(filepath = FILEPATH):
    with open(filepath, "r") as file_local:
        todo_local = file_local.readlines()
        return todo_local

def write_todo(todo_args, filepath = FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_args)

if __name__ == "__main__":
    print("Hello!")
    print(get_todo())