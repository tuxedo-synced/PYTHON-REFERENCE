import os

file_paths = ["Files/test.txt","Files/test.csv","something.pdf",r"C:\Users\rahul\OneDrive\Documents\dbms\DBMS REFERENCE PDF.pdf",r"C:\Users\rahul\OneDrive\Documents\ms excel and power bi\final project"]
# \U  \D  \O  -> have some other use so to avoid that conflict we place r before double quotes means 'read it as is'
for file_path in file_paths:
    if os.path.exists(file_path):
        print(f"The '{file_path}' allocation exists .")
        if os.path.isfile(file_path):
            print("Its a file .")
        if os.path.isfile(file_path) and file_path.endswith(".csv"):
            print("Its a csv file .")
        if os.path.isfile(file_path) and file_path.endswith(".json"):
            print("Its a json file .")     
        else:
            print("Its not a file .")
    else:
        print("The location does not exits")
