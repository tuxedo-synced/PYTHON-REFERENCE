# module = a file containing code you want to include in your program 
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable seperate files 

# syntax :-
# 1. import module_name
# 2. import module_name as any_identifier
# 3. from module_name import specific_part

# example 1:-
# import math 
# print(math.pi)

# example 2:-
# import math as m
# print(m.e)

# example 3:-
# from math import pi   ---------|  ------->    this synatx cause identifier duplicates 
# print(pi)             ---------|  ------->    values get changes example is below 

# from math import e
# a, b, c, d, e = 1, 2, 3, 4, 5
# print(e)                       

# We can also create and add other module which are user defined 
import Example as test
print(test.adding(2,3))
# print(help(test))