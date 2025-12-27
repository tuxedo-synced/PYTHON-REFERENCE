# Variable = A container for a value (string , integer , float , boolean )
#            A variable behaves as if it was the value it contains 

# Strings 
first_name = "S.Rahul"
food = "Pizza"
email = "rahul.synced@gmail.com"
print(first_name)
print(f"Hello {first_name}")
print(f"you love {food}")
print(f"your email is {email}")

# the variabled filled inside as {first_name} , {food} , .. etc are placeholders .

# Integers
age = 19 
quantity =  3
num_students = 30
print(f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_students} members")

# Floats
price = 10.99 
sgpa = 9.15
distance = 45.234
print(f"the price of item is {price}$")
print(f"your sgpa is {sgpa}")
print(f"your {distance} km away from me")

# Booleans
isTeen = False
isStudent = True

if isStudent:
    print("You are a student")
else: 
    print("You are not a student")
if isTeen:
    print("You are a teen")
else: 
    print("You are not a teen")

# print side by side 
i = 10 
j = 11 
print(f"{i} {j}")   #(or)
print(i, end = " ")
print(j)