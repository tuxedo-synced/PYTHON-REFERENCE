# collection = single "variable" used to store multiple  values
# List = [] ordered and changeable . Duplicates OK
# Set = {} unordered and immutable , but Add/Remove OK. NO dupicates 
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER THAN LISTS

# list :-  regular indexing , string indeexing , dir() , help() , len(list_variable) , .append("") , .remove("") , .insert(int,"") , .sort() , .reverse() , .clear() , .index("") , .count("") 
# "" -> string

fruit = ["apple","orange","banana"]
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[::-1])
print(fruit[2:1:-1])
for x in fruit:
    print(x)
print(dir(fruit))
# print(help(fruit))  # press enter for more information .
print(len(fruit))
fruit.append("coco")
fruit.remove("orange")
fruit.insert(2,"papaya")    # (index,data) -> data placed at specific index 
print(fruit)
fruit.sort()
fruit.reverse()
print(fruit)
# fruit.clear()
print(fruit)
print(fruit.index("banana"))
fruit.append("banana")
print(fruit.count("banana"))

# set :- len(set_variable) , .add("") , .remove("") , .pop() , .clear() 

fruit = {"apple","orange","banana","coconut","orange"}
print(fruit)
print(dir(fruit))
# print(help(fruit))
print(len(fruit))
print("pineapple" in fruit)
# we cannot use indexing (ie., fruit[0]) in a set as it is unordered .
fruit.add("pineapple")
print(fruit)
fruit.remove("apple")
print(fruit)
fruit.pop()     # as set is unordered cannot predict which element will be popped 
print(fruit)
fruit.clear()
print(fruit)

# for sets we can take union , intersection , difference , in A or B not in both
a = {1,2,3,4,5,6,7,8}
b = {2,3,4,5,7,10,11}
print(a|b)
print(a&b)
print(a-b)
print(a^b)

# Tuple :- len(Tuple_variable) , .index("") , .count("") 
# we can use indexing in tuples as it is ordered 
fruit = ("apple","orange","banana","coconut","orange")
print(fruit)
print(dir(fruit))
# print(help(fruit))
print(len(fruit))
print(fruit.index("banana"))
print(fruit.count("orange"))
print(fruit[0])



# note:- 
#        temp = [0] * 26
#       equalent to :- 
#         temp = []
#         for i in range(0,26):
#            temp.append(0)