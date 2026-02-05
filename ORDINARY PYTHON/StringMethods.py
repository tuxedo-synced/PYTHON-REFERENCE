
# len()
name = "Bro Code" 
len = len(name)
print(name)
print(len)

# .find() - returns the index of first occurance of character specified
# returns -1 if not founnd 
idx = name.find("Co")
print(idx)

# .rfind() - returns the index of last occurance of character specified 
# returns -1 if not found 
idx = name.rfind("o")
print(idx)

# .capitalize() -- only capitalize first character of a string 
cap = name.capitalize()
print(cap)

# .upper() and .lower()
cap = name.upper() 
print(cap)
low = name.lower()
print(low)

# .isdigit() 
result = name.isdigit()
print(result)

# .isalpha()
result = name.isalpha()   # should not include " " because its not an alphabet 
print(result)

# .count() -- counts specific group of characters 
name = "Rahul Sadaram"
result = name.count("a")
print(result)
name = "aabbabababaaabaa"       # is not repeateding once grouped substring ( best )
result = name.count("aa")
print(result)

# .replace() -- replace one character with other
name = "Rahul Sadaram"
name = name.replace("a","x")
print(name)

# reversal (done indirectly)
name = "Rahul Sadaram"
name = name[::-1]
print(name)

# | Key                | What it does                             |
# | ------------------ | ---------------------------------------- |
# | **Spacebar**       | Show the next full page of text          |
# | **Enter / Return** | Show one more line                       |
# | **q**              | Quit the help viewer (stop showing help) |
# | **h**              | Show help about the pager controls       |

# help() -- used for refernce of any particular type
help(str)
