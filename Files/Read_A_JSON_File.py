import json

file_path = r"Files\test.json"

try:
    with open(file_path,"r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
        print(content["age"])
        print(content["fav number"])
        print(content["job"])
except FileNotFoundError:
    print("The file was not found .")
except PermissionError:
    print("Ypu do not have permission to read that file .")