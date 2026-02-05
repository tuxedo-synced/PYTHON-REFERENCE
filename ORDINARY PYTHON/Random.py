import random

# print(dir(random))
# print(help(random))

number = random.randint(1,6)
print(number)
number = random.random()    # range [0,1)
print(number)

options = ["rock","paper","scissors"]
random.shuffle(options)
print(options)

# rock paper scissor game 

print("-------------------------------------------------------------------------------")
Pick = ("rock","paper","scissors")
player = None 
score = 0 
count = 0 
while 1:
    computer = random.choice(Pick)
    player = input("Enter your choice (q to quit): ").lower()
    if player == "rock" and computer == "paper":
        score-=1
        print(f"Player choice: {player} Computer choice: {computer}")
        count+=1
    elif player == "rock" and computer == "scissors":
        score+=1
        print(f"Player choice: {player} Computer choice: {computer}")
        count+=1
    elif player == "paper" and computer == "rock":
        score+=1
        print(f"Player choice: {player} Computer choice: {computer}")
        count+=1
    elif player == "paper" and computer == "scissors":
        score-=1
        print(f"Player choice: {player} Computer choice: {computer}")
        count+=1
    elif player == "scissors" and computer == "rock":
        score-=1
        print(f"Player choice: {player} Computer choice: {computer}")
        count+=1
    elif player == "scissors" and computer == "paper":
        score+=1
        print(f"Player choice: {player} Computer choice: {computer}")
        count+=1
    elif player == "q" :
        break
    elif player == computer:
        score = score 
        print(f"Player choice: {player} Computer choice: {computer}")
    else: 
        print("Enter valid input")
        count+=1
print("-------------SCORE-------------")
print(f"player score: {score}")
print(f"computer score: {count-score}")
if score > (count - score) :
    print("Player Wins!!!")
elif score == (count - score) : 
    print("Its a draw!!!")
else: print("Computer Wins!!!")
print("-------------------------------")
