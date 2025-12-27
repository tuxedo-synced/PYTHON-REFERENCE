file_path = r"Files\test.txt"

try:
    with open(file_path,"r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file was not found .")
except PermissionError:
    print("Ypu do not have permission to read that file .")