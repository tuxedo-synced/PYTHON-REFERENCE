import time 

# .sleep(number) ->  sleeps for {number} seconds 

# # method 1 :-

timer = int(input("Enter the timer value: "))

for i in range(1,timer+1):
    print(i)
    time.sleep(1)
print("Exiting\n\n\n\n")

# # method 2 :- 

timer = int(input("Enter the timer value: "))

for i in range(timer,0,-1):
    print(i)
    time.sleep(1)
print("Exiting\n\n\n\n")

# displaying minutes , seconds and hours :

timer = int(input("Enter the timer value: "))

hr = int(timer / 3600)
timer = int(timer % 3600)  
min = int(timer / 60)
timer = int(timer % 60) 
sec = int(timer)

print(f"final clock: {hr}:{min}:{sec}")

# timer actual :- 

timer = int(input("Enter the timer value: ")) 

for x in range(timer,0,-1):
    hr = int(x / 3600)
    min = int(x / 60) % 60 
    sec = x % 60 
    print(f"clock ticking: {hr}:{min}:{sec}")
    time.sleep(1)
print("Exiting\n\n\n")


