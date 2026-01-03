# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# printing even numbers
n = list(input("Enter a value: "))  
# assume :- input typed :- 1 2 3 4 5 6 7 8 9
#           n = ['1',' ','2',' ','3',' ','4',' ','5',' ','6',' ','7',' ','8',' ','9']
#           input typed :- 123456789
#           n = ['1','2','3','4','5','6','7','8','9']  
a = [b for b in n if int(b) % 2 == 0]   
print(a)