# syntax :- 

#         while condition:    ---
#              statement 1       |    while block 
#              statement 2       |
#              ......... .    ---
#         statements         outside while block 

# example 1
i = 10
while i != 0:
    print(i)
    i = int(i/2)
print("Exiting...")

# example 2
name = input("Enter your name: ")
while name == "":
    print("Enter valid name...")
    name = input("Enter your name: ")
print(f"hello {name}")

# use of not :-   not name == "q" 