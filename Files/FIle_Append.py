txt_data = "I love watching anime"
file_path = r"Files\test.txt"

with open(file_path,"a") as file:
    file.write(txt_data+"\n")
    print(f"text file {file_path} is saved .")

anime_characters = ["jin woo" , "peru" , "Naruto" , "Itachi" , "Tsunade"]

with open(file_path,"a") as file:
    for i in anime_characters:
        file.write(i+"\n")
    print(f"text file {file_path} is saved .")