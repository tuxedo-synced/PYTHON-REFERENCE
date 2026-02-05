# variable scope = where a variable is visible and accessible 
# scope resolution order = (LEGB) local -> Enclosed -> Global -> Built-in

# local variables - its presence only within its block 
# Enclosed - one function can be enclosed within another in python and the value given is used by inner function too .
# Global variables - the variables defined outside any function is global
# Built-in variables - any number of characters with a alphabet at first place is called identifer
#                      few identifiers are reserved by compiler for fixed use of the variable are built-in variables .

from math import e 
e = 3       # global version 
print(e)
