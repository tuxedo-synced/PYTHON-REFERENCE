# Python writing files (.txt , .json , .csv)

txt_data = "I love watching anime"
file_path = r"Files\test.txt"    # right click on file in vs code and select copy path directly .

try:
# with -> is a statement used to wrap a code block to excecute 
# generally when u open file with 'with' keyword , it itsel close after performing the operation .
    with open(file_path,"w") as file: # can also write as (file=file_path,mode="w")
        file.write("\n" + txt_data)
        print(f"text file {file_path} is saved .")

# it creates a file if not while writing data into the given respective file .
# it clears prv data during "w" and append the writing content sent in code .
except FileExistsError:
    print("The file already exists")



