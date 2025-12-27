# json file is represented in dictionaries .
import sys
import json
file_path = r"Files\test.json"
employee = {
    "name": "Tsunade",
    "age": sys.maxsize-1 ,
    "fav number": 106 ,
    "job": "paiso ko udana"
}
try:
    with open(file_path,"w") as file:
        json.dump(employee,file, indent=4)  # indent is for indenting each value by 4 spaces .
        print(f"json file {file_path} is saved .")

except FileExistsError:
    print("That file is already exists .")