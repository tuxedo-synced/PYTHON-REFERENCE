# Decorator = A function that extends the behaviour of anaother function 
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

#             @add_sprinkles
#             get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args,**kwargs):            # *args,**kwargs -> for accepting any number of parameters as given a parameter in line 26 , we do this .
        print("you add sprinkles .")
        func(*args,**kwargs)
    return wrapper

def add_scope(func):
    def scope(*args,**kwargs):
        print("you add scope .")
        func(*args,**kwargs)
    return scope

# first inner decorator is excected next (inner -> outer)
@add_sprinkles  # get_ice_cream = add_sprinkles(scope) -> later -> get_ice_cream = wrapper 
@add_scope      # get_ice_cream = add_scope(get_ice_cream) -> later -> get_ice_cream = scope 
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream .")

get_ice_cream("vanilla")



# order of excecution :-
"""
Program starts
↓
add_sprinkles defined
↓
add_scope defined
↓
get_ice_cream function defined
↓
@add_scope applied
↓
add_scope(get_ice_cream)
↓
scope created
↓
return scope
↓
@add_sprinkles applied
↓
add_sprinkles(scope)
↓
wrapper created
↓
return wrapper
↓
get_ice_cream → wrapper
↓
get_ice_cream() called
↓
wrapper() executes
↓
print "you add sprinkles ."
↓
scope() executes
↓
print "you add scope ."
↓
original get_ice_cream() executes
↓
print "Here is your ice cream ."
↓
Program ends

"""