# Iterables = An object/collection that can return its elements one at a time, 
#             allowing it to be iterated over in a loop 

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item , end = " ")
print()
for item in reversed(numbers):
    print(item , end = " ")
print()


# Similarly sets, tuples, dictionaries .