# syntax :- 

#            for variable in range(number1,number2):        [number1 , number2)
#                statement 1
#                statement 2
#                ...........
#            statements 

#            for variable in range(variable,stoping_number,steps):        
#                statement 1
#                statement 2
#                ...........
#            statements 

# example 1 :-
for i in range(1,11):
    print(i)
print("Exiting...")

# example 2 :- 
for i in range(1,11):
    if i == 3 :
        break 
    print(i)
print("Exiting...")

# example 3 :- 
for i in range(1,11):
    if i == 3 :
        continue 
    print(i)
print("Exiting...")

# example 4 :-
target = 5
for i in range(target,0,-1):
    print(i , end = " ")
            