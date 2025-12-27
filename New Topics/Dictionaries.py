# dictionary = a collection of {key:value} pairs 
#              ordered and changable . No duplications 

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals))
print(capitals.get("USA"))
# if not found returns "None"
print(capitals.get("Japan"))
capitals.update({"Geremany": "Berlin"})
print(capitals)
capitals.update({"India": "Gujrat"})
print(capitals)
capitals.pop("India")
print(capitals)
capitals.popitem()
print(capitals)
# capitals.clear()
# print(capitals)
keys = capitals.keys()
print(keys)
 
# printing every key
for key in capitals.keys():
    print(key , end = " ") 
print()

values = capitals.values()
print(values)

# printing every Value
for value in capitals.values():
    print(value , end = " ")
print()

items = capitals.items()
print(items)

# printing every key and value 
for key,value in capitals.items():
    print(f"{key}: {value}")



# example program :- designing a menu of some hotel 
menu = {"pop corn": 75,
        "chicken 65": 90,
        "lays": 50,
        "drinks": 20,
        "ice cream": 90,
        "noodles": 100}

cart = []
totalCost = 0 

print("-----------------------------------MENU-----------------------------------------------")
for key,value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("--------------------------------------------------------------------------------------")

while 1:
    food = input("Enter food you need (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("Food in cart: ")
for items in cart:
    print(items,end = " ")
    totalCost+=menu.get(items)
print()
print(f"Total amount: {totalCost}/-")
print("--------------------------------------------------------------------------------------")

