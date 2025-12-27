import csv 

employees = [
    ["name","Age","Job"],
    ["Raj",18,"developer"],
    ["Tej",65,"Senior developer"]
]

file_path = r"Files\test.csv"

try:
    with open(file_path,"w",newline = "") as file: # newline keyword used to control extra blank line .
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"json file {file_path} is saved .")
except Exception:
    print("Exception occur")
