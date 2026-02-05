fruits =        ["orange" , "apple" , "banana" , "coconut"]
vegitables =    ["carrot" , "potatoes" , "spinach"]
meats =         ["chicken" , "fish" , "turkey"]

groceries = [fruits , vegitables , meats] 

# (or)

# groceries = [["orange" , "apple" , "banana" , "coconut"] , ["carrot" , "potatoes" , "spinach"] , ["chicken" , "fish" , "turkey"]]

# print 2d list
print(groceries)

# print rows
print(groceries[0])
print(groceries[1])
print(groceries[2])

# print specific element
print(groceries[0][1])

# iterating a 2d list 

for collection in groceries:
    print(collection)

for collection in groceries:
    for food in collection:
        print(food , end = " ")
    print()