FILEPATH = "todo.txt"

def get_todo(filename = FILEPATH):
    with open(FILEPATH, "r") as file_local:
        todo_local = file_local.readlines()
        return todo_local

def write_todo(todo_args, filename = FILEPATH):
    with open(FILEPATH, "w") as file:
        file.writelines(todo_args)

if __name__ == "__main__":
    print("Hello!")
    print(get_todo())