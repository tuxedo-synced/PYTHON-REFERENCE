# List comprehension = A concite way to create lists in python 
#                      Compact and easier to read than traditional loopd 
#                      [expression for value in iterable if condition]

doubles = [x*2 for x in range(1,11)]
print(doubles)

fruits = ["apple" , "banaana" , "custurd apple" , "tomato"]
fruitsUpper = [fruit.upper() for fruit in fruits]
fruitsFirstUpper = [fruit[0].upper() for fruit in fruits]
print(fruitsUpper)
print(fruitsFirstUpper)

# printing a list of positive numbers 
numbers = [1, -2, 3, -4, 9]
positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)

