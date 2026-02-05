# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string 

input("Whats your name: ")

name = input("Whats your name: ")
print(f"name entered is: {name}")

age = input("How old are you: ")
print(f"you are {age} years old")
# age+=1 ----> throws an error as it returns a string 
print(type(age))
age = int(age)
age+=1 
print(age)
# shortcut
age = int(input("Enter your age: "))
print(type(age))
print(age)

# Practice 1 : Area of rectangele
print("------------------------")
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length*breadth
print(f"Area of rectangle: {area}")
print("------------------------")


