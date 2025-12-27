# Typecasting = the process of converting a variable from one data type to another .
#               str() , int() , float() , bool() 
# implicit typecasting order :- bool → int → float → string
# explicit typecasting have same order but can set manually .

# Integer 
# 1. int to string      possible
# 2. int to float       possible
# 3. int to bool        possible

val = 5 
print(str(val))
print(float(val))
print(bool(val))

# Floating pointer number
# 1. Float to string      possible
# 2. Float to int         possible
# 3. Float to bool        possible

val = 3.1425 
print(str(val))
print(int(val))
print(bool(val))

# Strings
# 1. string to float       not possible
# 2. string to int         not possible
# 3. string to bool        possible

val = "Rahul Sadaram"
# print(float(val))        
# print(int(val))          
print(bool(val))           

# Strings
# 1. bool to float         possible
# 2. bool to int           possible
# 3. bool to string        possible

val = True
print(str(val))
print(int(val))
print(float(val))

# NOTE :- strings with only digits can be converted to int 
#         strings with only floating pointing number can be converted to float 
#         strings with floating pointering numbers cannot be converted to int 
val = "123"
val = int(val) 
print(val)
print(type(val))
val = "123.345"
val = float(val)
print(val)
print(type(val))
# val = "3.1425"
# val = int(val)
# print(val)
# print(type(val))