import csv

file_path = r"Files\test.csv"

try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        print(content)  # <_csv.reader object at 0x000001AE6386DA80> returns address of csv.reader's object
        for every_line in content:
            print(every_line)
        file.seek(0)
        for every_line in content:
            print(every_line[0], end = " ")
            print(every_line[1], end = " ")
            print(every_line[2], end = "\n")
except FileNotFoundError:
    print("The file was not found .")
except PermissionError:
    print("Ypu do not have permission to read that file .")