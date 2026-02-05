choice = int(input("ENter choice (1-7): "))
match choice:
    case 1: 
            print("Monday")
    case 2: 
            print("Tuesday")
    case 3: 
            print("Wednesday")
    case 4: 
            print("Thursday")
    case 5: 
            print("Friday")
    case 6: 
            print("Saturday")
    case 7: 
            print("Sunday")
    case _:
            print("its not a day")

# no need of break , it automatically adjust to excecute set value only .
# spacing at each case must be same .

# make a program to check wheather given day is a weekend or not 

def weekendYesOrNo():
        day = input("Enter day: ")
        match day.upper():
                case "MONDAY" | "TUESDAY"  | "WEDNESDAY"  | "THURSDAY"  | "FRIDAY":
                        return False 
                case "SATURDAY"  | "SUNDAY":
                        return True 
                case _:
                        print("Entered Wrong choice")
                
randDay = weekendYesOrNo()
if randDay:
        print(f"The day you entered is a Week day")
else:
        print(f"The day you entered is not a Week day")



