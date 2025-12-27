# function = A block of reusable code 
#             place () after the function name to invoke it 

# syntax :- 

# def function_name(parameter1,parameter2,...):
    # statement1
    # statement2
    # statement3
    # statement4
    # return statement (if required)


# 1. Positional Arguments – Values passed in order according to parameters.
# 2. Default Arguments – Parameters that have preset values if not provided.
# 3. Keyword Arguments – Arguments passed with parameter names, so order doesn’t matter.
# 4. Arbitrary Arguments – Accepts variable numbers of values using *args or **kwargs.

# default argumnets - A default value for certain parameters 
#                       default is used when that argument is omitted
#                       make your functions more flexible, reducing of arguments


def net_price(list_price,discount=0,tax=0.05):      # discount  is max times 0 and tax is 0.0.5 so initiaise it at the parameters place itself .
    return list_price * (1-discount) * (1+tax) 

print(net_price(500))
print(net_price(500,0.1))
print(net_price(500,0.1,0))

# keyword arguments - an argument preceded by an identifier helps with readability 
#                     order of aurguments doesn't matter 

def empDetails(greet,name,designation,salary):
    print(f"{greet} {name} {designation} {salary}")

empDetails(greet="hello",designation="Manager",name="Sudhakar",salary="1,00,000")

# *args - allows you to pass multiple non key aurguments
# **kwargs - allows you to pass multiple keyword-aurguments 
#           * unpacking operator

def add(*args):
    total = 0 
    for i in args:
        total+=i
    return total

print(add(1,2))
print(add(3,4,6))

def print_address(**kwargs):
    print(type(kwargs))
    for i,j in kwargs.items():
        print(f"{i}: {j}")

print_address(street="appaya nagar",city="vizag",state="ap",zip="530009")

print()
print()
    
def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg)
    print(f"{kwargs.get("street")}")
    print(f"{kwargs.get("city")} {kwargs.get("state")}, {kwargs.get("zip")}")
    
shipping_label("Dr.","Spongebob","Squarepants","III",
                street="appaya nagar",city="vizag",state="ap",zip="530009"
                )
