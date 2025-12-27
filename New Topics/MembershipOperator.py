# Membership operator = used to test wheather a value or variable is found in a sequence 
#                       (string, list,tuple, set, or dictionary)
#                       1. in 
#                       2. not in 

word = "APPLE"

letter = input("Guess a letter in secret word: ")

if letter.upper() in word:
    print(f"there is {letter} in the secret word")
else:
    print(f"the letter {letter} you have entered is not in the secret word")


print()

if letter.upper() not in word:
    print(f"the letter {letter} you have entered is not in the secret word")
else:
    print(f"there is {letter} in the secret word")


# similar for list, tuple, set, dictionary .